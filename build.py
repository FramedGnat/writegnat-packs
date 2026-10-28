#!/usr/bin/env python3
"""Genera packs/*.wgpack y catalog.json a partir de src/*.py.

Uso: ./build.py  → después, git add -A && git commit && git push (la app lee catalog.json de main).
"""
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ORDER = ["fisica", "quimica", "biologia", "electronica", "robotica", "civil", "industrial", "economia", "arquitectura", "psicologia", "musica", "robots", "mascotas", "animales", "comida", "naturaleza", "espacio", "deportes", "transporte", "escuela", "marcadores", "estilo"]

sys.path.insert(0, os.path.join(HERE, "src"))

def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, "src", name + ".py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    # Plantillas, stickers y símbolos de la carrera (src/<nombre>_extra.py, si existe).
    extra = os.path.join(HERE, "src", name + "_extra.py")
    if os.path.exists(extra):
        spec = importlib.util.spec_from_file_location(name + "_extra", extra)
        ext = importlib.util.module_from_spec(spec); spec.loader.exec_module(ext); ext.extend(mod.pack)
    # Stickers con personalidad de la carrera (src/<nombre>_chars.py, si existe).
    chars = os.path.join(HERE, "src", name + "_chars.py")
    if os.path.exists(chars):
        spec = importlib.util.spec_from_file_location(name + "_chars", chars)
        ch = importlib.util.module_from_spec(spec); spec.loader.exec_module(ch); ch.extend(mod.pack); mod.pack.version += 1   # los stickers nuevos suben la versión del complemento
    # Figuras de las materias de la carrera (src/<nombre>_figs.py, si existe).
    figs = os.path.join(HERE, "src", name + "_figs.py")
    if os.path.exists(figs):
        spec = importlib.util.spec_from_file_location(name + "_figs", figs)
        fg = importlib.util.module_from_spec(spec); spec.loader.exec_module(fg); fg.extend(mod.pack); mod.pack.version += 1
    return mod.pack

out = os.path.join(HERE, "packs"); os.makedirs(out, exist_ok=True)
entries = [load(n).write(out) for n in ORDER]
catalog = {"format": 1, "packs": entries}
json.dump(catalog, open(os.path.join(HERE, "catalog.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for e in entries:
    c = e["counts"]; print(f"{e['id']:24} v{e['version']}  {c['figures']:3} fig  {c['formulas']:3} fórm  {c['stickers']:3} stick  {c.get('templates', 0):2} plant  {c.get('symbols', 0):3} símb  {e['size'] // 1024} KB")
print(sum(e["counts"]["figures"] for e in entries), "figuras,", sum(e["counts"]["formulas"] for e in entries), "fórmulas")
