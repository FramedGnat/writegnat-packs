import math
from _draw import *


def extend(P):
    def st(sid, name, en): return P.sticker("ch-" + sid, name, en, 80, 80)

    @st("piano", "Piano de cola", "Grand piano")
    def _(a):
        a._add([(8, 30), (50, 16), (74, 22), (74, 44), (68, 46), (68, 62), (62, 62), (62, 48), (24, 48), (24, 62), (18, 62), (18, 48), (8, 48)], "#334155", 1, True)
        a._add([(8, 30), (50, 16), (74, 22), (74, 44), (68, 46), (68, 62), (62, 62), (62, 48), (24, 48), (24, 62), (18, 62), (18, 48), (8, 48), (8, 30)], OL, 1.8)
        rr(a, 8, 44, 66, 54, 2, "#ffffff", w=1.5)
        for k in range(10): ln(a, 14 + k * 5.4, 44, 14 + k * 5.4, 54, w=0.8)
        for k in (0, 1, 3, 4, 5, 7, 8): rr(a, 12.6 + k * 5.4, 44, 16 + k * 5.4, 50, 0.6, "#1e293b", w=0.6)
        shine(a, 30, 25, 9, 1.6); face(a, 40, 35, "dot", "smile", 6, 1.9, my=38, col=WH) if False else None
        eyes(a, 42, 33, 6, 2, "dot", "#f8fafc"); smile(a, 42, 37, 3.2, 1.6)
        ln(a, 38, 48, 38, 56, w=0.1)

    @st("violin", "Violín", "Violin")
    def _(a):
        ln(a, 40, 36, 40, 10, color=OL, w=7); ln(a, 40, 36, 40, 10, color="#7c2d12", w=4.4)
        rr(a, 34, 2, 46, 12, 3, "#9a3412", w=1.4); cc(a, 31, 6, 1.8, "#fde68a", w=0.8); cc(a, 49, 6, 1.8, "#fde68a", w=0.8)
        cc(a, 40, 50, 14, "#c2410c", ry=12); cc(a, 40, 66, 17, "#c2410c", ry=13); rr(a, 31, 52, 49, 62, 2, "#c2410c", w=0.1)
        a._add([(26, 52), (31, 56), (31, 60), (26, 62)], OL, 1.8, False); a._add([(54, 52), (49, 56), (49, 60), (54, 62)], OL, 1.8, False)
        shine(a, 31, 44, 3, 1.6)
        rr(a, 34, 66, 46, 70, 1.5, "#1e293b", w=0.8); ln(a, 36, 36, 36, 66, color="#fde68a", w=0.8); ln(a, 44, 36, 44, 66, color="#fde68a", w=0.8)
        eyes(a, 40, 55, 4.4, 1.6, "dot", "#ffedd5") if False else None
        ln(a, 62, 14, 70, 76, color=OL, w=1.8); ln(a, 62, 14, 70, 76, color="#a16207", w=0.6)
        ln(a, 29, 58, 29, 58.1, w=0.1)

    @st("flauta", "Flauta", "Flute")
    def _(a):
        ln(a, 8, 62, 72, 22, color=OL, w=11); ln(a, 8, 62, 72, 22, color="#cbd5e1", w=8)
        for k in range(5):
            t = 0.28 + 0.13 * k; x = 8 + 64 * t; y = 62 - 40 * t
            cc(a, x, y, 2.4, "#475569", w=1.2)
        for t in (0.2, 0.62, 0.9): ln(a, 8 + 64 * t - 1, 62 - 40 * t - 5, 8 + 64 * t + 1, 62 - 40 * t + 5, color=OL, w=1.6)
        cc(a, 14, 58, 2, "#0f172a", w=0.5)
        shine(a, 30, 48, 8, 1.2)
        eyes(a, 28, 56, 5, 1.8, "dot"); smile(a, 28, 60, 3.2, 1.5)
        for k, (x, y) in enumerate(((6, 40), (10, 32), (16, 26))): a.text(x, y, "♪", 9, "#6366f1")

    @st("bateria", "Batería", "Drum kit")
    def _(a):
        ln(a, 12, 20, 12, 70, w=1.6); ln(a, 68, 18, 68, 70, w=1.6)
        a.circle(12, 18, 10, color="#fbbf24", fill=True, ry=3); a.circle(12, 18, 10, color=OL, w=1.6, ry=3)
        a.circle(68, 22, 9, color="#fbbf24", fill=True, ry=3); a.circle(68, 22, 9, color=OL, w=1.6, ry=3)
        rr(a, 20, 38, 40, 52, 3, "#ef4444"); rr(a, 42, 38, 62, 52, 3, "#ef4444")
        a.circle(30, 38, 10, color="#fef3c7", fill=True, ry=3); a.circle(30, 38, 10, color=OL, w=1.5, ry=3); a.circle(52, 38, 10, color="#fef3c7", fill=True, ry=3); a.circle(52, 38, 10, color=OL, w=1.5, ry=3)
        rr(a, 22, 50, 58, 72, 10, "#dc2626"); a.circle(40, 62, 14, color="#fef3c7", fill=True, ry=10); a.circle(40, 62, 14, color=OL, w=1.6, ry=10)
        eyes(a, 40, 59, 5.5, 1.8, "dot"); smile(a, 40, 63, 4, 1.7)
        ln(a, 16, 74, 20, 72, w=2); ln(a, 64, 74, 60, 72, w=2)
        ln(a, 10, 42, 24, 32, color="#e2e8f0", w=2.2); ln(a, 70, 42, 56, 32, color="#e2e8f0", w=2.2)

    @st("trompeta", "Trompeta", "Trumpet")
    def _(a):
        ln(a, 12, 42, 52, 42, color=OL, w=6); ln(a, 12, 42, 52, 42, color="#fbbf24", w=3.6)
        a._add([(52, 40), (60, 30), (72, 22), (72, 62), (60, 54), (52, 44)], "#fbbf24", 1, True); a._add([(52, 40), (60, 30), (72, 22), (72, 62), (60, 54), (52, 44), (52, 40)], OL, 1.8)
        a.circle(72, 42, 4, color="#fde68a", fill=True, ry=20); a.circle(72, 42, 4, color=OL, w=1.6, ry=20)
        rr(a, 6, 38, 16, 46, 3, "#f59e0b")
        for x in (24, 32, 40):
            ln(a, x, 42, x, 30, color=OL, w=5); ln(a, x, 42, x, 30, color="#fcd34d", w=2.6); cc(a, x, 28, 3, "#ef4444", w=1.3)
        a._add([(18, 46), (14, 62), (30, 62), (46, 56), (52, 46)], OL, 5); a._add([(18, 46), (14, 62), (30, 62), (46, 56), (52, 46)], "#fbbf24", 2.8)
        shine(a, 62, 34, 4, 1.6)

    @st("clave-fa", "Clave de fa", "Bass clef")
    def _(a):
        cc(a, 40, 40, 32, "#e0e7ff")
        a._add([(22, 28), (30, 20), (44, 20), (54, 28), (54, 40), (46, 54), (34, 62), (24, 66)], "#4338ca", 5.6)
        cc(a, 24, 29, 5.4, "#4338ca", w=1.4); cc(a, 61, 26, 2.6, "#4338ca", w=0.5); cc(a, 61, 40, 2.6, "#4338ca", w=0.5)
        eyes(a, 44, 45, 6, 1.9, "dot") if False else None

    @st("maracas", "Maracas", "Maracas")
    def _(a):
        for x, c, ang in ((22, "#ef4444", -18), (56, "#22c55e", 18)):
            r = math.radians(ang)
            x0, y0 = x + 10 * math.sin(r) * 0, 0
        ln(a, 24, 44, 14, 70, color=OL, w=7); ln(a, 24, 44, 14, 70, color="#b45309", w=4.4)
        ln(a, 56, 44, 66, 70, color=OL, w=7); ln(a, 56, 44, 66, 70, color="#b45309", w=4.4)
        cc(a, 25, 30, 17, "#f87171", ry=20); cc(a, 55, 30, 17, "#4ade80", ry=20)
        for x, c in ((25, "#fde047"), (55, "#fde047")): ln(a, x - 12, 22, x + 12, 40, color=c, w=2); ln(a, x - 12, 34, x + 6, 44, color=c, w=2)
        eyes(a, 25, 26, 5.4, 1.8, "dot"); smile(a, 25, 31, 3.4, 1.6); eyes(a, 55, 26, 5.4, 1.8, "dot"); smile(a, 55, 31, 3.4, 1.6)
        shine(a, 18, 17, 2.6, 4); shine(a, 48, 17, 2.6, 4)

    @st("diapason", "Diapasón", "Tuning fork")
    def _(a):
        a._add([(28, 6), (28, 40), (34, 48), (40, 48), (46, 48), (52, 40), (52, 6)], OL, 11); a._add([(28, 6), (28, 40), (34, 48), (40, 48), (46, 48), (52, 40), (52, 6)], "#cbd5e1", 8)
        ln(a, 40, 48, 40, 70, color=OL, w=9); ln(a, 40, 48, 40, 70, color="#cbd5e1", w=6); cc(a, 40, 72, 4, "#94a3b8", w=1.4)
        for s in (-1, 1):
            for k, r in enumerate((6, 11)): arc(a, 40 + s * 24, 24, r, 300 if s == 1 else 120, 420 if s == 1 else 240, color="#6366f1", w=1.8)
        eyes(a, 40, 60, 3.6, 1.5, "dot"); 

    @st("partitura", "Partitura", "Sheet music")
    def _(a):
        rr(a, 8, 8, 72, 72, 4, "#fffbeb")
        for r_ in range(2):
            y0 = 16 + r_ * 28
            for k in range(5): ln(a, 14, y0 + k * 4.4, 66, y0 + k * 4.4, color="#64748b", w=0.9)
        for x, y, up in ((24, 21, 1), (36, 38, 1), (48, 26, 1), (58, 46, 1)):
            ln(a, x + 3, y, x + 3, y - 14, w=1.4); cc(a, x, y, 3.2, "#1e293b", ry=2.6, w=0.5)
        ln(a, 27, 7 + 12, 27, 21, w=0.1)
        ln(a, 14, 16, 14, 33, w=1.2); ln(a, 14, 44, 14, 61, w=1.2)
        face(a, 40, 66, "dot", "smile", 6, 1.6, my=69) if False else None
        eyes(a, 28, 53, 4, 1.4, "dot"); smile(a, 28, 58, 2.6, 1.2)

    @st("altavoz", "Altavoz", "Speaker")
    def _(a):
        rr(a, 18, 6, 62, 74, 8, "#334155"); cc(a, 40, 24, 8, "#64748b", w=1.5); cc(a, 40, 24, 3.2, "#0f172a", w=1)
        cc(a, 40, 52, 16, "#475569", w=1.6); cc(a, 40, 52, 10, "#94a3b8", w=1.4); cc(a, 40, 52, 4, "#0f172a", w=1)
        eyes(a, 40, 50, 5, 1.6, "dot", "#f1f5f9") if False else None
        for s in (-1, 1):
            for r in (22, 28): arc(a, 40 + s * 0, 40, r, -25 if s == 1 else 155, 25 if s == 1 else 205, color="#6366f1", w=2) if False else None
        for r in (30, 36): arc(a, 40, 40, r, -28, 28, color="#6366f1", w=2); arc(a, 40, 40, r, 152, 208, color="#6366f1", w=2)
