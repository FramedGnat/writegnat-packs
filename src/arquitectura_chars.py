import math
from _draw import *


def extend(P):
    def st(sid, name, en): return P.sticker("ch-" + sid, name, en, 80, 80)

    @st("compas", "Compás de punta seca", "Drawing compass")
    def _(a):
        ln(a, 40, 14, 22, 70, color=OL, w=7); ln(a, 40, 14, 22, 70, color="#cbd5e1", w=4.4)
        ln(a, 40, 14, 58, 70, color=OL, w=7); ln(a, 40, 14, 58, 70, color="#cbd5e1", w=4.4)
        pg(a, 19, 66, 25, 66, 22, 76, fill="#64748b", w=1.3); pg(a, 55, 66, 61, 66, 58, 76, fill="#f59e0b", w=1.3)
        ln(a, 30, 42, 50, 42, color=OL, w=3.4); ln(a, 30, 42, 50, 42, color="#94a3b8", w=1.6)
        rr(a, 34, 6, 46, 16, 3, "#f97316"); cc(a, 40, 11, 1.6, WH, w=0.8)
        face(a, 40, 28, "dot", "smile", 4.2, 1.8, my=33)

    @st("maqueta", "Maqueta", "Scale model")
    def _(a):
        pg(a, 6, 56, 74, 56, 70, 68, 10, 68, fill="#a3e635", w=1.6); rr(a, 6, 66, 74, 72, 2, "#a16207", w=1.6)
        rr(a, 14, 38, 38, 58, 2, "#fde68a"); pg(a, 12, 38, 26, 26, 40, 38, fill="#ef4444", w=1.6)
        rr(a, 22, 46, 30, 58, 1.5, "#92400e", w=1.2); rr(a, 16, 41, 21, 46, 1, "#bae6fd", w=1)
        rr(a, 46, 22, 64, 58, 2, "#93c5fd"); 
        for r_ in range(3): rr(a, 50, 27 + r_ * 10, 55, 33 + r_ * 10, 1, "#fef9c3", w=1); rr(a, 58, 27 + r_ * 10, 62, 33 + r_ * 10, 1, "#fef9c3", w=1)
        cc(a, 68, 50, 4, "#22c55e", w=1.2); ln(a, 68, 54, 68, 58, w=1.4)
        face(a, 26, 52, "dot", "smile", 0.1, 0.1, my=54) if False else None

    @st("plano", "Plano enrollado", "Rolled blueprint")
    def _(a):
        pg(a, 14, 26, 62, 18, 66, 56, 18, 64, fill="#bfdbfe")
        for k in range(4): ln(a, 24, 30 + k * 8, 56, 26 + k * 8, color="#ffffff", w=1)
        ln(a, 24, 50, 40, 36, color="#ffffff", w=1.2); a.rect(38, 36, 50, 48, color="#ffffff", w=1.2)
        cc(a, 16, 46, 10, "#93c5fd", ry=18, w=1.8); cc(a, 16, 46, 4, "#dbeafe", ry=11, w=1.3)
        ln(a, 8, 72, 72, 72, color="#b45309", w=0.1)
        rr(a, 56, 20, 66, 62, 3, "#ef4444", w=1.6)
        face(a, 38, 52, "dot", "smile", 7, 2.2, my=58, col=OL)

    @st("regla-t", "Regla T", "T-square")
    def _(a):
        rr(a, 6, 10, 20, 70, 3, "#a16207"); rr(a, 16, 20, 74, 34, 2, "#fcd34d")
        for k in range(12): ln(a, 24 + k * 4.2, 20, 24 + k * 4.2, 20 + (6 if k % 2 == 0 else 3.5), w=1)
        face(a, 46, 29, "dot", "smile", 6, 1.7, my=32) if False else None
        cc(a, 13, 32, 3.4, "#fef3c7", w=1.2); cc(a, 13, 50, 3.4, "#fef3c7", w=1.2)
        eyes(a, 13, 22, 3.6, 1.6, "dot"); smile(a, 13, 62, 3.2, 1.5)

    @st("lapiz-tecnico", "Portaminas técnico", "Technical pencil")
    def _(a):
        pts = [(18, 62), (60, 20)]
        ln(a, 18, 62, 60, 20, color=OL, w=15); ln(a, 18, 62, 60, 20, color="#3b82f6", w=12)
        ln(a, 56, 24, 62, 18, color="#94a3b8", w=12); ln(a, 40, 40, 34, 46, color="#cbd5e1", w=12)
        pg(a, 10, 70, 14, 62, 22, 66, fill="#94a3b8", w=1.4); ln(a, 10, 70, 6, 76, color=OL, w=1.4)
        ln(a, 62, 20, 70, 12, color=OL, w=6); ln(a, 62, 20, 70, 12, color="#ef4444", w=3.6)
        face(a, 42, 38, "dot", "smile", 2, 1.4, my=42) if False else None
        cc(a, 34, 46, 0.1, WH, w=0.1)
        eyes(a, 38, 44, 3.2, 1.5, "dot"); 

    @st("escalimetro", "Escalímetro", "Architect's scale")
    def _(a):
        pg(a, 6, 34, 74, 24, 74, 44, 6, 54, fill="#34d399")
        pg(a, 6, 34, 74, 24, 74, 30, 6, 40, fill="#6ee7b7", w=1.2)
        for k in range(15):
            t = k / 14; x = 10 + 60 * t; y0 = 33.4 - 8.8 * t
            ln(a, x, y0, x, y0 + (5 if k % 2 == 0 else 3), w=1)
        face(a, 40, 42, "dot", "smile", 8, 2.2, my=47)
        a.text(8, 56, "1:100", 8, "#065f46")

    @st("cubo", "Cubo isométrico", "Isometric cube")
    def _(a):
        pg(a, 40, 8, 68, 22, 40, 36, 12, 22, fill="#fde68a"); pg(a, 12, 22, 40, 36, 40, 70, 12, 56, fill="#fb923c"); pg(a, 40, 36, 68, 22, 68, 56, 40, 70, fill="#f59e0b")
        face(a, 26, 48, "dot", "smile", 4, 1.7, my=54, cheeks=False)
        eyes(a, 54, 44, 4, 1.7, "dot"); smile(a, 54, 51, 3, 1.5)

    @st("columna", "Columna jónica", "Ionic column")
    def _(a):
        rr(a, 18, 8, 62, 14, 2, "#e2e8f0"); cc(a, 20, 18, 5, "#e2e8f0", w=1.6); cc(a, 60, 18, 5, "#e2e8f0", w=1.6); rr(a, 20, 14, 60, 22, 2, "#e2e8f0")
        rr(a, 25, 22, 55, 62, 2, "#f1f5f9")
        for x in (31, 40, 49): ln(a, x, 24, x, 60, color="#cbd5e1", w=1.4)
        rr(a, 20, 62, 60, 68, 2, "#e2e8f0"); rr(a, 14, 68, 66, 74, 2, "#cbd5e1")
        face(a, 40, 40, "dot", "smile", 7, 2.4, my=46, cheeks=True)

    @st("arco", "Arco de medio punto", "Round arch")
    def _(a):
        rr(a, 8, 28, 72, 72, 2, "#fca5a5"); a.circle(40, 40, 20, color="#fca5a5", fill=True)
        a._add([(20, 72), (20, 40)] + [(40 + 20 * math.cos(math.radians(180 + 6 * k)), 40 + 20 * math.sin(math.radians(180 + 6 * k))) for k in range(31)] + [(60, 40), (60, 72)], OL, 1.6, False)
        a._add([(20, 72), (20, 40)] + [(40 + 20 * math.cos(math.radians(180 + 6 * k)), 40 + 20 * math.sin(math.radians(180 + 6 * k))) for k in range(31)] + [(60, 40), (60, 72)], "#f8fafc", 1, True)
        ln(a, 8, 28, 72, 28, w=1.2)
        for k in range(7): a.line(40 + 20 * math.cos(math.radians(180 + 30 * k)), 40 + 20 * math.sin(math.radians(180 + 30 * k)), 40 + 28 * math.cos(math.radians(180 + 30 * k)), 40 + 28 * math.sin(math.radians(180 + 30 * k)), color=OL, w=1.1)
        pg(a, 36, 6, 44, 6, 44, 14, 36, 14, fill="#fbbf24", w=1.4)
        face(a, 40, 52, "dot", "smile", 6, 2.3, my=59)

    @st("flexometro", "Flexómetro", "Tape measure")
    def _(a):
        rr(a, 14, 18, 58, 62, 12, "#fbbf24"); cc(a, 36, 40, 10, "#fde68a", w=1.5)
        rr(a, 54, 50, 76, 60, 2, "#e2e8f0"); 
        for k in range(8): ln(a, 58 + k * 2.4, 50, 58 + k * 2.4, 50 + (5 if k % 2 == 0 else 3), w=1)
        rr(a, 72, 47, 77, 63, 1.5, "#64748b", w=1.3)
        face(a, 36, 40, "dot", "smile", 4, 1.6, my=44, cheeks=False)
        shine(a, 22, 26, 4, 1.6)
