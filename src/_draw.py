"""Primitivas para stickers de color con contorno (personajes y objetos con cara)."""
import math

OL = "#1e293b"      # contorno
WH = "#ffffff"


def rr(a, x0, y0, x1, y1, r, fill, w=1.6):
    a.round_rect(x0, y0, x1, y1, r, color=fill, fill=True); a.round_rect(x0, y0, x1, y1, r, color=OL, w=w)


def cc(a, cx, cy, r, fill, ry=None, w=1.6):
    a.circle(cx, cy, r, color=fill, fill=True, ry=ry); a.circle(cx, cy, r, color=OL, w=w, ry=ry)


def pg(a, *c, fill, w=1.6):
    a.poly(*c, color=fill, fill=True); a.poly(*c, color=OL, w=w)


def ln(a, *c, color=OL, w=2.0):
    a.line(*c, color=color, w=w)


def arc(a, cx, cy, r, a0, a1, color=OL, w=1.8, n=14, ry=None):
    ry = r if ry is None else ry
    a._add([(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), cy + ry * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)], color, w)


def smile(a, cx, cy, r=5, w=1.8): arc(a, cx, cy, r, 25, 155, w=w)
def frown(a, cx, cy, r=5, w=1.8): arc(a, cx, cy + r, r, 205, 335, w=w)


def eyes(a, cx, cy, gap=8, r=2.6, kind="dot", col=OL):
    for s in (-1, 1):
        x = cx + s * gap / 2 * 2 / 2
        x = cx + s * gap
        if kind == "dot":
            cc(a, x, cy, r, col, w=0.4)
            a.circle(x - r * 0.3, cy - r * 0.35, r * 0.35, color=WH, fill=True)
        elif kind == "big":
            cc(a, x, cy, r * 1.5, WH, w=1.2); a.circle(x + 0.4, cy + 0.4, r * 0.75, color=col, fill=True)
            a.circle(x - 0.5, cy - 0.5, r * 0.28, color=WH, fill=True)
        elif kind == "happy":
            arc(a, x, cy + r * 0.8, r * 1.2, 200, 340, w=1.8)
        elif kind == "sleep":
            arc(a, x, cy - r * 0.4, r * 1.2, 20, 160, w=1.8)
        elif kind == "glow":
            cc(a, x, cy, r * 1.35, col, w=1.0); a.circle(x, cy, r * 0.55, color=WH, fill=True)


def blush(a, cx, cy, gap=13, r=2.2, col="#fb7185"):
    for s in (-1, 1): a.circle(cx + s * gap, cy, r, color=col, fill=True, ry=r * 0.6)


def face(a, cx, cy, kind="dot", mouth="smile", gap=8, r=2.6, my=None, cheeks=False, col=OL):
    eyes(a, cx, cy, gap, r, kind, col)
    my = cy + 6 if my is None else my
    if mouth == "smile": smile(a, cx, my - 3, 4.2)
    elif mouth == "big":
        a.poly(cx - 4.5, my - 1, cx + 4.5, my - 1, cx + 3, my + 4, cx - 3, my + 4, color=OL, fill=True)
        a.poly(cx - 2.2, my + 2.2, cx + 2.2, my + 2.2, cx + 1.6, my + 4, cx - 1.6, my + 4, color="#fb7185", fill=True)
    elif mouth == "o": cc(a, cx, my + 1, 2.2, OL, w=0.4)
    elif mouth == "flat": ln(a, cx - 3.5, my + 1, cx + 3.5, my + 1, w=1.8)
    elif mouth == "frown": frown(a, cx, my - 1, 4)
    elif mouth == "grill":
        for k in (-3, 0, 3): ln(a, cx + k, my - 1, cx + k, my + 4, w=1.3)
        a.round_rect(cx - 5, my - 1.5, cx + 5, my + 4.5, 1.5, color=OL, w=1.3)
    if cheeks: blush(a, cx, cy + 4, gap + 5)


def screw(a, x, y, r=1.0): a.circle(x, y, r, color="#94a3b8", fill=True); a.circle(x, y, r, color=OL, w=0.5)


def bolt(a, cx, cy, s, fill="#fbbf24"):
    pg(a, cx + 0.15 * s, cy - s, cx - 0.55 * s, cy + 0.15 * s, cx - 0.05 * s, cy + 0.15 * s, cx - 0.25 * s, cy + s, cx + 0.6 * s, cy - 0.2 * s, cx + 0.05 * s, cy - 0.2 * s, fill=fill, w=1.2)


def heart(a, cx, cy, s, fill="#ef4444"):
    pts = []
    for k in range(41):
        t = 2 * math.pi * k / 40
        pts.append((cx + s * 16 * math.sin(t) ** 3 / 17, cy - s * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) / 17))
    a._add(pts, fill, 1.0, True); a._add(pts, OL, 1.4)


def star(a, cx, cy, r, fill="#fbbf24", n=5):
    pts = []
    for k in range(n * 2):
        rr_ = r if k % 2 == 0 else r * 0.45; t = -math.pi / 2 + math.pi * k / n
        pts += [cx + rr_ * math.cos(t), cy + rr_ * math.sin(t)]
    pg(a, *pts, fill=fill, w=1.3)


def gear(a, cx, cy, r, fill, teeth=8, hole=0.32):
    pts = []
    for k in range(teeth * 4):
        t = 2 * math.pi * k / (teeth * 4); q = r if (k // 2) % 2 == 0 else r * 0.78
        pts += [cx + q * math.cos(t), cy + q * math.sin(t)]
    pg(a, *pts, fill=fill, w=1.4); cc(a, cx, cy, r * hole, WH, w=1.2)


def shine(a, x, y, w_, h_): a.circle(x, y, w_, color="#ffffff", fill=True, ry=h_)
