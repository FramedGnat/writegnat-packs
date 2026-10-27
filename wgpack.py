"""Herramientas para escribir paquetes de contenido de WriteGnat (.wgpack).

Un .wgpack es un zip sólo de datos (nada ejecutable):
  manifest.json  – id, nombre, descripción, versión, área, icono y número de elementos
  content.json   – figuras, fórmulas, etiquetas y emojis
  strings_en.json – traducciones al inglés de los textos del paquete

Las figuras se describen en el marco local de la app: `u` a lo largo del arrastre (0 → 1) y `v`
perpendicular (positivo = arriba al arrastrar a la derecha), en unidades del largo del arrastre.
Así giran y crecen mientras se colocan, igual que las figuras incluidas en la app.
"""
import hashlib, json, math, os, zipfile

FORMAT = 1


class Fig:
    """Constructor de una figura: misma API que Figures.Builder en la app."""

    def __init__(self):
        self.parts = []   # {"p": [u, v, u, v…], "f": 1 (relleno), "d": 1 (discontinua)}
        self.labels = []  # [u, v, texto, escala]
        self.robot = None

    def _add(self, pts, fill=False, dashed=False):
        flat = []
        for u, v in pts:
            flat += [round(u, 4), round(v, 4)]
        part = {"p": flat}
        if fill: part["f"] = 1
        if dashed: part["d"] = 1
        self.parts.append(part)

    def line(self, *c, dashed=False):
        self._add(list(zip(c[0::2], c[1::2])), dashed=dashed)

    def poly(self, *c, fill=False, dashed=False):
        pts = list(zip(c[0::2], c[1::2]))
        self._add(pts + [pts[0]], fill, dashed)

    def rect(self, u0, v0, u1, v1, fill=False, dashed=False):
        self.poly(u0, v0, u1, v0, u1, v1, u0, v1, fill=fill, dashed=dashed)

    def arc(self, cu, cv, ru, rv=None, frm=0.0, to=360.0, fill=False, dashed=False):
        rv = ru if rv is None else rv
        n = max(6, int(abs(to - frm) / 7.5))
        pts = []
        for i in range(n + 1):
            t = math.radians(frm + (to - frm) * i / n)
            pts.append((cu + ru * math.cos(t), cv + rv * math.sin(t)))
        self._add(pts, fill, dashed)

    def circle(self, cu, cv, r, fill=False, dashed=False):
        self.arc(cu, cv, r, r, fill=fill, dashed=dashed)

    def ellipse(self, cu, cv, ru, rv, fill=False, dashed=False):
        self.arc(cu, cv, ru, rv, fill=fill, dashed=dashed)

    def head(self, u0, v0, u1, v1, size=0.06):
        a = math.atan2(v1 - v0, u1 - u0)
        a1 = a + math.pi * 5 / 6; a2 = a - math.pi * 5 / 6
        self.line(u1 + size * math.cos(a1), v1 + size * math.sin(a1), u1, v1, u1 + size * math.cos(a2), v1 + size * math.sin(a2))

    def arrow(self, u0, v0, u1, v1, size=0.06, dashed=False):
        self.line(u0, v0, u1, v1, dashed=dashed); self.head(u0, v0, u1, v1, size)

    def double_arrow(self, u0, v0, u1, v1, size=0.06):
        self.arrow(u0, v0, u1, v1, size); self.head(u1, v1, u0, v0, size)

    def hatch(self, u0, u1, v, n=6, depth=0.08):
        """Suelo o pared rayada bajo el segmento (u0, v)–(u1, v)."""
        self.line(u0, v, u1, v)
        for k in range(n):
            u = u0 + (u1 - u0) * (k + 0.5) / n
            self.line(u, v, u - depth, v - depth)

    def curve(self, f, u0, u1, n=64, dashed=False):
        """Gráfica v = f(u) entre u0 y u1."""
        self._add([(u0 + (u1 - u0) * i / n, f(u0 + (u1 - u0) * i / n)) for i in range(n + 1)], dashed=dashed)

    def polar(self, cu, cv, r, n=120):
        """Curva cerrada con radio r(t)."""
        self._add([(cu + r(2 * math.pi * i / n) * math.cos(2 * math.pi * i / n), cv + r(2 * math.pi * i / n) * math.sin(2 * math.pi * i / n)) for i in range(n + 1)])

    def regular(self, cu, cv, r, sides, rot=90.0, fill=False):
        pts = []
        for k in range(sides):
            a = math.radians(rot + 360.0 * k / sides)
            pts += [cu + r * math.cos(a), cv + r * math.sin(a)]
        self.poly(*pts, fill=fill)

    def label(self, u, v, text, scale=1.0):
        self.labels.append([round(u, 4), round(v, 4), text, scale])

    def zigzag(self, u0, u1, v, amp=0.08, n=8, lead=0.15):
        """Resistencia/resorte horizontal entre u0 y u1 con tramos rectos de [lead]."""
        pts = [(u0, v), (u0 + lead, v)]
        span = (u1 - u0) - 2 * lead
        for k in range(n):
            pts.append((u0 + lead + (k + 0.5) * span / n, v + (amp if k % 2 == 0 else -amp)))
        pts += [(u1 - lead, v), (u1, v)]
        self._add(pts)


class Pack:
    def __init__(self, pid, name, description, area, icon, version=1, en=None):
        self.id = pid; self.name = name; self.description = description; self.area = area
        self.icon = icon; self.version = version
        self.figures = {}       # categoría → [figura]
        self.formulas = []      # {"group", "category", "items": [[nombre, latex]]}
        self.labels = []        # [texto, "#rrggbb"]
        self.emoji = {}         # categoría → "😀 😁 …"
        self.en = dict(en or {})

    def figure(self, category, fid, name, en=None, robot=None):
        """Decorador: la función recibe un Fig y lo dibuja."""
        def deco(fn):
            g = Fig()
            fn(g)
            item = {"id": fid, "name": name, "parts": g.parts}
            if g.labels: item["labels"] = g.labels
            if robot: item["robot"] = robot
            self.figures.setdefault(category, []).append(item)
            if en: self.en[name] = en
            return fn
        return deco

    def robot(self, category, fid, name, joints, en=None):
        self.figures.setdefault(category, []).append({"id": fid, "name": name, "parts": [], "robot": joints})
        if en: self.en[name] = en

    def formulas_in(self, group, category, items, en_category=None):
        """items: [(nombre, latex) | (nombre, latex, nombre_en)]."""
        out = []
        for it in items:
            out.append([it[0], it[1]])
            if len(it) > 2: self.en[it[0]] = it[2]
        self.formulas.append({"group": group, "category": category, "items": out})
        if en_category: self.en[category] = en_category

    def counts(self):
        return {
            "figures": sum(len(v) for v in self.figures.values()),
            "formulas": sum(len(c["items"]) for c in self.formulas),
            "stickers": len(self.labels) + sum(len(v.split()) for v in self.emoji.values()),
        }

    def write(self, out_dir):
        ids = [f["id"] for v in self.figures.values() for f in v]
        assert len(ids) == len(set(ids)), f"{self.id}: ids de figura repetidos"
        manifest = {"format": FORMAT, "id": self.id, "name": self.name, "description": self.description,
                    "area": self.area, "icon": self.icon, "version": self.version, "counts": self.counts()}
        content = {
            "figures": [{"category": c, "items": items} for c, items in self.figures.items()],
            "formulas": self.formulas,
            "labels": self.labels,
            "emoji": [{"category": c, "items": s.split()} for c, s in self.emoji.items()],
        }
        path = os.path.join(out_dir, f"{self.id}.wgpack")
        # Zip determinista: misma fecha y orden, así el SHA-256 sólo cambia si cambia el contenido.
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for name, data in (("manifest.json", manifest), ("content.json", content), ("strings_en.json", self.en)):
                info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0)); info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, json.dumps(data, ensure_ascii=False, separators=(",", ":")))
        data = open(path, "rb").read()
        manifest.update({"file": f"packs/{self.id}.wgpack", "size": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                         "name_en": self.en.get(self.name, self.name), "description_en": self.en.get(self.description, self.description)})
        return manifest
