import math
from _common import M, W, H, header, badge


def extend(P):
    P.version = 2

    @P.template("observation", "Registro de observación", "Observation record")
    def _(a):
        y = header(a, "Registro de observación", ["Sujeto / grupo", "Observador", "Fecha"])
        a.fields(M, y + 8, W - M, ["Contexto", "Conducta meta"]); y += 22
        a.table(M, y, W - M, H - M - 140, [0.8, 2.4, 0.8, 2], 18, ["Hora", "Conducta observada", "Frecuencia", "Antecedente / consecuente"])
        a.section(M, H - M - 130, W - M, H - M, "Interpretación")

    @P.template("stats-table", "Tabla de frecuencias", "Frequency table")
    def _(a):
        y = header(a, "Distribución de frecuencias", ["Variable", "n", "Fecha"])
        a.table(M, y, W - M, y + 340, [1.4, 1, 1, 1, 1, 1], 14, ["Clase / xᵢ", "fᵢ", "frᵢ", "Fᵢ", "%", "xᵢ·fᵢ"])
        y += 350
        for i, t in enumerate(["Media", "Mediana", "Moda", "Desv. estándar"]):
            x0 = M + i * (W - 2 * M) / 4; a.rect(x0 + 2, y, x0 + (W - 2 * M) / 4 - 2, y + 50, w=0.8); a.text(x0 + 7, y + 4, t, 8.5)
        a.rect(M, y + 60, W - M, H - M, w=0.9); a.text(M + 5, y + 64, "Histograma", 9); a.grid(M + 6, y + 78, W - M - 6, H - M - 6, 14.17)

    @P.template("reading", "Ficha de lectura", "Reading card")
    def _(a):
        y = header(a, "Ficha de lectura", ["Autor(es)", "Año", "Título"])
        for name, hgt in (("Referencia (APA)", 60), ("Idea principal", 120), ("Conceptos clave", 120), ("Citas textuales (pág.)", 170), ("Reflexión personal", 0)):
            if hgt == 0: a.section(M, y, W - M, H - M, name); break
            a.section(M, y, W - M, y + hgt, name); y += hgt + 6

    @P.sticker("brain-pink", "Cerebro", "Brain")
    def _(a):
        a.circle(30, 30, 24, color="#f9a8d4", fill=True, ry=20)
        for k in range(5): a.line(14 + k * 8, 14, 18 + k * 8, 26, 12 + k * 8, 38, color="#db2777", w=1.4)
        a.line(30, 10, 30, 50, color="#db2777", w=1.6)

    @P.sticker("speech", "Diálogo", "Speech bubble", 64, 50)
    def _(a): a.round_rect(2, 2, 62, 36, 10, color="#e0f2fe", fill=True); a.poly(14, 34, 24, 34, 10, 48, color="#e0f2fe", fill=True); a.round_rect(2, 2, 62, 36, 10, color="#0284c7", w=1.4); a.text(14, 10, "···", 14, "#0284c7")

    @P.sticker("thought", "Pensamiento", "Thought", 64, 52)
    def _(a):
        for cx, cy, r in ((22, 20, 14), (38, 16, 14), (48, 26, 11), (30, 28, 14)): a.circle(cx, cy, r, color="#ede9fe", fill=True)
        a.circle(14, 42, 4, color="#ede9fe", fill=True); a.circle(8, 48, 2.5, color="#ede9fe", fill=True)

    @P.sticker("people", "Grupo", "Group", 70, 50)
    def _(a):
        for cx, c in ((18, "#60a5fa"), (52, "#f472b6"), (35, "#34d399")):
            a.circle(cx, 16, 8, color=c, fill=True); a.round_rect(cx - 12, 26, cx + 12, 48, 10, color=c, fill=True)

    @P.sticker("hypothesis", "Hipótesis", "Hypothesis", 86, 26)
    def _(a): badge(a, "H₀ Hipótesis", "#2563eb")

    @P.sticker("significant", "Significativo", "Significant", 96, 26)
    def _(a): badge(a, "p < 0.05 ✓", "#16a34a")

    P.symbols_in("Estadística (sociales)", [r"\bar{x}", r"s", r"s^{2}", r"\sigma", r"\mu", r"n", r"N", r"H_{0}", r"H_{1}", r"\alpha", r"\beta", r"p < 0.05",
                                            r"r", r"R^{2}", r"\chi^{2}", r"t", r"F", r"z", r"d", r"\eta^{2}", r"gl", r"\pm", r"M \pm DE"], "Statistics (social sciences)")
