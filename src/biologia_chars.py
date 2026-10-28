import math
from _draw import *


def extend(P):
    def st(sid, name, en): return P.sticker("ch-" + sid, name, en, 80, 80)

    def bez(p0, p1, p2, n=16):
        return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]) for t in (k / n for k in range(n + 1))]

    @st("microscopio", "Microscopio", "Microscope")
    def _(a):
        rr(a, 16, 64, 66, 72, 3, "#475569")
        a._add(bez((50, 22), (74, 34), (56, 64)), OL, 11); a._add(bez((50, 22), (74, 34), (56, 64)), "#94a3b8", 7.4)
        rr(a, 31, 5, 47, 13, 2, "#cbd5e1"); rr(a, 28, 13, 52, 45, 4, "#60a5fa"); rr(a, 34, 45, 46, 53, 2, "#1d4ed8", w=1.5)
        rr(a, 22, 55, 52, 60, 1.5, "#cbd5e1"); cc(a, 40, 66.5, 0.1, "#475569", w=0.1)
        face(a, 40, 29, "dot", "smile", 6.2, 2.4, my=35, cheeks=True); shine(a, 32, 18, 1.6, 3)

    @st("estetoscopio", "Estetoscopio", "Stethoscope")
    def _(a):
        for pts in (bez((22, 8), (20, 44), (40, 46)), bez((58, 8), (60, 44), (40, 46)), bez((40, 46), (40, 58), (50, 56))):
            a._add(pts, OL, 5.4); a._add(pts, "#64748b", 3)
        for x in (22, 58): cc(a, x, 7, 3.4, "#cbd5e1", w=1.5)
        cc(a, 54, 61, 14, "#cbd5e1"); cc(a, 54, 61, 10.4, "#f8fafc", w=1.2); shine(a, 47, 54, 2.4, 1.4)
        face(a, 54, 61, "dot", "smile", 4.4, 1.9, my=66, cheeks=False)

    @st("sangre", "Gota de sangre", "Blood drop")
    def _(a):
        r, cy, tip = 21, 50, 6; d = cy - tip; al = math.degrees(math.acos(r / d)); a0 = -90 + al
        pts = [(40, tip)] + [(40 + r * math.cos(math.radians(a0 + (360 - 2 * al) * k / 30)), cy + r * math.sin(math.radians(a0 + (360 - 2 * al) * k / 30))) for k in range(31)] + [(40, tip)]
        a._add(pts, "#ef4444", 1, True); a._add(pts, OL, 1.8); shine(a, 30, 48, 3, 7)
        face(a, 40, 52, "big", "smile", 7, 2.6, my=59, cheeks=True)
        a.poly(34, 66, 46, 66, 46, 69, 34, 69, color="#ffffff", fill=True) if False else None

    @st("hueso", "Hueso", "Bone")
    def _(a):
        ux, uy = 0.78, -0.62; nx, ny = 0.62, 0.78
        p0 = (14, 64); p1 = (66, 16)
        ln(a, *p0, *p1, color=OL, w=17); ln(a, *p0, *p1, color="#f8fafc", w=14)
        for (ex, ey) in (p0, p1):
            for s in (-1, 1): cc(a, ex + s * nx * 7 - ux * 1.5 * (1 if ex < 40 else -1) * -1, ey + s * ny * 7, 7.4, "#f8fafc")
        ln(a, *p0, *p1, color="#f8fafc", w=13.2)
        for (ex, ey) in (p0, p1):
            for s in (-1, 1): a.circle(ex + s * nx * 7, ey + s * ny * 7, 7.4, color="#f8fafc", fill=True)
        face(a, 40, 40, "dot", "smile", 5.4, 2.3, my=46, cheeks=True)

    @st("pulmones", "Pulmones", "Lungs")
    def _(a):
        ln(a, 40, 4, 40, 28, color=OL, w=8); ln(a, 40, 4, 40, 28, color="#fbcfe8", w=5)
        for s in (-1, 1): ln(a, 40, 28, 40 + s * 15, 40, color=OL, w=6); ln(a, 40, 28, 40 + s * 15, 40, color="#fbcfe8", w=3.4)
        cc(a, 26, 52, 16, "#fda4af", ry=22); cc(a, 54, 52, 16, "#fda4af", ry=22)
        a.circle(26, 52, 15, color="#fda4af", fill=True, ry=21); a.circle(54, 52, 15, color="#fda4af", fill=True, ry=21)
        shine(a, 20, 40, 2.4, 6); shine(a, 48, 40, 2.4, 6)
        face(a, 40, 52, "dot", "smile", 12, 2.7, my=60, cheeks=True)

    @st("semilla", "Semilla que brota", "Sprouting seed")
    def _(a):
        for x in (30, 40, 50): a._add(bez((x, 62), (x + (-1 if x < 40 else 1) * 4, 70), (x + (-1 if x < 40 else (0 if x == 40 else 1)) * 7, 76)), "#a16207", 1.8)
        ln(a, 40, 40, 40, 22, color=OL, w=5); ln(a, 40, 40, 40, 22, color="#22c55e", w=2.8)
        pg(a, 40, 30, 20, 18, 12, 30, 28, 34, fill="#4ade80"); pg(a, 40, 24, 60, 10, 70, 22, 54, 28, fill="#4ade80")
        cc(a, 40, 52, 19, "#d6a96b", ry=15); shine(a, 30, 45, 3.6, 1.8); face(a, 40, 53, "dot", "smile", 7, 2.6, my=59, cheeks=True)

    @st("pastilla", "Pastilla", "Capsule")
    def _(a):
        a.round_rect(6, 24, 74, 56, 16, color="#f8fafc", fill=True); a.poly(40, 24, 58, 24, 58, 56, 40, 56, color="#f8fafc", fill=True)
        a.round_rect(6, 24, 42, 56, 16, color="#f87171", fill=True); a.poly(24, 24, 42, 24, 42, 56, 24, 56, color="#f87171", fill=True)
        ln(a, 42, 24, 42, 56, w=1.8); a.round_rect(6, 24, 74, 56, 16, color=OL, w=1.9)
        shine(a, 20, 30, 6, 1.6); face(a, 40, 40, "dot", "smile", 8, 2.6, my=47, cheeks=True)
        a.text(60, 29, "+", 11, "#f87171") if False else None

    @st("jeringa", "Jeringa", "Syringe")
    def _(a):
        ln(a, 58, 40, 76, 40, color=OL, w=2.4); ln(a, 58, 40, 76, 40, color="#e2e8f0", w=1)
        ln(a, 6, 40, 18, 40, color=OL, w=4); rr(a, 2, 30, 9, 50, 2, "#38bdf8", w=1.5)
        rr(a, 16, 25, 58, 55, 5, "#f0f9ff"); rr(a, 41, 27, 56, 53, 3, "#86efac", w=0.1)
        rr(a, 16, 25, 58, 55, 5, "#f0f9ff", w=1.8) if False else a.round_rect(16, 25, 58, 55, 5, color=OL, w=1.8)
        rr(a, 53, 20, 59, 60, 2, "#cbd5e1", w=1.5); rr(a, 41, 27, 53, 53, 2, "#86efac", w=0.1)
        for k in range(5): ln(a, 20 + k * 5, 25, 20 + k * 5, 29 if k % 2 == 0 else 27, w=1.2)
        face(a, 30, 40, "dot", "smile", 5, 2.1, my=45, cheeks=False)

    @st("flor", "Flor", "Flower")
    def _(a):
        ln(a, 40, 50, 40, 76, color=OL, w=5.4); ln(a, 40, 50, 40, 76, color="#22c55e", w=3)
        pg(a, 40, 66, 60, 56, 66, 68, 46, 72, fill="#4ade80")
        for k in range(8):
            t = math.radians(45 * k); cc(a, 40 + 19 * math.cos(t), 32 + 19 * math.sin(t), 9, "#f9a8d4", w=1.6)
        cc(a, 40, 32, 14, "#fde047"); face(a, 40, 32, "dot", "smile", 5.8, 2.3, my=38, cheeks=True)

    @st("ojo", "Ojo", "Eye")
    def _(a):
        a._add([(40 + 34 * math.cos(math.radians(t)), 40 - 26 * math.sin(math.radians(t))) for t in range(0, 181, 10)] + [(40 + 34 * math.cos(math.radians(t)), 40 - 26 * math.sin(math.radians(t))) for t in range(180, 361, 10)], "#f8fafc", 1, True)
        cc(a, 40, 40, 17, "#38bdf8", w=1.5); cc(a, 40, 40, 9, "#0f172a", w=1); a.circle(35, 34, 3.6, color="#ffffff", fill=True); a.circle(45, 45, 1.6, color="#ffffff", fill=True)
        a._add([(40 + 34 * math.cos(math.radians(t)), 40 - 26 * math.sin(math.radians(t))) for t in range(0, 181, 10)] + [(40 + 34 * math.cos(math.radians(t)), 40 - 26 * math.sin(math.radians(t))) for t in range(180, 361, 10)], OL, 2)
        for k, t in enumerate((-60, -30, 0, 30, 60)): a_ = math.radians(-90 + t); ln(a, 40 + 30 * math.cos(a_), 38 + 26 * math.sin(a_), 40 + 38 * math.cos(a_), 38 + 36 * math.sin(a_), w=2)
        blush(a, 40, 58, 20, 2.6); smile(a, 40, 66, 5, 1.7)
