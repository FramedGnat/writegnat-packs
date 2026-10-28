import math
from wgpack import Pack
from _draw import *

pack = Pack("comida", "Comida y bebida", "24 antojos con carita: pizza, tacos, sushi, frutas, postres y bebidas para tus apuntes.",
            "General", "🍕", en={"Comida y bebida": "Food and drinks",
            "24 antojos con carita: pizza, tacos, sushi, frutas, postres y bebidas para tus apuntes.":
            "24 snacks with little faces: pizza, tacos, sushi, fruit, desserts and drinks for your notes."})
P = pack
S = 80.0


def st(sid, name, en):
    return P.sticker("comida-" + sid, name, en, S, S)


def cheeks(a, cx, cy, gap): blush(a, cx, cy, gap)


@st("pizza", "Pizza", "Pizza")
def _(a):
    pg(a, 40, 76, 8, 20, 72, 20, fill="#fcd34d")
    pg(a, 8, 20, 72, 20, 70, 28, 10, 28, fill="#d97706", w=1.8)
    for x, y, r in ((24, 31, 4.2), (50, 33, 4.6), (34, 52, 4), (45, 45, 3.6), (40, 63, 3)): cc(a, x, y, r, "#ef4444", w=1.3)
    for x, y in ((55, 38), (28, 42), (38, 36)): a.circle(x, y, 1.5, color="#16a34a", fill=True)
    face(a, 40, 44, "dot", "smile", 5, 2.2, my=51, cheeks=False); blush(a, 40, 49, 11)
    shine(a, 16, 24, 3, 1)


@st("hamburguesa", "Hamburguesa", "Burger")
def _(a):
    a.circle(40, 30, 28, color="#f59e0b", fill=True, ry=17); a.circle(40, 30, 28, color=OL, w=1.8, ry=17); a.rect(8, 30, 72, 34, color="#f59e0b", fill=True)
    for x, y in ((26, 20), (38, 15), (50, 21), (58, 27), (30, 28)): a.circle(x, y, 1.6, color="#fef3c7", fill=True, ry=0.9)
    rr(a, 10, 34, 70, 42, 3, "#84cc16", w=1.5); rr(a, 10, 40, 70, 52, 6, "#78350f", w=1.8); pg(a, 12, 42, 68, 42, 62, 50, 18, 50, fill="#fbbf24", w=1.2) if False else None
    a._add([(14, 42), (66, 42), (62, 47), (52, 44), (42, 48), (30, 44), (20, 47)], "#fbbf24", 1, True)
    rr(a, 8, 54, 72, 66, 6, "#f59e0b", w=1.8)
    face(a, 40, 46, "dot", "smile", 8, 2.2, my=52, cheeks=False)


@st("taco", "Taco", "Taco")
def _(a):
    a.circle(40, 52, 32, color="#fde68a", fill=True, ry=32); a.rect(0, 52, 80, 80, color="#ffffff", fill=True)
    pts = [(40 + 32 * math.cos(math.radians(g)), 56 + 32 * math.sin(math.radians(g))) for g in range(180, 361, 10)]
    a._add(pts + [pts[0]], "#fbbf24", 1, True); a._add(pts + [pts[0]], OL, 2)
    for x, y, c in ((22, 34, "#84cc16"), (34, 26, "#ef4444"), (48, 26, "#84cc16"), (60, 34, "#ef4444"), (40, 30, "#fde047")): cc(a, x, y, 5, c, w=1.3)
    pts2 = [(40 + 24 * math.cos(math.radians(g)), 56 + 24 * math.sin(math.radians(g)) * 0.9) for g in range(180, 361, 10)]
    a._add(pts2 + [(66, 70), (14, 70)], "#fbbf24", 1, True); a._add(pts2 + [(66, 70), (14, 70)], OL, 1.8)
    ln(a, 8, 56, 72, 56, color=OL, w=1.8) if False else None
    face(a, 40, 55, "dot", "smile", 8, 2.5, my=61); blush(a, 40, 60, 15); shine(a, 22, 44, 5, 1.8)


@st("sushi", "Sushi", "Sushi")
def _(a):
    rr(a, 14, 38, 66, 66, 10, "#1e293b"); rr(a, 17, 34, 63, 60, 10, "#f8fafc", w=1.8)
    pg(a, 12, 30, 68, 30, 64, 46, 16, 46, fill="#fb7185", w=1.8)
    for x in (26, 40, 54): ln(a, x, 33, x - 2, 43, color="#fecdd3", w=1.4)
    rr(a, 34, 36, 46, 66, 1, "#1e293b", w=0.1) if False else None
    face(a, 40, 54, "dot", "smile", 8, 2.5, my=59); blush(a, 40, 58, 15); shine(a, 22, 36, 4, 1)


@st("helado", "Helado", "Ice cream")
def _(a):
    pg(a, 22, 40, 58, 40, 40, 76, fill="#fcd34d", w=1.8)
    for k in range(4): ln(a, 25 + k * 3, 44 + k * 7, 55 - k * 3, 44 + k * 7, color="#d97706", w=1.2); ln(a, 28 + k * 4, 40, 40, 70, color="#d97706", w=0.1) if False else None
    for k in range(3): ln(a, 30 + k * 10, 42, 36 + k * 4, 70, color="#d97706", w=1.2)
    cc(a, 40, 28, 18, "#f9a8d4"); cc(a, 24, 36, 7, "#f9a8d4"); cc(a, 56, 36, 7, "#f9a8d4"); a.circle(40, 28, 17, color="#f9a8d4", fill=True)
    cc(a, 40, 12, 4.4, "#ef4444", w=1.4); ln(a, 40, 8, 44, 4, color="#16a34a", w=1.6)
    face(a, 40, 30, "dot", "smile", 8, 2.5, my=36); blush(a, 40, 35, 14); shine(a, 30, 20, 4, 2)


@st("dona", "Dona", "Donut")
def _(a):
    cc(a, 40, 42, 32, "#f59e0b", ry=28); cc(a, 40, 38, 31, "#f9a8d4", ry=26)
    a.circle(40, 38, 31, color="#f9a8d4", fill=True, ry=26)
    cc(a, 40, 38, 9, WH, ry=7.5, w=1.8)
    for x, y, c in ((18, 32, "#fde047"), (26, 20, "#38bdf8"), (52, 17, "#a78bfa"), (62, 30, "#fde047"), (20, 48, "#38bdf8"), (62, 50, "#4ade80"), (46, 58, "#fde047"), (30, 58, "#a78bfa")):
        a._add([(x - 2.4, y - 1), (x + 2.4, y + 1)], c, 2.8)
    eyes(a, 40, 54, 6, 2.2) if False else None
    for s in (-1, 1): cc(a, 40 + s * 17, 38, 2.1, OL, w=0.4)
    smile(a, 40, 16, 5, 1.6) if False else None
    arc(a, 40, 62, 3.4, 25, 155, w=1.5, n=8); shine(a, 22, 24, 4, 1.8)


@st("pastel", "Pastel", "Cake")
def _(a):
    rr(a, 12, 38, 68, 70, 6, "#fde68a"); rr(a, 12, 38, 68, 52, 5, "#f9a8d4", w=1.8)
    for x in (22, 36, 50, 62): cc(a, x, 52, 4.4, "#f9a8d4", w=1.5)
    for x in (24, 40, 56): ln(a, x, 38, x, 22, color=OL, w=0.1) if False else None
    for x, c in ((26, "#38bdf8"), (40, "#f59e0b"), (54, "#a78bfa")):
        rr(a, x - 2, 22, x + 2, 38, 1, c, w=1.3); pg(a, x, 12, x - 3, 20, x + 3, 20, fill="#fb923c", w=0.9) if False else cc(a, x, 18, 2.6, "#fde047", ry=4, w=1.2)
    face(a, 40, 60, "dot", "smile", 8, 2.5, my=64) if False else None
    eyes(a, 40, 58, 8, 2.5); smile(a, 40, 61, 4, 1.6); blush(a, 40, 62, 15); rr(a, 8, 68, 72, 74, 3, "#cbd5e1", w=1.5); shine(a, 18, 44, 3, 1)


@st("manzana", "Manzana", "Apple")
def _(a):
    cc(a, 29, 46, 19, "#ef4444", ry=22); cc(a, 51, 46, 19, "#ef4444", ry=22); a.circle(40, 48, 22, color="#ef4444", fill=True, ry=22)
    ln(a, 40, 24, 42, 12, color=OL, w=4); ln(a, 40, 24, 42, 12, color="#92400e", w=2)
    pg(a, 44, 18, 58, 8, 60, 20, 48, 24, fill="#4ade80", w=1.5)
    shine(a, 26, 36, 4, 7); face(a, 40, 50, "dot", "smile", 8, 2.6, my=56, cheeks=True)


@st("platano", "Plátano", "Banana")
def _(a):
    pts = [(14, 20), (30, 36), (44, 54), (58, 62), (70, 60), (72, 68), (58, 74), (38, 68), (20, 52), (10, 34)]
    a._add(pts + [pts[0]], "#fde047", 1, True); a._add(pts + [pts[0]], OL, 2)
    pg(a, 10, 20, 18, 12, 20, 22, fill="#92400e", w=1.5); pg(a, 70, 58, 76, 60, 72, 68, fill="#92400e", w=1.3)
    ln(a, 18, 28, 42, 62, color="#facc15", w=1.4)
    eyes(a, 39, 52, 5, 2.4); smile(a, 39, 57, 3.4, 1.5) if False else arc(a, 38, 58, 4, 25, 155, w=1.5, n=8); blush(a, 38, 57, 10); shine(a, 26, 36, 2.4, 5)


@st("fresa", "Fresa", "Strawberry")
def _(a):
    pg(a, 40, 76, 13, 40, 17, 34, 63, 34, 67, 40, fill="#ef4444", w=1.9)
    cc(a, 22, 38, 12, "#ef4444"); cc(a, 58, 38, 12, "#ef4444"); a.circle(40, 38, 20, color="#ef4444", fill=True)
    for x, y in ((24, 32), (56, 32), (30, 62), (50, 62), (40, 70), (22, 46), (58, 46)): a.circle(x, y, 1.1, color="#fde68a", fill=True, ry=1.6)
    pg(a, 40, 26, 26, 22, 30, 14, 36, 20, 40, 8, 44, 20, 50, 14, 54, 22, fill="#4ade80", w=1.6)
    face(a, 40, 46, "dot", "smile", 8, 2.6, my=52, cheeks=True); shine(a, 24, 34, 3, 5)


@st("sandia", "Sandía", "Watermelon")
def _(a):
    pts = [(40 + 33 * math.cos(math.radians(g)), 20 + 52 * math.sin(math.radians(g)) * 0.9) for g in range(0, 181, 10)]
    pts = [(40 + 33 * math.cos(math.radians(g)), 22 + 46 * math.sin(math.radians(g))) for g in range(0, 181, 10)]
    a._add(pts + [pts[0]], "#16a34a", 1, True); a._add(pts + [pts[0]], OL, 2)
    pts2 = [(40 + 27 * math.cos(math.radians(g)), 22 + 38 * math.sin(math.radians(g))) for g in range(0, 181, 10)]
    a._add(pts2 + [pts2[0]], "#fecdd3", 1, True); pts3 = [(40 + 24 * math.cos(math.radians(g)), 22 + 34 * math.sin(math.radians(g))) for g in range(0, 181, 10)]
    a._add(pts3 + [pts3[0]], "#fb7185", 1, True)
    for x, y in ((28, 38), (52, 38), (40, 44), (34, 52), (46, 52)): a.circle(x, y, 1.4, color=OL, fill=True, ry=2.2)
    ln(a, 7, 22, 73, 22, color=OL, w=2)
    face(a, 40, 33, "dot", "smile", 9, 2.6, my=39); blush(a, 40, 37, 16)


@st("aguacate", "Aguacate", "Avocado")
def _(a):
    cc(a, 40, 26, 17, "#4d7c0f"); cc(a, 40, 50, 24, "#4d7c0f", ry=26); a.circle(40, 38, 19, color="#4d7c0f", fill=True, ry=24)
    cc(a, 40, 28, 13, "#bef264", w=0.1); cc(a, 40, 50, 19, "#bef264", ry=22, w=0.1); a.circle(40, 40, 15, color="#bef264", fill=True, ry=19)
    cc(a, 40, 52, 9, "#92400e", w=1.8); shine(a, 36, 48, 2.4, 1.6)
    face(a, 40, 34, "dot", "smile", 6, 2.2, my=39)


@st("brocoli", "Brócoli", "Broccoli")
def _(a):
    rr(a, 32, 44, 48, 74, 4, "#84cc16")
    for x, y, r in ((24, 36, 12), (40, 26, 14), (56, 36, 12), (34, 44, 10), (46, 44, 10)): cc(a, x, y, r, "#22c55e", w=1.7)
    for x, y, r in ((24, 36, 11), (40, 26, 13), (56, 36, 11), (34, 44, 9), (46, 44, 9)): a.circle(x, y, r, color="#22c55e", fill=True)
    face(a, 40, 52, "dot", "smile", 6, 2.3, my=58, cheeks=True); shine(a, 30, 22, 4, 2)


@st("huevo", "Huevo frito", "Fried egg")
def _(a):
    pts = [(14, 40), (12, 28), (24, 14), (40, 18), (54, 10), (68, 24), (70, 42), (62, 62), (44, 68), (28, 64), (18, 56)]
    a._add(pts + [pts[0]], "#f8fafc", 1, True); a._add(pts + [pts[0]], OL, 2)
    cc(a, 42, 40, 14, "#fbbf24"); shine(a, 37, 34, 4, 2.4)
    eyes(a, 42, 40, 5, 2, "dot"); smile(a, 42, 43, 3.4, 1.4); blush(a, 42, 44, 9)


@st("pan", "Pan", "Bread")
def _(a):
    pts = [(14, 34), (14, 24), (26, 16), (40, 22), (54, 16), (66, 24), (66, 34), (62, 40), (62, 66), (18, 66), (18, 40)]
    a._add(pts + [pts[0]], "#f59e0b", 1, True); a._add(pts + [pts[0]], OL, 2)
    rr(a, 22, 34, 58, 62, 4, "#fde68a", w=1.5); shine(a, 22, 24, 4, 1.4)
    face(a, 40, 48, "dot", "smile", 8, 2.5, my=54, cheeks=True)


@st("queso", "Queso", "Cheese")
def _(a):
    pg(a, 8, 52, 60, 24, 72, 38, 72, 62, 8, 62, fill="#fde047", w=1.9); pg(a, 8, 52, 60, 24, 72, 38, 22, 52, fill="#fef08a", w=1.5) if False else pg(a, 8, 52, 60, 24, 72, 38, 18, 58, fill="#fef9c3", w=1.5)
    for x, y, r in ((52, 53, 3.6), (24, 61, 2.6), (62, 44, 2.4)): cc(a, x, y, r, "#fbbf24", w=1.3)
    face(a, 38, 56, "dot", "smile", 7, 2.2, my=61); blush(a, 38, 60, 13)


@st("te", "Té", "Tea")
def _(a):
    a.circle(40, 44, 24, color=OL, w=0.1, ry=1) if False else None
    ln(a, 56, 40, 70, 40, color=OL, w=0.1) if False else None
    a.circle(62, 46, 9, color="#e2e8f0", fill=True, ry=8); a.circle(62, 46, 9, color=OL, w=3, ry=8); a.circle(62, 46, 3.6, color="#ffffff", fill=True, ry=3.6)
    pg(a, 10, 30, 62, 30, 56, 62, 16, 62, fill="#f8fafc"); a.poly(11, 30, 61, 30, 60.4, 36, 11.6, 36, color="#b45309", fill=True)
    rr(a, 6, 62, 66, 70, 4, "#cbd5e1", w=1.6)
    ln(a, 28, 30, 28, 14, w=1.3); rr(a, 22, 6, 34, 16, 2, "#fde68a", w=1.5); a.text(24, 8.4, "TÉ", 6, "#92400e")
    eyes(a, 36, 47, 8, 2.4); smile(a, 36, 50, 4, 1.5); blush(a, 36, 52, 15)


@st("jugo", "Jugo", "Juice box")
def _(a):
    pg(a, 18, 24, 62, 24, 62, 72, 18, 72, fill="#fb923c", w=1.9); pg(a, 18, 24, 62, 24, 56, 16, 24, 16, fill="#fdba74", w=1.7)
    ln(a, 50, 16, 56, 4, color=OL, w=3.6); ln(a, 50, 16, 56, 4, color="#38bdf8", w=2); ln(a, 56, 4, 62, 5, color=OL, w=3.6); ln(a, 56, 4, 62, 5, color="#38bdf8", w=2)
    cc(a, 40, 36, 7, "#fde047", w=1.3); ln(a, 40, 29, 40, 43, color="#f59e0b", w=1); ln(a, 33, 36, 47, 36, color="#f59e0b", w=1)
    face(a, 40, 54, "dot", "smile", 8, 2.5, my=60, cheeks=True); a.text(33, 66, "JUGO", 5.5, "#7c2d12")


@st("refresco", "Refresco", "Soda")
def _(a):
    pg(a, 22, 20, 58, 20, 54, 74, 26, 74, fill="#f8fafc", w=1.9); pg(a, 23, 38, 57, 38, 54, 74, 26, 74, fill="#ef4444", w=1.5)
    rr(a, 18, 14, 62, 22, 3, "#cbd5e1", w=1.7); ln(a, 44, 14, 52, 2, color=OL, w=3.6); ln(a, 44, 14, 52, 2, color="#fbbf24", w=2)
    for x, y in ((30, 30), (50, 28), (40, 24)): cc(a, x, y, 1.8, "#bae6fd", w=0.9)
    face(a, 40, 52, "dot", "smile", 7, 2.4, my=57, cheeks=False); blush(a, 40, 56, 13); shine(a, 30, 28, 2, 6)


@st("palomitas", "Palomitas", "Popcorn")
def _(a):
    for x, y, r in ((22, 22, 9), (36, 14, 9), (50, 14, 9), (62, 24, 9), (30, 28, 8), (46, 26, 9)): cc(a, x, y, r, "#fffbeb", w=1.6)
    pg(a, 14, 32, 66, 32, 58, 74, 22, 74, fill="#f8fafc", w=1.9)
    for x in (20, 36, 52): pg(a, x, 32, x + 14, 32, x + 12, 74, x - 2 + 2, 74, fill="#ef4444", w=0.1) if False else None
    for x0 in (14, 34, 54):
        pg(a, x0 + 4 * (x0 > 14 and 0), 32, x0 + 12, 32, x0 + 10, 74 if x0 < 54 else 74, x0 + 2, 74, fill="#ef4444", w=0.1) if False else None
    for k, x in enumerate((17, 31, 45, 59)): a._add([(x, 33), (x + 1.6 - 0.8 * (k > 1), 73)], "#ef4444", 6.2)
    pg(a, 14, 32, 66, 32, 58, 74, 22, 74, fill="#00000000", w=1.9) if False else a.poly(14, 32, 66, 32, 58, 74, 22, 74, color=OL, w=1.9)
    face(a, 40, 52, "dot", "smile", 8, 2.5, my=58); blush(a, 40, 57, 14)


@st("galleta", "Galleta", "Cookie")
def _(a):
    cc(a, 40, 40, 31, "#d6a35c"); shine(a, 26, 24, 5, 2)
    for x, y, r in ((24, 28, 4), (52, 22, 4.4), (58, 44, 4), (22, 52, 3.6), (48, 60, 4), (36, 20, 2.6), (62, 32, 2.4)): cc(a, x, y, r, "#5b3a1e", w=1.1)
    face(a, 40, 42, "dot", "smile", 8, 2.6, my=48, cheeks=True)
    a.poly(70, 54, 74, 58, 68, 60, color="#d6a35c", fill=True) if False else None


@st("paleta", "Paleta helada", "Ice pop")
def _(a):
    rr(a, 35, 52, 45, 76, 4, "#fde68a", w=1.7)
    rr(a, 20, 6, 60, 58, 20, "#f472b6"); a.round_rect(20, 6, 60, 58, 20, color=OL, w=1.9)
    pts = [(24, 30), (30, 24), (40, 30), (50, 24), (56, 30)]
    a.poly(22, 30, 30, 24, 40, 31, 50, 24, 58, 30, 58, 46, 22, 46, color="#fde047", fill=True) if False else None
    a._add([(21, 36), (28, 31), (36, 37), (44, 31), (52, 37), (59, 32)], "#38bdf8", 8)
    a.round_rect(20, 6, 60, 58, 20, color=OL, w=1.9)
    face(a, 40, 26, "dot", "smile", 8, 2.6, my=32, cheeks=True); shine(a, 28, 14, 3, 5)


@st("elote", "Elote", "Corn")
def _(a):
    pts = [(40, 6), (54, 20), (56, 56), (40, 68), (24, 56), (26, 20)]
    cc(a, 40, 38, 17, "#fde047", ry=32)
    for r_ in range(7):
        for c in range(4):
            x = 29 + c * 7.4 + (r_ % 2) * 3.2; y = 14 + r_ * 8
            a.circle(x, y, 2.9, color="#facc15", fill=True, ry=3.2); a.circle(x, y, 2.9, color="#eab308", w=0.7, ry=3.2) if False else None
    a.circle(40, 38, 17, color=OL, w=1.8, ry=32)
    pg(a, 40, 76, 16, 44, 24, 34, 40, 50, 56, 34, 64, 44, fill="#4ade80", w=1.8); ln(a, 40, 50, 40, 70, color="#16a34a", w=1.3)
    face(a, 40, 30, "dot", "smile", 7, 2.4, my=36, cheeks=True) if False else None
    for s in (-1, 1): cc(a, 40 + s * 6.5, 30, 2.4, OL, w=0.4)
    smile(a, 40, 33, 4, 1.6); blush(a, 40, 34, 11)


@st("papas", "Papas fritas", "French fries")
def _(a):
    for k, (x, y0, c) in enumerate(((22, 6, "#fde047"), (30, 2, "#fbbf24"), (40, 8, "#fde047"), (50, 3, "#fbbf24"), (58, 9, "#fde047"))):
        rr(a, x - 3.4, y0, x + 3.4, 50, 2, c, w=1.5)
    pg(a, 14, 40, 66, 40, 58, 74, 22, 74, fill="#ef4444", w=1.9); pg(a, 14, 40, 22, 40, 26, 74, 22, 74, fill="#dc2626", w=0.1) if False else None
    a.rect(14, 40, 66, 44, color="#dc2626", fill=True) if False else None
    cc(a, 40, 56, 9, "#fde047", w=1.3); a.text(33.5, 51.5, "M", 11, "#ef4444") if False else None
    face(a, 40, 56, "dot", "smile", 7, 2.3, my=61, cheeks=False); blush(a, 40, 60, 13)
