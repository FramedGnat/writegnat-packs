import math
from _draw import *


def extend(P):
    def st(sid, name, en): return P.sticker("ch-" + sid, name, en, 80, 80)

    def drop(a, cx, cy, r, tip, fill):
        d = cy - tip; al = math.degrees(math.acos(r / d)); a0 = -90 + al
        pts = [(cx, tip)] + [(cx + r * math.cos(math.radians(a0 + (360 - 2 * al) * k / 30)), cy + r * math.sin(math.radians(a0 + (360 - 2 * al) * k / 30))) for k in range(31)] + [(cx, tip)]
        a._add(pts, fill, 1.0, True); a._add(pts, OL, 1.8)

    @st("tubo", "Tubo de ensayo", "Test tube")
    def _(a):
        a.round_rect(30, 8, 50, 70, 10, color="#e0f2fe", fill=True)
        a.round_rect(30.8, 38, 49.2, 70, 9, color="#a78bfa", fill=True); a.poly(30.8, 38, 49.2, 38, 49.2, 50, 30.8, 50, color="#a78bfa", fill=True)
        a.round_rect(30, 8, 50, 70, 10, color=OL, w=1.7); rr(a, 27, 5, 53, 11, 2.2, "#e2e8f0", w=1.5)
        for x, y, r in ((35, 46, 1.6), (45, 43, 1.2), (44, 33, 1.4)): a.circle(x, y, r, color="#ffffff", fill=True); a.circle(x, y, r, color=OL, w=0.8)
        face(a, 40, 55, "dot", "smile", 5, 2.2, my=60, cheeks=True); shine(a, 33.5, 22, 1.6, 7)

    @st("mechero", "Mechero", "Bunsen burner")
    def _(a):
        pg(a, 40, 4, 48, 20, 50, 32, 40, 38, 30, 32, 32, 20, fill="#fb923c"); pg(a, 40, 16, 44, 26, 44, 32, 40, 35, 36, 32, 36, 26, fill="#fde047", w=1.1)
        rr(a, 35, 36, 45, 62, 2, "#94a3b8"); rr(a, 32, 46, 48, 53, 2.5, "#64748b", w=1.4)
        rr(a, 22, 60, 58, 74, 5, "#475569"); face(a, 40, 67, "dot", "smile", 7, 2.2, my=71)
        shine(a, 38, 44, 1, 3)

    @st("agua", "Molécula de agua", "Water molecule")
    def _(a):
        ln(a, 34, 50, 18, 63, color=OL, w=5); ln(a, 46, 50, 62, 63, color=OL, w=5)
        ln(a, 34, 50, 18, 63, color="#e2e8f0", w=2.6); ln(a, 46, 50, 62, 63, color="#e2e8f0", w=2.6)
        cc(a, 40, 38, 18, "#f87171"); shine(a, 32, 28, 4, 2); face(a, 40, 37, "dot", "smile", 7, 2.7, my=43, cheeks=True)
        for x in (16, 64):
            cc(a, x, 66, 9, "#f8fafc"); a.text(x - 2.6, 62.4, "H", 7, "#1e293b"); 
        a.text(33, 3, "H₂O", 8, "#1e293b")

    @st("probeta", "Probeta", "Graduated cylinder")
    def _(a):
        pg(a, 29, 66, 51, 66, 56, 74, 24, 74, fill="#94a3b8")
        rr(a, 29, 8, 51, 68, 3, "#e0f2fe"); rr(a, 30, 36, 50, 67, 2, "#4ade80", w=0.1)
        rr(a, 29, 8, 51, 68, 3, "#e0f2fe", w=0.1); a.rect(29, 8, 51, 68, color=OL, w=1.7)
        for k in range(6): ln(a, 29, 14 + k * 8.5, 34 if k % 2 == 0 else 32, 14 + k * 8.5, w=1.3)
        a.rect(30, 36, 50, 67, color="#4ade80", fill=True); a.rect(29, 8, 51, 68, color=OL, w=1.7)
        pg(a, 26, 8, 54, 8, 54, 11, 26, 11, fill="#e2e8f0", w=1.4)
        face(a, 41, 50, "dot", "smile", 4.8, 2.1, my=55, cheeks=False)

    @st("gota", "Gota", "Drop")
    def _(a):
        drop(a, 40, 50, 22, 6, "#38bdf8"); shine(a, 30, 48, 3.2, 8)
        face(a, 40, 52, "dot", "smile", 7.5, 2.7, my=59, cheeks=True)

    @st("tabla", "Tabla periódica", "Periodic table")
    def _(a):
        cols = {"a": "#f87171", "b": "#fb923c", "t": "#60a5fa", "n": "#4ade80", "g": "#c084fc", "m": "#fbbf24"}
        rows = ["a........g", "ab....nnng", "ab....nnng", "abttttmnng", "abttttmmng"]
        for r, row in enumerate(rows):
            for c, ch in enumerate(row):
                if ch == ".": continue
                x = 8 + c * 6.4; y = 12 + r * 10.4
                rr(a, x, y, x + 5.6, y + 9.4, 1.2, cols[ch], w=0.9)
        for k, c in enumerate(cols.values()): cc(a, 12 + k * 11, 72, 3.2, c, w=1)

    @st("cristal", "Cristal", "Crystal")
    def _(a):
        pg(a, 22, 20, 58, 20, 72, 36, 40, 72, 8, 36, fill="#67e8f9")
        ln(a, 8, 36, 72, 36, color=OL, w=1.2); ln(a, 22, 20, 30, 36, 40, 72, w=1.2); ln(a, 58, 20, 50, 36, 40, 72, w=1.2); ln(a, 30, 36, 40, 20, 50, 36, w=1.2)
        a.poly(22, 20, 30, 36, 8, 36, color="#a5f3fc", fill=True); a.poly(58, 20, 72, 36, 50, 36, color="#22d3ee", fill=True)
        pg(a, 22, 20, 58, 20, 72, 36, 40, 72, 8, 36, fill="#67e8f9", w=1.8) if False else None
        a.poly(22, 20, 58, 20, 72, 36, 40, 72, 8, 36, color=OL, w=1.8)
        face(a, 40, 40, "dot", "smile", 6, 2.4, my=46, cheeks=False); star(a, 66, 12, 4, "#fde68a"); star(a, 12, 18, 3, "#fde68a")

    @st("vaso", "Vaso de precipitados", "Beaker")
    def _(a):
        a.round_rect(18, 10, 62, 70, 5, color="#e0f2fe", fill=True)
        a.round_rect(19, 34, 61, 70, 5, color="#fdba74", fill=True); a.poly(19, 34, 61, 34, 61, 46, 19, 46, color="#fdba74", fill=True)
        a.round_rect(18, 10, 62, 70, 5, color=OL, w=1.7); pg(a, 14, 10, 66, 10, 66, 13, 14, 13, fill="#e2e8f0", w=1.4)
        for k in range(3): ln(a, 18, 22 + k * 12, 27 if k % 2 == 0 else 24, 22 + k * 12, w=1.3)
        for x, y, r in ((26, 62, 1.8), (52, 56, 1.4), (30, 42, 1.3)): a.circle(x, y, r, color="#ffffff", fill=True); a.circle(x, y, r, color=OL, w=0.8)
        face(a, 42, 52, "dot", "smile", 7, 2.5, my=58, cheeks=True); shine(a, 24, 26, 1.8, 6)

    @st("embudo", "Embudo", "Funnel")
    def _(a):
        rr(a, 36, 44, 44, 72, 2, "#bae6fd"); pg(a, 10, 10, 70, 10, 46, 46, 34, 46, fill="#e0f2fe")
        a.poly(10, 10, 70, 10, 46, 46, 34, 46, color="#e0f2fe", fill=True); a.poly(10, 10, 70, 10, 46, 46, 34, 46, color=OL, w=1.8)
        ln(a, 16, 12, 34, 40, color="#ffffff", w=1.6); face(a, 40, 22, "dot", "smile", 8, 2.6, my=28, cheeks=True)
        drop(a, 40, 74, 3, 66, "#38bdf8") if False else None

    @st("bata", "Científico con bata", "Scientist")
    def _(a):
        for s in (-1, 1):
            ln(a, 40 + s * 14, 46, 40 + s * 24, 64, color=OL, w=9); ln(a, 40 + s * 14, 46, 40 + s * 24, 64, color="#f8fafc", w=6.4); cc(a, 40 + s * 24, 66, 3.6, "#fcd7a8", w=1.4)
        pg(a, 22, 38, 58, 38, 64, 76, 16, 76, fill="#f8fafc")
        pg(a, 34, 38, 46, 38, 40, 52, fill="#38bdf8", w=1.4); ln(a, 40, 52, 40, 76, w=1.3); cc(a, 40, 58, 1.2, OL, w=0.3); cc(a, 40, 66, 1.2, OL, w=0.3)
        rr(a, 20, 56, 30, 66, 1.5, "#e2e8f0", w=1.2); ln(a, 24, 52, 24, 58, color="#ef4444", w=1.6)
        cc(a, 40, 22, 15, "#fde68a"); pg(a, 25, 18, 28, 8, 40, 5, 52, 8, 55, 18, 40, 13, fill="#92400e", w=1.5)
        rr(a, 27, 17, 53, 27, 5, "#bae6fd", w=1.6); ln(a, 25, 22, 22, 22, w=1.6); ln(a, 55, 22, 58, 22, w=1.6)
        eyes(a, 40, 22, 6.2, 2, "dot"); smile(a, 40, 31, 4, 1.7)
