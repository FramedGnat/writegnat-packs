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

    def spline(self, pts, n=10, dashed=False, closed=False):
        """Curva suave (Catmull-Rom) que pasa por [pts] = [(u, v), …]."""
        P = list(pts)
        if closed: P = [P[-1]] + P + [P[0], P[1]]
        else: P = [P[0]] + P + [P[-1]]
        out = []
        for i in range(1, len(P) - 2):
            p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
            for k in range(n):
                t = k / n; t2 = t * t; t3 = t2 * t
                out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2 + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
        out.append(tuple(P[-2]))
        self._add(out, dashed=dashed)

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


GUIDE, SOFT, LABEL = "#9ca3af", "#d4d4d8", "#6b7280"


class Art:
    """Dibujo en pt (y hacia abajo): plantillas de página y stickers de color."""

    def __init__(self, w, h):
        self.w = w; self.h = h; self.parts = []; self.texts = []

    def _add(self, pts, color, width, fill=False, dashed=False):
        flat = []
        for x, y in pts: flat += [round(x, 2), round(y, 2)]
        part = {"p": flat, "c": color, "w": width}
        if fill: part["f"] = 1
        if dashed: part["d"] = 1
        self.parts.append(part)

    def line(self, *c, color=GUIDE, w=0.85, dashed=False):
        self._add(list(zip(c[0::2], c[1::2])), color, w, dashed=dashed)

    def poly(self, *c, color=GUIDE, w=0.85, fill=False):
        pts = list(zip(c[0::2], c[1::2])); self._add(pts + [pts[0]], color, w, fill)

    def rect(self, x0, y0, x1, y1, color=GUIDE, w=0.85, fill=False, dashed=False):
        self._add([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], color, w, fill, dashed)

    def round_rect(self, x0, y0, x1, y1, r, color=GUIDE, w=0.85, fill=False):
        pts = []
        for cx, cy, a0 in ((x1 - r, y0 + r, -90), (x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90), (x0 + r, y0 + r, 180)):
            for k in range(7): a = math.radians(a0 + 15 * k); pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        self._add(pts + [pts[0]], color, w, fill)

    def circle(self, cx, cy, r, color=GUIDE, w=0.85, fill=False, ry=None):
        ry = r if ry is None else ry
        self._add([(cx + r * math.cos(2 * math.pi * k / 40), cy + ry * math.sin(2 * math.pi * k / 40)) for k in range(41)], color, w, fill)

    def text(self, x, y, t, size=9.0, color=LABEL):
        self.texts.append([round(x, 2), round(y, 2), t, size, color])

    def ruled(self, x0, y0, x1, y1, step=22.0):
        y = y0 + step
        while y <= y1 - 4: self.line(x0, y, x1, y, color=SOFT, w=0.5); y += step

    def grid(self, x0, y0, x1, y1, step=14.17, color=SOFT, w=0.4):
        x = x0
        while x <= x1 + 0.01: self.line(x, y0, x, y1, color=color, w=w); x += step
        y = y0
        while y <= y1 + 0.01: self.line(x0, y, x1, y, color=color, w=w); y += step

    def dots(self, x0, y0, x1, y1, step=14.17):
        y = y0
        while y <= y1 + 0.01:
            x = x0
            # Un punto = trazo diminuto con punta redonda (mucho más ligero que un círculo).
            while x <= x1 + 0.01: self._add([(x, y), (x + 0.05, y)], GUIDE, 1.1); x += step
            y += step

    def fields(self, x0, y, x1, names, size=9.0):
        """Fila de campos «Nombre: ____» repartidos de x0 a x1."""
        cw = (x1 - x0) / len(names)
        for i, n in enumerate(names):
            x = x0 + i * cw; self.text(x, y - size * 1.2, n + ":", size); self.line(x + len(n) * size * 0.55 + 8, y, x + cw - 10, y, w=0.6)

    def title(self, x, y, t, size=16.0):
        self.text(x, y, t, size, "#4b5563")

    def table(self, x0, y0, x1, y1, cols, rows, headers=None, header_h=20.0):
        """cols: anchos relativos; rows: filas de datos (sin contar la cabecera)."""
        self.rect(x0, y0, x1, y1, w=0.9)
        tot = sum(cols); x = x0
        for i, c in enumerate(cols):
            if headers: self.text(x + 4, y0 + 5, headers[i], 8.5)
            x += (x1 - x0) * c / tot
            if i < len(cols) - 1: self.line(x, y0, x, y1, w=0.6)
        top = y0 + (header_h if headers else 0)
        if headers: self.line(x0, top, x1, top, w=0.9)
        rh = (y1 - top) / max(1, rows)
        for r in range(1, rows): self.line(x0, top + r * rh, x1, top + r * rh, color=SOFT, w=0.5)

    def section(self, x0, y0, x1, y1, name, ruled=True):
        self.rect(x0, y0, x1, y1, w=0.7); self.text(x0 + 5, y0 + 4, name, 9.0)
        if ruled: self.ruled(x0 + 6, y0 + 10, x1 - 6, y1)

    def to_json(self, sid, name):
        d = {"id": sid, "name": name, "w": self.w, "h": self.h, "parts": self.parts}
        if self.texts: d["texts"] = self.texts
        return d


class Pack:
    def __init__(self, pid, name, description, area, icon, version=1, en=None):
        self.id = pid; self.name = name; self.description = description; self.area = area
        self.icon = icon; self.version = version
        self.figures = {}       # categoría → [figura]
        self.formulas = []      # {"group", "category", "items": [[nombre, latex]]}
        self.labels = []        # [texto, "#rrggbb"]
        self.emoji = {}         # categoría → "😀 😁 …"
        self.en = dict(en or {})
        self.templates = []     # Art (hoja A4 en pt) para «Plantillas · paquete»
        self.stickers = []      # Art de color
        self.symbols = []       # {"category", "items": [latex]}
        self.snap = set()       # categorías de figuras que se pegan a la rejilla (circuitos)

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

    def template(self, tid, name, en=None, w=595.0, h=842.0):
        """Decorador: la función dibuja en un Art del tamaño de la hoja (A4 vertical por defecto)."""
        def deco(fn):
            a = Art(w, h); fn(a); self.templates.append(a.to_json(tid, name))
            if en: self.en[name] = en
            return fn
        return deco

    def sticker(self, sid, name, en=None, w=60.0, h=60.0):
        def deco(fn):
            a = Art(w, h); fn(a); self.stickers.append(a.to_json(sid, name))
            if en: self.en[name] = en
            return fn
        return deco

    def symbols_in(self, category, items, en=None):
        self.symbols.append({"category": category, "items": items.split() if isinstance(items, str) else items})
        if en: self.en[category] = en

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
            "stickers": len(self.labels) + len(self.stickers) + sum(len(v.split()) for v in self.emoji.values()),
            "templates": len(self.templates),
            "symbols": sum(len(s["items"]) for s in self.symbols),
        }

    def write(self, out_dir):
        ids = [f["id"] for v in self.figures.values() for f in v]
        assert len(ids) == len(set(ids)), f"{self.id}: ids de figura repetidos"
        manifest = {"format": FORMAT, "id": self.id, "name": self.name, "description": self.description,
                    "area": self.area, "icon": self.icon, "version": self.version, "counts": self.counts()}
        content = {
            "figures": [dict({"category": c, "items": items}, **({"snap": True} if c in self.snap else {})) for c, items in self.figures.items()],
            "formulas": self.formulas,
            "labels": self.labels,
            "emoji": [{"category": c, "items": s.split()} for c, s in self.emoji.items()],
            "templates": self.templates,
            "stickers": self.stickers,
            "symbols": self.symbols,
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
