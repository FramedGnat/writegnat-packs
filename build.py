#!/usr/bin/env python3
"""Genera packs/*.wgpack y catalog.json a partir de src/*.py.

Uso: ./build.py  → después, git add -A && git commit && git push (la app lee catalog.json de main).
"""
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ORDER = ["fisica", "quimica", "biologia", "electronica", "robotica", "civil", "industrial", "economia", "arquitectura", "psicologia"]

def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, "src", name + ".py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod.pack

out = os.path.join(HERE, "packs"); os.makedirs(out, exist_ok=True)
entries = [load(n).write(out) for n in ORDER]
catalog = {"format": 1, "packs": entries}
json.dump(catalog, open(os.path.join(HERE, "catalog.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for e in entries:
    c = e["counts"]; print(f"{e['id']:24} v{e['version']}  {c['figures']:3} figuras  {c['formulas']:3} fórmulas  {c['stickers']:3} stickers  {e['size'] // 1024} KB")
print(sum(e["counts"]["figures"] for e in entries), "figuras,", sum(e["counts"]["formulas"] for e in entries), "fórmulas")
