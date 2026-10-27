import math
from _common import M, W, H, header, badge, gear


def extend(P):
    P.version = 2

    @P.template("dh-table", "Tabla de Denavit-Hartenberg", "Denavit–Hartenberg table")
    def _(a):
        y = header(a, "Cinemática del manipulador", ["Robot", "Nombre", "Fecha"])
        a.table(M, y, W - M, y + 200, [0.6, 1, 1, 1, 1, 1.4], 7, ["i", "θᵢ", "dᵢ", "aᵢ", "αᵢ", "Tipo (R/P)"])
        y += 210
        a.rect(M, y, W / 2 - 4, y + 280, w=0.9); a.text(M + 5, y + 4, "Esquema y marcos", 9); a.grid(M + 6, y + 18, W / 2 - 10, y + 274, 14.17)
        a.section(W / 2 + 4, y, W - M, y + 280, "Matrices ⁱ⁻¹Tᵢ", ruled=False); a.ruled(W / 2 + 10, y + 14, W - M - 6, y + 280, 26)
        a.section(M, y + 290, W - M, H - M, "Cinemática directa / inversa")

    @P.template("logbook", "Bitácora de proyecto", "Project logbook")
    def _(a):
        y = header(a, "Bitácora de proyecto", ["Proyecto", "Equipo", "Semana"])
        for name, hgt in (("Objetivo de la sesión", 70), ("Avances", 200), ("Problemas y soluciones", 150), ("Pruebas y mediciones", 120)):
            a.section(M, y, W - M, y + hgt, name); y += hgt + 6
        a.table(M, y, W - M, H - M, [3, 1, 1], 4, ["Pendiente", "Responsable", "Fecha"])

    @P.template("control", "Diagrama de bloques de control", "Control block diagram")
    def _(a):
        y = header(a, "Sistema de control", ["Sistema", "Nombre", "Fecha"])
        cy = y + 80
        a.circle(M + 60, cy, 12, w=1); a.text(M + 54, cy - 30, "+", 9); a.text(M + 40, cy + 14, "−", 9)
        for x0, x1, t in ((M + 100, M + 200, "C(s)"), (M + 240, M + 360, "G(s)")):
            a.rect(x0, cy - 22, x1, cy + 22, w=1); a.text(x0 + 30, cy - 6, t, 11)
        a.line(M, cy, M + 48, cy, w=1); a.line(M + 72, cy, M + 100, cy, w=1); a.line(M + 200, cy, M + 240, cy, w=1); a.line(M + 360, cy, W - M, cy, w=1)
        a.rect(M + 240, cy + 50, M + 360, cy + 90, w=1); a.text(M + 280, cy + 62, "H(s)", 11)
        a.line(M + 420, cy, M + 420, cy + 70, M + 360, cy + 70, w=1); a.line(M + 240, cy + 70, M + 60, cy + 70, M + 60, cy + 12, w=1)
        a.text(M, cy - 18, "R(s)", 9); a.text(W - M - 30, cy - 18, "Y(s)", 9)
        y = cy + 110
        a.section(M, y, W - M, y + 200, "Análisis (polos, ceros, estabilidad)")
        a.rect(M, y + 210, W - M, H - M, w=0.9); a.text(M + 5, y + 214, "Respuesta / Bode", 9); a.grid(M + 6, y + 228, W - M - 6, H - M - 6, 14.17)

    @P.sticker("robot-face", "Robot", "Robot")
    def _(a):
        a.line(30, 4, 30, 12, color="#6b7280", w=2); a.circle(30, 4, 3, color="#ef4444", fill=True)
        a.round_rect(8, 12, 52, 50, 8, color="#94a3b8", fill=True); a.round_rect(8, 12, 52, 50, 8, color="#334155", w=1.6)
        a.circle(21, 28, 5, color="#38bdf8", fill=True); a.circle(39, 28, 5, color="#38bdf8", fill=True)
        a.round_rect(18, 38, 42, 44, 2, color="#334155", fill=True)

    @P.sticker("gear-grey", "Engrane", "Gear")
    def _(a): gear(a, 30, 30, 26, "#64748b", 12)

    @P.sticker("gears-pair", "Engranes", "Gears", 70, 60)
    def _(a): gear(a, 24, 34, 20, "#f59e0b", 10); gear(a, 52, 18, 14, "#0ea5e9", 8)

    @P.sticker("arm-color", "Brazo robótico", "Robot arm")
    def _(a):
        a.rect(10, 50, 34, 56, color="#475569", fill=True); a.line(22, 50, 22, 36, color="#f97316", w=6); a.circle(22, 34, 5, color="#334155", fill=True)
        a.line(22, 34, 44, 18, color="#f97316", w=6); a.circle(44, 18, 4.5, color="#334155", fill=True)
        a.line(44, 18, 54, 30, color="#f97316", w=5); a.line(50, 34, 58, 30, color="#334155", w=2); a.line(54, 38, 58, 34, color="#334155", w=2)

    @P.sticker("sensor-badge", "Sensor", "Sensor", 70, 26)
    def _(a): badge(a, "📡 Sensor", "#0891b2")

    @P.sticker("motor-badge", "Actuador", "Actuator", 80, 26)
    def _(a): badge(a, "⚙ Actuador", "#dc2626")

    P.symbols_in("Robótica", [r"\dot{q}", r"\ddot{q}", r"{}^{i}T_{j}", r"{}^{0}R_{1}", r"\theta_{i}", r"d_{i}", r"a_{i}", r"\alpha_{i}", r"J(q)", r"J^{T}",
                              r"J^{\dagger}", r"\tau", r"\omega \times r", r"\hat{z}", r"s_{12}", r"c_{12}", r"\operatorname{atan2}", r"K_{p}", r"K_{i}",
                              r"K_{d}", r"e(t)", r"u(t)", r"\mathcal{L}", r"G(s)", r"\zeta", r"\omega_{n}"], "Robotics")
