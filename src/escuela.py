import math
from wgpack import Pack
from _draw import *

pack = Pack("escuela", "Útiles y oficina", "24 útiles escolares y de oficina con carita: mochila, regla, compás, tijeras, cuaderno, pizarrón, tablet y más.",
            "General", "📎", en={"Útiles y oficina": "School and office supplies",
            "24 útiles escolares y de oficina con carita: mochila, regla, compás, tijeras, cuaderno, pizarrón, tablet y más.":
            "24 school and office supplies with faces: backpack, ruler, compass, scissors, notebook, chalkboard, tablet and more."})
P = pack
S = 80.0


def st(sid, name, en, w=S, h=S):
    return P.sticker("escuela-" + sid, name, en, w, h)


def path(*segs):
    """Une tramos: ('p', x, y, ...) puntos sueltos; ('a', cx, cy, r, a0, a1) arco."""
    pts = []
    for s in segs:
        if s[0] == "p":
            pts += list(zip(s[1::2], s[2::2]))
        else:
            _, cx, cy, r, a0, a1 = s
            pts += [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / 12)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / 12))) for k in range(13)]
    return pts


def chalkface(a, cx, cy, s=1.0):
    for sx in (-1, 1): a.circle(cx + sx * 7 * s, cy, 2 * s, color=WH, fill=True)
    arc(a, cx, cy + 1 * s, 5 * s, 25, 155, color=WH, w=1.6)


@st("mochila", "Mochila", "Backpack")
def _(a):
    arc(a, 40, 20, 9, 180, 360, w=3.6); arc(a, 40, 20, 9, 180, 360, color="#b91c1c", w=2)
    rr(a, 10, 40, 17, 62, 3, "#b91c1c"); rr(a, 63, 40, 70, 62, 3, "#b91c1c")
    rr(a, 16, 16, 64, 74, 15, "#ef4444"); shine(a, 28, 26, 3.6, 1.6)
    rr(a, 24, 50, 56, 70, 6, "#fca5a5"); ln(a, 24, 54, 56, 54, w=1.4); cc(a, 40, 54, 2.2, "#fbbf24", w=1.1)
    face(a, 40, 34, "dot", "smile", 7.5, 2.6, my=41, cheeks=True)


@st("regla", "Regla", "Ruler")
def _(a):
    rr(a, 26, 4, 54, 76, 3, "#7dd3fc")
    for k in range(18):
        y = 8 + k * 3.8; ln(a, 26, y, 26 + (9 if k % 5 == 0 else 5), y, w=1.1)
    face(a, 43, 40, "dot", "smile", 5.5, 2.2, my=46, cheeks=False)
    blush(a, 43, 43, 9, 1.8)


@st("escuadra", "Escuadra", "Set square")
def _(a):
    pg(a, 8, 72, 8, 8, 72, 72, fill="#6ee7b7")
    pg(a, 20, 60, 20, 34, 46, 60, fill=WH, w=1.4)
    for k in range(7): ln(a, 8, 14 + k * 8, 12 + (k % 2) * 2, 14 + k * 8, w=1.1)
    face(a, 26, 53, "dot", "smile", 3.8, 1.5, my=57)
    shine(a, 15, 22, 1.5, 4)


@st("compas", "Compás", "Compass")
def _(a):
    for x1, x2 in ((22, 40), (58, 40)):
        ln(a, x2, 18, x1, 70, color=OL, w=7); ln(a, x2, 18, x1, 70, color="#cbd5e1", w=4.2)
    pg(a, 20, 70, 24, 70, 22, 77, fill="#475569", w=1.2)
    pg(a, 56, 70, 60, 70, 58, 77, fill="#f97316", w=1.2)
    ln(a, 29, 50, 51, 50, color=OL, w=3)
    cc(a, 40, 14, 9, "#fbbf24"); face(a, 40, 13.5, "dot", "smile", 3.6, 1.5, my=17.5)
    cc(a, 40, 4, 2.4, "#94a3b8", w=1.2)


@st("tijeras", "Tijeras", "Scissors")
def _(a):
    for x in (24, 56):
        ln(a, 40, 40, x, 8, color=OL, w=7.4); ln(a, 40, 40, x, 8, color="#e2e8f0", w=4.8)
    for cx in (24, 56):
        cc(a, cx, 64, 11, "#ef4444"); cc(a, cx, 64, 5.5, WH, w=1.4)
    ln(a, 40, 40, 28, 55, color=OL, w=4.6); ln(a, 40, 40, 52, 55, color=OL, w=4.6)
    ln(a, 40, 40, 28, 55, color="#ef4444", w=2.4); ln(a, 40, 40, 52, 55, color="#ef4444", w=2.4)
    cc(a, 40, 40, 6, "#fde047"); face(a, 40, 39.5, "dot", "smile", 2.4, 1.1, my=42.5)


@st("pegamento", "Pegamento", "Glue")
def _(a):
    rr(a, 24, 32, 56, 74, 7, WH); rr(a, 24, 46, 56, 64, 0.1, "#38bdf8", w=1.4)
    pg(a, 30, 32, 50, 32, 45, 14, 35, 14, fill="#f97316"); cc(a, 40, 12, 3.5, "#fde047", w=1.3)
    cc(a, 40, 8, 1, "#fde047", w=0.3)
    face(a, 40, 55, "dot", "smile", 6, 2.1, my=61, cheeks=False)
    a.text(30, 35, "GLUE", 6, "#38bdf8") if False else None
    shine(a, 29, 38, 1.6, 4)


@st("borrador", "Borrador", "Eraser")
def _(a):
    rr(a, 8, 24, 72, 58, 7, "#fb7185"); rr(a, 8, 24, 32, 58, 7, "#3b82f6"); rr(a, 26, 24, 32, 58, 0.1, "#3b82f6", w=1)
    ln(a, 32, 24, 32, 58, w=1.6)
    face(a, 52, 41, "dot", "smile", 6.5, 2.5, my=47, cheeks=True); shine(a, 22, 31, 2.4, 1.4)
    a.circle(14, 66, 3, color="#fecdd3", fill=True); a.circle(24, 70, 2, color="#fecdd3", fill=True); a.circle(58, 68, 2.4, color="#fecdd3", fill=True)


@st("sacapuntas", "Sacapuntas", "Sharpener")
def _(a):
    rr(a, 12, 20, 62, 62, 7, "#a3e635"); cc(a, 28, 41, 7.5, OL, w=1.2); cc(a, 28, 41, 4, "#64748b", w=0.8)
    pg(a, 40, 24, 58, 24, 58, 58, 40, 58, fill="#bef264", w=0.1)
    face(a, 48, 38, "dot", "smile", 5, 2.2, my=44)
    rr(a, 54, 28, 60, 54, 1.5, "#cbd5e1", w=1.3)
    arc(a, 70, 60, 6, 180, 440, color="#fcd34d", w=2, n=12); arc(a, 66, 70, 4, 0, 280, color="#fcd34d", w=1.8, n=10)


@st("plumones", "Plumones", "Markers")
def _(a):
    for x, c, d in ((20, "#ef4444", "#b91c1c"), (40, "#3b82f6", "#1d4ed8"), (60, "#22c55e", "#15803d")):
        pg(a, x - 6, 60, x + 6, 60, x + 2.5, 74, x - 2.5, 74, fill="#f1f5f9", w=1.4)
        pg(a, x - 1.2, 69, x + 1.2, 69, x + 0.5, 74, x - 0.5, 74, fill=c, w=0.8)
        rr(a, x - 8, 20, x + 8, 61, 3, c); rr(a, x - 8, 8, x + 8, 28, 4, d)
    face(a, 40, 42, "dot", "smile", 4.4, 1.9, my=47, cheeks=False)
    shine(a, 34, 33, 1.2, 5)


@st("colores", "Caja de colores", "Colour pencils")
def _(a):
    for k, c in enumerate(("#ef4444", "#f97316", "#fde047", "#22c55e", "#3b82f6", "#a855f7")):
        x = 14 + k * 10.4
        pg(a, x - 4, 30, x + 4, 30, x, 12, fill="#fde7c3", w=1.2); pg(a, x - 1.6, 17, x + 1.6, 17, x, 12, fill=c, w=0.8)
        rr(a, x - 4, 28, x + 4, 40, 0.5, c, w=1.2)
    rr(a, 8, 34, 72, 70, 5, "#2563eb"); rr(a, 12, 38, 68, 44, 2, "#1d4ed8", w=1)
    face(a, 40, 56, "dot", "smile", 8, 2.6, my=62, cheeks=True)


@st("postit", "Nota adhesiva", "Sticky note")
def _(a):
    pg(a, 10, 10, 70, 10, 70, 52, 52, 70, 10, 70, fill="#fde047"); pg(a, 52, 70, 52, 52, 70, 52, fill="#facc15", w=1.4)
    rr(a, 26, 4, 54, 15, 2, "#fef08a", w=0.1)
    face(a, 38, 34, "dot", "smile", 8, 2.7, my=41, cheeks=True)
    ln(a, 20, 53, 40, 53, color="#ca8a04", w=1.4); ln(a, 20, 60, 34, 60, color="#ca8a04", w=1.4)


@st("clip", "Clip", "Paper clip")
def _(a):
    pts = path(("p", 47, 52, 47, 30), ("a", 40, 30, 7, 0, -180), ("p", 33, 52), ("a", 43, 52, 10, 180, 0), ("p", 53, 26), ("a", 38, 26, 15, 0, -180), ("p", 23, 62), ("a", 35, 62, 12, 180, 0))
    a._add(pts, OL, 6.4); a._add(pts, "#94a3b8", 4)
    a._add(pts, "#e2e8f0", 1.2)
    eyes(a, 66, 56, 5, 2.2, "dot"); smile(a, 66, 59, 3.6)


@st("engrapadora", "Engrapadora", "Stapler")
def _(a):
    rr(a, 6, 50, 74, 62, 3, "#475569"); rr(a, 10, 30, 70, 50, 7, "#ef4444")
    pg(a, 8, 52, 12, 48, 12, 52, fill="#475569", w=0.1)
    rr(a, 56, 24, 72, 34, 3, "#b91c1c", w=1.5); cc(a, 64, 29, 1.6, "#fbbf24", w=0.8)
    face(a, 36, 40, "dot", "smile", 7, 2.5, my=46, cheeks=True); shine(a, 22, 35, 5, 1.4)
    path_ = [(58, 66), (58, 71), (68, 71), (68, 66)]; a._add(path_, "#94a3b8", 2)


@st("carpeta", "Carpeta", "Folder")
def _(a):
    rr(a, 8, 14, 38, 30, 4, "#f59e0b"); rr(a, 8, 22, 72, 68, 5, "#f59e0b")
    rr(a, 16, 18, 64, 36, 2, WH, w=1.3); ln(a, 22, 24, 50, 24, color="#cbd5e1", w=1.2); ln(a, 22, 29, 42, 29, color="#cbd5e1", w=1.2)
    rr(a, 8, 32, 72, 70, 5, "#fcd34d")
    face(a, 40, 50, "dot", "smile", 8, 2.7, my=57, cheeks=True); shine(a, 18, 38, 3, 1.4)


@st("cuaderno", "Cuaderno", "Notebook")
def _(a):
    rr(a, 14, 8, 66, 72, 5, "#f472b6"); shine(a, 28, 14, 3.4, 1.2)
    rr(a, 24, 20, 58, 34, 3, WH, w=1.3); ln(a, 28, 27, 54, 27, color="#f472b6", w=1.4)
    face(a, 42, 50, "dot", "smile", 8, 2.6, my=57, cheeks=True)
    for k in range(7): cc(a, 14, 14 + k * 8.8, 3, "#e2e8f0", w=1.4)


@st("agenda", "Calendario", "Calendar")
def _(a):
    rr(a, 8, 12, 72, 72, 6, WH); rr(a, 8, 12, 72, 30, 6, "#ef4444"); rr(a, 8, 24, 72, 30, 0.1, "#ef4444", w=0.1)
    for x in (24, 56): rr(a, x - 2.5, 5, x + 2.5, 18, 2.5, "#94a3b8", w=1.4)
    a.text(26, 15.5, "OCTUBRE", 7.5, WH)
    for r_ in range(2):
        for c in range(5): a.rect(14 + c * 11, 35 + r_ * 6, 20 + c * 11, 39 + r_ * 6, color="#e2e8f0", w=0.8)
    face(a, 40, 55, "dot", "smile", 8, 2.6, my=62, cheeks=True)


@st("pizarron", "Pizarrón", "Chalkboard")
def _(a):
    rr(a, 6, 10, 74, 58, 3, "#a16207"); rr(a, 10, 14, 70, 54, 2, "#166534", w=1.2)
    rr(a, 4, 58, 76, 64, 2, "#78350f", w=1.5); rr(a, 54, 55, 62, 58, 1, WH, w=0.8)
    a.text(15, 17, "a²+b²=c²", 8, WH); chalkface(a, 40, 40)
    ln(a, 18, 49, 38, 49, color="#86efac", w=1.2)
    ln(a, 20, 64, 20, 74, w=2.4); ln(a, 60, 64, 60, 74, w=2.4)


@st("globo", "Globo terráqueo", "Globe")
def _(a):
    cc(a, 40, 34, 24, "#38bdf8"); shine(a, 28, 22, 4, 2)
    pg(a, 22, 26, 30, 20, 36, 26, 32, 36, 24, 38, fill="#4ade80", w=1.2)
    pg(a, 46, 30, 58, 28, 60, 40, 52, 48, 46, 40, fill="#4ade80", w=1.2)
    face(a, 40, 36, "dot", "smile", 7, 2.4, my=42, cheeks=False)
    arc(a, 40, 34, 29, 120, 420, color=OL, w=4.6, n=30); arc(a, 40, 34, 29, 120, 420, color="#d97706", w=2.6, n=30)
    ln(a, 40, 63, 40, 70, color=OL, w=4.6); ln(a, 40, 63, 40, 70, color="#d97706", w=2.6)
    rr(a, 26, 70, 54, 77, 2.5, "#b45309", w=1.5)


@st("reloj", "Reloj de pared", "Wall clock")
def _(a):
    cc(a, 40, 40, 32, "#b45309"); cc(a, 40, 40, 26, WH, w=1.4)
    for k in range(12):
        r = math.radians(30 * k); ln(a, 40 + 21.5 * math.cos(r), 40 + 21.5 * math.sin(r), 40 + 24 * math.cos(r), 40 + 24 * math.sin(r), w=1.4)
    a.text(37, 17, "12", 6, OL); a.text(37, 58, "6", 6, OL); a.text(61, 37, "3", 6, OL); a.text(17, 37, "9", 6, OL)
    ln(a, 40, 40, 40, 26, w=2.2); ln(a, 40, 40, 50, 46, w=2.2); cc(a, 40, 40, 1.8, "#ef4444", w=0.8)
    eyes(a, 40, 32, 6, 1.7, "dot") if False else None
    shine(a, 24, 22, 2, 5)


@st("taza", "Taza de lápices", "Pencil cup")
def _(a):
    for x, y, c, ang in ((26, 8, "#ef4444", -14), (36, 4, "#3b82f6", -4), (46, 6, "#22c55e", 4), (56, 10, "#f59e0b", 14)):
        r = math.radians(ang); x2 = x + 34 * math.sin(r); y2 = y + 34 * math.cos(r)
        ln(a, x, y, x2, y2, color=OL, w=6.6); ln(a, x, y, x2, y2, color=c, w=4.2)
        pg(a, x - 3.3, y - 0.5, x + 3.3, y - 0.5, x, y - 7, fill="#fde7c3", w=1.1)
    rr(a, 20, 38, 60, 74, 6, "#818cf8"); shine(a, 28, 46, 2, 7)
    face(a, 40, 55, "dot", "smile", 8, 2.6, my=61, cheeks=True)


@st("tabla", "Tabla con hoja", "Clipboard")
def _(a):
    rr(a, 14, 8, 66, 74, 5, "#b45309"); rr(a, 19, 16, 61, 68, 2, WH, w=1.3)
    for y in (24, 32, 60): ln(a, 24, y, 56, y, color="#cbd5e1", w=1.2)
    face(a, 40, 44, "dot", "smile", 7.5, 2.5, my=50, cheeks=True)
    rr(a, 28, 4, 52, 16, 3, "#94a3b8"); rr(a, 34, 1, 46, 8, 3, "#64748b", w=1.3)


@st("sobre", "Sobre", "Envelope")
def _(a):
    rr(a, 6, 20, 74, 64, 4, "#fef3c7")
    a._add([(6, 22), (40, 46), (74, 22)], OL, 1.8); pg(a, 6, 22, 40, 46, 74, 22, fill="#fde68a", w=1.6)
    heart(a, 40, 46, 2.4)
    face(a, 40, 55, "dot", "smile", 6.5, 2, my=60, cheeks=False)
    ln(a, 8, 62, 28, 44, color="#e7d9a6", w=1); ln(a, 72, 62, 52, 44, color="#e7d9a6", w=1)


@st("tablet", "Tablet", "Tablet")
def _(a):
    rr(a, 10, 8, 70, 72, 7, "#334155"); rr(a, 15, 14, 65, 62, 3, "#bae6fd", w=1.2); cc(a, 40, 67.5, 2.4, "#94a3b8", w=1)
    face(a, 40, 34, "dot", "smile", 8, 2.7, my=41, cheeks=True)
    for k, c in enumerate(("#f87171", "#fbbf24", "#4ade80", "#818cf8")): rr(a, 21 + k * 10.5, 50, 28.5 + k * 10.5, 57.5, 2, c, w=1)
    shine(a, 20, 18, 4, 1.2)


@st("audifonos", "Audífonos", "Headphones")
def _(a):
    pts = path(("a", 40, 44, 27, 180, 360))
    a._add(pts, OL, 7.6); a._add(pts, "#94a3b8", 4.8)
    for x in (13, 67):
        rr(a, x - 8, 38, x + 8, 66, 6, "#f43f5e"); rr(a, x - 4.5, 43, x + 4.5, 61, 3.5, "#fb7185", w=1.2)
    arc(a, 13, 52, 3, 200, 340, w=1.8); arc(a, 67, 52, 3, 200, 340, w=1.8)
    smile(a, 40, 52, 6, 2); blush(a, 40, 53, 17, 2.2)
    a.text(31, 17, "♪", 11, "#6366f1") if False else None
    shine(a, 12, 41, 1.4, 4)
