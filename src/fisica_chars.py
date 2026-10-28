import math
from _draw import *


def extend(P):
    def st(sid, name, en): return P.sticker("ch-" + sid, name, en, 80, 80)

    @st("pendulo", "Péndulo", "Pendulum")
    def _(a):
        rr(a, 12, 4, 68, 11, 2, "#94a3b8"); arc(a, 40, 9, 56, 62, 118, color="#94a3b8", w=1.2)
        ln(a, 40, 10, 24, 56, color=OL, w=3.4); ln(a, 40, 10, 24, 56, color="#cbd5e1", w=1.6); cc(a, 40, 10, 2.4, "#475569", w=1.2)
        cc(a, 22, 62, 13, "#f87171"); shine(a, 17, 56, 3.4, 1.8); face(a, 22, 62, "dot", "smile", 5, 2.2, my=68, cheeks=True)

    @st("prisma", "Prisma", "Prism")
    def _(a):
        ln(a, 3, 52, 27, 47, color="#475569", w=3.4); ln(a, 3, 52, 27, 47, color="#ffffff", w=1.6)
        for k, c in enumerate(("#ef4444", "#fb923c", "#fde047", "#4ade80", "#38bdf8", "#8b5cf6")):
            ln(a, 54, 45, 77, 28 + k * 5.5, color=c, w=3)
        pg(a, 40, 14, 66, 62, 14, 62, fill="#bae6fd"); shine(a, 33, 38, 2.2, 7)
        face(a, 40, 48, "dot", "smile", 6.5, 2.4, my=54, cheeks=True)

    @st("balanza", "Balanza", "Balance")
    def _(a):
        rr(a, 36, 20, 44, 66, 2, "#94a3b8"); rr(a, 22, 66, 58, 74, 3, "#64748b")
        ln(a, 12, 24, 68, 24, color=OL, w=5); ln(a, 12, 24, 68, 24, color="#fbbf24", w=3)
        for x in (12, 68):
            ln(a, x, 24, x - 8, 48, w=1.4); ln(a, x, 24, x + 8, 48, w=1.4)
            pg(a, x - 13, 48, x + 13, 48, x + 8, 55, x - 8, 55, fill="#cbd5e1")
        cc(a, 12, 42, 5.5, "#4ade80", w=1.4); rr(a, 61, 40, 75, 48, 2, "#60a5fa", w=1.4); a.text(65, 41, "kg", 5.5, "#ffffff")
        cc(a, 40, 24, 9, "#fde047"); face(a, 40, 24, "dot", "smile", 3.6, 1.7, my=27)

    @st("telescopio", "Telescopio", "Telescope")
    def _(a):
        for x in (22, 38, 54): ln(a, 38, 40, x, 74, w=2.6)
        ln(a, 14, 56, 54, 26, color=OL, w=15); ln(a, 14, 56, 54, 26, color="#60a5fa", w=11.6)
        ln(a, 26, 47, 30, 44, color=OL, w=15.4); ln(a, 42, 35, 46, 32, color=OL, w=15.4)
        ln(a, 26, 47, 30, 44, color="#1d4ed8", w=11); ln(a, 42, 35, 46, 32, color="#1d4ed8", w=11)
        cc(a, 60, 22, 12, "#f8fafc"); face(a, 60, 22, "big", "smile", 4.4, 1.7, my=28)
        ln(a, 10, 60, 6, 64, w=4); star(a, 16, 14, 4); star(a, 70, 64, 3.2, "#fde68a")

    @st("saturno", "Planeta con anillos", "Ringed planet")
    def _(a):
        def ring(a0, a1, col, w_):
            pts = []
            for k in range(25):
                t = math.radians(a0 + (a1 - a0) * k / 24); x, y = 36 * math.cos(t), 10 * math.sin(t); r = math.radians(-20)
                pts.append((40 + x * math.cos(r) - y * math.sin(r), 40 + x * math.sin(r) + y * math.cos(r)))
            a._add(pts, col, w_)
        ring(180, 360, OL, 7); ring(180, 360, "#fde68a", 4.4)
        cc(a, 40, 40, 21, "#fb923c"); a.circle(40, 40, 21, color="#fdba74", w=0.1)
        shine(a, 31, 29, 4, 2); face(a, 40, 41, "dot", "smile", 7, 2.6, my=47, cheeks=True)
        ring(0, 180, OL, 7); ring(0, 180, "#fde68a", 4.4); star(a, 10, 12, 3.4); star(a, 72, 70, 3)

    @st("resorte", "Resorte", "Spring")
    def _(a):
        rr(a, 12, 4, 68, 10, 2, "#94a3b8")
        pts = [(40, 10)] + [(40 + (11 if k % 2 else -11), 14 + k * 4.6) for k in range(8)] + [(40, 49)]
        a._add(pts, OL, 4.2); a._add(pts, "#cbd5e1", 2.4)
        rr(a, 20, 49, 60, 74, 5, "#60a5fa"); a.text(36, 52, "m", 9, "#ffffff"); face(a, 40, 62, "dot", "smile", 8, 2.4, my=67, cheeks=True)

    @st("termometro", "Termómetro", "Thermometer")
    def _(a):
        rr(a, 32, 6, 48, 56, 8, "#f8fafc"); rr(a, 37.5, 20, 42.5, 58, 2.5, "#ef4444", w=0.1)
        cc(a, 40, 62, 13, "#ef4444")
        for k in range(5): ln(a, 52, 14 + k * 8, 57 if k % 2 == 0 else 55, 14 + k * 8, w=1.5)
        shine(a, 35, 57, 2.4, 3.4); face(a, 40, 63, "dot", "smile", 5, 2.2, my=68, col=OL) if False else face(a, 40, 63, "big", "smile", 4.6, 1.6, my=68)

    @st("cuna", "Cuna de Newton", "Newton's cradle")
    def _(a):
        rr(a, 4, 6, 76, 13, 3, "#94a3b8"); rr(a, 8, 66, 72, 74, 3, "#475569")
        for x in (34, 44, 54, 64):
            ln(a, x, 13, x, 45, w=1.3); cc(a, x, 50, 5.2, "#cbd5e1", w=1.5)
        ln(a, 24, 13, 6, 45, w=1.3); cc(a, 6, 49, 5.2, "#f87171", w=1.5)
        for x, y in ((6, 49),): eyes(a, x, y - 0.5, 1.8, 0.9, "dot")
        for x in (34, 44, 54, 64): eyes(a, x, 49.5, 1.7, 0.9, "dot")
        ln(a, 24, 13, 24, 13, w=1)

    @st("lente", "Lente", "Lens")
    def _(a):
        for y in (22, 40, 58): ln(a, 4, y, 37, y, color="#fb923c", w=1.8); ln(a, 43, y, 76, 40, color="#fb923c", w=1.8) if False else None
        ln(a, 4, 40, 76, 40, color="#cbd5e1", w=1)
        for y in (20, 40, 60):
            ln(a, 4, y, 40, y, color="#fb923c", w=2); ln(a, 40, y, 74, 40, color="#fb923c", w=2)
        cc(a, 40, 40, 13, "#bae6fd", ry=31); shine(a, 35, 22, 2.4, 6)
        face(a, 40, 40, "dot", "smile", 4.4, 2.2, my=46); star(a, 74, 40, 2.6, "#ef4444")

    @st("plano", "Plano inclinado", "Inclined plane")
    def _(a):
        pg(a, 6, 72, 74, 72, 74, 28, fill="#fcd34d")
        ln(a, 6, 72, 74, 28, color=OL, w=1.8)
        cx, cy = 34.4, 42.4
        cc(a, cx, cy, 10, "#f87171"); shine(a, cx - 4, cy - 4, 2.6, 1.4); face(a, cx, cy, "dot", "smile", 4, 1.8, my=cy + 5.5, cheeks=True)
        arc(a, 74, 72, 16, 180, 212, color=OL, w=1.5)
