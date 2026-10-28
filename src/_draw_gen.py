"""Ayudas de dibujo para los paquetes generales (espacio, deportes, transporte)."""
import math
from _draw import *


def ellpts(cx, cy, rx, ry, rot=0.0, t0=0.0, t1=360.0, n=36):
    r = math.radians(rot); out = []
    for k in range(n + 1):
        t = math.radians(t0 + (t1 - t0) * k / n); x, y = rx * math.cos(t), ry * math.sin(t)
        out.append((cx + x * math.cos(r) - y * math.sin(r), cy + x * math.sin(r) + y * math.cos(r)))
    return out


def ell(a, cx, cy, rx, ry, rot, fill, w=1.6):
    pts = ellpts(cx, cy, rx, ry, rot, n=40)
    a._add(pts, fill, 1.0, True)
    if w: a._add(pts, OL, w)


def rotpoly(a, cx, cy, w_, h_, rot, fill, w=1.6):
    r = math.radians(rot); pts = []
    for x, y in ((-w_ / 2, -h_ / 2), (w_ / 2, -h_ / 2), (w_ / 2, h_ / 2), (-w_ / 2, h_ / 2)):
        pts += [cx + x * math.cos(r) - y * math.sin(r), cy + x * math.sin(r) + y * math.cos(r)]
    pg(a, *pts, fill=fill, w=w)


def regpoly(a, cx, cy, r, n, fill, rot=-90.0, w=1.4):
    pts = []
    for k in range(n):
        t = math.radians(rot + 360.0 * k / n); pts += [cx + r * math.cos(t), cy + r * math.sin(t)]
    pg(a, *pts, fill=fill, w=w)


def blob(a, rects=(), circles=(), fill="#fff", w=3.2):
    """Unión de rectángulos redondeados y círculos con un solo contorno exterior."""
    for x0, y0, x1, y1, r in rects: a.round_rect(x0, y0, x1, y1, r, color=OL, w=w)
    for cx, cy, r in circles: a.circle(cx, cy, r, color=OL, w=w)
    for x0, y0, x1, y1, r in rects: a.round_rect(x0, y0, x1, y1, r, color=fill, fill=True)
    for cx, cy, r in circles: a.circle(cx, cy, r, color=fill, fill=True)


def poly_line(a, pts, color=OL, w=1.6):
    a._add(pts, color, w)


def wheel(a, cx, cy, r, tire="#334155", hub="#cbd5e1"):
    cc(a, cx, cy, r, tire, w=1.5); cc(a, cx, cy, r * 0.45, hub, w=1.1)


def ring(a, cx, cy, r, col, w=2.6, ry=None):
    a.circle(cx, cy, r, color=OL, w=w + 2.0, ry=ry); a.circle(cx, cy, r, color=col, w=w, ry=ry)


def thick(a, *c, color, w=3.0):
    ln(a, *c, color=OL, w=w + 2.2); ln(a, *c, color=color, w=w)


def tiny(a, cx, cy, kind="dot", mouth="smile", gap=4.0, r=1.5, my=None, col=OL):
    face(a, cx, cy, kind, mouth, gap, r, my=my, col=col)
