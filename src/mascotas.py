import math
from wgpack import Pack
from _draw import *

pack = Pack("mascotas", "Compañeros de estudio", "Objetos con cara por carrera y de uso diario: matraz, átomo, célula, cerebro, casco, chip, libro, calculadora, cohete y más.",
            "General", "😊", en={"Compañeros de estudio": "Study buddies",
            "Objetos con cara por carrera y de uso diario: matraz, átomo, célula, cerebro, casco, chip, libro, calculadora, cohete y más.":
            "Characters by field and everyday study objects: flask, atom, cell, brain, hard hat, chip, book, calculator, rocket and more."})
P = pack
S = 80.0


def st(sid, name, en):
    return P.sticker("mas-" + sid, name, en, S, S)


@st("matraz", "Matraz (Química)", "Flask (Chemistry)")
def _(a):
    pg(a, 33, 8, 47, 8, 47, 30, 66, 66, 66, 71, 14, 71, 14, 66, 33, 30, fill="#e0f2fe")
    pg(a, 25, 48, 55, 48, 66, 66, 66, 71, 14, 71, 14, 66, fill="#4ade80")
    rr(a, 30, 5, 50, 11, 2, "#cbd5e1", w=1.4)
    for x, y, r in ((28, 44, 2.4), (52, 41, 1.8), (47, 34, 1.4)): a.circle(x, y, r, color="#ffffff", fill=True); a.circle(x, y, r, color=OL, w=0.9)
    face(a, 40, 58, "dot", "smile", 8, 2.6, my=64, cheeks=True)


@st("atomo", "Átomo (Física)", "Atom (Physics)")
def _(a):
    for ang in (0, 60, 120):
        pts = []
        for k in range(41):
            t = 2 * math.pi * k / 40; x, y = 33 * math.cos(t), 12 * math.sin(t); r = math.radians(ang)
            pts.append((40 + x * math.cos(r) - y * math.sin(r), 40 + x * math.sin(r) + y * math.cos(r)))
        a._add(pts, "#6366f1", 2.2)
    for x, y in ((71, 40), (24, 13), (24, 67)): cc(a, x, y, 3.6, "#38bdf8", w=1.4)
    cc(a, 40, 40, 13, "#f87171"); shine(a, 35, 34, 3.4, 1.8); face(a, 40, 39, "dot", "smile", 5, 2, my=44, cheeks=False)


@st("celula", "Célula (Biología)", "Cell (Biology)")
def _(a):
    pts = []
    for k in range(61):
        t = 2 * math.pi * k / 60; r = 31 + 2.2 * math.sin(5 * t)
        pts.append((40 + r * math.cos(t), 40 + r * 0.9 * math.sin(t)))
    a._add(pts, "#bbf7d0", 1, True); a._add(pts, OL, 2)
    cc(a, 52, 29, 8.5, "#a78bfa"); cc(a, 52, 29, 3, "#7c3aed", w=1.0)
    cc(a, 20, 52, 4, "#fb923c", ry=2.6, w=1.2); cc(a, 61, 54, 4, "#fb923c", ry=2.6, w=1.2); cc(a, 24, 26, 3, "#f472b6", w=1.2)
    face(a, 38, 44, "dot", "smile", 7, 2.6, my=51, cheeks=True)


@st("cerebro", "Cerebro (Psicología)", "Brain (Psychology)")
def _(a):
    for x, y, r in ((24, 36, 14), (38, 26, 15), (54, 28, 14), (63, 42, 12), (52, 52, 15), (32, 52, 15), (18, 48, 9)):
        cc(a, x, y, r, "#fbcfe8", w=1.8)
    for x, y, r in ((24, 36, 13), (38, 26, 14), (54, 28, 13), (63, 42, 11), (52, 52, 14), (32, 52, 14), (18, 48, 8)):
        a.circle(x, y, r, color="#fbcfe8", fill=True)
    arc(a, 38, 30, 7, 200, 330, color="#f472b6", w=1.6); arc(a, 56, 40, 6, 100, 240, color="#f472b6", w=1.6); arc(a, 28, 46, 6, 330, 460, color="#f472b6", w=1.6)
    face(a, 42, 46, "dot", "smile", 8, 2.6, my=53, cheeks=True)
    rr(a, 34, 64, 46, 74, 3, "#f9a8d4", w=1.6)


@st("casco", "Casco (Civil)", "Hard hat (Civil)")
def _(a):
    pg(a, 8, 52, 72, 52, 72, 58, 8, 58, fill="#f59e0b", w=1.6)
    a.poly(14, 52, 18, 28, 40, 14, 62, 28, 66, 52, color="#fbbf24", fill=True); a.poly(14, 52, 18, 28, 40, 14, 62, 28, 66, 52, color=OL, w=1.8)
    rr(a, 34, 11, 46, 52, 3, "#f59e0b", w=1.5)
    cc(a, 40, 62, 0.1, "#fbbf24", w=0.1)
    face(a, 40, 40, "dot", "smile", 11, 2.6, my=46)
    shine(a, 24, 32, 3, 5)


@st("engrane", "Engrane (Mecánica)", "Gear (Mechanics)")
def _(a):
    gear(a, 40, 40, 31, "#94a3b8", 10, 0.0); cc(a, 40, 40, 20, "#cbd5e1", w=1.6)
    face(a, 40, 38, "dot", "smile", 7.5, 2.6, my=45, cheeks=True)


@st("chip", "Chip (Electrónica)", "Chip (Electronics)")
def _(a):
    for k in range(5):
        x = 22 + k * 9
        for y0, y1 in ((8, 16), (64, 72)): ln(a, x, y0, x, y1, color="#d1d5db", w=3.2); ln(a, x, y0, x, y1, color=OL, w=0.6)
        for xx0, xx1, yy in ((8, 16, x), (64, 72, x)): ln(a, xx0, yy, xx1, yy, color="#d1d5db", w=3.2)
    rr(a, 14, 14, 66, 66, 6, "#1e293b"); rr(a, 14, 14, 66, 66, 6, "#334155", w=1.6)
    cc(a, 20, 20, 2, "#64748b", w=0.8)
    eyes(a, 40, 36, 9, 3, "glow", "#4ade80"); arc(a, 40, 44, 7, 25, 155, color="#4ade80", w=2)
    a.text(31, 52, "µC", 10, "#94a3b8")


@st("edificio", "Edificio (Arquitectura)", "Building (Architecture)")
def _(a):
    rr(a, 18, 10, 62, 72, 3, "#fcd34d"); rr(a, 18, 10, 62, 18, 2, "#f59e0b", w=1.6)
    for r_ in range(3):
        for c in range(3): rr(a, 23 + c * 13, 23 + r_ * 11, 31 + c * 13, 30 + r_ * 11, 1.2, "#bae6fd", w=1.1)
    rr(a, 33, 52, 47, 72, 2, "#b45309", w=1.5); face(a, 40, 58, "dot", "smile", 3, 1.3, my=62)
    ln(a, 40, 10, 40, 3, w=1.6); a.poly(40, 3, 48, 5, 40, 8, color="#ef4444", fill=True)


@st("moneda", "Moneda (Economía)", "Coin (Economics)")
def _(a):
    cc(a, 40, 40, 31, "#fbbf24"); cc(a, 40, 40, 25, "#fcd34d", w=1.2); shine(a, 28, 24, 5, 2.4)
    a.text(34, 12, "$", 13, "#b45309"); face(a, 40, 42, "dot", "smile", 8.5, 2.7, my=49, cheeks=True)


@st("nota", "Nota musical (Música)", "Music note")
def _(a):
    ln(a, 52, 14, 52, 56, color=OL, w=6); ln(a, 52, 14, 52, 56, color="#475569", w=3.4)
    pg(a, 50, 12, 66, 20, 66, 34, 50, 28, fill="#6366f1", w=1.6)
    cc(a, 38, 58, 14, "#6366f1", ry=11); face(a, 38, 58, "dot", "smile", 5.5, 2, my=62, cheeks=False, col="#ffffff") if False else face(a, 38, 57, "big", "smile", 5.4, 1.5, my=62)


@st("laptop", "Laptop (Computación)", "Laptop (Computing)")
def _(a):
    rr(a, 14, 12, 66, 52, 5, "#94a3b8"); rr(a, 18, 16, 62, 48, 3, "#0f172a", w=1.2)
    pg(a, 8, 56, 72, 56, 66, 66, 14, 66, fill="#cbd5e1", w=1.6); ln(a, 32, 61, 48, 61, color="#64748b", w=1.8)
    eyes(a, 40, 30, 9, 2.8, "glow", "#4ade80"); arc(a, 40, 36, 6, 25, 155, color="#4ade80", w=2)
    a.text(21, 18.5, "</>", 6, "#38bdf8")


@st("libro", "Libro", "Book")
def _(a):
    rr(a, 14, 8, 66, 72, 5, "#3b82f6"); rr(a, 14, 8, 22, 72, 3, "#1d4ed8", w=1.6)
    rr(a, 62, 12, 66, 68, 1, "#fef3c7", w=1.1)
    rr(a, 28, 16, 58, 28, 2.5, "#bfdbfe", w=1.2); a.text(35, 18.5, "NOTAS", 7, "#1e3a8a")
    face(a, 43, 44, "dot", "smile", 8, 2.6, my=51, cheeks=True)
    pg(a, 54, 72, 54, 80 - 0.01, 58, 77, 62, 80 - 0.01, 62, 72, fill="#ef4444", w=1.2)


@st("lapiz", "Lápiz", "Pencil")
def _(a):
    pg(a, 28, 6, 52, 6, 52, 58, 40, 76, 28, 58, fill="#fcd34d"); rr(a, 28, 6, 52, 18, 4, "#fb7185", w=1.6); rr(a, 28, 18, 52, 24, 1, "#94a3b8", w=1.4)
    pg(a, 28, 58, 52, 58, 40, 76, fill="#fde7c3", w=1.6); pg(a, 35, 69, 45, 69, 40, 76, fill="#334155", w=1.2)
    face(a, 40, 36, "dot", "smile", 6, 2.4, my=42, cheeks=True)


@st("calculadora", "Calculadora", "Calculator")
def _(a):
    rr(a, 16, 6, 64, 74, 6, "#475569"); rr(a, 21, 11, 59, 26, 3, "#bbf7d0", w=1.3)
    eyes(a, 40, 18, 7, 2.2, "dot"); smile(a, 40, 19, 3, 1.5)
    for r_ in range(4):
        for c in range(3): rr(a, 21 + c * 13, 31 + r_ * 10.5, 30 + c * 13, 38 + r_ * 10.5, 2, "#fb923c" if c == 2 else "#e2e8f0", w=1.1)


@st("lupa", "Lupa", "Magnifier")
def _(a):
    ln(a, 52, 52, 70, 70, color=OL, w=11); ln(a, 52, 52, 70, 70, color="#b45309", w=7.4)
    cc(a, 34, 34, 25, "#7dd3fc", w=3.2); a.circle(34, 34, 25, color="#bae6fd", fill=True); a.circle(34, 34, 25, color=OL, w=3.2)
    shine(a, 22, 20, 5, 2.2); face(a, 34, 34, "dot", "smile", 8, 2.7, my=41, cheeks=True)


@st("salud", "Corazón (Salud)", "Heart (Health)")
def _(a):
    heart(a, 40, 36, 38); shine(a, 22, 22, 4, 2)
    face(a, 40, 34, "dot", "smile", 8, 2.7, my=41, cheeks=True)


@st("adn", "ADN", "DNA")
def _(a):
    for k in range(9):
        t = k / 8; y = 8 + 64 * t; x1 = 40 + 22 * math.sin(t * 2.5 * math.pi * 2); x2 = 80 - x1
        ln(a, x1, y, x2, y, color="#fde68a", w=3.2); ln(a, x1, y, x2, y, color=OL, w=0.6)
    for sgn, col in ((0, "#38bdf8"), (math.pi, "#f472b6")):
        pts = [(40 + 22 * math.sin(k / 40 * 2.5 * math.pi * 2 + sgn), 8 + 64 * k / 40) for k in range(41)]
        a._add(pts, OL, 6.4); a._add(pts, col, 4)
    cc(a, 68, 18, 0.1, "#fff", w=0.1)


@st("planta", "Planta", "Plant")
def _(a):
    pg(a, 20, 48, 60, 48, 54, 74, 26, 74, fill="#fb923c"); rr(a, 17, 44, 63, 52, 3, "#f97316", w=1.6)
    ln(a, 40, 44, 40, 24, color=OL, w=5.2); ln(a, 40, 44, 40, 24, color="#22c55e", w=2.8)
    pg(a, 40, 34, 18, 22, 8, 36, 24, 40, fill="#4ade80"); pg(a, 40, 28, 62, 14, 72, 28, 56, 34, fill="#4ade80")
    face(a, 40, 58, "dot", "smile", 7, 2.4, my=64, cheeks=True)


@st("foco", "Idea", "Idea")
def _(a):
    for ang in range(-150, 31, 30):
        r = math.radians(ang); ln(a, 40 + 30 * math.cos(r), 36 + 30 * math.sin(r), 40 + 37 * math.cos(r), 36 + 37 * math.sin(r), color="#fbbf24", w=2.4)
    cc(a, 40, 34, 20, "#fde047"); shine(a, 31, 24, 4, 2.2)
    rr(a, 31, 52, 49, 66, 3, "#cbd5e1"); ln(a, 32, 58, 48, 58, w=1.2); ln(a, 33, 63, 47, 63, w=1.2); rr(a, 35, 66, 45, 72, 2.5, "#64748b", w=1.4)
    face(a, 40, 33, "dot", "smile", 7, 2.4, my=40, cheeks=True)


@st("cafe", "Café", "Coffee")
def _(a):
    for x in (30, 40, 50): arc(a, x, 11, 4, 100, 440, color="#94a3b8", w=1.8, n=10, ry=6)
    ln(a, 56, 40, 66, 40, color=OL, w=1); a.circle(60, 44, 9, color="#e2e8f0", fill=True, ry=8); a.circle(60, 44, 9, color=OL, w=3, ry=8); a.circle(60, 44, 3.6, color="#ffffff", fill=True, ry=3.6)
    pg(a, 16, 28, 58, 28, 54, 62, 20, 62, fill="#f8fafc"); rr(a, 10, 60, 64, 68, 4, "#cbd5e1", w=1.6)
    a.poly(17, 28, 57, 28, 56.4, 33, 17.6, 33, color="#7c4a2d", fill=True)
    face(a, 37, 44, "dot", "smile", 8, 2.5, my=51, cheeks=True)


@st("reloj", "Despertador", "Alarm clock")
def _(a):
    for s in (-1, 1): cc(a, 40 + s * 24, 13, 8, "#f87171", ry=7); ln(a, 40 + s * 27, 21, 40 + s * 20, 24, w=2)
    ln(a, 26, 66, 20, 74, w=2.6); ln(a, 54, 66, 60, 74, w=2.6)
    cc(a, 40, 44, 27, "#fde68a"); cc(a, 40, 44, 22, "#ffffff", w=1.2)
    for k in range(12): r = math.radians(30 * k); ln(a, 40 + 19 * math.cos(r), 44 + 19 * math.sin(r), 40 + 21 * math.cos(r), 44 + 21 * math.sin(r), w=1.2)
    ln(a, 40, 44, 40, 30, w=2); ln(a, 40, 44, 51, 50, w=2); face(a, 40, 46, "dot", "smile", 7, 2.2, my=54, cheeks=False)
    cc(a, 40, 44, 1.6, "#ef4444", w=0.8)


@st("birrete", "Graduado", "Graduate")
def _(a):
    cc(a, 40, 50, 21, "#fde68a"); face(a, 40, 50, "dot", "smile", 8, 2.6, my=57, cheeks=True)
    pg(a, 40, 8, 74, 22, 40, 36, 6, 22, fill="#1e293b", w=1.8); pg(a, 22, 28, 22, 38, 40, 44, 58, 38, 58, 28, 40, 36, fill="#334155", w=1.6)
    ln(a, 40, 22, 66, 26, color="#fbbf24", w=1.8); ln(a, 66, 26, 66, 40, color="#fbbf24", w=1.8); cc(a, 66, 42, 2.8, "#fbbf24", w=1.2)


@st("cohete", "Cohete", "Rocket")
def _(a):
    pg(a, 40, 70, 30, 56, 50, 56, fill="#fb923c", w=1.6); pg(a, 40, 76, 35, 62, 45, 62, fill="#fde047", w=1.2)
    pg(a, 26, 52, 14, 66, 26, 60, fill="#ef4444"); pg(a, 54, 52, 66, 66, 54, 60, fill="#ef4444")
    a.poly(40, 4, 52, 22, 54, 52, 26, 52, 28, 22, color="#f1f5f9", fill=True); a.poly(40, 4, 52, 22, 54, 52, 26, 52, 28, 22, color=OL, w=1.8)
    pg(a, 40, 4, 48, 14, 32, 14, fill="#ef4444", w=1.6)
    cc(a, 40, 32, 8.5, "#bae6fd", w=2); face(a, 40, 31.5, "dot", "smile", 3.2, 1.2, my=34)


@st("trofeo", "Trofeo", "Trophy")
def _(a):
    for s in (-1, 1): a.circle(40 + s * 22, 24, 9, color=OL, w=3, ry=9); a.circle(40 + s * 22, 24, 9, color="#fbbf24", w=1.4, ry=9)
    pg(a, 20, 8, 60, 8, 56, 38, 48, 48, 32, 48, 24, 38, fill="#fbbf24"); ln(a, 40, 48, 40, 60, color=OL, w=6); ln(a, 40, 48, 40, 60, color="#f59e0b", w=3.4)
    rr(a, 26, 60, 54, 72, 3, "#b45309"); star(a, 40, 66, 4.2, "#fde68a"); shine(a, 28, 18, 2.6, 6)
    face(a, 40, 26, "dot", "smile", 7, 2.5, my=32, cheeks=True)


@st("estrella", "Estrella", "Star")
def _(a):
    star(a, 40, 42, 36, "#fbbf24"); shine(a, 28, 28, 3.2, 1.6); face(a, 40, 42, "dot", "smile", 8, 2.7, my=48, cheeks=True)


@st("sol", "Sol", "Sun")
def _(a):
    for k in range(12): r = math.radians(30 * k); ln(a, 40 + 24 * math.cos(r), 40 + 24 * math.sin(r), 40 + 34 * math.cos(r), 40 + 34 * math.sin(r), color="#f59e0b", w=3.4)
    cc(a, 40, 40, 21, "#fde047"); shine(a, 31, 30, 4, 2); face(a, 40, 40, "happy", "big", 7.5, 2.6, my=46, cheeks=True)


@st("regla", "Regla y escuadra", "Ruler")
def _(a):
    rr(a, 8, 26, 72, 54, 4, "#fcd34d")
    for k in range(17):
        x = 12 + k * 3.75; ln(a, x, 26, x, 26 + (8 if k % 4 == 0 else 4.4), w=1.1)
    for k in range(5): a.text(10.5 + k * 15 - (0 if k < 1 else 2), 36, str(k), 6, "#78350f")
    face(a, 40, 46, "dot", "smile", 8, 2.2, my=51)
