"""Figuras de las materias de Química: operaciones unitarias, balances, termodinámica y cinética."""
import math

OPU, TER, BAL = "Química: operaciones unitarias", "Química: termodinámica y cinética", "Química: equipos y diagramas de proceso"


def extend(P):
    P.en.update({OPU: "Chemistry: unit operations", TER: "Chemistry: thermodynamics and kinetics", BAL: "Chemistry: equipment and process diagrams"})

    def axes(g, w=1.0, h=0.7):
        g.arrow(0, 0, w + 0.05, 0, 0.03); g.arrow(0, 0, 0, h + 0.05, 0.03)

    # --- Operaciones unitarias -------------------------------------------------------------------
    @P.figure(OPU, "x-distill", "Columna de destilación", "Distillation column")
    def _(g):
        g.rect(0.35, -0.5, 0.6, 0.5); g.arc(0.475, 0.5, 0.125, 0.07, 0, 180); g.arc(0.475, -0.5, 0.125, 0.07, 180, 360)
        for k in range(6): y = 0.35 - k * 0.14; g.line(0.35, y, 0.55, y, 0.6, y - 0.05) if False else g.line(0.37, y, 0.58, y)
        g.arrow(0.0, 0.0, 0.35, 0.0, 0.04); g.label(0.0, 0.08, "alimentación", 0.32)
        g.arrow(0.475, 0.58, 0.475, 0.75, 0.04); g.label(0.475, 0.82, "destilado", 0.32)
        g.arrow(0.475, -0.58, 0.475, -0.75, 0.04); g.label(0.475, -0.82, "fondos", 0.32)
        g.line(0.6, 0.4, 0.85, 0.4, 0.85, 0.2); g.circle(0.85, 0.12, 0.08); g.label(0.85, 0.12, "C", 0.3) if False else None
        g.circle(0.9, 0.4, 0.0, fill=False) if False else None; g.label(1.05, 0.35, "reflujo", 0.3); g.circle(0.85, -0.45, 0.08); g.label(0.85, -0.45, "R", 0.3)

    @P.figure(OPU, "x-heat-exchanger", "Intercambiador de tubos y coraza", "Shell-and-tube exchanger")
    def _(g):
        g.rect(0.1, -0.18, 0.9, 0.18); g.arc(0.1, 0, 0.0, 0.18, 90, 270) if False else None
        g.line(0.0, 0.1, 1.0, 0.1) if False else None
        for y in (0.1, 0.0, -0.1): g.line(0.0, y, 1.0, y)
        g.line(0.3, 0.18, 0.3, -0.18); g.line(0.7, 0.18, 0.7, -0.18)
        g.arrow(0.2, 0.38, 0.2, 0.19, 0.03); g.arrow(0.8, -0.19, 0.8, -0.38, 0.03)
        g.arrow(-0.2, 0.0, 0.0, 0.0, 0.03); g.arrow(1.0, 0.0, 1.2, 0.0, 0.03)
        g.label(0.2, 0.46, "coraza (frío)", 0.3); g.label(-0.1, 0.1, "tubos (caliente)", 0.3)

    @P.figure(OPU, "x-cstr", "Reactor CSTR (tanque agitado)", "CSTR reactor")
    def _(g):
        g.rect(0.25, -0.35, 0.75, 0.3); g.arc(0.5, 0.3, 0.25, 0.08, 0, 180); g.arc(0.5, -0.35, 0.25, 0.08, 180, 360)
        g.line(0.5, 0.38, 0.5, -0.2); g.line(0.4, -0.2, 0.6, -0.2); g.line(0.4, -0.12, 0.6, -0.12) if False else None
        g.arrow(0.0, 0.2, 0.25, 0.2, 0.04); g.label(0.0, 0.28, "F_A0", 0.35); g.arrow(0.75, -0.3, 1.0, -0.3, 0.04); g.label(1.05, -0.22, "F_A", 0.35)
        g.rect(0.45, 0.45, 0.55, 0.5) if False else g.rect(0.44, 0.42, 0.56, 0.48); g.label(0.5, 0.56, "M", 0.4); g.label(0.5, -0.5, "V = F_A0 X / (−r_A)", 0.32)

    @P.figure(OPU, "x-pfr", "Reactor de flujo pistón (PFR)", "Plug-flow reactor")
    def _(g):
        g.rect(0.2, -0.12, 0.8, 0.12); g.arrow(0.0, 0.0, 0.2, 0.0, 0.04); g.arrow(0.8, 0.0, 1.0, 0.0, 0.04)
        for k in range(1, 6): g.line(0.2 + 0.1 * k, -0.12, 0.2 + 0.1 * k, 0.12, dashed=True)
        g.label(-0.05, 0.1, "F_A0", 0.35); g.label(1.05, 0.1, "F_A", 0.35); g.double_arrow(0.2, -0.22, 0.8, -0.22, 0.03); g.label(0.5, -0.3, "V (dV)", 0.35)

    @P.figure(OPU, "x-pump", "Bomba centrífuga", "Centrifugal pump")
    def _(g):
        g.circle(0.4, 0.0, 0.25); g.circle(0.4, 0.0, 0.05, fill=True); g.line(0.4, 0.25, 0.4, 0.25 + 0.2, 0.7, 0.25 + 0.2) if False else None
        g.line(0.4, 0.25, 0.8, 0.25); g.line(0.0, 0.0, 0.15, 0.0); g.arrow(0.0, 0.0, 0.15, 0.0, 0.0)
        g.arrow(-0.2, 0.0, 0.15, 0.0, 0.04); g.arrow(0.8, 0.25, 1.0, 0.25, 0.04) if False else g.arrow(0.7, 0.25, 1.0, 0.25, 0.04); g.line(0.4, -0.25, 0.8, -0.25) if False else None
        for a in (0, 90, 180, 270): g.line(0.4, 0.0, 0.4 + 0.2 * math.cos(math.radians(a + 25)), 0.2 * math.sin(math.radians(a + 25)))
        g.label(-0.1, 0.1, "succión", 0.3); g.label(0.9, 0.35, "descarga", 0.3)

    @P.figure(OPU, "x-tank", "Tanque de almacenamiento", "Storage tank")
    def _(g):
        g.rect(0.2, -0.3, 0.8, 0.3); g.line(0.2, 0.3, 0.5, 0.42, 0.8, 0.3); g.line(0.2, 0.05, 0.8, 0.05, dashed=True)
        g.arrow(0.0, -0.2, 0.2, -0.2, 0.04); g.arrow(0.8, -0.28, 1.0, -0.28, 0.04); g.arrow(0.5, 0.6, 0.5, 0.44, 0.04)
        g.label(0.5, -0.1, "L", 0.45)
        g.line(0.28, 0.0, 0.28, 0.3) if False else None

    @P.figure(OPU, "x-evaporator", "Evaporador", "Evaporator")
    def _(g):
        g.rect(0.2, -0.3, 0.8, 0.3); g.arc(0.5, 0.3, 0.3, 0.12, 0, 180)
        g.zigzag(0.28, 0.72, -0.15, 0.04, 6, 0.04); g.arrow(0.5, 0.52, 0.5, 0.7, 0.04); g.label(0.5, 0.78, "vapor", 0.3)
        g.arrow(0.0, -0.1, 0.2, -0.1, 0.04); g.label(0.0, -0.02, "alim.", 0.3); g.arrow(0.5, -0.32, 0.5, -0.5, 0.04); g.label(0.5, -0.58, "concentrado", 0.3)
        g.arrow(1.0, -0.15, 0.82, -0.15, 0.03); g.label(1.0, -0.07, "vapor vivo", 0.3)

    @P.figure(OPU, "x-dryer", "Secador rotatorio", "Rotary dryer")
    def _(g):
        g.poly(0.1, 0.12, 0.9, 0.18, 0.9, -0.18, 0.1, -0.12); g.line(0.15, 0.1, 0.85, 0.14, dashed=True) if False else None
        g.circle(0.3, 0.0, 0.0) if False else None
        g.arrow(0.0, 0.3, 0.2, 0.15, 0.04); g.label(0.0, 0.4, "sólido húmedo", 0.3); g.arrow(0.8, -0.15, 1.0, -0.3, 0.04); g.label(1.05, -0.4, "sólido seco", 0.3)
        g.arrow(1.0, 0.0, 0.9, 0.0, 0.0) if False else g.arrow(1.0, 0.05, 0.9, 0.05, 0.03); g.label(1.05, 0.15, "aire", 0.3)
        g.line(0.2, -0.12, 0.15, -0.3); g.line(0.8, -0.18, 0.85, -0.3); g.line(0.1, -0.3, 0.9, -0.3)

    @P.figure(OPU, "x-absorber", "Columna de absorción", "Absorption column")
    def _(g):
        g.rect(0.3, -0.45, 0.65, 0.45)
        for y in (0.3, 0.1, -0.1, -0.3): g.line(0.3, y, 0.65, y, dashed=True)
        g.arrow(0.475, 0.8, 0.475, 0.46, 0.04); g.label(0.475, 0.86, "líquido", 0.3); g.arrow(0.0, -0.35, 0.3, -0.35, 0.04); g.label(0.0, -0.28, "gas", 0.3)
        g.arrow(0.65, 0.35, 0.95, 0.35, 0.04); g.label(1.05, 0.38, "gas limpio", 0.3); g.arrow(0.475, -0.46, 0.475, -0.7, 0.04)

    @P.figure(OPU, "x-filter-press", "Filtración", "Filtration")
    def _(g):
        g.poly(0.15, 0.4, 0.85, 0.4, 0.55, 0.0, 0.45, 0.0); g.line(0.45, 0.0, 0.45, -0.25); g.line(0.55, 0.0, 0.55, -0.25)
        g.line(0.15, 0.1, 0.85, 0.1, dashed=True); g.label(0.5, 0.25, "suspensión", 0.35); g.label(0.5, 0.06, "papel filtro", 0.28)
        g.arrow(0.5, -0.3, 0.5, -0.45, 0.04); g.label(0.5, -0.52, "filtrado", 0.3)
        for x in (0.35, 0.5, 0.62): g.circle(x, 0.14, 0.015, fill=True)

    # --- Equipos y diagramas de proceso -----------------------------------------------------------
    @P.figure(BAL, "x-block-process", "Diagrama de bloques de proceso", "Process block diagram")
    def _(g):
        for x, t in ((0.15, "Reactor"), (0.55, "Separador")): g.rect(x, -0.12, x + 0.3, 0.12); g.label(x + 0.15, 0.0, t, 0.4)
        g.arrow(-0.15, 0.0, 0.15, 0.0, 0.04); g.label(-0.15, 0.08, "A + B", 0.35); g.arrow(0.45, 0.0, 0.55, 0.0, 0.04); g.arrow(0.85, 0.05, 1.15, 0.05, 0.04); g.label(1.1, 0.13, "Producto", 0.32)
        g.line(0.85, -0.05, 1.0, -0.05, 1.0, -0.3, 0.3, -0.3, 0.3, -0.12); g.head(0.3, -0.3, 0.3, -0.12, 0.04); g.label(0.65, -0.37, "reciclo", 0.32)
        g.arrow(0.7, 0.12, 0.7, 0.3, 0.04); g.label(0.7, 0.38, "purga", 0.3)

    @P.figure(BAL, "x-mass-balance", "Balance de materia (volumen de control)", "Mass balance")
    def _(g):
        g.rect(0.3, -0.2, 0.7, 0.2, dashed=True); g.label(0.5, 0.0, "Proceso", 0.45)
        g.arrow(0.0, 0.1, 0.3, 0.1, 0.04); g.arrow(0.0, -0.1, 0.3, -0.1, 0.04); g.arrow(0.7, 0.0, 1.0, 0.0, 0.04)
        g.label(0.0, 0.2, "ṁ₁", 0.4); g.label(0.0, -0.2, "ṁ₂", 0.4); g.label(1.05, 0.1, "ṁ₃", 0.4); g.label(0.5, -0.4, "Entra − Sale + Gen = Acum", 0.35)

    @P.figure(BAL, "x-pid-symbols", "Símbolos P&ID (válvula, instrumento)", "P&ID symbols")
    def _(g):
        g.line(0.0, 0.0, 0.8, 0.0); g.poly(0.2, 0.08, 0.2, -0.08, 0.35, 0.0) if False else None
        g.poly(0.25, 0.08, 0.4, 0.0, 0.25, -0.08, 0.1, 0.0); g.poly(0.4, 0.0, 0.55, 0.08, 0.55, -0.08, 0.4, 0.0) if False else g.poly(0.1, 0.08, 0.25, 0.0, 0.1, -0.08)
        g.poly(0.25, 0.0, 0.4, 0.08, 0.4, -0.08)
        g.circle(0.65, 0.3, 0.08); g.label(0.65, 0.3, "FT", 0.35); g.line(0.65, 0.22, 0.65, 0.0)
        g.circle(0.9, 0.3, 0.08); g.line(0.82, 0.3, 0.98, 0.3); g.label(0.9, 0.34, "PIC", 0.28); g.label(0.9, 0.26, "101", 0.28); g.line(0.9, 0.22, 0.9, 0.0, dashed=True)
        g.label(0.25, -0.15, "válvula", 0.3)

    @P.figure(BAL, "x-flash", "Separador flash", "Flash separator")
    def _(g):
        g.rect(0.35, -0.3, 0.65, 0.3); g.arc(0.5, 0.3, 0.15, 0.06, 0, 180); g.arc(0.5, -0.3, 0.15, 0.06, 180, 360)
        g.arrow(0.0, 0.0, 0.35, 0.0, 0.04); g.label(0.0, 0.08, "F, z", 0.35); g.arrow(0.5, 0.38, 0.5, 0.6, 0.04); g.label(0.5, 0.68, "V, y", 0.35)
        g.arrow(0.5, -0.38, 0.5, -0.6, 0.04); g.label(0.5, -0.68, "L, x", 0.35); g.line(0.35, -0.1, 0.65, -0.1, dashed=True)

    # --- Termodinámica y cinética ----------------------------------------------------------------
    @P.figure(TER, "x-pv-cycle", "Ciclo en diagrama P–V", "P–V cycle")
    def _(g):
        axes(g, 1.0, 0.8); g.line(0.2, 0.2, 0.2, 0.6); g.spline([(0.2, 0.6), (0.4, 0.45), (0.7, 0.32)]); g.line(0.7, 0.32, 0.7, 0.2); g.line(0.7, 0.2, 0.2, 0.2)
        g.arrow(0.2, 0.3, 0.2, 0.45, 0.03); g.label(0.12, 0.2, "1", 0.4); g.label(0.12, 0.6, "2", 0.4); g.label(0.76, 0.34, "3", 0.4); g.label(0.76, 0.18, "4", 0.4)
        g.label(1.05, -0.07, "V", 0.45); g.label(-0.07, 0.8, "P", 0.45); g.label(0.45, 0.28, "W", 0.45)

    @P.figure(TER, "x-ts", "Diagrama T–s (ciclo)", "T–s diagram")
    def _(g):
        axes(g, 1.0, 0.8); g.spline([(0.1, 0.0), (0.2, 0.3), (0.4, 0.5), (0.5, 0.55), (0.6, 0.5), (0.8, 0.3), (0.95, 0.0)], dashed=True)
        g.line(0.25, 0.15, 0.25, 0.65, 0.75, 0.65, 0.75, 0.15, 0.25, 0.15); g.label(0.5, 0.72, "T", 0.0) if False else None
        g.label(1.05, -0.07, "s", 0.45); g.label(-0.07, 0.8, "T", 0.45); g.label(0.5, 0.45, "vapor + líquido", 0.3)

    @P.figure(TER, "x-phase", "Diagrama de fases P–T", "P–T phase diagram")
    def _(g):
        axes(g, 1.0, 0.8); g.line(0, 0.1, 0.3, 0.2); g.spline([(0.3, 0.2), (0.5, 0.35), (0.7, 0.55), (0.85, 0.7)]); g.line(0.3, 0.2, 0.4, 0.75)
        g.circle(0.3, 0.2, 0.02, fill=True); g.label(0.38, 0.12, "punto triple", 0.28); g.circle(0.85, 0.7, 0.02, fill=False); g.label(0.9, 0.78, "crítico", 0.28)
        g.label(0.15, 0.45, "sólido", 0.35); g.label(0.65, 0.2, "gas", 0.35); g.label(0.6, 0.6, "líquido", 0.35)

    @P.figure(TER, "x-arrhenius", "Gráfica de Arrhenius", "Arrhenius plot")
    def _(g):
        axes(g, 1.0, 0.8); g.line(0.1, 0.65, 0.9, 0.1)
        for x, y in ((0.15, 0.62), (0.3, 0.52), (0.45, 0.45), (0.62, 0.33), (0.8, 0.18)): g.circle(x, y, 0.015, fill=True)
        g.label(1.05, -0.07, "1/T", 0.45); g.label(-0.1, 0.8, "ln k", 0.4); g.label(0.7, 0.55, "pendiente = −Eₐ/R", 0.32)

    @P.figure(TER, "x-activation", "Energía de activación (con y sin catalizador)", "Activation energy")
    def _(g):
        axes(g, 1.0, 0.8); g.spline([(0.05, 0.25), (0.25, 0.25), (0.4, 0.7), (0.6, 0.2), (0.95, 0.1)]) if False else None
        g.spline([(0.05, 0.3), (0.2, 0.3), (0.35, 0.72), (0.5, 0.35), (0.65, 0.15), (0.95, 0.15)]); g.spline([(0.2, 0.3), (0.35, 0.52), (0.5, 0.3)], dashed=True)
        g.double_arrow(0.7, 0.3, 0.7, 0.15, 0.03) if False else None
        g.label(0.35, 0.8, "Eₐ", 0.45); g.label(0.8, 0.08, "ΔH", 0.4); g.label(0.55, 0.55, "con catalizador", 0.28); g.label(0.05, 0.38, "reactivos", 0.28); g.label(0.9, 0.22, "productos", 0.28); g.label(1.0, -0.07, "avance", 0.35)

    @P.figure(TER, "x-conc-time", "Concentración vs tiempo (orden 1)", "Concentration vs time")
    def _(g):
        axes(g, 1.0, 0.8); g.curve(lambda t: 0.7 * math.exp(-3 * t), 0, 0.95); g.curve(lambda t: 0.7 * (1 - math.exp(-3 * t)), 0, 0.95, dashed=True)
        g.label(0.1, 0.78, "[A]", 0.45); g.label(0.85, 0.62, "[P]", 0.45); g.label(1.05, -0.07, "t", 0.45); g.label(0.45, 0.18, "[A] = [A]₀ e^(−kt)", 0.32)

    @P.figure(TER, "x-mccabe", "Método de McCabe–Thiele", "McCabe–Thiele diagram")
    def _(g):
        axes(g, 1.0, 1.0); g.line(0, 0, 1, 1, dashed=True); g.spline([(0, 0), (0.1, 0.3), (0.3, 0.58), (0.6, 0.8), (1.0, 1.0)])
        pts = [(0.1, 0.1)]
        for x, y in ((0.1, 0.3), (0.3, 0.3), (0.3, 0.58), (0.58, 0.58), (0.58, 0.78), (0.78, 0.78)): pts.append((x, y))
        g._add(pts); g.label(1.08, -0.07, "x", 0.45); g.label(-0.07, 1.05, "y", 0.45)

    @P.figure(TER, "x-enthalpy", "Diagrama de entalpía (exo/endotérmica)", "Enthalpy diagram")
    def _(g):
        g.arrow(0, 0, 0, 0.8, 0.03); g.line(0.1, 0.55, 0.45, 0.55); g.line(0.55, 0.15, 0.9, 0.15); g.arrow(0.5, 0.55, 0.5, 0.18, 0.04)
        g.label(0.28, 0.62, "reactivos", 0.32); g.label(0.72, 0.08, "productos", 0.32); g.label(0.64, 0.38, "ΔH < 0", 0.38); g.label(-0.06, 0.8, "H", 0.45)
