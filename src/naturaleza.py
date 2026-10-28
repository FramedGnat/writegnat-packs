import math
from wgpack import Pack
from _draw import *

pack = Pack("naturaleza", "Naturaleza y clima", "24 elementos con carita: plantas, paisajes, clima y cielo para decorar tus apuntes.",
            "General", "🌳", en={"Naturaleza y clima": "Nature and weather",
            "24 elementos con carita: plantas, paisajes, clima y cielo para decorar tus apuntes.":
            "24 little characters: plants, landscapes, weather and sky to decorate your notes."})
P = pack
S = 80.0


def st(sid, name, en):
    return P.sticker("naturaleza-" + sid, name, en, S, S)


@st("arbol", "Árbol", "Tree")
def _(a):
    pg(a, 34, 76, 36, 44, 44, 44, 46, 76, fill="#92400e", w=1.8); ln(a, 40, 54, 30, 44, color=OL, w=3.4); ln(a, 40, 54, 30, 44, color="#92400e", w=1.8)
    for x, y, r in ((24, 34, 14), (56, 34, 14), (40, 22, 17), (32, 44, 12), (48, 44, 12)): cc(a, x, y, r, "#22c55e", w=1.8)
    for x, y, r in ((24, 34, 13), (56, 34, 13), (40, 22, 16), (32, 44, 11), (48, 44, 11)): a.circle(x, y, r, color="#22c55e", fill=True)
    cc(a, 52, 30, 2.6, "#ef4444", w=1) ; cc(a, 28, 40, 2.6, "#ef4444", w=1)
    face(a, 40, 32, "dot", "smile", 8, 2.6, my=38, cheeks=True); shine(a, 28, 18, 4, 2)


@st("pino", "Pino", "Pine tree")
def _(a):
    rr(a, 35, 62, 45, 76, 2, "#92400e", w=1.7)
    pg(a, 40, 4, 22, 28, 58, 28, fill="#16a34a", w=1.8); pg(a, 40, 18, 16, 46, 64, 46, fill="#22c55e", w=1.8); pg(a, 40, 34, 10, 66, 70, 66, fill="#4ade80", w=1.8)
    star(a, 40, 6, 4, "#fde047"); face(a, 40, 50, "dot", "smile", 8, 2.6, my=56, cheeks=True)
    for x, y, c in ((26, 60, "#ef4444"), (54, 61, "#fbbf24"), (34, 40, "#38bdf8")): cc(a, x, y, 2, c, w=0.8)


@st("tulipan", "Tulipán", "Tulip")
def _(a):
    ln(a, 40, 40, 40, 76, color=OL, w=5.4); ln(a, 40, 40, 40, 76, color="#22c55e", w=3); pg(a, 40, 64, 18, 50, 26, 70, fill="#4ade80", w=1.6); pg(a, 40, 70, 62, 56, 58, 76, fill="#4ade80", w=1.6)
    pg(a, 20, 10, 30, 22, 40, 8, 50, 22, 60, 10, 62, 34, 52, 46, 28, 46, 18, 34, fill="#f472b6", w=1.9); pg(a, 30, 22, 40, 8, 50, 22, 50, 40, 30, 40, fill="#fb7185", w=1.4)
    face(a, 40, 32, "dot", "smile", 6, 2.3, my=38, cheeks=False); blush(a, 40, 37, 12)


@st("girasol", "Girasol", "Sunflower")
def _(a):
    ln(a, 40, 50, 40, 78, color=OL, w=5.4); ln(a, 40, 50, 40, 78, color="#22c55e", w=3); pg(a, 40, 66, 22, 56, 26, 72, fill="#4ade80", w=1.5)
    for k in range(12):
        t = math.radians(k * 30); cc(a, 40 + 25 * math.cos(t), 32 + 25 * math.sin(t), 7, "#fde047", w=1.5)
    cc(a, 40, 32, 18, "#92400e"); face(a, 40, 32, "dot", "smile", 6, 2.3, my=38, cheeks=False, col="#ffffff") if False else None
    for s in (-1, 1): cc(a, 40 + s * 6, 30, 2.5, WH, w=0.5); a.circle(40 + s * 6, 30.3, 1.2, color=OL, fill=True)
    arc(a, 40, 35, 5, 25, 155, color="#fde047", w=1.7, n=8); blush(a, 40, 36, 11, col="#fb923c")


@st("cactus", "Cactus", "Cactus")
def _(a):
    rr(a, 22, 58, 58, 76, 4, "#f97316", w=1.8); rr(a, 20, 54, 60, 62, 3, "#fb923c", w=1.7)
    rr(a, 46, 26, 60, 38, 6, "#4ade80", w=1.7); rr(a, 54, 26, 60, 50, 3, "#4ade80", w=0.1) if False else rr(a, 50, 28, 60, 48, 5, "#4ade80", w=1.7)
    rr(a, 20, 32, 34, 44, 6, "#4ade80", w=1.7); rr(a, 20, 32, 28, 52, 3, "#4ade80", w=1.7) if False else None
    rr(a, 28, 8, 52, 58, 11, "#4ade80", w=1.9)
    for x, y in ((34, 18), (46, 24), (34, 38), (46, 44)): ln(a, x - 1.5, y, x + 1.5, y, color="#fef9c3", w=1.4)
    cc(a, 40, 8, 3, "#f472b6", w=1.2)
    face(a, 40, 34, "dot", "smile", 6, 2.4, my=40, cheeks=True); shine(a, 33, 16, 2, 5)


@st("hongo", "Hongo", "Mushroom")
def _(a):
    rr(a, 28, 42, 52, 74, 8, "#fff7ed", w=1.9)
    a.circle(40, 40, 33, color="#ef4444", fill=True, ry=26); a.circle(40, 40, 33, color=OL, w=1.9, ry=26); a.rect(5, 40, 75, 48, color="#ffffff", fill=True)
    pts = [(40 + 33 * math.cos(math.radians(g)), 40 + 26 * math.sin(math.radians(g))) for g in range(180, 361, 10)]
    a._add(pts + [pts[0]], "#ef4444", 1, True); a._add(pts + [pts[0]], OL, 1.9)
    for x, y, r in ((22, 30, 4.4), (40, 20, 5), (58, 30, 4.4), (50, 38, 2.6), (30, 39, 2.6)): cc(a, x, y, r, "#fff7ed", w=1.3)
    face(a, 40, 55, "dot", "smile", 6, 2.4, my=61, cheeks=True); shine(a, 22, 22, 3, 5)


@st("hoja", "Hoja", "Leaf")
def _(a):
    pts = [(12, 68), (14, 40), (30, 16), (62, 8), (70, 14), (66, 42), (46, 64), (22, 72)]
    a._add(pts + [pts[0]], "#4ade80", 1, True); a._add(pts + [pts[0]], OL, 2)
    ln(a, 12, 70, 56, 24, color="#16a34a", w=2); ln(a, 28, 54, 24, 36, color="#16a34a", w=1.3); ln(a, 38, 44, 48, 52, color="#16a34a", w=1.3); ln(a, 46, 34, 50, 18, color="#16a34a", w=1.3)
    eyes(a, 44, 38, 6, 2.2); smile(a, 44, 42, 3.4, 1.4); blush(a, 44, 42, 11); shine(a, 28, 28, 2, 6)


@st("montana", "Montaña", "Mountain")
def _(a):
    pg(a, 4, 72, 28, 24, 52, 72, fill="#94a3b8", w=1.9); pg(a, 34, 72, 56, 34, 78, 72, fill="#64748b", w=1.9)
    pg(a, 28, 24, 20, 38, 26, 35, 30, 40, 36, 36, 36, 36, fill="#f8fafc", w=1.4) if False else pg(a, 28, 24, 19, 40, 24, 37, 28, 42, 33, 37, 37, 40, fill="#f8fafc", w=1.5)
    pg(a, 56, 34, 50, 44, 55, 41, 58, 46, 62, 42, 64, 46, fill="#f8fafc", w=1.3) if False else None
    face(a, 28, 54, "dot", "smile", 6, 2.4, my=59, cheeks=True); cc(a, 66, 14, 6, "#fde047", w=1.5)


@st("volcan", "Volcán", "Volcano")
def _(a):
    for x, y, r in ((36, 10, 5), (46, 6, 4), (42, 16, 4)): cc(a, x, y, r, "#cbd5e1", w=1.4)
    pg(a, 8, 74, 30, 28, 52, 28, 74, 74, fill="#a16207", w=1.9); pg(a, 30, 28, 52, 28, 50, 22, 32, 22, fill="#ef4444", w=1.7)
    pg(a, 34, 28, 38, 36, 40, 30, 44, 42, 46, 28, fill="#fb923c", w=1.2) if False else a._add([(36, 28), (35, 38), (40, 40), (44, 36), (46, 28)], "#fb923c", 2.6)
    face(a, 41, 56, "dot", "smile", 8, 2.6, my=62, cheeks=True); shine(a, 26, 46, 2.4, 5)


@st("isla", "Isla", "Island")
def _(a):
    a.circle(40, 70, 36, color="#38bdf8", fill=True, ry=9); a.circle(40, 70, 36, color=OL, w=1.8, ry=9)
    a.circle(40, 62, 24, color="#fde68a", fill=True, ry=8); a.circle(40, 62, 24, color=OL, w=1.8, ry=8)
    a._add([(40, 62), (38, 44), (42, 28)], OL, 5.6); a._add([(40, 62), (38, 44), (42, 28)], "#92400e", 3.2)
    for ang, c in ((-160, "#16a34a"), (-110, "#22c55e"), (-60, "#16a34a"), (-10, "#22c55e")):
        r = math.radians(ang); pg(a, 42, 28, 42 + 20 * math.cos(r) - 3, 28 + 14 * math.sin(r) - 2, 42 + 20 * math.cos(r) + 4, 28 + 14 * math.sin(r) + 5, fill=c, w=1.4)
    face(a, 40, 60, "dot", "smile", 8, 2.4, my=64) if False else None
    for s in (-1, 1): cc(a, 40 + s * 9, 62, 2.2, OL, w=0.4)
    smile(a, 40, 63, 3.4, 1.4); cc(a, 54, 14, 6, "#fde047", w=1.4)


@st("nube", "Nube", "Cloud")
def _(a):
    for x, y, r in ((24, 46, 14), (40, 34, 18), (58, 44, 15), (44, 52, 14)): cc(a, x, y, r, "#e0f2fe", w=1.9)
    for x, y, r in ((24, 46, 13), (40, 34, 17), (58, 44, 14), (44, 52, 13)): a.circle(x, y, r, color="#e0f2fe", fill=True)
    a.rect(24, 50, 56, 62, color="#e0f2fe", fill=True) if False else None
    shine(a, 32, 28, 5, 2.4); face(a, 42, 46, "dot", "smile", 8, 2.6, my=52, cheeks=True)


@st("lluvia", "Nube con lluvia", "Rain cloud")
def _(a):
    for x, y, r in ((22, 28, 12), (38, 20, 15), (56, 28, 13), (42, 34, 12)): cc(a, x, y, r, "#cbd5e1", w=1.9)
    for x, y, r in ((22, 28, 11), (38, 20, 14), (56, 28, 12), (42, 34, 11)): a.circle(x, y, r, color="#cbd5e1", fill=True)
    face(a, 40, 28, "dot", "smile", 8, 2.5, my=34, cheeks=True)
    for x, y in ((22, 52), (34, 60), (46, 52), (58, 60), (28, 68), (52, 70)): pg(a, x, y - 5, x - 3.2, y + 1, x + 3.2, y + 1, fill="#38bdf8", w=1.3); cc(a, x, y + 1, 3.2, "#38bdf8", w=1.3) if False else None


@st("rayo", "Rayo", "Lightning")
def _(a):
    for x, y, r in ((24, 20, 11), (38, 14, 13), (54, 20, 12), (42, 26, 11)): cc(a, x, y, r, "#64748b", w=1.9)
    for x, y, r in ((24, 20, 10), (38, 14, 12), (54, 20, 11), (42, 26, 10)): a.circle(x, y, r, color="#64748b", fill=True)
    pg(a, 44, 24, 26, 46, 38, 46, 30, 76, 56, 38, 42, 38, 52, 24, fill="#fde047", w=1.9)
    eyes(a, 40, 18, 7, 2.3, "dot", WH) if False else None
    for s in (-1, 1): cc(a, 40 + s * 7, 18, 2.4, WH, w=0.4); a.circle(40 + s * 7, 18.2, 1.2, color=OL, fill=True)
    arc(a, 40, 21, 4, 25, 155, color=WH, w=1.6, n=8)


@st("arcoiris", "Arcoíris", "Rainbow")
def _(a):
    for k, c in enumerate(("#ef4444", "#fb923c", "#fde047", "#4ade80", "#38bdf8", "#a78bfa")):
        r = 34 - k * 4.6; arc(a, 40, 58, r, 180, 360, color=OL, w=5.8, n=24); 
    for k, c in enumerate(("#ef4444", "#fb923c", "#fde047", "#4ade80", "#38bdf8", "#a78bfa")):
        r = 34 - k * 4.6; arc(a, 40, 58, r, 180, 360, color=c, w=4.2, n=24)
    for x, y, r in ((12, 62, 8), (22, 66, 8), (68, 62, 8), (58, 66, 8)): cc(a, x, y, r, "#ffffff", w=1.8)
    for x, y, r in ((12, 62, 7), (22, 66, 7), (68, 62, 7), (58, 66, 7)): a.circle(x, y, r, color="#ffffff", fill=True)
    for s in (-1, 1): cc(a, 40 + s * 40 * 0 + (-8 if s < 0 else 8), 66, 0.1, OL, w=0.1)
    for x in (16, 63): cc(a, x - 2, 64, 1.5, OL, w=0.3); cc(a, x + 3, 64, 1.5, OL, w=0.3); smile(a, x + 0.5, 66, 2, 1.1)


@st("copo", "Copo de nieve", "Snowflake")
def _(a):
    for k in range(6):
        t = math.radians(k * 60 - 90); ex, ey = 40 + 32 * math.cos(t), 40 + 32 * math.sin(t)
        ln(a, 40, 40, ex, ey, color=OL, w=5.6); ln(a, 40, 40, ex, ey, color="#7dd3fc", w=3.2)
        for f, sp in ((0.62, 8), (0.8, 6)):
            bx, by = 40 + 32 * f * math.cos(t), 40 + 32 * f * math.sin(t)
            for d in (-1, 1):
                u = t + d * math.radians(50); ln(a, bx, by, bx + sp * math.cos(u), by + sp * math.sin(u), color=OL, w=4.2); ln(a, bx, by, bx + sp * math.cos(u), by + sp * math.sin(u), color="#7dd3fc", w=2.2)
    cc(a, 40, 40, 11, "#e0f2fe"); face(a, 40, 40, "dot", "smile", 4.2, 1.8, my=45)


@st("luna", "Luna", "Moon")
def _(a):
    pts = []
    for g in range(-60, 241, 8): pts.append((40 + 30 * math.cos(math.radians(g)), 40 + 30 * math.sin(math.radians(g))))
    for g in range(240, -61, -8): pts.append((50 + 24 * math.cos(math.radians(g)), 38 + 24 * math.sin(math.radians(g))))
    pts = []
    for g in range(-50, 231, 7): pts.append((38 + 30 * math.cos(math.radians(g)), 42 + 30 * math.sin(math.radians(g))))
    for g in range(230, -51, -7): pts.append((50 + 25 * math.cos(math.radians(g)), 36 + 25 * math.sin(math.radians(g))))
    a._add(pts + [pts[0]], "#fde68a", 1, True); a._add(pts + [pts[0]], OL, 2)
    cc(a, 20, 52, 3.4, "#fcd34d", w=1.1); cc(a, 26, 30, 2.4, "#fcd34d", w=1)
    cc(a, 17, 38, 2, OL, w=0.4); arc(a, 15, 47, 3, 20, 160, w=1.4, n=8); a.circle(14, 43, 2.2, color="#fb7185", fill=True, ry=1.4)
    star(a, 62, 18, 6, "#fde047"); star(a, 70, 42, 4, "#fde047"); star(a, 56, 66, 3.6, "#fde047"); shine(a, 22, 28, 2.4, 5)


@st("solnube", "Sol con nube", "Sun and cloud")
def _(a):
    for k in range(10): r = math.radians(36 * k); ln(a, 30 + 17 * math.cos(r), 30 + 17 * math.sin(r), 30 + 25 * math.cos(r), 30 + 25 * math.sin(r), color="#f59e0b", w=3)
    cc(a, 30, 30, 16, "#fde047"); shine(a, 24, 24, 3, 1.6)
    for s in (-1, 1): cc(a, 30 + s * 5.4, 28, 2.2, OL, w=0.4)
    smile(a, 30, 32, 4, 1.5)
    for x, y, r in ((46, 58, 11), (58, 50, 14), (68, 60, 10), (56, 64, 11)): cc(a, x, y, r, "#f8fafc", w=1.8)
    for x, y, r in ((46, 58, 10), (58, 50, 13), (68, 60, 9), (56, 64, 10)): a.circle(x, y, r, color="#f8fafc", fill=True)
    eyes(a, 58, 58, 6, 2.2); smile(a, 58, 62, 3.4, 1.4); blush(a, 58, 62, 11)


@st("estrella-fugaz", "Estrella fugaz", "Shooting star")
def _(a):
    for k, (dx, dy, c) in enumerate(((0, 0, "#fde68a"), (-1, -5, "#fcd34d"))):
        pass
    a.poly(52, 28, 6, 70, 10, 74, 56, 36, color="#bae6fd", fill=True); a.poly(52, 28, 6, 70, 10, 74, 56, 36, color=OL, w=1.5)
    a._add([(14, 54), (30, 42)], "#7dd3fc", 2.4); a._add([(20, 66), (38, 52)], "#e0f2fe", 2.4)
    star(a, 56, 28, 22, "#fde047"); face(a, 56, 30, "dot", "smile", 6.4, 2.3, my=36, cheeks=True); shine(a, 46, 20, 2.4, 4)
    star(a, 20, 20, 4, "#fde047"); star(a, 70, 66, 3.6, "#fde047")


@st("fogata", "Fogata", "Campfire")
def _(a):
    a._add([(14, 70), (66, 58)], OL, 9); a._add([(14, 70), (66, 58)], "#92400e", 6.4); a._add([(14, 58), (66, 70)], OL, 9); a._add([(14, 58), (66, 70)], "#a16207", 6.4)
    pg(a, 40, 6, 58, 34, 62, 54, 52, 64, 28, 64, 18, 54, 22, 34, 34, 28, fill="#fb923c", w=1.9)
    pg(a, 40, 26, 52, 44, 54, 56, 46, 62, 34, 62, 26, 56, 28, 44, fill="#fde047", w=1.4)
    face(a, 40, 50, "dot", "smile", 6, 2.3, my=56, cheeks=True)


@st("ola", "Ola", "Wave")
def _(a):
    pts = [(4, 74), (4, 46), (14, 36), (28, 34), (40, 24), (54, 16), (68, 22), (62, 30), (52, 28), (46, 38), (56, 46), (70, 52), (76, 74)]
    a._add(pts + [pts[0]], "#38bdf8", 1, True); a._add(pts + [pts[0]], OL, 2)
    a._add([(10, 54), (22, 46), (34, 48)], "#e0f2fe", 3); a._add([(42, 34), (52, 24), (62, 24)], "#e0f2fe", 3)
    for x, y, r in ((60, 12, 2.4), (70, 10, 1.8), (74, 20, 2)): cc(a, x, y, r, "#bae6fd", w=1)
    face(a, 34, 58, "dot", "smile", 8, 2.6, my=64, cheeks=True)


@st("tornado", "Tornado", "Tornado")
def _(a):
    for k, (y, hw) in enumerate(((10, 32), (24, 26), (38, 20), (52, 14), (66, 8))):
        a.circle(40, y, hw, color="#94a3b8" if k % 2 == 0 else "#cbd5e1", fill=True, ry=7); a.circle(40, y, hw, color=OL, w=1.7, ry=7)
    face(a, 40, 30, "dot", "smile", 8, 2.6, my=36, cheeks=False) if False else None
    eyes(a, 40, 36, 8, 2.5); smile(a, 40, 40, 4, 1.5); blush(a, 40, 40, 14)
    for x, y in ((8, 54), (70, 70), (64, 46)): a._add([(x, y), (x + 6, y - 2)], "#94a3b8", 2)


@st("paraguas", "Paraguas", "Umbrella")
def _(a):
    ln(a, 40, 36, 40, 66, color=OL, w=5); ln(a, 40, 36, 40, 66, color="#94a3b8", w=2.4)
    a._add([(40, 66), (40, 72), (34, 74)], OL, 5); a._add([(40, 66), (40, 72), (34, 74)], "#94a3b8", 2.4)
    pts = [(40 + 34 * math.cos(math.radians(g)), 40 + 28 * math.sin(math.radians(g))) for g in range(180, 361, 6)]
    a._add(pts + [pts[0]], "#ef4444", 1, True); a._add(pts + [pts[0]], OL, 2)
    for k, x in enumerate((6, 23, 40, 57, 74)):
        pass
    for x in (18, 29, 40, 51, 62): pass
    for k in range(4):
        x0 = 6 + k * 17; a.poly(x0, 40, x0 + 17, 40, 40 + (x0 + 8.5 - 40) * 0.3, 14 + abs(x0 + 8.5 - 40) * 0.2, color="#00000000", w=0.1) if False else None
    for x in (23, 40, 57): ln(a, x, 40, 40 + (x - 40) * 0.55, 12 + abs(x - 40) * 0.1, color=OL, w=1.3)
    for x in (6, 23, 40, 57): arc(a, x + 8.5, 40, 8.5, 0, 180, color=OL, w=1.8, n=8)
    for s in (-1, 1): cc(a, 40 + s * 8, 28, 2.6, OL, w=0.4)
    smile(a, 40, 32, 4.4, 1.6); blush(a, 40, 33, 14); shine(a, 22, 20, 3, 4)


@st("viento", "Viento", "Wind")
def _(a):
    for y, x1, c in ((26, 62, "#7dd3fc"), (42, 70, "#bae6fd"), (58, 56, "#7dd3fc")):
        a._add([(8, y), (x1 - 12, y), (x1, y - 4), (x1 + 4, y - 14), (x1 - 8, y - 16)], OL, 7.4); a._add([(8, y), (x1 - 12, y), (x1, y - 4), (x1 + 4, y - 14), (x1 - 8, y - 16)], c, 4.6)
    cc(a, 22, 44, 11, "#e0f2fe", w=1.8); eyes(a, 22, 42, 4.4, 1.9); smile(a, 22, 47, 2.8, 1.3); blush(a, 22, 47, 8)
    for x, y in ((66, 56), (72, 30)): a._add([(x, y), (x + 5, y + 3)], "#4ade80", 3)


@st("trebol", "Trébol", "Clover")
def _(a):
    a._add([(40, 46), (44, 62), (52, 72)], OL, 5); a._add([(40, 46), (44, 62), (52, 72)], "#16a34a", 2.8)
    for dx, dy in ((-11, -11), (11, -11), (-11, 11), (11, 11)):
        cc(a, 40 + dx, 40 + dy, 12, "#22c55e", w=1.9)
    for dx, dy in ((-11, -11), (11, -11), (-11, 11), (11, 11)): a.circle(40 + dx, 40 + dy, 11, color="#22c55e", fill=True)
    ln(a, 40, 40, 29, 29, color="#16a34a", w=1.2); ln(a, 40, 40, 51, 29, color="#16a34a", w=1.2); ln(a, 40, 40, 29, 51, color="#16a34a", w=1.2); ln(a, 40, 40, 51, 51, color="#16a34a", w=1.2)
    face(a, 40, 38, "dot", "smile", 6, 2.4, my=43, cheeks=True); shine(a, 28, 26, 3, 2)
