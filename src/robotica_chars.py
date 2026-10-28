import math
from _draw import *


def extend(P):
    def st(sid, name, en):
        return P.sticker("ch-" + sid, name, en, 80, 80)

    @st("servo", "Servomotor", "Servo motor")
    def _(a):
        rr(a, 10, 26, 58, 62, 4, "#3b82f6"); rr(a, 6, 34, 14, 54, 2, "#2563eb", w=1.4); rr(a, 54, 34, 62, 54, 2, "#2563eb", w=1.4)
        cc(a, 11, 38, 1.6, "#cbd5e1", w=0.8); cc(a, 11, 50, 1.6, "#cbd5e1", w=0.8); cc(a, 57, 38, 1.6, "#cbd5e1", w=0.8); cc(a, 57, 50, 1.6, "#cbd5e1", w=0.8)
        rr(a, 58, 38, 66, 50, 2, "#1e3a8a", w=1.4); cc(a, 70, 44, 7.5, "#e2e8f0"); cc(a, 70, 44, 2.6, "#64748b", w=1.2)
        for k in range(8):
            r = math.radians(45 * k); ln(a, 70 + 5 * math.cos(r), 44 + 5 * math.sin(r), 70 + 7.5 * math.cos(r), 44 + 7.5 * math.sin(r), w=1.2)
        for x, c in ((22, "#ef4444"), (28, "#fbbf24"), (34, "#475569")): ln(a, x, 62, x, 72, color=c, w=2.6)
        shine(a, 20, 31, 5, 1.6); face(a, 34, 45, "dot", "smile", 8, 2.6, my=52, cheeks=True)

    @st("ultrasonico", "Sensor ultrasónico", "Ultrasonic sensor")
    def _(a):
        rr(a, 6, 38, 74, 70, 4, "#0ea5e9")
        for x in (24, 56):
            cc(a, x, 54, 13, "#cbd5e1"); cc(a, x, 54, 9, "#475569", w=1.2); cc(a, x, 54, 3.5, "#1e293b", w=1)
        face(a, 40, 51, "dot", "smile", 3.4, 1.6, my=57)
        for k in range(4): ln(a, 24 + k * 10.7, 70, 24 + k * 10.7, 77, color="#fbbf24", w=2.6)
        for r_ in (8, 15, 22): arc(a, 40, 34, r_, 215, 325, color="#7dd3fc", w=1.8, n=10)

    @st("omni", "Rueda omnidireccional", "Omni wheel")
    def _(a):
        cc(a, 40, 40, 33, "#475569"); cc(a, 40, 40, 23, "#e2e8f0", w=1.6)
        for k in range(8):
            r = math.radians(45 * k + 22); cc(a, 40 + 28 * math.cos(r), 40 + 28 * math.sin(r), 5.2, "#f97316", ry=3.4, w=1.4)
        for k in range(6):
            r = math.radians(60 * k); ln(a, 40, 40, 40 + 22 * math.cos(r), 40 + 22 * math.sin(r), color="#94a3b8", w=2)
        cc(a, 40, 40, 11, "#cbd5e1"); face(a, 40, 40, "dot", "smile", 4.2, 1.8, my=45)

    @st("pinza", "Pinza robótica", "Robot gripper")
    def _(a):
        rr(a, 24, 6, 56, 26, 4, "#94a3b8"); rr(a, 30, 24, 50, 34, 2, "#64748b", w=1.4)
        for s in (-1, 1):
            pg(a, 40 + s * 8, 34, 40 + s * 22, 34, 40 + s * 26, 54, 40 + s * 14, 74, 40 + s * 10, 70, 40 + s * 17, 54, fill="#fb923c")
            ln(a, 40 + s * 15, 56, 40 + s * 11, 70, color="#334155", w=2)
        face(a, 40, 15, "dot", "smile", 8, 2.6, my=21, cheeks=True)
        cc(a, 40, 54, 7, "#fde047", w=1.6); star(a, 40, 54, 3.4, "#f59e0b")

    @st("camara", "Cámara de visión", "Vision camera")
    def _(a):
        rr(a, 10, 20, 70, 62, 7, "#334155"); rr(a, 14, 24, 66, 58, 5, "#475569", w=1.2)
        cc(a, 40, 41, 19, "#cbd5e1"); cc(a, 40, 41, 14, "#0f172a", w=1.6); cc(a, 40, 41, 8, "#1d4ed8", w=1.2); cc(a, 40, 41, 3.4, "#38bdf8", w=0.8)
        a.circle(36, 37, 2.2, color=WH, fill=True); rr(a, 52, 12, 64, 20, 2, "#334155", w=1.4); cc(a, 16, 28, 2, "#ef4444", w=1.0)
        ln(a, 28, 66, 28, 72, w=2); ln(a, 52, 66, 52, 72, w=2)

    @st("lipo", "Batería LiPo", "LiPo battery")
    def _(a):
        rr(a, 8, 20, 66, 62, 5, "#fbbf24"); rr(a, 66, 32, 74, 50, 2, "#cbd5e1", w=1.6)
        rr(a, 8, 20, 22, 62, 4, "#f59e0b", w=1.6); bolt(a, 15, 41, 7, "#fff7ed")
        face(a, 42, 38, "dot", "smile", 8.5, 2.7, my=45, cheeks=True)
        for k, c in enumerate(("#22c55e", "#22c55e", "#22c55e", "#e2e8f0")): rr(a, 28 + k * 9, 52, 35 + k * 9, 58, 1, c, w=1.1)
        for x, c in ((20, "#ef4444"), (28, "#1e293b")): ln(a, x, 62, x, 72, color=c, w=3)

    @st("brazo3", "Brazo de 3 GDL", "3-DOF arm")
    def _(a):
        rr(a, 12, 66, 48, 75, 2, "#475569"); rr(a, 22, 56, 38, 67, 2, "#38bdf8")
        cc(a, 30, 54, 7.5, "#7dd3fc"); ln(a, 30, 54, 22, 32, color=OL, w=9.6); ln(a, 30, 54, 22, 32, color="#38bdf8", w=7)
        cc(a, 22, 30, 6.5, "#7dd3fc"); ln(a, 22, 30, 52, 22, color=OL, w=8.2); ln(a, 22, 30, 52, 22, color="#38bdf8", w=5.6)
        cc(a, 54, 22, 7.5, "#fef3c7", w=1.8); face(a, 54, 21.5, "dot", "smile", 3, 1.4, my=24.5)
        ln(a, 54, 29, 62, 40, color=OL, w=6); ln(a, 54, 29, 62, 40, color="#94a3b8", w=3.6); ln(a, 62, 40, 58, 47, w=2.2); ln(a, 62, 40, 67, 46, w=2.2)
        for x, y in ((30, 54), (22, 30)): screw(a, x, y, 1.3)
        a.text(12, 4, "q1  q2  q3", 6.5, "#475569")

    @st("mano", "Mano robótica", "Robot hand")
    def _(a):
        for k, (x, h) in enumerate(((22, 28), (32, 20), (42, 18), (52, 22))):
            rr(a, x - 4.2, 40 - h, x + 4.2, 46, 4.2, "#e2e8f0"); ln(a, x - 4, 40 - h * 0.45, x + 4, 40 - h * 0.45, color="#94a3b8", w=1.2)
        pg(a, 58, 52, 70, 36, 76, 42, 66, 58, fill="#e2e8f0", w=1.6)
        rr(a, 16, 42, 62, 66, 7, "#cbd5e1"); face(a, 38, 52, "dot", "smile", 8, 2.6, my=58, cheeks=True)
        rr(a, 24, 66, 54, 76, 3, "#f97316"); ln(a, 30, 66, 30, 76, w=1.2); ln(a, 48, 66, 48, 76, w=1.2)

    @st("lidar", "Sensor LIDAR", "LIDAR sensor")
    def _(a):
        rr(a, 22, 52, 58, 68, 4, "#334155"); cc(a, 40, 40, 18, "#e2e8f0", ry=16); rr(a, 24, 30, 56, 52, 5, "#e2e8f0")
        rr(a, 24, 26, 56, 40, 5, "#f87171"); rr(a, 28, 31, 52, 37, 3, "#7f1d1d", w=1.2)
        eyes(a, 40, 46, 7, 2.3, "dot"); smile(a, 40, 47, 3.4, 1.5)
        for k, r_ in enumerate((14, 22, 30)): arc(a, 40, 34, r_, 205, 335, color="#f87171", w=1.8, n=12)

    @st("placa", "Microcontrolador", "Microcontroller board")
    def _(a):
        rr(a, 8, 14, 72, 66, 5, "#0d9488"); rr(a, 12, 18, 68, 62, 3, "#0f766e", w=0.9)
        rr(a, 6, 24, 20, 38, 2, "#cbd5e1", w=1.5); rr(a, 6, 44, 18, 58, 2, "#1e293b", w=1.4)
        rr(a, 30, 28, 52, 52, 3, "#1e293b")
        eyes(a, 41, 38, 5, 1.8, "glow", "#4ade80"); arc(a, 41, 44, 4, 25, 155, color="#4ade80", w=1.6)
        for k in range(8): rr(a, 22 + k * 5.6, 8, 25.6 + k * 5.6, 14, 0.6, "#fbbf24", w=0.8)
        for k in range(8): rr(a, 22 + k * 5.6, 66, 25.6 + k * 5.6, 72, 0.6, "#fbbf24", w=0.8)
        cc(a, 60, 24, 2, "#4ade80", w=0.8); cc(a, 60, 32, 2, "#fbbf24", w=0.8)
