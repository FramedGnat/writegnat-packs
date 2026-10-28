import math
from _draw import *


def extend(P):
    def st(sid, name, en): return P.sticker("ch-" + sid, name, en, 80, 80)

    @st("capacitor", "Capacitor", "Capacitor")
    def _(a):
        for x in (32, 48): ln(a, x, 62, x, 77, color="#cbd5e1", w=3); ln(a, x, 62, x, 77, color=OL, w=0.6)
        rr(a, 22, 10, 58, 66, 7, "#38bdf8"); rr(a, 22, 10, 58, 24, 5, "#0c4a6e", w=1.7)
        for k in range(3): a.text(30 + k * 7, 11, "−", 9, "#ffffff")
        ln(a, 30, 16, 50, 16, color="#0ea5e9", w=0.1)
        face(a, 40, 42, "dot", "smile", 7, 2.6, my=48, cheeks=True); shine(a, 28, 34, 1.8, 6)

    @st("protoboard", "Protoboard", "Breadboard")
    def _(a):
        rr(a, 6, 14, 74, 66, 5, "#f1f5f9")
        ln(a, 10, 20, 70, 20, color="#ef4444", w=1.6); ln(a, 10, 24, 70, 24, color="#3b82f6", w=1.6)
        ln(a, 10, 56, 70, 56, color="#3b82f6", w=1.6); ln(a, 10, 60, 70, 60, color="#ef4444", w=1.6)
        rr(a, 8, 38, 72, 42, 1, "#cbd5e1", w=0.8)
        for r_ in (29, 33, 47, 51):
            for c in range(12): a.circle(13 + c * 5, r_, 0.9, color="#475569", fill=True)
        a._add([(23, 33), (23, 28), (43, 28), (43, 33)], OL, 3.4); a._add([(23, 33), (23, 28), (43, 28), (43, 33)], "#facc15", 1.8)
        a._add([(53, 47), (53, 52), (33, 52), (33, 47)], OL, 3.4); a._add([(53, 47), (53, 52), (33, 52), (33, 47)], "#f43f5e", 1.8)
        cc(a, 63, 48, 4.4, "#4ade80", w=1.5); a.circle(61.8, 46.8, 1.2, color="#ffffff", fill=True)
        eyes(a, 28, 40, 0, 0, "dot") if False else None

    @st("osciloscopio", "Osciloscopio", "Oscilloscope")
    def _(a):
        rr(a, 6, 10, 74, 66, 6, "#475569"); rr(a, 12, 16, 50, 58, 4, "#0f172a", w=1.5)
        for k in (1, 2, 3): ln(a, 12 + k * 9.5, 16, 12 + k * 9.5, 58, color="#14532d", w=0.5)
        for k in (1, 2, 3): ln(a, 12, 16 + k * 10.5, 50, 16 + k * 10.5, color="#14532d", w=0.5)
        a._add([(14 + k, 47 - 6 * math.sin(k / 38 * 6 * math.pi)) for k in range(0, 35)], "#4ade80", 1.8)
        eyes(a, 31, 28, 6, 2, "glow", "#4ade80"); arc(a, 31, 31, 4, 25, 155, color="#4ade80", w=1.6)
        for y in (22, 36, 50): cc(a, 62, y, 5, "#e2e8f0", w=1.4); ln(a, 62, y, 62, y - 4, w=1.4)
        for x in (14, 70): rr(a, x - 4, 66, x + 4, 72, 2, "#1e293b", w=1.2)

    @st("multimetro", "Multímetro", "Multimeter")
    def _(a):
        rr(a, 22, 6, 58, 74, 7, "#fbbf24"); rr(a, 27, 11, 53, 29, 3, "#bbf7d0", w=1.4)
        eyes(a, 40, 17, 6, 1.7, "dot"); smile(a, 40, 21, 3.6, 1.5)
        cc(a, 40, 46, 12, "#f8fafc"); ln(a, 40, 46, 47, 38, w=2); cc(a, 40, 46, 2, "#ef4444", w=1)
        for k in range(7): t = math.radians(-150 + k * 50); ln(a, 40 + 9.4 * math.cos(t), 46 + 9.4 * math.sin(t), 40 + 11 * math.cos(t), 46 + 11 * math.sin(t), w=1.1)
        for x, c in ((30, "#475569"), (40, "#ef4444"), (50, "#1e293b")): cc(a, x, 66, 3.2, c, w=1.3)

    @st("interruptor", "Interruptor", "Switch")
    def _(a):
        rr(a, 20, 6, 60, 74, 9, "#f1f5f9"); rr(a, 28, 14, 52, 66, 6, "#cbd5e1", w=1.5)
        rr(a, 28, 14, 52, 40, 6, "#4ade80"); rr(a, 28, 30, 52, 40, 1, "#4ade80", w=0.1)
        a.rect(28, 40, 52, 40.1, color=OL, w=1.5); a.round_rect(28, 14, 52, 66, 6, color=OL, w=1.7)
        face(a, 40, 27, "dot", "smile", 5.4, 2.1, my=32); a.text(36, 46, "ON", 7.5, "#475569")
        for y in (11, 69): screw(a, 40, y, 1.3)

    @st("bobina", "Bobina", "Inductor")
    def _(a):
        ln(a, 4, 40, 14, 40, color=OL, w=3); ln(a, 66, 40, 76, 40, color=OL, w=3)
        rr(a, 12, 28, 68, 52, 9, "#cbd5e1")
        for x in list(range(16, 30, 5)) + list(range(50, 66, 5)):
            ln(a, x, 25, x + 4, 55, color=OL, w=5.6); ln(a, x, 25, x + 4, 55, color="#f97316", w=3.4)
        face(a, 40, 38, "dot", "smile", 5.2, 2.1, my=44, cheeks=False)
        a.text(33, 58, "L", 9, "#475569")

    @st("transistor", "Transistor", "Transistor")
    def _(a):
        for x in (28, 40, 52): ln(a, x, 50, x, 76, color=OL, w=4.4); ln(a, x, 50, x, 76, color="#cbd5e1", w=2.4)
        a.poly(*([18, 52] + [c for t in range(180, 361, 12) for c in (40 + 22 * math.cos(math.radians(t)), 34 + 22 * math.sin(math.radians(t)))] + [62, 52]), color="#475569", fill=True)
        a.poly(*([18, 52] + [c for t in range(180, 361, 12) for c in (40 + 22 * math.cos(math.radians(t)), 34 + 22 * math.sin(math.radians(t)))] + [62, 52]), color=OL, w=1.8)
        eyes(a, 40, 32, 7, 2.2, "glow", "#4ade80"); arc(a, 40, 36, 5, 25, 155, color="#4ade80", w=2)
        a.text(31.5, 41, "NPN", 6, "#cbd5e1"); shine(a, 28, 24, 2, 3)

    @st("enchufe", "Enchufe", "Plug")
    def _(a):
        for x in (32, 48): rr(a, x - 2.5, 3, x + 2.5, 20, 1, "#cbd5e1", w=1.5)
        a._add([(40, 52), (40, 66), (52, 72), (68, 72)], OL, 6); a._add([(40, 52), (40, 66), (52, 72), (68, 72)], "#334155", 3.6)
        rr(a, 22, 18, 58, 54, 9, "#60a5fa"); shine(a, 28, 25, 2, 5)
        face(a, 40, 36, "dot", "smile", 7, 2.6, my=42, cheeks=True); bolt(a, 69, 66, 5)

    @st("antena", "Antena wifi", "Wi-Fi antenna")
    def _(a):
        for r_, c in ((44, "#7dd3fc"), (34, "#38bdf8"), (24, "#0ea5e9")):
            arc(a, 40, 62, r_, 228, 312, color=OL, w=7.6, n=18); arc(a, 40, 62, r_, 228, 312, color=c, w=4.8, n=18)
        cc(a, 40, 62, 14, "#38bdf8"); shine(a, 33, 55, 3, 1.6); face(a, 40, 62, "dot", "smile", 5.2, 2.2, my=67, cheeks=True)

    @st("soldador", "Soldador", "Soldering iron")
    def _(a):
        ln(a, 12, 68, 36, 44, color=OL, w=15); ln(a, 12, 68, 36, 44, color="#ef4444", w=11.6)
        ln(a, 36, 44, 50, 30, color=OL, w=10); ln(a, 36, 44, 50, 30, color="#94a3b8", w=7)
        ln(a, 50, 30, 62, 18, color=OL, w=6); ln(a, 50, 30, 62, 18, color="#e2e8f0", w=3.4)
        cc(a, 63, 17, 3, "#fb923c", w=1.2)
        arc(a, 70, 10, 4, 100, 400, color="#94a3b8", w=1.6, n=10, ry=5)
        face(a, 22, 58, "dot", "smile", 4.6, 2, my=63, cheeks=False)

    @st("onda", "Señal senoidal", "Sine wave")
    def _(a):
        rr(a, 6, 14, 74, 66, 8, "#0f172a")
        ln(a, 12, 40, 68, 40, color="#334155", w=1)
        a._add([(12 + 56 * k / 40, 40 - 14 * math.sin(2 * math.pi * 1.5 * k / 40)) for k in range(41)], "#4ade80", 2.4)
        eyes(a, 40, 24, 8, 2.2, "glow", "#38bdf8"); arc(a, 40, 54, 5, 25, 155, color="#38bdf8", w=1.8)

    @st("adc", "Convertidor A/D", "A/D converter")
    def _(a):
        rr(a, 18, 12, 62, 68, 6, "#1e293b")
        for k in range(4):
            ln(a, 12, 20 + k * 12, 18, 20 + k * 12, color="#d1d5db", w=3); ln(a, 62, 20 + k * 12, 68, 20 + k * 12, color="#d1d5db", w=3)
        a.text(26, 15, "A/D", 10, "#fbbf24"); eyes(a, 40, 40, 7, 2.2, "glow", "#4ade80"); arc(a, 40, 50, 4, 25, 155, color="#4ade80", w=1.6)
        a.text(25, 56, "0101", 8, "#94a3b8"); cc(a, 24, 18, 1.4, "#64748b", w=0.6)

    @st("filtro", "Filtro de frecuencias", "Frequency filter")
    def _(a):
        rr(a, 8, 12, 72, 68, 8, "#f1f5f9"); ln(a, 14, 56, 66, 56, w=1.4); ln(a, 14, 56, 14, 18, w=1.4)
        a._add([(16, 28), (36, 28), (46, 32), (54, 46), (66, 54)], "#6366f1", 2.6)
        face(a, 36, 42, "dot", "smile", 6, 2, my=47, cheeks=False)
        a.text(52, 18, "fc", 8, "#475569")
