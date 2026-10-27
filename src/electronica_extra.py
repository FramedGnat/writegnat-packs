import math
from _common import M, W, H, header, title_block, badge


def extend(P):
    P.version = 2
    # Los componentes se pegan a la rejilla de circuitos y a las terminales (y se unen con la herramienta Cable).
    P.snap = {"Electrónica: pasivos", "Electrónica: fuentes y conexiones", "Electrónica: semiconductores", "Electrónica: digital", "Electrónica: instrumentos y otros"}

    @P.template("circuit", "Hoja de circuitos", "Circuit sheet")
    def _(a):
        y = header(a, "Circuito", ["Proyecto", "Nombre", "Fecha"])
        a.dots(M, y + 4, W - M, H - M - 70, 10.0)
        title_block(a, W - M - 220, H - M - 62, W - M, H - M, ("Circuito", "Diseñó", "Revisión", "Fecha"))

    @P.template("truth-table", "Tabla de verdad y mapa de Karnaugh", "Truth table and Karnaugh map")
    def _(a):
        y = header(a, "Lógica digital", ["Función", "Nombre", "Fecha"])
        a.table(M, y, W / 2 - 10, y + 360, [1, 1, 1, 1, 1.4], 16, ["A", "B", "C", "D", "Y"])
        kx = W / 2 + 20; ky = y + 30; s = 44
        a.text(kx, y + 4, "Mapa de Karnaugh (4 variables)", 9)
        for i in range(5): a.line(kx + 30, ky + 30 + i * s, kx + 30 + 4 * s, ky + 30 + i * s, w=0.8); a.line(kx + 30 + i * s, ky + 30, kx + 30 + i * s, ky + 30 + 4 * s, w=0.8)
        for i, g in enumerate(["00", "01", "11", "10"]):
            a.text(kx + 30 + i * s + 14, ky + 14, g, 8.5); a.text(kx + 6, ky + 30 + i * s + 16, g, 8.5)
        a.text(kx, ky, "CD →  AB ↓", 7.5)
        a.section(M, y + 370, W - M, H - M, "Expresión simplificada y circuito", ruled=False)
        a.dots(M + 8, y + 390, W - M - 8, H - M - 8, 10.0)

    @P.template("lab-measure", "Práctica de mediciones", "Measurement lab")
    def _(a):
        y = header(a, "Práctica de electrónica", ["Práctica", "Nombre", "Fecha"])
        a.rect(M, y, W - M, y + 230, w=0.9); a.text(M + 5, y + 4, "Diagrama del circuito", 9); a.dots(M + 10, y + 20, W - M - 10, y + 222, 10.0)
        y += 240
        a.table(M, y, W - M, y + 230, [1.2, 1, 1, 1, 1], 10, ["Punto", "Teórico", "Medido", "Error %", "Instrumento"])
        a.section(M, y + 240, W - M, H - M, "Conclusiones")

    @P.sticker("resistor-bands", "Resistencia (código de colores)", "Resistor (color code)", 90, 30)
    def _(a):
        a.line(0, 15, 90, 15, color="#9ca3af", w=2.4); a.round_rect(18, 4, 72, 26, 8, color="#e8c99b", fill=True)
        for x, c in ((28, "#a16207"), (38, "#111111"), (48, "#dc2626"), (62, "#ca8a04")): a.rect(x, 4.5, x + 5, 25.5, color=c, w=0.5, fill=True)

    @P.sticker("led-red", "LED rojo", "Red LED", 40, 60)
    def _(a):
        a.round_rect(8, 4, 32, 34, 12, color="#ef4444", fill=True); a.rect(6, 30, 34, 34, color="#b91c1c", fill=True)
        a.line(14, 34, 14, 58, color="#9ca3af", w=2); a.line(26, 34, 26, 52, color="#9ca3af", w=2)
        a.circle(15, 14, 3, color="#fecaca", fill=True)

    @P.sticker("battery-color", "Batería", "Battery", 60, 34)
    def _(a):
        a.round_rect(2, 4, 52, 30, 4, color="#111827", fill=True); a.rect(52, 12, 57, 22, color="#111827", fill=True)
        a.rect(4, 6, 20, 28, color="#f59e0b", fill=True); a.text(28, 9, "+ −", 11, "#ffffff")

    @P.sticker("chip", "Chip", "Chip", 60, 50)
    def _(a):
        a.round_rect(12, 6, 48, 44, 3, color="#1f2937", fill=True)
        for k in range(4): y = 11 + k * 9; a.rect(4, y, 12, y + 4, color="#9ca3af", fill=True); a.rect(48, y, 56, y + 4, color="#9ca3af", fill=True)
        a.circle(18, 12, 2, color="#6b7280", fill=True)

    @P.sticker("high-voltage", "Alto voltaje", "High voltage")
    def _(a):
        a.poly(30, 3, 57, 54, 3, 54, color="#facc15", fill=True); a.poly(30, 3, 57, 54, 3, 54, color="#111111", w=2.5)
        a.poly(32, 16, 22, 36, 30, 36, 26, 48, 38, 30, 30, 30, 34, 16, color="#111111", fill=True)

    @P.sticker("vcc-badge", "Vcc", "Vcc", 60, 26)
    def _(a): badge(a, "Vcc ⚡", "#dc2626")

    @P.sticker("gnd-badge", "GND", "GND", 60, 26)
    def _(a): badge(a, "GND ⏚", "#334155")

    P.symbols_in("Electrónica", [r"\Omega", r"\text{k}\Omega", r"\text{M}\Omega", r"\mu\text{F}", r"\text{nF}", r"\text{pF}", r"\text{mH}", r"j\omega",
                                 r"\angle\theta", r"V_{rms}", r"V_{pp}", r"V_{CC}", r"V_{GS}", r"I_{D}", r"I_{C}", r"Z_{L}", r"X_{C}", r"\tau", r"\text{dB}",
                                 r"\overline{A}", r"A \cdot B", r"A + B", r"A \oplus B", r"\overline{A \cdot B}", r"\sim", r"\parallel"], "Electronics")
