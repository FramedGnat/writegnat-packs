import math
from wgpack import Pack
from _draw_gen import *

pack = Pack("espacio", "Espacio", "20 stickers del cosmos: astronautas, cohetes, planetas, la Luna, cometas, ovnis, estaciones y más.",
            "General", "🪐", en={"Espacio": "Space",
            "20 stickers del cosmos: astronautas, cohetes, planetas, la Luna, cometas, ovnis, estaciones y más.":
            "20 cosmos stickers: astronauts, rockets, planets, the Moon, comets, UFOs, stations and more."})
P = pack
S = 80.0


def st(sid, name, en):
    return P.sticker("espacio-" + sid, name, en, S, S)


@st("astronauta", "Astronauta", "Astronaut")
def _(a):
    rr(a, 26, 40, 54, 62, 5, "#94a3b8")
    for x0, x1 in ((31, 39), (41, 49)): rr(a, x0, 62, x1, 73, 3, "#e2e8f0", w=1.5); rr(a, x0 - 1, 71, x1 + 1, 77, 2, "#64748b", w=1.4)
    thick(a, 31, 47, 21, 59, color="#f8fafc", w=5); thick(a, 49, 47, 59, 37, color="#f8fafc", w=5)
    cc(a, 21, 60, 3.4, "#94a3b8", w=1.3); cc(a, 59, 35, 3.4, "#94a3b8", w=1.3)
    rr(a, 29, 42, 51, 66, 6, "#f8fafc"); rr(a, 34, 49, 46, 57, 2, "#e2e8f0", w=1.2)
    cc(a, 37, 53, 1.8, "#ef4444", w=0.6); cc(a, 43, 53, 1.8, "#22c55e", w=0.6)
    cc(a, 40, 26, 17, "#f8fafc"); cc(a, 40, 27, 12, "#1e3a8a", ry=10.5, w=1.4); shine(a, 33, 21, 3.4, 1.5)
    cc(a, 35, 26.5, 2.1, "#bae6fd", w=0.4); cc(a, 45, 26.5, 2.1, "#bae6fd", w=0.4); arc(a, 40, 28, 4, 25, 155, color="#bae6fd", w=1.6)


@st("cohete-retro", "Cohete retro", "Retro rocket")
def _(a):
    pg(a, 34, 58, 46, 58, 40, 77, fill="#fb923c", w=1.4); pg(a, 37, 58, 43, 58, 40, 70, fill="#fde047", w=0.9)
    pg(a, 30, 44, 16, 66, 30, 60, fill="#ef4444"); pg(a, 50, 44, 64, 66, 50, 60, fill="#ef4444")
    a.poly(40, 3, 50, 20, 53, 58, 27, 58, 30, 20, color="#f8fafc", fill=True); a.poly(40, 3, 50, 20, 53, 58, 27, 58, 30, 20, color=OL, w=1.8)
    pg(a, 40, 3, 47, 14, 33, 14, fill="#ef4444"); rr(a, 28, 46, 52, 52, 1.5, "#ef4444", w=1.4)
    pg(a, 36, 58, 44, 58, 44, 62, 36, 62, fill="#64748b", w=1.2)
    cc(a, 40, 31, 8.5, "#bae6fd", w=2); tiny(a, 40, 30.5, "dot", "smile", 3.2, 1.2, my=34)


@st("ovni", "Ovni", "UFO")
def _(a):
    pg(a, 30, 52, 50, 52, 64, 77, 16, 77, fill="#fef9c3", w=1.2)
    cc(a, 40, 34, 13, "#bae6fd", w=1.6); cc(a, 40, 35, 7.5, "#86efac", w=1.3)
    cc(a, 37, 34, 1.7, "#0f172a", ry=2.4, w=0.4); cc(a, 43, 34, 1.7, "#0f172a", ry=2.4, w=0.4); smile(a, 40, 38.2, 2.6, 1.2)
    cc(a, 40, 47, 30, "#94a3b8", ry=9); shine(a, 25, 24, 3, 1.4)
    for x, c in ((20, "#fbbf24"), (30, "#f43f5e"), (40, "#38bdf8"), (50, "#f43f5e"), (60, "#fbbf24")): cc(a, x, 49.5, 2.2, c, w=1.0)


@st("planeta-anillos", "Planeta con anillos", "Ringed planet")
def _(a):
    pts = ellpts(40, 42, 36, 10, -22, 0, 360, 40)
    a._add(pts, OL, 6.6); a._add(pts, "#fbbf24", 4)
    cc(a, 40, 41, 19, "#c084fc"); a._add(ellpts(40, 41, 15, 3.4, -22, 190, 350, 14), "#a855f7", 1.8)
    front = ellpts(40, 42, 36, 10, -22, 10, 170, 22)
    a._add(front, OL, 6.6); a._add(front, "#fbbf24", 4)
    shine(a, 31, 31, 3.6, 1.6); tiny(a, 40, 39, "dot", "smile", 5.5, 2.1, my=46)


@st("tierra", "Tierra", "Earth")
def _(a):
    cc(a, 40, 40, 29, "#38bdf8")
    pg(a, 20, 26, 30, 18, 40, 22, 36, 32, 28, 34, 20, 38, fill="#4ade80", w=1.2)
    pg(a, 52, 52, 62, 46, 66, 56, 58, 64, 50, 62, fill="#4ade80", w=1.2); pg(a, 54, 18, 62, 20, 60, 28, 54, 26, fill="#4ade80", w=1.2)
    a.circle(40, 40, 29, color=OL, w=1.8)
    cc(a, 22, 56, 4.5, "#ffffff", ry=2.6, w=0.9); cc(a, 28, 58, 3.5, "#ffffff", ry=2.2, w=0.9)
    shine(a, 28, 24, 4, 1.8); face(a, 40, 41, "dot", "smile", 7, 2.6, my=48, cheeks=True)


@st("luna", "Luna con cara", "Smiling Moon")
def _(a):
    cc(a, 40, 40, 28, "#fde68a")
    for x, y, r in ((24, 28, 4.6), (56, 26, 3.4), (58, 54, 5), (26, 58, 3.2), (48, 62, 2.6)): cc(a, x, y, r, "#fcd34d", w=1.0)
    shine(a, 28, 22, 4, 1.8); face(a, 40, 41, "sleep", "smile", 7, 2.5, my=48, cheeks=True)
    star(a, 8, 12, 5); star(a, 71, 68, 4.4, "#fde047")


@st("marte", "Marte", "Mars")
def _(a):
    cc(a, 68, 14, 5, "#a8a29e", w=1.3)
    cc(a, 38, 42, 27, "#f87171")
    for x, y, r, ry in ((22, 30, 5, 4), (56, 54, 6, 4.4), (54, 28, 3, 2.4), (24, 56, 3.4, 2.6)): cc(a, x, y, r, "#dc2626", ry=ry, w=1.0)
    arc(a, 38, 42, 27, 245, 295, color="#ffffff", w=3.2)
    shine(a, 26, 28, 4, 1.8); face(a, 38, 43, "dot", "smile", 7, 2.6, my=50, cheeks=True)


@st("sol-lentes", "Sol con lentes", "Sun with sunglasses")
def _(a):
    star(a, 40, 40, 37, "#f59e0b", 12); cc(a, 40, 40, 23, "#fde047"); shine(a, 30, 28, 4, 1.8)
    rr(a, 24, 32, 38, 43, 3, "#111827", w=1.4); rr(a, 42, 32, 56, 43, 3, "#111827", w=1.4)
    ln(a, 38, 36, 42, 36, w=2); ln(a, 24, 35, 20, 33, w=1.8); ln(a, 56, 35, 60, 33, w=1.8)
    a.line(27, 35, 31, 35, color="#94a3b8", w=1.2); a.line(45, 35, 49, 35, color="#94a3b8", w=1.2)
    smile(a, 40, 47, 6.5, 2.2); blush(a, 40, 46, 15)


@st("cometa", "Cometa", "Comet")
def _(a):
    pg(a, 67.5, 37, 50.5, 17, 4, 74, fill="#bae6fd", w=1.3)
    pg(a, 64, 33, 54, 21, 16, 62, fill="#e0f2fe", w=0.9)
    cc(a, 59, 27, 13, "#7dd3fc"); shine(a, 54, 21, 3.4, 1.6); tiny(a, 59, 27, "dot", "smile", 4.8, 2, my=33)
    star(a, 18, 18, 4.4, "#fde047"); star(a, 72, 62, 3.8, "#fde047"); star(a, 12, 46, 3, "#ffffff")


@st("estrella-centelleante", "Estrella centelleante", "Twinkling star")
def _(a):
    pts = []
    for k in range(8):
        r_ = 34 if k % 2 == 0 else 10; t = math.radians(-90 + 45 * k); pts += [40 + r_ * math.cos(t), 40 + r_ * math.sin(t)]
    pg(a, *pts, fill="#fde047", w=1.8); shine(a, 36, 30, 2.6, 1.3); tiny(a, 40, 40, "dot", "smile", 5, 2.1, my=46)
    for x, y, r_ in ((12, 14, 5), (70, 14, 4), (68, 68, 5.4), (12, 66, 3.6)):
        q = []
        for k in range(8): rr_ = r_ if k % 2 == 0 else r_ * 0.3; t = math.radians(-90 + 45 * k); q += [x + rr_ * math.cos(t), y + rr_ * math.sin(t)]
        pg(a, *q, fill="#fef08a", w=1.0)


@st("galaxia", "Galaxia", "Galaxy")
def _(a):
    cc(a, 40, 40, 33, "#1e1b4b")
    for base, col, w in ((0, "#f472b6", 3.4), (180, "#a78bfa", 3.4), (90, "#c084fc", 2), (270, "#f9a8d4", 2)):
        pts = []
        for k in range(28):
            t = k / 27; ang = math.radians(base + t * 230); r_ = 6 + t * 24
            pts.append((40 + r_ * math.cos(ang), 40 + r_ * math.sin(ang)))
        a._add(pts, col, w)
    for x, y in ((18, 22), (60, 18), (64, 56), (22, 62), (50, 66), (30, 16)): a.circle(x, y, 1.1, color="#ffffff", fill=True)
    cc(a, 40, 40, 8, "#fde047", w=1.4); tiny(a, 40, 40, "dot", "smile", 2.8, 1.2, my=43.5)


@st("satelite", "Satélite", "Satellite")
def _(a):
    for x0, x1 in ((3, 27), (53, 77)):
        rr(a, x0, 29, x1, 51, 2, "#3b82f6", w=1.6)
        for k in range(1, 4): ln(a, x0 + (x1 - x0) * k / 4, 29, x0 + (x1 - x0) * k / 4, 51, color="#bfdbfe", w=0.8)
        ln(a, x0, 40, x1, 40, color="#bfdbfe", w=0.8)
    ln(a, 27, 40, 30, 40, w=2.4); ln(a, 50, 40, 53, 40, w=2.4)
    ln(a, 40, 27, 40, 17, w=1.8); a.poly(31, 6, 49, 6, 40, 17, color="#e2e8f0", fill=True); a.poly(31, 6, 49, 6, 40, 17, color=OL, w=1.5); cc(a, 40, 6, 2.2, "#ef4444", w=1.0)
    rr(a, 30, 26, 50, 54, 4, "#fbbf24"); ln(a, 30, 33, 50, 33, color="#f59e0b", w=1.2); face(a, 40, 40, "dot", "smile", 5.4, 2.1, my=48, cheeks=False)
    rr(a, 34, 54, 46, 60, 2, "#94a3b8", w=1.3)


@st("estacion", "Estación espacial", "Space station")
def _(a):
    ln(a, 4, 40, 76, 40, color=OL, w=4.6); ln(a, 4, 40, 76, 40, color="#cbd5e1", w=2.6)
    for x0, x1 in ((6, 24), (56, 74)):
        for y0, y1 in ((8, 32), (48, 72)):
            rr(a, x0, y0, x1, y1, 2, "#3b82f6", w=1.5); ln(a, (x0 + x1) / 2, y0, (x0 + x1) / 2, y1, color="#bfdbfe", w=0.8); ln(a, x0, (y0 + y1) / 2, x1, (y0 + y1) / 2, color="#bfdbfe", w=0.8)
    rr(a, 26, 30, 54, 50, 6, "#f1f5f9"); rr(a, 54, 35, 60, 45, 1.5, "#94a3b8", w=1.3); rr(a, 20, 35, 26, 45, 1.5, "#94a3b8", w=1.3)
    ln(a, 26, 42, 54, 42, color="#cbd5e1", w=0.8)
    face(a, 40, 36, "dot", "smile", 6, 2.2, my=43, cheeks=True)


@st("telescopio-espacial", "Telescopio espacial", "Space telescope")
def _(a):
    for y0, y1 in ((4, 22), (58, 76)):
        rr(a, 26, y0, 46, y1, 2, "#3b82f6", w=1.5); ln(a, 36, y0, 36, y1, color="#bfdbfe", w=0.8); ln(a, 26, (y0 + y1) / 2, 46, (y0 + y1) / 2, color="#bfdbfe", w=0.8)
    ln(a, 36, 22, 36, 26, w=2.4); ln(a, 36, 54, 36, 58, w=2.4)
    rr(a, 14, 26, 62, 54, 6, "#cbd5e1"); rr(a, 14, 26, 24, 54, 4, "#fbbf24", w=1.5); rr(a, 54, 26, 62, 54, 3, "#94a3b8", w=1.5)
    cc(a, 66, 40, 5, "#0f172a", ry=13, w=1.8); a.circle(66, 40, 2.6, color="#38bdf8", fill=True, ry=8)
    shine(a, 40, 31, 7, 1.4); face(a, 38, 41, "dot", "smile", 6.5, 2.4, my=48, cheeks=True)


@st("alienigena", "Alienígena", "Alien")
def _(a):
    for s in (-1, 1): ln(a, 40 + s * 10, 12, 40 + s * 15, 4, w=1.8); cc(a, 40 + s * 15, 4, 2.6, "#fde047", w=1.3)
    thick(a, 33, 58, 25, 66, color="#4ade80", w=3.6); thick(a, 47, 58, 55, 66, color="#4ade80", w=3.6)
    rr(a, 31, 52, 49, 72, 7, "#4ade80"); ln(a, 40, 58, 40, 66, color="#16a34a", w=1.2)
    cc(a, 40, 30, 23, "#86efac", ry=20); shine(a, 28, 20, 4, 1.8)
    for s in (-1, 1):
        cx = 40 + s * 10; a.circle(cx, 31, 6, color="#0f172a", fill=True, ry=8.5); a.circle(cx, 31, 6, color=OL, w=0.6, ry=8.5)
        a.circle(cx - 1.6, 28, 1.6, color="#ffffff", fill=True)
    smile(a, 40, 43, 5, 1.8)


@st("agujero-negro", "Agujero negro", "Black hole")
def _(a):
    a.circle(40, 40, 34, color=OL, w=2, ry=11, fill=True); a.circle(40, 40, 34, color="#f97316", fill=True, ry=11)
    a.circle(40, 40, 27, color="#fde047", fill=True, ry=7)
    cc(a, 40, 40, 18, "#020617", w=1.6)
    arc(a, 40, 40, 34, 8, 172, color=OL, w=5.6, ry=11); arc(a, 40, 40, 34, 8, 172, color="#f97316", w=3.4, ry=11); arc(a, 40, 40, 27, 8, 172, color="#fde047", w=2.4, ry=7)
    for s in (-1, 1): cc(a, 40 + s * 6.5, 36, 2.4, "#e2e8f0", w=0.4)
    arc(a, 40, 41, 5, 25, 155, color="#e2e8f0", w=1.8); blush(a, 40, 41, 11, 2, "#a78bfa")
    star(a, 10, 12, 3.4); star(a, 70, 66, 3.4)


@st("constelacion", "Constelación", "Constellation")
def _(a):
    rr(a, 5, 5, 75, 75, 10, "#1e1b4b")
    pts = [(14, 54), (27, 47), (38, 51), (46, 42), (64, 41), (62, 25), (47, 28)]
    ln(a, pts[0][0], pts[0][1], pts[1][0], pts[1][1], pts[2][0], pts[2][1], pts[3][0], pts[3][1], color="#a5b4fc", w=1.4)
    ln(a, 46, 42, 64, 41, 62, 25, 47, 28, 46, 42, color="#a5b4fc", w=1.4)
    for x, y in pts: star(a, x, y, 4.6, "#fde047")
    for x, y in ((18, 16), (60, 14), (24, 66), (56, 62), (70, 54), (14, 34)): a.circle(x, y, 1.2, color="#e0e7ff", fill=True)


@st("capsula", "Cápsula con paracaídas", "Capsule with parachute")
def _(a):
    pts = [(40 + 24 * math.cos(math.radians(t)), 28 + 24 * math.sin(math.radians(t))) for t in range(180, 361, 10)]
    ps = []
    for x, y in pts: ps += [x, y]
    pg(a, *ps, fill="#ef4444", w=1.7)
    pg(a, 28, 28, 28, 7.2, 52, 7.2, 52, 28, fill="#f8fafc", w=1.3)
    ln(a, 28, 28, 28, 7.2, w=1.3); ln(a, 52, 28, 52, 7.2, w=1.3)
    for x in (16, 28, 52, 64): ln(a, x, 28, 35 if x < 40 else 45, 49, w=1.2)
    tiny(a, 40, 15.5, "dot", "smile", 5, 2, my=21.5)
    pg(a, 35, 49, 45, 49, 52, 68, 28, 68, fill="#e2e8f0", w=1.7); rr(a, 27, 67, 53, 74, 3, "#f59e0b", w=1.5)
    cc(a, 40, 58, 5, "#bae6fd", w=1.6); tiny(a, 40, 57.6, "dot", "smile", 2.4, 1.0, my=60.4)


@st("rover-lunar", "Rover lunar", "Lunar rover")
def _(a):
    ln(a, 60, 40, 66, 22, w=1.8); a.poly(60, 16, 74, 20, 66, 27, color="#e2e8f0", fill=True); a.poly(60, 16, 74, 20, 66, 27, color=OL, w=1.4)
    for x in (28, 46): rr(a, x - 5, 28, x + 5, 42, 2.5, "#64748b", w=1.5)
    rr(a, 12, 40, 68, 56, 5, "#cbd5e1"); ln(a, 12, 46, 68, 46, color="#94a3b8", w=1.0)
    for x in (18, 33, 49, 63): wheel(a, x, 63, 7, "#475569", "#e2e8f0")
    face(a, 40, 50, "dot", "smile", 6, 2.1, my=54.6)


@st("meteorito", "Meteorito", "Meteorite")
def _(a):
    pg(a, 48.2, 59.7, 23.8, 36.3, 76, 6, fill="#fb923c", w=1.4)
    pg(a, 44, 54, 28, 40, 66, 14, fill="#fde047", w=0.9)
    pg(a, 20, 44, 26, 32, 40, 30, 52, 38, 54, 54, 44, 66, 28, 66, 18, 56, fill="#a8a29e", w=1.9)
    for x, y, r in ((30, 38, 3.2), (46, 56, 3.6), (24, 56, 2.2)): cc(a, x, y, r, "#78716c", w=1.0)
    shine(a, 32, 36, 3, 1.4); face(a, 38, 50, "dot", "smile", 6, 2.3, my=56)
