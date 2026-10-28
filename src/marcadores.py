import math
from wgpack import Pack
from _draw import *

pack = Pack("marcadores", "Marcadores de estudio", "Sellos y marcas para tus apuntes: «¡Importante!», «Repasar», «Examen», checks, flechas, llaves, banderines, estrellas de calificación y más.",
            "General", "⭐", en={"Marcadores de estudio": "Study markers",
            "Sellos y marcas para tus apuntes: «¡Importante!», «Repasar», «Examen», checks, flechas, llaves, banderines, estrellas de calificación y más.":
            "Stamps and marks for your notes: Important, Review, Exam, checks, arrows, braces, pennants, rating stars and more."})
P = pack


def st(sid, name, en, w=80.0, h=80.0):
    return P.sticker("marca-" + sid, name, en, w, h)


def stamp(a, text, fill, fg=WH, w=110.0, h=34.0, size=None, dark=None):
    size = size or min(15.0, (w - 18) / (len(text) * 0.6))
    rr(a, 2, 2, w - 2, h - 2, 9, fill, w=1.8)
    rr(a, 5.5, 5.5, w - 5.5, h - 5.5, 6.5, fill, w=0.1); a.round_rect(5.5, 5.5, w - 5.5, h - 5.5, 6.5, color=dark or fg, w=0.9)
    a.text(w / 2 - len(text) * size * 0.285, h / 2 - size * 0.62, text, size, fg)


SELLOS = [("importante", "¡Importante!", "Important!", "#dc2626", WH, 120), ("repasar", "Repasar", "Review", "#2563eb", WH, 100),
          ("examen", "Examen", "Exam", "#7c3aed", WH, 100), ("duda", "Duda", "Doubt", "#ea580c", WH, 90),
          ("tarea", "Tarea", "Homework", "#16a34a", WH, 90), ("ejemplo", "Ejemplo", "Example", "#0d9488", WH, 100),
          ("definicion", "Definición", "Definition", "#4f46e5", WH, 110), ("ojo", "Ojo", "Careful", "#facc15", OL, 80),
          ("formula", "Fórmula", "Formula", "#db2777", WH, 100), ("resumen", "Resumen", "Summary", "#475569", WH, 105)]
for sid, text, en, col, fg, w in SELLOS:
    P.sticker("marca-" + sid, text, en, float(w), 34.0)(lambda a, text=text, col=col, fg=fg, w=w: stamp(a, text, col, fg, float(w), 34.0, dark=fg))


@st("check", "Check verde", "Green check")
def _(a):
    cc(a, 40, 40, 34, "#22c55e"); shine(a, 28, 22, 6, 2.4)
    a._add([(22, 42), (35, 55), (59, 27)], OL, 11); a._add([(22, 42), (35, 55), (59, 27)], WH, 7.4)


@st("cruz", "Cruz roja", "Red cross")
def _(a):
    cc(a, 40, 40, 34, "#ef4444"); shine(a, 30, 13, 5, 1.8)
    for p in (((26, 26), (54, 54)), ((54, 26), (26, 54))):
        a._add(list(p), OL, 11); a._add(list(p), WH, 7.4)


@st("exclamacion", "¡!", "Exclamation", 100.0, 60.0)
def _(a):
    # ¡ (punto arriba) y ! (punto abajo)
    pg(a, 20.4, 22, 29.6, 22, 27.6, 52, 22.4, 52, fill="#ef4444", w=1.6); cc(a, 25, 12, 5, "#ef4444", w=1.6)
    pg(a, 70.4, 8, 79.6, 8, 77.6, 38, 72.4, 38, fill="#ef4444", w=1.6); cc(a, 75, 48, 5, "#ef4444", w=1.6)


@st("interrogacion", "¿?", "Question", 100.0, 60.0)
def _(a):
    def q(x, flip):
        pts = [(x + 11 * math.cos(math.radians(190 + 245 * k / 14)), 22 + 11 * math.sin(math.radians(190 + 245 * k / 14))) for k in range(15)]
        pts += [(x, pts[-1][1] + 8), (x, 38)]
        dot = (x, 52)
        if flip: pts = [(2 * x - px, 60 - py) for px, py in pts]; dot = (x, 8)
        a._add(pts, OL, 9); a._add(pts, "#3b82f6", 5.4); cc(a, dot[0], dot[1], 4.8, "#3b82f6", w=1.6)
    q(25, True); q(75, False)


@st("flecha-curva", "Flecha curva", "Curved arrow")
def _(a):
    pts = [(14 + 52 * k / 16, 56 - 38 * math.sin(math.pi * k / 16)) for k in range(17)]
    a._add(pts, OL, 9.6); a._add(pts, "#f97316", 6)
    pg(a, 56, 54, 76, 54, 66, 72, fill="#f97316", w=1.8)
    cc(a, 14, 56, 4.4, "#f97316", w=1.5)


@st("flecha-doble", "Flecha doble", "Double arrow", 100.0, 40.0)
def _(a):
    pg(a, 4, 20, 26, 4, 26, 14, 74, 14, 74, 4, 96, 20, 74, 36, 74, 26, 26, 26, 26, 36, fill="#8b5cf6", w=2)
    shine(a, 50, 17, 14, 1.4)


@st("llave", "Llave", "Brace", 44.0, 80.0)
def _(a):
    pts = [(34, 4), (28, 6), (24, 12), (24, 30), (21, 37), (12, 40), (21, 43), (24, 50), (24, 68), (28, 74), (34, 76)]
    sm = []
    for i in range(len(pts) - 1):
        for k in range(6): t = k / 6; sm.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * t, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * t))
    sm.append(pts[-1])
    a._add(sm, OL, 9); a._add(sm, "#a855f7", 5.6)


@st("banderin", "Banderín", "Pennant")
def _(a):
    ln(a, 14, 8, 14, 74, color=OL, w=6); ln(a, 14, 8, 14, 74, color="#94a3b8", w=3.2); cc(a, 14, 8, 3.6, "#fbbf24", w=1.4)
    pg(a, 17, 12, 70, 28, 17, 44, fill="#ef4444")
    star(a, 30, 28, 6.4, "#fde047"); rr(a, 6, 72, 22, 77, 2, "#475569", w=1.4)


@st("liston", "Listón de premio", "Award ribbon")
def _(a):
    pg(a, 24, 46, 14, 78, 28, 70, 36, 78, 40, 46, fill="#3b82f6"); pg(a, 56, 46, 66, 78, 52, 70, 44, 78, 40, 46, fill="#2563eb")
    for k in range(14): t = 2 * math.pi * k / 14; cc(a, 40 + 24 * math.cos(t), 30 + 24 * math.sin(t), 5.6, "#f43f5e", w=1.4)
    cc(a, 40, 30, 21, "#fb7185"); cc(a, 40, 30, 14, "#fecdd3", w=1.4); star(a, 40, 30, 9, "#fbbf24")


@st("marco", "Marco de estrellas", "Star frame")
def _(a):
    a.round_rect(10, 10, 70, 70, 6, color=OL, w=6.6); a.round_rect(10, 10, 70, 70, 6, color="#fbbf24", w=4)
    a.round_rect(10, 10, 70, 70, 6, color="#fde68a", w=1.2)
    for x, y in ((10, 10), (70, 10), (10, 70), (70, 70)): star(a, x, y, 10, "#f97316")
    for x, y in ((40, 10), (40, 70), (10, 40), (70, 40)): star(a, x, y, 5.4, "#fde047")


@st("dialogo", "Burbuja de diálogo", "Speech bubble", 80.0, 70.0)
def _(a):
    rr(a, 6, 6, 74, 50, 14, WH); pg(a, 20, 48, 16, 66, 36, 48, fill=WH, w=1.8)
    rr(a, 8.5, 8.5, 71.5, 47.5, 12, WH, w=0.1); a._add([(19, 49), (36, 49)], WH, 3.4)
    for x in (26, 40, 54): cc(a, x, 28, 4.2, "#3b82f6", w=1.2)


@st("pensamiento", "Burbuja de pensamiento", "Thought bubble", 80.0, 76.0)
def _(a):
    for x, y, r in ((22, 28, 14), (38, 20, 15), (56, 24, 14), (62, 36, 11), (44, 40, 13), (26, 38, 12)): cc(a, x, y, r, "#e0f2fe", w=1.8)
    for x, y, r in ((22, 28, 13), (38, 20, 14), (56, 24, 13), (62, 36, 10), (44, 40, 12), (26, 38, 11)): a.circle(x, y, r, color="#e0f2fe", fill=True)
    cc(a, 26, 58, 5, "#e0f2fe", w=1.6); cc(a, 16, 69, 3, "#e0f2fe", w=1.5)
    a.text(30, 22, "¿...?", 14, "#2563eb")


@st("numeros", "Números 1 al 5", "Numbers 1-5", 150.0, 34.0)
def _(a):
    for k, c in enumerate(("#ef4444", "#f97316", "#eab308", "#22c55e", "#3b82f6")):
        x = 17 + k * 29; cc(a, x, 17, 14, c)
        a.text(x - 3.4, 17 - 7.5, str(k + 1), 13, WH)


@st("subrayado", "Subrayado ondulado", "Wavy underline", 110.0, 24.0)
def _(a):
    pts = [(6 + 98 * k / 40, 12 + 5 * math.sin(2 * math.pi * k / 40 * 4)) for k in range(41)]
    a._add(pts, "#fecaca", 7.4); a._add(pts, "#ef4444", 3.6)


@st("resaltador", "Resaltador", "Highlighter", 110.0, 30.0)
def _(a):
    pts = [(4, 6), (104, 4), (107, 14), (105, 26), (6, 27), (3, 16), (4, 6)]
    a._add(pts, "#fef08a", 1, True); a._add(pts, "#fde047", 1.4)
    for k in range(8): ln(a, 14 + k * 12, 8, 8 + k * 12, 24, color="#facc15", w=1.2)


@st("chincheta", "Chincheta", "Pushpin")
def _(a):
    ln(a, 40, 44, 40, 74, color=OL, w=3.4); ln(a, 40, 44, 40, 74, color="#94a3b8", w=1.6)
    rr(a, 24, 40, 56, 48, 3, "#b91c1c", w=1.6); pg(a, 28, 40, 52, 40, 48, 14, 32, 14, fill="#ef4444"); rr(a, 30, 8, 50, 16, 4, "#ef4444")
    shine(a, 36, 26, 2.4, 8)


@st("estrellas", "Calificación", "Rating", 150.0, 32.0)
def _(a):
    for k in range(5): star(a, 15 + k * 30, 17, 14, "#fbbf24")


@st("animo", "¡Tú puedes!", "You can do it!", 96.0, 94.0)
def _(a):
    cc(a, 48, 34, 28, "#fde047"); shine(a, 36, 18, 5, 2.4)
    face(a, 48, 32, "happy", "big", 9, 2.8, my=40, cheeks=True)
    rr(a, 6, 68, 90, 90, 9, "#16a34a", w=1.8)
    a.text(48 - 10 * 11 * 0.285, 74, "¡Tú puedes!", 11, WH)
    for x, y in ((12, 14), (84, 12)): star(a, x, y, 7, "#fbbf24")
