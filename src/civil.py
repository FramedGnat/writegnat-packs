import math
from wgpack import Pack

pack = Pack("civil", "Ingeniería civil", "Apoyos, vigas, cargas, armaduras, secciones, suelos e hidráulica, con formulario de estructuras, materiales, hidráulica y geotecnia.",
            "Ingenierías", "🏗️", en={"Ingeniería civil": "Civil engineering",
            "Apoyos, vigas, cargas, armaduras, secciones, suelos e hidráulica, con formulario de estructuras, materiales, hidráulica y geotecnia.":
            "Supports, beams, loads, trusses, sections, soils and hydraulics, with formulas for structures, materials, hydraulics and geotechnics."})
P = pack
EST, SEC, HID = "Civil: estructuras", "Civil: secciones y elementos", "Civil: suelos e hidráulica"
P.en.update({EST: "Civil: structures", SEC: "Civil: sections and members", HID: "Civil: soils and hydraulics"})

@P.figure(EST, "fixed-support", "Empotramiento", "Fixed support")
def _(g):
    g.line(0, 0.5, 0, -0.5)
    for k in range(6): v = -0.45 + k * 0.18; g.line(0, v, -0.08, v - 0.08)
    g.line(0, 0, 1, 0)

@P.figure(EST, "pin-support", "Apoyo articulado", "Pin support")
def _(g): g.poly(0.5, 0, 0.35, -0.25, 0.65, -0.25); g.circle(0.5, 0, 0.03, fill=True); g.hatch(0.25, 0.75, -0.25, 5, 0.06)

@P.figure(EST, "roller-support", "Apoyo de rodillo", "Roller support")
def _(g):
    g.poly(0.5, 0, 0.37, -0.2, 0.63, -0.2); g.circle(0.5, 0, 0.03, fill=True)
    g.circle(0.42, -0.24, 0.04); g.circle(0.58, -0.24, 0.04); g.hatch(0.25, 0.75, -0.28, 5, 0.06)

@P.figure(EST, "simple-beam", "Viga simplemente apoyada", "Simply supported beam")
def _(g):
    g.rect(0, 0, 1, 0.06); g.poly(0.03, 0, -0.04, -0.12, 0.1, -0.12); g.hatch(-0.07, 0.13, -0.12, 3, 0.04)
    g.poly(0.97, 0, 0.9, -0.1, 1.04, -0.1); g.circle(0.93, -0.12, 0.02); g.circle(1.01, -0.12, 0.02); g.hatch(0.87, 1.07, -0.14, 3, 0.04)
    g.double_arrow(0.03, -0.25, 0.97, -0.25, 0.03); g.label(0.5, -0.31, "L", 0.7)

@P.figure(EST, "cantilever", "Viga en voladizo", "Cantilever beam")
def _(g):
    g.line(0, 0.3, 0, -0.3)
    for k in range(5): v = -0.25 + k * 0.13; g.line(0, v, -0.07, v - 0.07)
    g.rect(0, -0.03, 0.9, 0.03); g.arrow(0.9, 0.3, 0.9, 0.04, 0.04); g.label(0.95, 0.25, "P", 0.7)

@P.figure(EST, "dist-load", "Carga distribuida", "Distributed load")
def _(g):
    g.rect(0, 0, 1, 0.06)
    for k in range(7): g.arrow(0.08 + k * 0.14, 0.3, 0.08 + k * 0.14, 0.07, 0.035)
    g.line(0.08, 0.3, 0.92, 0.3); g.label(0.5, 0.38, "w", 0.8)

@P.figure(EST, "tri-load", "Carga triangular", "Triangular load")
def _(g):
    g.rect(0, 0, 1, 0.06); g.line(0, 0.07, 1, 0.4)
    for k in range(1, 7): u = k / 7; g.arrow(u, 0.07 + 0.33 * u, u, 0.07, 0.03)

@P.figure(EST, "point-load", "Carga puntual", "Point load")
def _(g): g.rect(0, 0, 1, 0.06); g.arrow(0.5, 0.45, 0.5, 0.07, 0.05); g.label(0.56, 0.4, "P", 0.8)

@P.figure(EST, "moment", "Momento aplicado", "Applied moment")
def _(g):
    g.rect(0, 0, 1, 0.06); g.arc(0.5, 0.03, 0.15, 0.15, 200, 520 - 180)
    a = math.radians(340); g.head(0.5 + 0.15 * math.cos(a - 0.2), 0.03 + 0.15 * math.sin(a - 0.2), 0.5 + 0.15 * math.cos(a), 0.03 + 0.15 * math.sin(a), 0.04)
    g.label(0.5, 0.25, "M", 0.7)

@P.figure(EST, "truss-pratt", "Armadura Pratt", "Pratt truss")
def _(g):
    n = 6; h = 0.3
    g.line(0, 0, 1, 0); g.line(1 / n, h, 1 - 1 / n, h); g.line(0, 0, 1 / n, h); g.line(1, 0, 1 - 1 / n, h)
    for k in range(1, n): g.line(k / n, 0, k / n, h)
    for k in range(1, n - 1): (g.line(k / n, h, (k + 1) / n, 0) if k >= n / 2 else g.line((k + 1) / n, h, k / n, 0))

@P.figure(EST, "truss-warren", "Armadura Warren", "Warren truss")
def _(g):
    n = 6; h = 0.3; g.line(0, 0, 1, 0); g.line(0.5 / n, h, 1 - 0.5 / n, h)
    zig = []
    for k in range(n): zig += [k / n, 0, (k + 0.5) / n, h]
    zig += [1, 0]; g.line(*zig)

@P.figure(EST, "frame", "Marco rígido", "Rigid frame")
def _(g):
    g.line(0.1, -0.4, 0.1, 0.35, 0.9, 0.35, 0.9, -0.4); g.hatch(0.0, 0.2, -0.4, 3, 0.05); g.hatch(0.8, 1.0, -0.4, 3, 0.05)
    g.arrow(-0.15, 0.35, 0.08, 0.35, 0.04); g.label(-0.1, 0.42, "H", 0.6)

@P.figure(EST, "shear-moment", "Diagramas de cortante y momento", "Shear and moment diagrams")
def _(g):
    g.line(0, 0.25, 1, 0.25); g.line(0, 0.25, 0, 0.4, 1, 0.1, 1, 0.25); g.label(-0.06, 0.32, "V", 0.6)
    g.line(0, -0.3, 1, -0.3); g.curve(lambda u: -0.3 + 0.4 * u * (1 - u) * 4 / 4 * 1.0, 0, 1, 40); g.label(-0.06, -0.2, "M", 0.6)

# --- Secciones y elementos ------------------------------------------------------------------------------

@P.figure(SEC, "i-section", "Perfil I", "I-section")
def _(g): g.poly(0.2, 0.35, 0.8, 0.35, 0.8, 0.28, 0.54, 0.28, 0.54, -0.28, 0.8, -0.28, 0.8, -0.35, 0.2, -0.35, 0.2, -0.28, 0.46, -0.28, 0.46, 0.28, 0.2, 0.28)

@P.figure(SEC, "t-section", "Perfil T", "T-section")
def _(g): g.poly(0.2, 0.35, 0.8, 0.35, 0.8, 0.27, 0.54, 0.27, 0.54, -0.35, 0.46, -0.35, 0.46, 0.27, 0.2, 0.27)

@P.figure(SEC, "c-section", "Perfil C (canal)", "C-channel")
def _(g): g.poly(0.3, 0.35, 0.7, 0.35, 0.7, 0.28, 0.38, 0.28, 0.38, -0.28, 0.7, -0.28, 0.7, -0.35, 0.3, -0.35)

@P.figure(SEC, "angle-section", "Ángulo (L)", "Angle (L)")
def _(g): g.poly(0.3, 0.35, 0.38, 0.35, 0.38, -0.27, 0.7, -0.27, 0.7, -0.35, 0.3, -0.35)

@P.figure(SEC, "rect-section", "Sección rectangular", "Rectangular section")
def _(g):
    g.rect(0.35, -0.3, 0.65, 0.3); g.double_arrow(0.35, -0.38, 0.65, -0.38, 0.03); g.label(0.5, -0.44, "b", 0.6)
    g.double_arrow(0.72, -0.3, 0.72, 0.3, 0.03); g.label(0.78, 0, "h", 0.6); g.line(0.3, 0, 0.7, 0, dashed=True)

@P.figure(SEC, "rc-section", "Sección de concreto armado", "Reinforced concrete section")
def _(g):
    g.rect(0.3, -0.35, 0.7, 0.35); g.rect(0.34, -0.31, 0.66, 0.31, dashed=True)
    for u in (0.38, 0.5, 0.62): g.circle(u, -0.26, 0.025, fill=True)
    for u in (0.38, 0.62): g.circle(u, 0.26, 0.02, fill=True)

@P.figure(SEC, "circ-section", "Sección circular hueca", "Hollow circular section")
def _(g): g.circle(0.5, 0, 0.35); g.circle(0.5, 0, 0.27); g.line(0.1, 0, 0.9, 0, dashed=True); g.line(0.5, -0.4, 0.5, 0.4, dashed=True)

@P.figure(SEC, "column", "Columna", "Column")
def _(g): g.rect(0.42, -0.4, 0.58, 0.4); g.hatch(0.25, 0.75, -0.4, 5, 0.05); g.arrow(0.5, 0.7, 0.5, 0.42, 0.04); g.label(0.56, 0.65, "P", 0.7)

@P.figure(SEC, "footing", "Zapata", "Footing")
def _(g):
    g.rect(0.42, 0.0, 0.58, 0.5); g.rect(0.15, -0.2, 0.85, 0.0); g.line(0, 0.25, 1, 0.25, dashed=True)
    for k in range(9): u = 0.1 + k * 0.1; g.line(u, -0.3, u - 0.05, -0.35)

@P.figure(SEC, "wall", "Muro de contención", "Retaining wall")
def _(g): g.poly(0.3, 0.5, 0.42, 0.5, 0.5, -0.2, 0.75, -0.2, 0.75, -0.3, 0.1, -0.3, 0.1, -0.2, 0.3, -0.2); g.line(0.42, 0.5, 1, 0.5)

@P.figure(SEC, "rebar", "Varilla corrugada", "Rebar")
def _(g):
    g.line(0, 0.04, 1, 0.04); g.line(0, -0.04, 1, -0.04)
    for k in range(16): u = 0.03 + k * 0.06; g.line(u, -0.06, u + 0.03, 0.06)

# --- Suelos e hidráulica ---------------------------------------------------------------------------------

@P.figure(HID, "soil-layers", "Estratos de suelo", "Soil layers")
def _(g):
    g.line(0, 0.4, 1, 0.4); g.line(0, 0.1, 1, 0.12); g.line(0, -0.2, 1, -0.17)
    for k in range(10): g.circle(0.05 + k * 0.1, 0.25 + 0.04 * (k % 2), 0.015, fill=True)
    for k in range(12): u = 0.04 + k * 0.08; g.line(u, -0.02, u + 0.04, -0.02)
    for k in range(10): u = 0.05 + k * 0.1; g.line(u, -0.3, u + 0.04, -0.34)
    g.label(1.08, 0.25, "arena", 0.45); g.label(1.08, -0.04, "arcilla", 0.45); g.label(1.08, -0.3, "roca", 0.45)

@P.figure(HID, "water-level", "Nivel freático", "Water table")
def _(g): g.line(0, 0, 1, 0); g.poly(0.45, 0.1, 0.55, 0.1, 0.5, 0.01); g.line(0.42, -0.04, 0.58, -0.04); g.line(0.46, -0.08, 0.54, -0.08)

@P.figure(HID, "level-mark", "Cota de nivel", "Level mark")
def _(g): g.line(0, 0, 1, 0); g.poly(0.4, 0.12, 0.6, 0.12, 0.5, 0.01); g.label(0.75, 0.12, "+0.00", 0.6)

@P.figure(HID, "open-channel", "Canal abierto", "Open channel")
def _(g):
    g.line(0, 0.4, 0.25, -0.3, 0.75, -0.3, 1, 0.4); g.line(0.1, 0.12, 0.9, 0.12, dashed=True); g.poly(0.45, 0.2, 0.55, 0.2, 0.5, 0.13)
    g.double_arrow(0.85, 0.12, 0.85, -0.3, 0.03); g.label(0.92, -0.08, "y", 0.6)

@P.figure(HID, "pipe", "Tubería con flujo", "Pipe flow")
def _(g):
    g.line(0, 0.15, 1, 0.15); g.line(0, -0.15, 1, -0.15); g.ellipse(0, 0, 0.04, 0.15); g.ellipse(1, 0, 0.04, 0.15)
    g.curve(lambda u: 0, 0.1, 0.1, 2); g.arrow(0.2, 0, 0.5, 0, 0.04); g.label(0.35, 0.06, "Q", 0.6)
    g.curve(lambda u: 0.13 * (1 - ((u - 0.75) / 0.12) ** 2) if abs(u - 0.75) < 0.12 else 0, 0.63, 0.87, 20)

@P.figure(HID, "dam", "Presa", "Dam")
def _(g):
    g.poly(0.4, 0.45, 0.5, 0.45, 0.75, -0.3, 0.3, -0.3); g.line(0, 0.35, 0.37, 0.35); g.poly(0.15, 0.43, 0.25, 0.43, 0.2, 0.36)
    g.line(0, -0.3, 1, -0.3); g.line(0.75, -0.22, 1, -0.22)
    for k in range(4): g.arrow(0.38 - 0.07 * k, -0.25 + 0.15 * k, 0.33 - 0.07 * k + 0.02, -0.25 + 0.15 * k, 0.02)

@P.figure(HID, "mohr", "Círculo de Mohr", "Mohr's circle")
def _(g):
    g.arrow(0, 0, 1, 0, 0.03); g.arrow(0.1, -0.45, 0.1, 0.45, 0.03); g.circle(0.55, 0, 0.3); g.line(0.35, 0.22, 0.75, -0.22)
    g.label(0.97, -0.06, "σ", 0.7); g.label(0.15, 0.42, "τ", 0.7); g.label(0.25, -0.06, "σ₂", 0.5); g.label(0.85, -0.06, "σ₁", 0.5)

@P.figure(HID, "north", "Norte", "North arrow")
def _(g): g.poly(0.5, 0.45, 0.62, -0.25, 0.5, -0.12, fill=True); g.poly(0.5, 0.45, 0.38, -0.25, 0.5, -0.12); g.label(0.5, 0.58, "N", 0.8)

# --- Fórmulas -------------------------------------------------------------------------------------------------

G = "Ingenierías"
P.formulas_in(G, "Mecánica de materiales", [
    ("Esfuerzo normal", r"\sigma = \frac{F}{A}", "Normal stress"),
    ("Esfuerzo cortante", r"\tau = \frac{V}{A}", "Shear stress"),
    ("Deformación unitaria", r"\varepsilon = \frac{\Delta L}{L_{0}}", "Strain"),
    ("Ley de Hooke", r"\sigma = E \varepsilon", "Hooke's law"),
    ("Alargamiento axial", r"\delta = \frac{P L}{A E}", "Axial elongation"),
    ("Relación de Poisson", r"\nu = -\frac{\varepsilon_{lat}}{\varepsilon_{axial}}", "Poisson's ratio"),
    ("Flexión", r"\sigma = \frac{M y}{I}", "Bending"),
    ("Cortante en vigas", r"\tau = \frac{V Q}{I t}", "Shear in beams"),
    ("Torsión", r"\tau = \frac{T r}{J}", "Torsion"),
    ("Ángulo de torsión", r"\phi = \frac{T L}{G J}", "Angle of twist"),
    ("Momento de inercia (rectángulo)", r"I = \frac{b h^{3}}{12}", "Moment of inertia (rectangle)"),
    ("Momento de inercia (círculo)", r"I = \frac{\pi d^{4}}{64}", "Moment of inertia (circle)"),
    ("Pandeo de Euler", r"P_{cr} = \frac{\pi^{2} E I}{(K L)^{2}}", "Euler buckling"),
    ("Esfuerzos principales", r"\sigma_{1,2} = \frac{\sigma_{x} + \sigma_{y}}{2} \pm \sqrt{\left( \frac{\sigma_{x} - \sigma_{y}}{2} \right)^{2} + \tau_{xy}^{2}}", "Principal stresses"),
    ("Von Mises", r"\sigma_{v} = \sqrt{\sigma_{1}^{2} - \sigma_{1}\sigma_{2} + \sigma_{2}^{2}}", "Von Mises"),
], "Mechanics of materials")
P.formulas_in(G, "Análisis estructural", [
    ("Equilibrio", r"\sum F_{x} = 0, \; \sum F_{y} = 0, \; \sum M = 0", "Equilibrium"),
    ("Relación carga-cortante", r"\frac{dV}{dx} = -w(x)", "Load–shear relation"),
    ("Relación cortante-momento", r"\frac{dM}{dx} = V(x)", "Shear–moment relation"),
    ("Ecuación de la elástica", r"E I \frac{d^{2} y}{dx^{2}} = M(x)", "Elastic curve equation"),
    ("Momento máximo (viga simple)", r"M_{max} = \frac{w L^{2}}{8}", "Maximum moment (simple beam)"),
    ("Flecha máxima (viga simple)", r"\delta_{max} = \frac{5 w L^{4}}{384 E I}", "Maximum deflection (simple beam)"),
    ("Voladizo con carga puntual", r"\delta_{max} = \frac{P L^{3}}{3 E I}", "Cantilever with point load"),
    ("Grado de indeterminación", r"GI = r + m - 2j", "Degree of indeterminacy"),
    ("Método de los nudos", r"\sum F_{x} = 0, \; \sum F_{y} = 0 \text{ en cada nudo}", "Method of joints"),
    ("Concreto: resistencia a flexión", r"M_{n} = A_{s} f_{y} \left( d - \frac{a}{2} \right), \; a = \frac{A_{s} f_{y}}{0.85 f'_{c} b}", "Concrete: flexural strength"),
], "Structural analysis")
P.formulas_in(G, "Hidráulica", [
    ("Caudal", r"Q = A v", "Flow rate"),
    ("Bernoulli con pérdidas", r"z_{1} + \frac{P_{1}}{\gamma} + \frac{v_{1}^{2}}{2g} = z_{2} + \frac{P_{2}}{\gamma} + \frac{v_{2}^{2}}{2g} + h_{f}", "Bernoulli with losses"),
    ("Darcy-Weisbach", r"h_{f} = f \frac{L}{D} \frac{v^{2}}{2g}", "Darcy–Weisbach"),
    ("Hazen-Williams", r"v = 0.849 \, C R_{h}^{0.63} S^{0.54}", "Hazen–Williams"),
    ("Manning", r"V = \frac{1}{n} R_{h}^{2/3} S^{1/2}", "Manning"),
    ("Radio hidráulico", r"R_{h} = \frac{A}{P_{m}}", "Hydraulic radius"),
    ("Número de Froude", r"Fr = \frac{v}{\sqrt{g y}}", "Froude number"),
    ("Número de Reynolds", r"Re = \frac{\rho v D}{\mu}", "Reynolds number"),
    ("Empuje sobre una pared", r"F = \gamma \, h_{c} \, A", "Force on a wall"),
    ("Vertedor rectangular", r"Q = C L H^{3/2}", "Rectangular weir"),
    ("Método racional", r"Q = \frac{C i A}{3.6}", "Rational method"),
], "Hydraulics")
P.formulas_in(G, "Geotecnia", [
    ("Esfuerzo efectivo", r"\sigma' = \sigma - u", "Effective stress"),
    ("Relación de vacíos", r"e = \frac{V_{v}}{V_{s}}", "Void ratio"),
    ("Porosidad", r"n = \frac{e}{1 + e}", "Porosity"),
    ("Peso volumétrico seco", r"\gamma_{d} = \frac{\gamma}{1 + w}", "Dry unit weight"),
    ("Mohr-Coulomb", r"\tau = c + \sigma' \tan\phi", "Mohr–Coulomb"),
    ("Darcy (flujo en suelos)", r"q = k i A", "Darcy (seepage)"),
    ("Capacidad de carga (Terzaghi)", r"q_{u} = c N_{c} + q N_{q} + \frac{1}{2} \gamma B N_{\gamma}", "Bearing capacity (Terzaghi)"),
    ("Empuje activo (Rankine)", r"K_{a} = \tan^{2}\left( 45^{\circ} - \frac{\phi}{2} \right)", "Active pressure (Rankine)"),
    ("Asentamiento por consolidación", r"S = \frac{C_{c} H}{1 + e_{0}} \log \frac{\sigma'_{f}}{\sigma'_{0}}", "Consolidation settlement"),
], "Geotechnics")

P.labels = [["Carga muerta", "#334155"], ["Carga viva", "#dc2626"], ["Reacción", "#2563eb"], ["Tensión", "#16a34a"],
            ["Compresión", "#ea580c"], ["Revisar", "#ca8a04"], ["Planta", "#0891b2"], ["Corte", "#7c3aed"]]
P.en.update({"Carga muerta": "Dead load", "Carga viva": "Live load", "Reacción": "Reaction", "Tensión": "Tension", "Compresión": "Compression",
             "Revisar": "Check", "Planta": "Plan", "Corte": "Section"})
P.emoji = {"Ingeniería civil": "🏗️ 🧱 🏢 🌉 🛣️ 🚧 🏠 💧 🌊 ⛰️ 📐 📏 🦺 🚜 🏛️"}
