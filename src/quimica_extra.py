import math
from _common import M, W, H, header, lab_report, diamond_sign, badge


def extend(P):
    P.version = 2

    @P.template("lab", "Reporte de laboratorio de química", "Chemistry lab report")
    def _(a): lab_report(a, "Reporte de laboratorio · Química", ["Reactivo", "Fórmula", "Cantidad", "Riesgo"], [("Reacciones", 70)])

    @P.template("stoichiometry", "Hoja de estequiometría", "Stoichiometry sheet")
    def _(a):
        y = header(a, "Estequiometría", ["Tema", "Nombre", "Fecha"])
        a.rect(M, y, W - M, y + 50, w=0.9); a.text(M + 5, y + 4, "Ecuación balanceada", 9)
        y += 60
        a.table(M, y, W - M, y + 160, [2, 1, 1, 1, 1, 1], 6, ["Sustancia", "M (g/mol)", "masa (g)", "moles", "relación", "rendimiento"])
        y += 170
        a.section(M, y, W - M, H - M, "Cálculos", ruled=False); a.grid(M + 6, y + 18, W - M - 6, H - M - 6, 14.17)

    @P.template("organic", "Química orgánica (hexagonal)", "Organic chemistry (hexagonal)")
    def _(a):
        y = header(a, "Química orgánica", ["Tema", "Nombre", "Fecha"])
        r = 14.0; hw = r * math.sqrt(3); row = 0; cy = y + 20
        while cy < H - M:
            cx = M + (hw / 2 if row % 2 else 0) + hw / 2
            while cx < W - M:
                pts = []
                for k in range(6): t = math.pi / 6 + k * math.pi / 3; pts += [cx + r * math.cos(t), cy + r * math.sin(t)]
                a.poly(*pts, color="#e5e7eb", w=0.5); cx += hw
            cy += 1.5 * r; row += 1

    for sid, name, en, glyph, label in (("flammable", "Inflamable", "Flammable", "🔥", "Inflamable"), ("toxic", "Tóxico", "Toxic", "☠", "Tóxico"),
                                         ("warning", "Peligro", "Hazard", "!", "Peligro"), ("corrosive", "Corrosivo", "Corrosive", "⚗", "Corrosivo"),
                                         ("explosive", "Explosivo", "Explosive", "💥", "Explosivo"), ("oxidizer", "Oxidante", "Oxidizer", "◎", "Oxidante"),
                                         ("health", "Riesgo para la salud", "Health hazard", "✱", "Salud"), ("environment", "Peligro ambiental", "Environmental hazard", "🐟", "Ambiente")):
        P.sticker(sid, name, en, 60, 72)(lambda a, g=glyph, l=label: diamond_sign(a, g, l))

    @P.sticker("goggles", "Usa lentes", "Wear goggles", 100, 30)
    def _(a): badge(a, "🥽 Usa lentes", "#2563eb")

    @P.sticker("flask-color", "Matraz", "Flask")
    def _(a):
        a.poly(24, 4, 36, 4, 36, 20, 54, 54, 6, 54, 24, 20, color="#ffffff", w=1, fill=True)
        a.poly(16, 36, 44, 36, 54, 54, 6, 54, color="#22c55e", w=1, fill=True)
        a.poly(24, 4, 36, 4, 36, 20, 54, 54, 6, 54, 24, 20, color="#374151", w=1.6)
        a.circle(26, 44, 2.5, color="#ffffff", fill=True); a.circle(34, 40, 1.8, color="#ffffff", fill=True)

    P.symbols_in("Química", [r"\text{H}_{2}\text{O}", r"\text{CO}_{2}", r"\rightleftharpoons", r"\xrightarrow{\Delta}", r"\uparrow", r"\downarrow",
                             r"\Delta H", r"\Delta G", r"\Delta S", r"[\text{A}]", r"\text{mol}", r"\text{M}", r"\text{pH}", r"K_{a}", r"K_{eq}",
                             r"^{+}", r"^{2+}", r"^{-}", r"^{2-}", r"\text{(s)}", r"\text{(l)}", r"\text{(g)}", r"\text{(ac)}", r"\text{e}^{-}",
                             r"\delta^{+}", r"\delta^{-}", r"\cdot n\text{H}_{2}\text{O}", r"{}^{14}_{6}\text{C}"], "Chemistry")
