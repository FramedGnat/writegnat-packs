import math
from _draw import *


def extend(P):
    def st(sid, name, en):
        return P.sticker("ch-" + sid, name, en, 80, 80)

    @st("grua", "Grúa torre", "Tower crane")
    def _(a):
        rr(a, 12, 72, 44, 77, 2, "#475569")
        for k in range(5):
            y0 = 72 - k * 12; ln(a, 24, y0, 32, y0 - 12, color="#f59e0b", w=2); ln(a, 32, y0, 24, y0 - 12, color="#f59e0b", w=2)
        ln(a, 24, 12, 24, 72, color="#f59e0b", w=2.6); ln(a, 32, 12, 32, 72, color="#f59e0b", w=2.6)
        rr(a, 4, 8, 78, 14, 2, "#fbbf24"); rr(a, 26, 2, 46, 8, 1, "#fde68a", w=1.3)
        ln(a, 28, 2, 60, 8, color=OL, w=1.2); rr(a, 6, 14, 18, 22, 2, "#64748b", w=1.4)
        ln(a, 62, 14, 62, 40, color=OL, w=1.6); rr(a, 55, 40, 69, 52, 3, "#38bdf8"); face(a, 62, 45, "dot", "smile", 3.4, 1.3, my=49)
        pg(a, 52, 56, 70, 56, 70, 62, 52, 62, fill="#ef4444", w=1.3)
        ln(a, 56, 52, 56, 56, w=1.2); ln(a, 66, 52, 66, 56, w=1.2)

    @st("viga", "Viga en I", "I-beam")
    def _(a):
        rr(a, 6, 16, 74, 28, 2, "#94a3b8"); rr(a, 6, 52, 74, 64, 2, "#94a3b8"); rr(a, 30, 26, 50, 54, 1, "#cbd5e1")
        for x in (12, 22, 58, 68): cc(a, x, 22, 1.6, "#64748b", w=0.8); cc(a, x, 58, 1.6, "#64748b", w=0.8)
        face(a, 40, 40, "dot", "smile", 5.4, 2.2, my=46, cheeks=False)
        shine(a, 22, 19.5, 6, 1.1)

    @st("excavadora", "Excavadora", "Excavator")
    def _(a):
        rr(a, 8, 56, 56, 74, 8, "#475569")
        for x in (16, 32, 48): cc(a, x, 65, 4, "#cbd5e1", w=1.3)
        rr(a, 14, 36, 50, 58, 4, "#fbbf24"); rr(a, 16, 26, 36, 40, 3, "#7dd3fc"); face(a, 26, 33, "dot", "smile", 4.4, 1.7, my=37)
        ln(a, 46, 44, 62, 24, color=OL, w=7.4); ln(a, 46, 44, 62, 24, color="#f59e0b", w=5)
        ln(a, 62, 24, 70, 50, color=OL, w=6.4); ln(a, 62, 24, 70, 50, color="#f59e0b", w=4)
        pg(a, 64, 50, 78, 50, 74, 64, 68, 64, fill="#94a3b8", w=1.6); cc(a, 62, 24, 3, "#64748b", w=1.2)
        a.rect(10, 74, 70, 77, color="#92400e", fill=True)

    @st("plano", "Plano enrollado", "Blueprint")
    def _(a):
        rr(a, 8, 16, 72, 66, 3, "#2563eb"); rr(a, 8, 16, 72, 24, 3, "#1d4ed8", w=1.6)
        for k in range(1, 6): ln(a, 8 + k * 10.7, 24, 8 + k * 10.7, 66, color="#60a5fa", w=0.6)
        for k in range(1, 4): ln(a, 8, 24 + k * 10.5, 72, 24 + k * 10.5, color="#60a5fa", w=0.6)
        a.rect(18, 32, 46, 56, color="#e0f2fe", w=1.4); ln(a, 32, 32, 32, 44, color="#e0f2fe", w=1.4); ln(a, 18, 44, 46, 44, color="#e0f2fe", w=1.4)
        ln(a, 52, 38, 66, 38, color="#e0f2fe", w=1.1); ln(a, 52, 44, 62, 44, color="#e0f2fe", w=1.1)
        face(a, 59, 56, "dot", "smile", 4, 1.7, my=60, col="#ffffff")
        cc(a, 8, 41, 4, "#e2e8f0", ry=25, w=1.6); cc(a, 72, 41, 4, "#e2e8f0", ry=25, w=1.6)

    @st("mezcladora", "Mezcladora de concreto", "Concrete mixer")
    def _(a):
        rr(a, 6, 52, 66, 62, 3, "#475569")
        for x in (18, 50): cc(a, x, 66, 7, "#334155", w=1.6); cc(a, x, 66, 2.8, "#cbd5e1", w=1)
        rr(a, 52, 34, 74, 56, 4, "#fbbf24"); rr(a, 56, 38, 68, 48, 2, "#7dd3fc", w=1.2)
        pg(a, 6, 28, 46, 14, 56, 30, 54, 52, 14, 52, fill="#f97316")
        for k in range(3): arc(a, 30, 34, 18 + k * 0, 200 + k * 35, 260 + k * 35, color="#fff7ed", w=2, n=6)
        face(a, 30, 38, "dot", "smile", 8, 2.6, my=45, cheeks=True)
        pg(a, 10, 30, 6, 24, 14, 22, fill="#fb923c", w=1.4)

    @st("nivel", "Nivel de burbuja", "Spirit level")
    def _(a):
        rr(a, 6, 28, 74, 52, 4, "#fbbf24"); rr(a, 28, 33, 52, 47, 7, "#bef264", w=1.6)
        cc(a, 40, 40, 5.4, "#fef9c3", w=1.4); ln(a, 34, 33, 34, 47, w=1.2); ln(a, 46, 33, 46, 47, w=1.2)
        cc(a, 40, 40, 1.4, OL, w=0.4)
        for k in range(4): ln(a, 10 + k * 3, 52, 10 + k * 3, 48, w=1.1); ln(a, 56 + k * 5, 52, 56 + k * 5, 48, w=1.1)
        cc(a, 16, 40, 2, OL, w=0.4); cc(a, 64, 40, 2, OL, w=0.4); smile(a, 64, 41, 2.6, 1.3)
        a.circle(15.4, 39.4, 0.6, color=WH, fill=True); a.circle(63.4, 39.4, 0.6, color=WH, fill=True)
        a.text(34, 56, "0°", 9, "#475569")

    @st("columna", "Columna y cimiento", "Column and footing")
    def _(a):
        rr(a, 8, 60, 72, 74, 2, "#a8a29e"); rr(a, 18, 54, 62, 62, 2, "#d6d3d1"); rr(a, 28, 8, 52, 56, 2, "#e7e5e4")
        rr(a, 24, 6, 56, 14, 2, "#d6d3d1"); ln(a, 34, 16, 34, 54, color="#d6d3d1", w=1.2); ln(a, 46, 16, 46, 54, color="#d6d3d1", w=1.2)
        face(a, 40, 32, "dot", "smile", 6, 2.4, my=38, cheeks=True)
        for x in (12, 68): ln(a, x, 74, x, 78, w=1.4)
        a.text(9.5, 64, "cimiento", 6, "#44403c")

    @st("teodolito", "Teodolito", "Theodolite")
    def _(a):
        for x, y in ((40, 40), ): pass
        ln(a, 40, 44, 22, 76, color=OL, w=3.2); ln(a, 40, 44, 58, 76, color=OL, w=3.2); ln(a, 40, 44, 40, 76, color=OL, w=3.2)
        rr(a, 28, 36, 52, 46, 3, "#94a3b8"); rr(a, 28, 10, 52, 36, 5, "#fbbf24")
        rr(a, 18, 18, 30, 28, 2, "#475569", w=1.4); cc(a, 15, 23, 3.2, "#bae6fd", w=1.3)
        face(a, 41, 21, "dot", "smile", 5.4, 2.2, my=27, cheeks=True)
        cc(a, 40, 6, 3.2, "#ef4444", w=1.3)

    @st("barrera", "Barrera de obra", "Road barrier")
    def _(a):
        ln(a, 16, 40, 12, 72, color=OL, w=4.4); ln(a, 64, 40, 68, 72, color=OL, w=4.4)
        rr(a, 6, 24, 74, 46, 4, "#ffffff")
        for k in range(6): pg(a, 8 + k * 12, 46, 18 + k * 12, 46, 26 + k * 12, 24, 16 + k * 12, 24, fill="#f97316", w=0.8) if k * 12 + 26 <= 74 else None
        a.round_rect(6, 24, 74, 46, 4, color=OL, w=1.8)
        cc(a, 40, 35, 11, "#fde047", w=1.6); face(a, 40, 34, "dot", "smile", 4.4, 1.8, my=39)
        cc(a, 12, 18, 3, "#fbbf24", w=1.4); cc(a, 68, 18, 3, "#fbbf24", w=1.4)

    @st("ladrillo", "Ladrillo feliz", "Happy brick")
    def _(a):
        pg(a, 8, 32, 60, 32, 72, 22, 20, 22, fill="#fdba74", w=1.6); pg(a, 60, 32, 72, 22, 72, 52, 60, 62, fill="#c2410c", w=1.6)
        rr(a, 8, 32, 60, 62, 3, "#ea580c")
        for x, y in ((18, 56), (38, 40), (52, 56)): cc(a, x, y, 1.4, "#fdba74", w=0.1)
        face(a, 34, 46, "dot", "smile", 8, 2.7, my=52, cheeks=True)
        a.rect(10, 64, 58, 70, color="#d6d3d1", fill=True); a.rect(10, 64, 58, 70, color=OL, w=1.2)
        rr(a, 14, 70, 66, 77, 2, "#ea580c", w=1.4)
