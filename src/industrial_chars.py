import math
from _draw import *


def extend(P):
    def st(sid, name, en):
        return P.sticker("ch-" + sid, name, en, 80, 80)

    @st("banda", "Banda transportadora", "Conveyor belt")
    def _(a):
        rr(a, 6, 52, 74, 66, 7, "#475569")
        for x in (14, 66): cc(a, x, 59, 5, "#cbd5e1", w=1.4)
        for x in range(22, 62, 8): ln(a, x, 54, x, 64, color="#94a3b8", w=1.2)
        rr(a, 12, 30, 34, 52, 3, "#fbbf24"); ln(a, 12, 38, 34, 38, w=1.2); face(a, 23, 45, "dot", "smile", 4.4, 1.7, my=49)
        rr(a, 44, 38, 62, 52, 3, "#38bdf8"); ln(a, 44, 44, 62, 44, w=1.2)
        cc(a, 49, 47, 1.4, OL, w=0.4); cc(a, 57, 47, 1.4, OL, w=0.4); smile(a, 53, 47.5, 2.4, 1.2)
        for x in (18, 62): ln(a, x, 66, x, 74, w=2.4)

    @st("caja", "Paquete con cara", "Package")
    def _(a):
        pg(a, 8, 26, 56, 26, 72, 14, 24, 14, fill="#fdba74", w=1.6); pg(a, 56, 26, 72, 14, 72, 52, 56, 64, fill="#b45309", w=1.6)
        rr(a, 8, 26, 56, 64, 2, "#f59e0b"); rr(a, 24, 26, 40, 34, 0.5, "#fef3c7", w=1.2)
        face(a, 32, 46, "dot", "smile", 8, 2.7, my=52, cheeks=True)
        ln(a, 40, 14, 48, 26, color="#fef3c7", w=3.4)

    @st("flujo", "Diagrama de flujo", "Flowchart")
    def _(a):
        rr(a, 22, 3, 58, 15, 6, "#4ade80"); a.text(30, 4.5, "inicio", 7, OL)
        ln(a, 40, 15, 40, 21, w=1.8)
        pg(a, 40, 21, 62, 33, 40, 45, 18, 33, fill="#fde047", w=1.7); a.text(35.5, 28, "¿?", 9, OL)
        ln(a, 40, 45, 40, 51, w=1.8); ln(a, 62, 33, 72, 33, 72, 58, 58, 58, w=1.8); a.text(63, 26, "no", 6, OL)
        rr(a, 22, 51, 58, 65, 3, "#60a5fa"); eyes(a, 40, 57, 6, 1.7, "dot"); smile(a, 40, 58, 2.6, 1.2)
        ln(a, 40, 65, 40, 69, w=1.8); rr(a, 26, 69, 54, 78, 4, "#f87171"); a.text(34, 70, "fin", 6.5, WH)

    @st("servidor", "Servidor", "Server")
    def _(a):
        for k, y in enumerate((8, 31, 54)):
            rr(a, 12, y, 68, y + 19, 4, "#64748b"); rr(a, 16, y + 4, 40, y + 15, 2, "#334155", w=1.2)
            cc(a, 50, y + 9.5, 2.4, ("#4ade80", "#fbbf24", "#4ade80")[k], w=1); cc(a, 59, y + 9.5, 2.4, "#ef4444" if k == 1 else "#4ade80", w=1)
        eyes(a, 28, 18, 4, 1.4, "dot", "#4ade80")
        for y in (18, 41, 64): cc(a, 24, y, 1.6, "#4ade80", w=0.4); cc(a, 32, y, 1.6, "#4ade80", w=0.4); arc(a, 28, y + 0.5, 2.8, 25, 155, color="#4ade80", w=1.1, n=6)
        ln(a, 20, 73, 20, 77, w=2); ln(a, 60, 73, 60, 77, w=2)

    @st("basedatos", "Base de datos", "Database")
    def _(a):
        for y, c in ((54, "#3b82f6"), (36, "#60a5fa"), (18, "#93c5fd")):
            rr(a, 14, y, 66, y + 18, 2, c, w=1.6); a.circle(40, y, 26, color=OL, w=1.6, ry=6) ; a.circle(40, y, 26, color=c, fill=True, ry=6); a.circle(40, y, 26, color=OL, w=1.6, ry=6)
        face(a, 40, 50, "dot", "smile", 8.5, 2.6, my=57, cheeks=True)

    @st("teclado", "Teclado", "Keyboard")
    def _(a):
        rr(a, 4, 22, 76, 62, 7, "#94a3b8")
        for r_, (n, off) in enumerate(((10, 0), (9, 3.5), (8, 7))):
            for c in range(n): rr(a, 9 + off + c * 6.4, 27 + r_ * 9, 14 + off + c * 6.4, 33 + r_ * 9, 1, "#f1f5f9", w=0.9)
        rr(a, 24, 54, 56, 60, 1.5, "#f1f5f9", w=1)
        eyes(a, 40, 16, 7, 2.2, "dot"); smile(a, 40, 15.5, 3.4, 1.5)

    @st("diagrama", "Diagrama de barras", "Process chart")
    def _(a):
        rr(a, 8, 8, 72, 72, 4, "#f1f5f9")
        for y in (24, 40, 56): ln(a, 14, y, 66, y, color="#cbd5e1", w=0.8)
        for k, (w_, c) in enumerate(((30, "#60a5fa"), (44, "#fbbf24"), (22, "#4ade80"))):
            rr(a, 16, 14 + k * 17, 16 + w_, 25 + k * 17, 2.5, c, w=1.4)
        cc(a, 60, 59, 7.4, "#fde68a", w=1.5); eyes(a, 60, 58, 2.6, 1.1, "dot"); smile(a, 60, 59.2, 2.4, 1.2)

    @st("wifi", "Red y router", "Network router")
    def _(a):
        rr(a, 8, 48, 72, 66, 5, "#e2e8f0"); ln(a, 18, 48, 14, 28, color=OL, w=4.4); ln(a, 18, 48, 14, 28, color="#94a3b8", w=2.4); ln(a, 62, 48, 66, 28, color=OL, w=4.4); ln(a, 62, 48, 66, 28, color="#94a3b8", w=2.4)
        for k, x in enumerate((32, 38, 44, 50)): cc(a, x, 61, 1.6, ("#22c55e", "#22c55e", "#fbbf24", "#cbd5e1")[k], w=0.7)
        cc(a, 24, 55, 1.8, OL, w=0.4); cc(a, 34, 55, 1.8, OL, w=0.4)
        for r_ in (8, 15, 22): arc(a, 40, 40, r_, 215, 325, color="#38bdf8", w=2.4, n=10)
        cc(a, 40, 40, 2.6, "#38bdf8", w=1.1)

    @st("engranereloj", "Eficiencia", "Efficiency")
    def _(a):
        gear(a, 28, 42, 22, "#94a3b8", 9, 0.0); cc(a, 28, 42, 14, "#e2e8f0", w=1.4)
        for k in range(12): r = math.radians(30 * k); ln(a, 28 + 12 * math.cos(r), 42 + 12 * math.sin(r), 28 + 13.4 * math.cos(r), 42 + 13.4 * math.sin(r), w=0.9)
        ln(a, 28, 42, 28, 33, w=1.6); ln(a, 28, 42, 35, 46, w=1.6)
        cc(a, 56, 24, 14, "#fbbf24"); cc(a, 56, 24, 10, "#fef3c7", w=1.2)
        for k in range(4): r = math.radians(90 * k); ln(a, 56 + 8 * math.cos(r), 24 + 8 * math.sin(r), 56 + 9.4 * math.cos(r), 24 + 9.4 * math.sin(r), w=1)
        ln(a, 56, 24, 56, 17, w=1.4); ln(a, 56, 24, 61, 27, w=1.4)
        a.text(50, 52, "%", 20, "#16a34a")

    @st("scrum", "Tablero de tareas", "Task board")
    def _(a):
        rr(a, 6, 10, 74, 70, 4, "#e2e8f0")
        for k, (t, c) in enumerate((("Por hacer", "#fca5a5"), ("Haciendo", "#fde68a"), ("Listo", "#86efac"))):
            x = 9 + k * 22; rr(a, x, 13, x + 20, 67, 2, "#f8fafc", w=1.1); rr(a, x, 13, x + 20, 21, 2, c, w=1.1)
        for x, y, c in ((11, 25, "#fca5a5"), (11, 36, "#fca5a5"), (33, 25, "#fde68a"), (55, 25, "#86efac"), (55, 36, "#86efac"), (55, 47, "#86efac")):
            rr(a, x, y, x + 16, y + 9, 1.5, c, w=1.1)
        eyes(a, 41, 56, 4, 1.4, "dot"); smile(a, 41, 56.8, 2.4, 1.2)
