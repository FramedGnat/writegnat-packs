import math
from _common import M, W, H, header, badge


def extend(P):
    P.version = 2

    @P.template("microscope", "Observación al microscopio", "Microscope observation")
    def _(a):
        y = header(a, "Observación al microscopio", ["Práctica", "Nombre", "Fecha"])
        cw = (W - 2 * M) / 2; ch = (H - M - y) / 2
        for i in range(2):
            for j in range(2):
                x0 = M + j * cw; y0 = y + i * ch
                a.circle(x0 + cw / 2, y0 + 100, 88, w=1.0)
                a.fields(x0 + 8, y0 + 212, x0 + cw - 8, ["Muestra", "Aumento"], 8.0)
                a.ruled(x0 + 8, y0 + 218, x0 + cw - 8, y0 + ch - 6, 18)

    @P.template("species", "Ficha de especie", "Species card")
    def _(a):
        y = header(a, "Ficha de especie", ["Nombre común", "Nombre científico"])
        a.rect(M, y, W / 2 - 4, y + 260, w=0.9); a.text(M + 5, y + 4, "Dibujo o foto", 9)
        a.table(W / 2 + 4, y, W - M, y + 260, [1, 1.4], 8, ["Clasificación", ""])
        for k, t in enumerate(["Reino", "Filo", "Clase", "Orden", "Familia", "Género", "Especie", "Hábitat"]):
            a.text(W / 2 + 9, y + 26 + k * 30, t, 8.5)
        a.section(M, y + 270, W - M, H - M, "Características y observaciones")

    @P.template("clinical", "Historia clínica (práctica)", "Clinical history (practice)")
    def _(a):
        y = header(a, "Historia clínica", ["Paciente", "Edad", "Sexo", "Fecha"])
        a.table(M, y, W - M, y + 50, [1] * 6, 1, ["T/A", "FC", "FR", "Temp", "SatO₂", "Peso"])
        y += 58
        for name, hgt in (("Motivo de consulta", 70), ("Padecimiento actual", 130), ("Antecedentes", 100), ("Exploración física", 130), ("Diagnóstico", 60)):
            a.section(M, y, W - M, y + hgt, name); y += hgt + 6
        a.section(M, y, W - M, H - M, "Plan / tratamiento")

    @P.sticker("cell-color", "Célula", "Cell")
    def _(a):
        a.circle(30, 30, 26, color="#fde68a", fill=True); a.circle(30, 30, 26, color="#b45309", w=1.6)
        a.circle(34, 26, 9, color="#a78bfa", fill=True); a.circle(34, 26, 3, color="#5b21b6", fill=True)
        a.circle(18, 40, 4, color="#fb7185", fill=True, ry=2.5); a.circle(40, 44, 4, color="#fb7185", fill=True, ry=2.5)

    @P.sticker("dna-color", "ADN", "DNA")
    def _(a):
        p1, p2 = [], []
        for i in range(41):
            y = 2 + i * 1.4; x = 30 + 16 * math.sin(i / 40 * 4 * math.pi)
            p1 += [x, y]; p2 += [60 - x, y]
            if i % 4 == 2: a.line(x, y, 60 - x, y, color=["#f472b6", "#60a5fa", "#34d399", "#fbbf24"][(i // 4) % 4], w=2.2)
        a.line(*p1, color="#7c3aed", w=2.6); a.line(*p2, color="#2563eb", w=2.6)

    @P.sticker("leaf-color", "Hoja", "Leaf")
    def _(a):
        pts = []
        for i in range(31): t = i / 30; pts += [6 + 48 * t, 30 - 20 * math.sin(math.pi * t) ** 0.8]
        for i in range(31): t = 1 - i / 30; pts += [6 + 48 * t, 30 + 20 * math.sin(math.pi * t) ** 0.8]
        a.poly(*pts, color="#22c55e", fill=True); a.line(2, 30, 54, 30, color="#15803d", w=1.4)

    @P.sticker("heart-red", "Corazón", "Heart")
    def _(a):
        pts = []
        for i in range(61):
            t = 2 * math.pi * i / 60
            pts += [30 + 1.7 * 16 * math.sin(t) ** 3, 28 - 1.7 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))]
        a.poly(*pts, color="#ef4444", fill=True)

    @P.sticker("microbe", "Microbio", "Microbe")
    def _(a):
        a.circle(30, 30, 18, color="#86efac", fill=True); a.circle(30, 30, 18, color="#15803d", w=1.4)
        for k in range(10): t = 2 * math.pi * k / 10; a.line(30 + 18 * math.cos(t), 30 + 18 * math.sin(t), 30 + 26 * math.cos(t), 30 + 26 * math.sin(t), color="#15803d", w=1.6)
        a.circle(24, 26, 3, color="#15803d", fill=True); a.circle(36, 34, 2, color="#15803d", fill=True)

    @P.sticker("rx", "Receta", "Prescription", 70, 30)
    def _(a): badge(a, "℞ Receta", "#0891b2")

    P.symbols_in("Biología y salud", [r"\text{ATP}", r"\text{ADN}", r"\text{ARN}", r"\text{O}_{2}", r"\text{CO}_{2}", r"\text{mg/kg}", r"\text{mmHg}",
                                      r"\mu\text{m}", r"\text{Na}^{+}", r"\text{K}^{+}", r"\text{Ca}^{2+}", r"\text{Cl}^{-}", r"\text{mEq/L}", r"\text{UI}",
                                      r"\leftrightarrow", r"\rightarrow", r"\%", r"\times 10^{n}", r"\bar{x} \pm s", r"\text{♂}", r"\text{♀}"], "Biology and health")
