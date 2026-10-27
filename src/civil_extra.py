import math
from _common import M, W, H, header, title_block, badge


def extend(P):
    P.version = 2

    @P.template("calc-sheet", "Hoja de cálculo estructural", "Structural calculation sheet")
    def _(a):
        y = header(a, "Memoria de cálculo", ["Proyecto", "Elemento", "Calculó"])
        a.grid(M, y, W - M, H - M - 70, 14.17, color="#e5e7eb", w=0.3)
        a.line(M + 140, y, M + 140, H - M - 70, w=0.8); a.line(W - M - 110, y, W - M - 110, H - M - 70, w=0.8)
        a.text(M + 4, y + 3, "Datos / referencia", 8); a.text(M + 144, y + 3, "Cálculo", 8); a.text(W - M - 106, y + 3, "Resultado", 8)
        title_block(a, W - M - 240, H - M - 62, W - M, H - M, ("Obra", "Revisó", "Hoja", "Fecha"))

    @P.template("survey", "Libreta de topografía", "Survey field book")
    def _(a):
        y = header(a, "Levantamiento topográfico", ["Obra", "Brigada", "Fecha"])
        a.table(M, y, W - M, H - M - 160, [0.8, 0.8, 1, 1, 1, 1, 1], 24, ["Est.", "P.V.", "Distancia", "Ángulo", "Rumbo", "Cota", "Notas"])
        a.rect(M, H - M - 150, W - M, H - M, w=0.9); a.text(M + 5, H - M - 146, "Croquis", 9); a.grid(M + 6, H - M - 132, W - M - 6, H - M - 6, 14.17)

    @P.template("plan-sheet", "Lámina de planos (horizontal)", "Drawing sheet (landscape)", 842.0, 595.0)
    def _(a):
        a.rect(20, 20, 822, 575, w=1.6); a.rect(28, 28, 814, 567, w=0.6)
        title_block(a, 600, 485, 814, 567)

    @P.sticker("hard-hat", "Casco", "Hard hat", 64, 44)
    def _(a):
        pts = []
        for k in range(21): t = math.pi * k / 20; pts += [32 - 24 * math.cos(t), 32 - 26 * math.sin(t)]
        a.poly(*pts, color="#facc15", fill=True); a.round_rect(2, 30, 62, 38, 3, color="#eab308", fill=True)
        a.line(32, 8, 32, 30, color="#ca8a04", w=3)

    @P.sticker("cone", "Cono de tránsito", "Traffic cone", 50, 60)
    def _(a):
        a.poly(20, 4, 30, 4, 42, 50, 8, 50, color="#f97316", fill=True)
        a.poly(15.5, 22, 34.5, 22, 37, 32, 13, 32, color="#ffffff", fill=True); a.rect(2, 50, 48, 56, color="#ea580c", fill=True)

    @P.sticker("bridge", "Puente", "Bridge", 80, 44)
    def _(a):
        pts = []
        for k in range(31): t = k / 30; pts += [6 + 68 * t, 30 - 22 * math.sin(math.pi * t)]
        a.line(*pts, color="#dc2626", w=3); a.line(2, 30, 78, 30, color="#374151", w=4)
        for k in range(1, 8): x = 6 + 68 * k / 8; a.line(x, 30, x, 30 - 22 * math.sin(math.pi * k / 8), color="#dc2626", w=1.2)
        a.line(2, 40, 78, 40, color="#38bdf8", w=3)

    @P.sticker("check-structure", "Revisar", "Check", 76, 26)
    def _(a): badge(a, "⚠ Revisar", "#ca8a04")

    @P.sticker("ok-structure", "Cumple", "OK", 76, 26)
    def _(a): badge(a, "✓ Cumple", "#16a34a")

    @P.sticker("brick", "Muro", "Wall", 60, 40)
    def _(a):
        for r in range(4):
            off = 0 if r % 2 == 0 else -10
            for c in range(4): x = off + c * 20; a.rect(max(0, x), r * 10, min(60, x + 19), r * 10 + 9, color="#b45309", fill=True)

    P.symbols_in("Ingeniería civil", [r"\sigma", r"\tau", r"\varepsilon", r"f'_{c}", r"f_{y}", r"E I", r"\delta", r"M_{max}", r"V_{max}", r"\text{kN}",
                                      r"\text{kN}\cdot\text{m}", r"\text{MPa}", r"\text{kg/cm}^{2}", r"\gamma", r"\phi", r"\text{kg/m}^{3}", r"\text{m}^{3}\text{/s}",
                                      r"R_{h}", r"\sum F_{x} = 0", r"\sum M = 0", r"\phi M_{n}", r"A_{s}", r"\rho"], "Civil engineering")
