"""Figuras de las materias de Civil: estática y resistencia de materiales, topografía, hidráulica y mecánica de suelos."""
import math

CES, CTP, CHG = "Civil: estática y resistencia", "Civil: topografía", "Civil: hidráulica y geotecnia"


def pin(g, x, y, s=0.07):
    g.poly(x, y, x - s, y - 1.6 * s, x + s, y - 1.6 * s); g.hatch(x - 1.6 * s, x + 1.6 * s, y - 1.6 * s, 5, 0.04)


def roller(g, x, y, s=0.07):
    g.poly(x, y, x - s, y - 1.4 * s, x + s, y - 1.4 * s); g.circle(x - s * 0.5, y - 1.4 * s - 0.02, 0.02); g.circle(x + s * 0.5, y - 1.4 * s - 0.02, 0.02)
    g.line(x - 1.6 * s, y - 1.4 * s - 0.04, x + 1.6 * s, y - 1.4 * s - 0.04)


def axes(g, w=1.0, h=0.7):
    g.arrow(0, 0, w + 0.05, 0, 0.03); g.arrow(0, 0, 0, h + 0.05, 0.03)


def extend(P):
    P.en.update({CES: "Civil: statics and strength of materials", CTP: "Civil: surveying", CHG: "Civil: hydraulics and geotechnics"})

    # --- Estática y resistencia de materiales -----------------------------------------------------
    @P.figure(CES, "x-fbd-beam", "Viga con cargas y reacciones", "Beam with loads and reactions")
    def _(g):
        g.line(0, 0, 1, 0); pin(g, 0.0, 0.0); roller(g, 1.0, 0.0)
        g.arrow(0.4, 0.3, 0.4, 0.02, 0.04); g.label(0.4, 0.36, "P", 0.5)
        g.line(0.6, 0.15, 0.9, 0.15)
        for k in range(7): x = 0.6 + k * 0.05; g.arrow(x, 0.15, x, 0.02, 0.025)
        g.label(0.75, 0.22, "w", 0.5)
        g.arrow(0.0, -0.45, 0.0, -0.2, 0.04); g.label(0.0, -0.52, "R_A", 0.4); g.arrow(1.0, -0.45, 1.0, -0.2, 0.04); g.label(1.0, -0.52, "R_B", 0.4)

    @P.figure(CES, "x-vm-diagram", "Diagramas de cortante y momento", "Shear and moment diagrams")
    def _(g):
        g.line(0, 0.5, 1, 0.5); g.arrow(0.5, 0.75, 0.5, 0.52, 0.04); g.label(0.5, 0.8, "P", 0.45)
        g.line(0, 0.18, 1, 0.18); g.line(0, 0.18, 0, 0.36, 0.5, 0.36, 0.5, 0.0, 1, 0.0, 1, 0.18); g.label(-0.08, 0.36, "V", 0.4)
        g.line(0, -0.15, 1, -0.15); g.line(0, -0.15, 0.5, -0.45, 1, -0.15); g.label(-0.08, -0.45, "M", 0.4); g.label(0.5, -0.52, "Pl/4", 0.4)

    @P.figure(CES, "x-bending-stress", "Esfuerzo por flexión", "Bending stress")
    def _(g):
        g.rect(0, -0.3, 0.3, 0.3); g.line(0, 0, 0.3, 0, dashed=True); g.label(0.15, 0.04, "E.N.", 0.3)
        g.arrow(0.45, 0.3, 0.45, -0.3, 0.0) if False else g.line(0.45, 0.3, 0.45, -0.3)
        g.poly(0.45, 0, 0.75, 0.3, 0.45, 0.3, fill=False); g.poly(0.45, 0, 0.15 + 0.3, -0.3, 0.75 - 0.3 + 0.0, -0.3) if False else g.poly(0.45, 0, 0.15, -0.3, 0.45, -0.3)
        g.label(0.85, 0.3, "σ máx (C)", 0.35); g.label(0.0, -0.38, "σ máx (T)", 0.35); g.label(0.15, 0.42, "σ = M y / I", 0.4)

    @P.figure(CES, "x-stress-strain", "Curva esfuerzo-deformación", "Stress-strain curve")
    def _(g):
        axes(g, 1.0, 0.8)
        g.line(0, 0, 0.25, 0.5); g.spline([(0.25, 0.5), (0.32, 0.56), (0.45, 0.55), (0.6, 0.6), (0.8, 0.72), (0.9, 0.65), (0.95, 0.5)])
        g.line(0.25, 0.5, 0.25, 0.0, dashed=True)
        g.label(0.27, 0.62, "fluencia", 0.35); g.label(0.8, 0.8, "σ_u", 0.4); g.label(1.0, -0.08, "ε", 0.45); g.label(-0.07, 0.8, "σ", 0.45); g.label(0.07, 0.35, "E", 0.4)

    @P.figure(CES, "x-deflection", "Viga deformada (elástica)", "Deflected beam")
    def _(g):
        g.line(0, 0, 1, 0); g.curve(lambda x: -0.25 * math.sin(math.pi * x), 0, 1, dashed=True); pin(g, 0, 0); roller(g, 1, 0)
        g.arrow(0.5, 0.3, 0.5, 0.02, 0.04); g.double_arrow(0.5, -0.02, 0.5, -0.23, 0.03); g.label(0.58, -0.12, "δ", 0.5)

    @P.figure(CES, "x-buckling", "Pandeo de columna (Euler)", "Euler buckling")
    def _(g):
        g.line(0.5, 0.5, 0.5, -0.5); g.curve(lambda y: 0.5 + 0.09 * math.sin(math.pi * (y + 0.5)), -0.5, 0.5, dashed=True) if False else None
        g._add([(0.5 + 0.1 * math.sin(math.pi * (t / 40)), 0.5 - t / 40) for t in range(41)], dashed=True)
        g.arrow(0.5, 0.8, 0.5, 0.52, 0.04); g.label(0.5, 0.86, "P", 0.45); pin(g, 0.5, -0.5); g.label(1.15, 0.0, "P_cr = π²EI / L²", 0.4); g.double_arrow(0.25, -0.5, 0.25, 0.5, 0.03); g.label(0.17, 0.0, "L", 0.45)

    @P.figure(CES, "x-torsion", "Torsión en un eje", "Torsion of a shaft")
    def _(g):
        g.line(0, 0.15, 0.9, 0.15); g.line(0, -0.15, 0.9, -0.15); g.ellipse(0, 0, 0.05, 0.15); g.ellipse(0.9, 0, 0.05, 0.15)
        g.arc(1.0, 0, 0.22, 0.22, -60, 60); g.head(1.0 + 0.22 * math.cos(math.radians(55)), 0.22 * math.sin(math.radians(55)), 1.0 + 0.22 * math.cos(math.radians(60)), 0.22 * math.sin(math.radians(60)), 0.06)
        g.label(1.3, 0.0, "T", 0.5); hatch_wall(g)
        g.label(0.45, -0.28, "τ = T r / J", 0.4)

    @P.figure(CES, "x-cont-beam", "Viga continua", "Continuous beam")
    def _(g):
        g.line(0, 0, 1.2, 0); pin(g, 0, 0); roller(g, 0.6, 0); roller(g, 1.2, 0)
        for x0, x1 in ((0.05, 0.55), (0.65, 1.15)):
            n = 6
            for k in range(n + 1): x = x0 + (x1 - x0) * k / n; g.arrow(x, 0.18, x, 0.02, 0.025)
            g.line(x0, 0.18, x1, 0.18)

    @P.figure(CES, "x-truss-forces", "Armadura con fuerzas nodales", "Truss with nodal forces")
    def _(g):
        g.line(0, 0, 0.5, 0.4, 1, 0, 0, 0); g.line(0.5, 0.4, 0.5, 0)
        pin(g, 0, 0); roller(g, 1, 0)
        g.arrow(0.5, 0.75, 0.5, 0.42, 0.04); g.label(0.5, 0.8, "P", 0.45)
        g.label(-0.05, 0.1, "A", 0.45); g.label(0.5, 0.48, "C", 0.0) if False else None; g.label(1.05, 0.1, "B", 0.45); g.label(0.26, 0.28, "F_AC", 0.32); g.label(0.76, 0.28, "F_BC", 0.32); g.label(0.5, -0.07, "F_AB", 0.3)

    # --- Topografía -------------------------------------------------------------------------------
    @P.figure(CTP, "x-contour", "Curvas de nivel (cerro)", "Contour lines (hill)")
    def _(g):
        for k, (rx, ry, c) in enumerate(((0.5, 0.35, 100), (0.38, 0.26, 110), (0.26, 0.17, 120), (0.12, 0.08, 130))):
            pts = [(0.5 + rx * math.cos(t) * (1 + 0.1 * math.sin(3 * t + k)), 0.05 + ry * math.sin(t) * (1 + 0.1 * math.cos(2 * t))) for t in [2 * math.pi * i / 40 for i in range(41)]]
            g._add(pts); g.label(0.5 + rx, 0.05, str(c), 0.28)
        g.circle(0.5, 0.05, 0.015, fill=True); g.label(0.5, -0.12, "▲ 135", 0.3) if False else None

    @P.figure(CTP, "x-topo-profile", "Perfil del terreno y rasante", "Ground profile and grade line")
    def _(g):
        g.spline([(0, 0.1), (0.2, 0.22), (0.4, 0.05), (0.6, 0.2), (0.8, 0.12), (1.0, 0.3)]); g.line(0, 0.08, 1.0, 0.28, dashed=True)
        g.line(0, -0.1, 1, -0.1)
        for k in range(6): g.line(k * 0.2, -0.1, k * 0.2, -0.14); g.label(k * 0.2, -0.2, f"0+{k*20:02d}", 0.28)
        g.label(1.12, 0.28, "rasante", 0.3); g.label(1.1, 0.14, "terreno", 0.3)

    @P.figure(CTP, "x-theodolite", "Medición de altura con teodolito", "Height with theodolite")
    def _(g):
        g.line(0, 0, 1.2, 0); g.line(0.0, 0.0, 0.0, 0.1); g.line(1.0, 0, 1.0, 0.7); g.line(-0.05, 0.1, 0.05, 0.1)
        g.line(0.0, 0.1, 1.0, 0.7, dashed=True); g.line(0.0, 0.1, 1.0, 0.1, dashed=True)
        g.arc(0.0, 0.1, 0.28, 0.28, 0, 31); g.label(0.38, 0.17, "α", 0.5); g.label(0.5, 0.03, "d", 0.45); g.label(1.1, 0.4, "h", 0.5)
        g.label(0.5, -0.15, "h = d · tan α + h_i", 0.4)

    @P.figure(CTP, "x-leveling", "Nivelación diferencial", "Differential leveling")
    def _(g):
        g.spline([(0, 0.05), (0.3, 0.08), (0.6, 0.0), (1.0, -0.12)]); g.line(0.15, 0.06, 0.15, 0.55); g.line(0.9, -0.1, 0.9, 0.35)
        g.line(0.15, 0.4, 0.9, 0.4, dashed=True); g.poly(0.46, 0.4, 0.52, 0.4, 0.49, 0.48, fill=True) if False else g.circle(0.5, 0.45, 0.04)
        g.label(0.08, 0.55, "atrás", 0.3); g.label(0.98, 0.35, "adelante", 0.3); g.label(0.04, 0.3, "L₁", 0.35); g.label(1.0, 0.15, "L₂", 0.35); g.label(0.5, 0.53, "ΔH = L₁ − L₂", 0.35)

    @P.figure(CTP, "x-traverse", "Poligonal cerrada", "Closed traverse")
    def _(g):
        V = [(0.1, 0.0), (0.9, 0.05), (1.0, 0.5), (0.5, 0.75), (0.0, 0.45)]
        g.line(*[c for v in V + [V[0]] for c in v])
        for (x, y), t in zip(V, "ABCDE"): g.circle(x, y, 0.02, fill=True); g.label(x + (0.07 if x > 0.5 else -0.07), y + (0.06 if y > 0.4 else -0.06), t, 0.4)
        g.arrow(0.1, 0.0, 0.1, 0.2, 0.03); g.label(0.04, 0.22, "N", 0.4); g.label(0.5, 0.25, "Σ ángulos = (n−2)·180°", 0.32)

    # --- Hidráulica y geotecnia -------------------------------------------------------------------
    @P.figure(CHG, "x-venturi", "Venturi y línea de energía", "Venturi and energy line")
    def _(g):
        g.line(0, 0.1, 0.35, 0.1, 0.5, 0.04, 0.65, 0.04, 0.8, 0.1, 1.0, 0.1); g.line(0, -0.1, 0.35, -0.1, 0.5, -0.04, 0.65, -0.04, 0.8, -0.1, 1.0, -0.1)
        g.line(0.1, 0.1, 0.1, 0.35); g.line(0.57, 0.04, 0.57, 0.22); g.line(0.9, 0.1, 0.9, 0.35)
        g.line(0, 0.52, 1.0, 0.48, dashed=True); g.line(0.1, 0.35, 0.57, 0.22, 0.9, 0.34, dashed=True)
        g.label(1.08, 0.5, "EGL", 0.3); g.label(1.08, 0.34, "HGL", 0.3); g.arrow(0.05, 0, 0.25, 0, 0.03); g.label(0.57, -0.2, "v₁A₁ = v₂A₂", 0.35)

    @P.figure(CHG, "x-hydrostatic", "Presión hidrostática en una pared", "Hydrostatic pressure on a wall")
    def _(g):
        g.line(0, 0.5, 0, -0.1); g.hatch(-0.12, 0, -0.1, 1, 0.0) if False else None
        g.line(0, -0.1, 0.8, -0.1); g.line(-0.4, 0.5, 0, 0.5, dashed=True)
        g.line(0, 0.5, 0.4, -0.1); g.line(0.4, -0.1, 0, -0.1)
        for k in range(1, 5): y = 0.5 - k * 0.12; g.arrow(0.4 * (0.5 - y) / 0.6 + 0.0, y, 0.0, y, 0.03)
        g.label(0.55, 0.15, "p = ρ g h", 0.4); g.label(-0.2, 0.55, "▽", 0.4); g.label(0.5, -0.2, "F = ½ ρ g h² b", 0.38)

    @P.figure(CHG, "x-weir", "Vertedor de cresta", "Weir")
    def _(g):
        g.line(0, 0.4, 0.5, 0.4, dashed=True); g.line(0.3, 0.0, 0.5, 0.0, 0.5, 0.3, 0.7, 0.3, 0.7, 0.0, 1.0, 0.0)
        g.curve(lambda x: 0.3 + 0.12 * (1 - ((x - 0.7) / 0.3) ** 2) if x < 0.7 else 0.3 - 0.0, 0.5, 0.7) if False else None
        g.spline([(0.65, 0.4), (0.78, 0.33), (0.9, 0.12), (0.97, 0.01)], dashed=False)
        g.arrow(0.05, 0.2, 0.3, 0.2, 0.03); g.double_arrow(0.1, 0.0, 0.1, 0.4, 0.03); g.label(0.0, 0.2, "H", 0.5); g.label(0.5, -0.12, "Q = C L H^(3/2)", 0.38)

    @P.figure(CHG, "x-pipe-net", "Red de tuberías", "Pipe network")
    def _(g):
        V = {"A": (0.0, 0.3), "B": (0.5, 0.3), "C": (1.0, 0.3), "D": (0.0, -0.1), "E": (0.5, -0.1), "F": (1.0, -0.1)}
        for a, b in (("A", "B"), ("B", "C"), ("D", "E"), ("E", "F"), ("A", "D"), ("B", "E"), ("C", "F")): g.line(*V[a], *V[b])
        for k, (x, y) in V.items(): g.circle(x, y, 0.035, fill=True); g.label(x + (-0.08 if x == 0 else 0.0), y + 0.08, k, 0.4)
        g.arrow(-0.3, 0.3, -0.05, 0.3, 0.04); g.label(-0.3, 0.38, "Q", 0.45); g.arrow(1.05, -0.1, 1.3, -0.1, 0.04); g.label(0.25, 0.1, "I", 0.45); g.label(0.75, 0.1, "II", 0.45)

    @P.figure(CHG, "x-mohr-coulomb", "Círculo de Mohr y envolvente", "Mohr-Coulomb envelope")
    def _(g):
        axes(g, 1.0, 0.7); g.circle(0.5, 0.0, 0.25); g.line(0, 0.15, 0.85, 0.15 + 0.85 * 0.45)
        g.arc(0.2, 0.15, 0.12, 0.12, 0, 24); g.label(0.38, 0.18, "φ", 0.45); g.label(-0.06, 0.15, "c", 0.45); g.label(1.05, -0.07, "σ", 0.45); g.label(-0.06, 0.72, "τ", 0.45)

    @P.figure(CHG, "x-soil-phases", "Diagrama de fases del suelo", "Soil phase diagram")
    def _(g):
        g.rect(0, 0, 0.3, 0.5); g.line(0, 0.18, 0.3, 0.18); g.line(0, 0.38, 0.3, 0.38)
        g.label(0.15, 0.09, "Sólidos", 0.32); g.label(0.15, 0.28, "Agua", 0.32); g.label(0.15, 0.44, "Aire", 0.32)
        for y, t in ((0.09, "V_s"), (0.28, "V_w"), (0.44, "V_a")): g.label(0.42, y, t, 0.35)
        g.rect(0.7, 0, 1.0, 0.5); g.line(0.7, 0.18, 1.0, 0.18); g.line(0.7, 0.38, 1.0, 0.38)
        for y, t in ((0.09, "W_s"), (0.28, "W_w"), (0.44, "0")): g.label(1.12, y, t, 0.35)
        g.label(0.15, 0.58, "volúmenes", 0.32); g.label(0.85, 0.58, "pesos", 0.32)

    @P.figure(CHG, "x-retaining", "Muro de contención y empuje", "Retaining wall and earth pressure")
    def _(g):
        g.poly(0.3, 0.0, 0.6, 0.0, 0.6, 0.6, 0.5, 0.6, 0.45, 0.1, 0.3, 0.1); g.line(0.6, 0.6, 1.2, 0.6); g.line(0.6, 0.0, 1.2, 0.0)
        g.hatch(0.2, 1.2, 0.0, 9, 0.06)
        g.poly(0.6, 0.0, 0.6, 0.45, 0.95, 0.0) if False else None
        g.arrow(0.9, 0.2, 0.62, 0.2, 0.04) if False else None
        for y in (0.1, 0.25, 0.4): g.arrow(0.6 + 0.35 * (y / 0.6), y, 0.62, y, 0.03) if False else g.arrow(0.62 + 0.3 * (0.6 - y) / 0.6, y, 0.62, y, 0.03)
        g.label(1.0, 0.3, "E_a = ½ K_a γ H²", 0.32)

    @P.figure(CHG, "x-footing-types", "Cimentaciones (zapata, pilotes, losa)", "Foundation types")
    def _(g):
        g.line(0, 0, 1.2, 0); g.rect(0.12, 0.0, 0.32, -0.06); g.rect(0.18, 0.0, 0.26, 0.3)
        g.rect(0.55, 0.3, 0.75, 0.3) if False else None
        for x in (0.52, 0.62, 0.72): g.line(x, 0.0, x, -0.4)
        g.line(0.5, 0.0, 0.5, 0.0); g.rect(0.46, 0.0, 0.78, 0.06)
        g.rect(0.95, -0.06, 1.2, 0.0); g.line(1.0, 0.0, 1.0, 0.25); g.line(1.15, 0.0, 1.15, 0.25)
        g.label(0.22, -0.18, "zapata", 0.3); g.label(0.62, -0.48, "pilotes", 0.3); g.label(1.08, -0.16, "losa", 0.3)

    @P.figure(CHG, "x-grain-curve", "Curva granulométrica", "Grain-size curve")
    def _(g):
        axes(g, 1.0, 0.7)
        g.spline([(0.05, 0.02), (0.25, 0.1), (0.45, 0.35), (0.65, 0.58), (0.85, 0.66), (0.98, 0.68)])
        for x, t in ((0.1, "0.01"), (0.4, "0.1"), (0.7, "1"), (0.95, "10")): g.line(x, 0, x, -0.03); g.label(x, -0.1, t, 0.3)
        g.line(0, 0.1, 0.25, 0.1, dashed=True); g.label(-0.1, 0.1, "10 %", 0.28); g.label(0.5, -0.2, "D (mm), escala log", 0.32); g.label(-0.05, 0.75, "% que pasa", 0.3)

    @P.figure(CHG, "x-consolidation", "Curva de consolidación (e–log σ′)", "Consolidation curve")
    def _(g):
        axes(g, 1.0, 0.7)
        g.spline([(0.05, 0.62), (0.3, 0.6), (0.5, 0.5), (0.75, 0.3), (0.95, 0.18)]); g.line(0.5, 0.5, 0.65, 0.45, dashed=True) if False else None
        g.line(0.5, 0.0, 0.5, 0.5, dashed=True); g.label(0.5, -0.1, "σ′_c", 0.4); g.label(1.05, -0.1, "log σ′", 0.35); g.label(-0.06, 0.72, "e", 0.45); g.label(0.9, 0.34, "C_c", 0.4)


def hatch_wall(g):
    g.line(-0.1, 0.25, -0.1, -0.25)
    for k in range(5): y = -0.2 + k * 0.1; g.line(-0.1, y, -0.18, y - 0.06)
