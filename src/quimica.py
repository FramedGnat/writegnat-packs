import math
from wgpack import Pack

pack = Pack("quimica", "Química", "Material de laboratorio, estructuras moleculares, orbitales y formulario de estequiometría, gases, termoquímica, cinética, equilibrio y electroquímica.",
            "Ciencias", "🧪", en={"Química": "Chemistry",
            "Material de laboratorio, estructuras moleculares, orbitales y formulario de estequiometría, gases, termoquímica, cinética, equilibrio y electroquímica.":
            "Lab equipment, molecular structures, orbitals and formulas for stoichiometry, gases, thermochemistry, kinetics, equilibrium and electrochemistry."})
P = pack
LAB, MOL = "Química: laboratorio", "Química: moléculas y átomos"
P.en.update({LAB: "Chemistry: laboratory", MOL: "Chemistry: molecules and atoms"})

# --- Laboratorio -------------------------------------------------------------------------------

@P.figure(LAB, "flask", "Matraz Erlenmeyer", "Erlenmeyer flask")
def _(g): g.line(0.4, 0.6, 0.4, 0.3, 0.1, -0.3, 0.9, -0.3, 0.6, 0.3, 0.6, 0.6); g.line(0.37, 0.6, 0.63, 0.6); g.line(0.2, -0.1, 0.8, -0.1, dashed=True)

@P.figure(LAB, "round-flask", "Matraz de bola", "Round-bottom flask")
def _(g):
    a = math.degrees(math.asin(0.09 / 0.35))
    g.arc(0.5, -0.05, 0.35, 0.35, 90 + a, 360 + 90 - a); g.line(0.41, 0.29, 0.41, 0.6); g.line(0.59, 0.29, 0.59, 0.6); g.line(0.2, -0.15, 0.8, -0.15, dashed=True)

@P.figure(LAB, "volumetric", "Matraz aforado", "Volumetric flask")
def _(g):
    g.arc(0.5, -0.15, 0.3, 0.25, 100, 440); g.line(0.45, 0.1, 0.45, 0.65); g.line(0.55, 0.1, 0.55, 0.65); g.line(0.43, 0.45, 0.57, 0.45)

@P.figure(LAB, "beaker", "Vaso de precipitados", "Beaker")
def _(g):
    g.line(0.15, 0.4, 0.2, 0.35, 0.2, -0.3, 0.8, -0.3, 0.8, 0.4); g.line(0.2, 0, 0.8, 0, dashed=True)
    for k in range(1, 4): g.line(0.2, -0.3 + k * 0.15, 0.27, -0.3 + k * 0.15)

@P.figure(LAB, "test-tube", "Tubo de ensayo", "Test tube")
def _(g): g.line(0.4, 0.5, 0.4, -0.3); g.arc(0.5, -0.3, 0.1, 0.1, 180, 360); g.line(0.6, -0.3, 0.6, 0.5); g.line(0.4, -0.1, 0.6, -0.1, dashed=True)

@P.figure(LAB, "graduated", "Probeta", "Graduated cylinder")
def _(g):
    g.line(0.4, 0.6, 0.4, -0.35); g.line(0.6, 0.6, 0.6, -0.35); g.line(0.3, -0.35, 0.7, -0.35); g.line(0.3, -0.42, 0.7, -0.42)
    for k in range(8): g.line(0.4, -0.3 + k * 0.1, 0.46 if k % 2 else 0.5, -0.3 + k * 0.1)

@P.figure(LAB, "burette", "Bureta", "Burette")
def _(g):
    g.line(0.45, 0.6, 0.45, -0.2); g.line(0.55, 0.6, 0.55, -0.2); g.line(0.45, -0.2, 0.49, -0.3, 0.49, -0.45); g.line(0.55, -0.2, 0.51, -0.3, 0.51, -0.45)
    g.rect(0.38, -0.27, 0.62, -0.23); for_ = [g.line(0.45, 0.5 - k * 0.1, 0.5, 0.5 - k * 0.1) for k in range(7)]

@P.figure(LAB, "pipette", "Pipeta", "Pipette")
def _(g): g.line(0.48, 0.6, 0.48, -0.4, 0.5, -0.5); g.line(0.52, 0.6, 0.52, -0.4, 0.5, -0.5); g.line(0.46, 0.35, 0.54, 0.35)

@P.figure(LAB, "funnel", "Embudo", "Funnel")
def _(g): g.line(0.2, 0.4, 0.46, 0.0, 0.46, -0.4); g.line(0.8, 0.4, 0.54, 0.0, 0.54, -0.4); g.ellipse(0.5, 0.4, 0.3, 0.05)

@P.figure(LAB, "sep-funnel", "Embudo de separación", "Separatory funnel")
def _(g):
    g.line(0.45, 0.6, 0.45, 0.45, 0.25, 0.1, 0.48, -0.25, 0.48, -0.5); g.line(0.55, 0.6, 0.55, 0.45, 0.75, 0.1, 0.52, -0.25, 0.52, -0.5)
    g.rect(0.42, -0.35, 0.58, -0.3); g.line(0.3, 0.05, 0.7, 0.05, dashed=True)

@P.figure(LAB, "bunsen", "Mechero Bunsen", "Bunsen burner")
def _(g):
    g.rect(0.3, -0.45, 0.7, -0.38); g.rect(0.45, -0.38, 0.55, 0.2)
    # Flama en forma de gota (punta hacia arriba).
    pts = []
    for i in range(61):
        t = 2 * math.pi * i / 60; pts += [0.5 + 0.1 * math.sin(t) * math.sin(t / 2) ** 2, 0.4 + 0.18 * math.cos(t)]
    g.line(*pts)

@P.figure(LAB, "condenser", "Refrigerante (condensador)", "Condenser")
def _(g):
    g.line(0.05, 0.05, 0.95, 0.05); g.line(0.05, -0.05, 0.95, -0.05); g.rect(0.2, -0.13, 0.8, 0.13)
    g.line(0.3, 0.13, 0.3, 0.3); g.line(0.7, -0.13, 0.7, -0.3); g.arrow(0.25, -0.4, 0.25, -0.15, 0.03); g.label(0.5, 0.2, "H₂O", 0.5)

@P.figure(LAB, "petri", "Caja de Petri", "Petri dish")
def _(g): g.ellipse(0.5, 0.05, 0.4, 0.12); g.line(0.1, 0.05, 0.1, -0.05); g.line(0.9, 0.05, 0.9, -0.05); g.arc(0.5, -0.05, 0.4, 0.12, 180, 360)

@P.figure(LAB, "stand", "Soporte universal", "Ring stand")
def _(g): g.rect(0.1, -0.45, 0.6, -0.4); g.line(0.2, -0.4, 0.2, 0.6); g.line(0.2, 0.2, 0.5, 0.2); g.ellipse(0.62, 0.2, 0.12, 0.04)

@P.figure(LAB, "thermometer-lab", "Termómetro", "Thermometer")
def _(g):
    g.line(0.47, 0.55, 0.47, -0.3); g.line(0.53, 0.55, 0.53, -0.3); g.circle(0.5, -0.36, 0.06, fill=True)
    for k in range(8): g.line(0.53, -0.25 + k * 0.1, 0.57, -0.25 + k * 0.1)

@P.figure(LAB, "mortar", "Mortero", "Mortar and pestle")
def _(g): g.arc(0.5, 0.05, 0.35, 0.35, 180, 360); g.line(0.15, 0.05, 0.85, 0.05); g.line(0.62, -0.05, 0.85, 0.4); g.line(0.66, -0.07, 0.89, 0.38)

@P.figure(LAB, "hazard", "Peligro (rombo)", "Hazard (diamond)")
def _(g): g.poly(0.5, 0.45, 0.95, 0, 0.5, -0.45, 0.05, 0); g.label(0.5, 0.05, "!", 1.6)

# --- Moléculas y átomos ----------------------------------------------------------------------------

def hexagon(g, cu, cv, r, rot=90.0):
    g.regular(cu, cv, r, 6, rot)

@P.figure(MOL, "benzene", "Anillo bencénico", "Benzene ring")
def _(g): hexagon(g, 0.5, 0, 0.5, 30); g.circle(0.5, 0, 0.3)

@P.figure(MOL, "benzene-kekule", "Benceno (Kekulé)", "Benzene (Kekulé)")
def _(g):
    hexagon(g, 0.5, 0, 0.5, 30)
    for k in (0, 2, 4):
        a1, a2 = math.radians(30 + 60 * k), math.radians(30 + 60 * (k + 1))
        f = 0.78; g.line(0.5 + 0.5 * f * math.cos(a1), 0.5 * f * math.sin(a1), 0.5 + 0.5 * f * math.cos(a2), 0.5 * f * math.sin(a2))

@P.figure(MOL, "cyclohexane", "Ciclohexano", "Cyclohexane")
def _(g): hexagon(g, 0.5, 0, 0.5, 30)

@P.figure(MOL, "cyclopentane", "Ciclopentano", "Cyclopentane")
def _(g): g.regular(0.5, 0, 0.5, 5, 90)

@P.figure(MOL, "chair", "Silla (ciclohexano)", "Chair (cyclohexane)")
def _(g): g.poly(0.0, 0.0, 0.25, 0.15, 0.55, 0.05, 0.75, 0.2, 1.0, 0.05, 0.75, -0.1, 0.45, 0.0, 0.25, -0.15)

@P.figure(MOL, "bond-single", "Enlace sencillo", "Single bond")
def _(g): g.line(0, 0, 1, 0)

@P.figure(MOL, "bond-double", "Enlace doble", "Double bond")
def _(g): g.line(0, 0.05, 1, 0.05); g.line(0, -0.05, 1, -0.05)

@P.figure(MOL, "bond-triple", "Enlace triple", "Triple bond")
def _(g): g.line(0, 0.08, 1, 0.08); g.line(0, 0, 1, 0); g.line(0, -0.08, 1, -0.08)

@P.figure(MOL, "bond-wedge", "Enlace en cuña", "Wedge bond")
def _(g): g.poly(0, 0, 1, 0.07, 1, -0.07, fill=True)

@P.figure(MOL, "bond-hash", "Enlace punteado (atrás)", "Hashed bond")
def _(g):
    for k in range(1, 9): u = k / 8; w = 0.07 * u; g.line(u, -w, u, w)

@P.figure(MOL, "zigzag-chain", "Cadena carbonada", "Carbon chain")
def _(g): g.line(*[x for k in range(7) for x in (k / 6, 0.12 if k % 2 else -0.12)])

@P.figure(MOL, "tetrahedral", "Geometría tetraédrica", "Tetrahedral geometry")
def _(g):
    g.circle(0.5, 0, 0.06); g.line(0.5, 0.06, 0.5, 0.5); g.circle(0.5, 0.55, 0.05)
    g.line(0.45, -0.03, 0.12, -0.25); g.circle(0.08, -0.28, 0.05); g.poly(0.55, -0.02, 0.88, -0.2, 0.84, -0.27, fill=True); g.circle(0.9, -0.28, 0.05)
    for k in range(1, 6): t = k / 6; x, y = 0.5 + 0.05 * t, -0.06 - 0.38 * t; g.line(x - 0.02 * t, y, x + 0.04 * t, y)
    g.circle(0.55, -0.5, 0.05)

@P.figure(MOL, "water", "Molécula de agua", "Water molecule")
def _(g):
    g.circle(0.5, 0.1, 0.16); g.label(0.5, 0.1, "O", 0.8); g.circle(0.2, -0.2, 0.1); g.label(0.2, -0.2, "H", 0.6); g.circle(0.8, -0.2, 0.1); g.label(0.8, -0.2, "H", 0.6)
    g.line(0.39, -0.02, 0.27, -0.13); g.line(0.61, -0.02, 0.73, -0.13); g.arc(0.5, 0.1, 0.28, 0.28, 220, 320, dashed=True); g.label(0.5, -0.32, "104.5°", 0.5)

@P.figure(MOL, "atom", "Átomo", "Atom")
def _(g):
    g.circle(0.5, 0, 0.05, fill=True)
    for k in range(3):
        rot = k * math.pi / 3; pts = []
        for i in range(73):
            t = 2 * math.pi * i / 72; x, y = 0.5 * math.cos(t), 0.17 * math.sin(t)
            pts += [0.5 + x * math.cos(rot) - y * math.sin(rot), x * math.sin(rot) + y * math.cos(rot)]
        g.line(*pts)

@P.figure(MOL, "bohr", "Modelo de Bohr", "Bohr model")
def _(g):
    g.circle(0.5, 0, 0.08, fill=True)
    for k, n in ((0.2, 2), (0.33, 6), (0.46, 3)):
        g.circle(0.5, 0, k)
        for j in range(n): a = 2 * math.pi * j / n + k; g.circle(0.5 + k * math.cos(a), k * math.sin(a), 0.022, fill=True)

@P.figure(MOL, "orbital-s", "Orbital s", "s orbital")
def _(g): g.circle(0.5, 0, 0.35, dashed=False); g.arrow(0.5, 0, 0.98, 0, 0.03); g.arrow(0.5, 0, 0.5, 0.5, 0.03)

@P.figure(MOL, "orbital-p", "Orbital p", "p orbital")
def _(g):
    g.polar(0.5, 0, lambda t: 0.42 * abs(math.cos(t)) ** 1.0 + 0.001)
    g.line(0.0, 0, 1.0, 0, dashed=True); g.line(0.5, -0.35, 0.5, 0.35, dashed=True)

@P.figure(MOL, "orbital-d", "Orbital d", "d orbital")
def _(g): g.polar(0.5, 0, lambda t: 0.42 * abs(math.sin(2 * t)) + 0.001); g.line(0, 0, 1, 0, dashed=True); g.line(0.5, -0.45, 0.5, 0.45, dashed=True)

@P.figure(MOL, "energy-diagram", "Diagrama de energía de reacción", "Reaction energy diagram")
def _(g):
    g.arrow(0, -0.3, 1, -0.3, 0.03); g.arrow(0, -0.3, 0, 0.5, 0.03); g.label(-0.05, 0.45, "E", 0.7)
    g.curve(lambda u: 0.05 + 0.35 * math.exp(-((u - 0.5) / 0.12) ** 2) - 0.25 * (1 / (1 + math.exp(-(u - 0.6) * 20))), 0.05, 0.95, 90)
    g.label(0.15, 0.12, "reactivos", 0.5); g.label(0.85, -0.12, "productos", 0.5); g.double_arrow(0.5, 0.06, 0.5, 0.38, 0.03); g.label(0.58, 0.22, "Eₐ", 0.6)

@P.figure(MOL, "equilibrium-arrow", "Flecha de equilibrio", "Equilibrium arrow")
def _(g): g.line(0, 0.04, 1, 0.04); g.line(1, 0.04, 0.9, 0.12); g.line(0, -0.04, 1, -0.04); g.line(0, -0.04, 0.1, -0.12)

@P.figure(MOL, "titration-curve", "Curva de titulación", "Titration curve")
def _(g):
    g.arrow(0, -0.35, 1, -0.35, 0.03); g.arrow(0, -0.35, 0, 0.5, 0.03); g.label(0.95, -0.42, "V", 0.6); g.label(-0.07, 0.45, "pH", 0.6)
    g.curve(lambda u: -0.25 + 0.6 / (1 + math.exp(-(u - 0.5) * 25)), 0.03, 0.97, 80); g.line(0.5, -0.35, 0.5, 0.05, dashed=True)

# --- Fórmulas -------------------------------------------------------------------------------------------

G = "Ciencias"
P.formulas_in(G, "Química: estequiometría y disoluciones", [
    ("Moles", r"n = \frac{m}{M}", "Moles"),
    ("Número de partículas", r"N = n \, N_{A}", "Number of particles"),
    ("Molaridad", r"M = \frac{n_{soluto}}{V_{L}}", "Molarity"),
    ("Molalidad", r"m = \frac{n_{soluto}}{kg_{disolvente}}", "Molality"),
    ("Normalidad", r"N = M \cdot \text{eq}", "Normality"),
    ("Fracción molar", r"\chi_{i} = \frac{n_{i}}{n_{total}}", "Mole fraction"),
    ("Porcentaje en masa", r"\% m/m = \frac{m_{soluto}}{m_{disolución}} \times 100", "Mass percent"),
    ("Partes por millón", r"ppm = \frac{m_{soluto} (mg)}{V (L)}", "Parts per million"),
    ("Dilución", r"C_{1} V_{1} = C_{2} V_{2}", "Dilution"),
    ("Rendimiento", r"\% R = \frac{\text{real}}{\text{teórico}} \times 100", "Yield"),
    ("Densidad", r"\rho = \frac{m}{V}", "Density"),
], "Chemistry: stoichiometry and solutions")
P.formulas_in(G, "Química: gases", [
    ("Gas ideal", r"P V = n R T", "Ideal gas"),
    ("Ley combinada", r"\frac{P_{1} V_{1}}{T_{1}} = \frac{P_{2} V_{2}}{T_{2}}", "Combined gas law"),
    ("Boyle", r"P_{1} V_{1} = P_{2} V_{2}", "Boyle"),
    ("Charles", r"\frac{V_{1}}{T_{1}} = \frac{V_{2}}{T_{2}}", "Charles"),
    ("Gay-Lussac", r"\frac{P_{1}}{T_{1}} = \frac{P_{2}}{T_{2}}", "Gay-Lussac"),
    ("Dalton", r"P_{total} = \sum_{i} P_{i}, \quad P_{i} = \chi_{i} P_{total}", "Dalton"),
    ("Van der Waals", r"\left( P + \frac{a n^{2}}{V^{2}} \right) (V - n b) = n R T", "Van der Waals"),
    ("Velocidad cuadrática media", r"v_{rms} = \sqrt{\frac{3 R T}{M}}", "Root-mean-square speed"),
    ("Graham", r"\frac{v_{1}}{v_{2}} = \sqrt{\frac{M_{2}}{M_{1}}}", "Graham"),
], "Chemistry: gases")
P.formulas_in(G, "Química: termoquímica y cinética", [
    ("Entalpía de reacción", r"\Delta H^{\circ} = \sum \Delta H_{f}^{\circ}(\text{prod}) - \sum \Delta H_{f}^{\circ}(\text{react})", "Reaction enthalpy"),
    ("Gibbs", r"\Delta G = \Delta H - T \Delta S", "Gibbs"),
    ("Gibbs y equilibrio", r"\Delta G^{\circ} = -R T \ln K", "Gibbs and equilibrium"),
    ("Calorimetría", r"q = m c \Delta T", "Calorimetry"),
    ("Ley de velocidad", r"v = k [A]^{m} [B]^{n}", "Rate law"),
    ("Primer orden", r"\ln [A] = \ln [A]_{0} - k t", "First order"),
    ("Segundo orden", r"\frac{1}{[A]} = \frac{1}{[A]_{0}} + k t", "Second order"),
    ("Vida media (1er orden)", r"t_{1/2} = \frac{\ln 2}{k}", "Half-life (1st order)"),
    ("Arrhenius", r"k = A e^{-E_{a}/RT}", "Arrhenius"),
    ("Arrhenius (dos temperaturas)", r"\ln \frac{k_{2}}{k_{1}} = \frac{E_{a}}{R} \left( \frac{1}{T_{1}} - \frac{1}{T_{2}} \right)", "Arrhenius (two temperatures)"),
], "Chemistry: thermochemistry and kinetics")
P.formulas_in(G, "Química: equilibrio, ácidos y electroquímica", [
    ("Constante de equilibrio", r"K_{c} = \frac{[C]^{c} [D]^{d}}{[A]^{a} [B]^{b}}", "Equilibrium constant"),
    ("Kp y Kc", r"K_{p} = K_{c} (R T)^{\Delta n}", "Kp and Kc"),
    ("pH", r"\text{pH} = -\log [\text{H}^{+}]", "pH"),
    ("pOH", r"\text{pH} + \text{pOH} = 14", "pOH"),
    ("Producto iónico del agua", r"K_{w} = [\text{H}^{+}][\text{OH}^{-}] = 10^{-14}", "Ion product of water"),
    ("Constante ácida", r"K_{a} = \frac{[\text{H}^{+}][\text{A}^{-}]}{[\text{HA}]}", "Acid constant"),
    ("Henderson-Hasselbalch", r"\text{pH} = \text{p}K_{a} + \log \frac{[\text{A}^{-}]}{[\text{HA}]}", "Henderson–Hasselbalch"),
    ("Titulación", r"M_{a} V_{a} = M_{b} V_{b}", "Titration"),
    ("Producto de solubilidad", r"K_{ps} = [\text{M}^{n+}]^{m} [\text{X}^{m-}]^{n}", "Solubility product"),
    ("Potencial de celda", r"E^{\circ}_{celda} = E^{\circ}_{cátodo} - E^{\circ}_{ánodo}", "Cell potential"),
    ("Nernst", r"E = E^{\circ} - \frac{RT}{nF} \ln Q", "Nernst"),
    ("Electrólisis (Faraday)", r"m = \frac{Q M}{n F} = \frac{I t M}{n F}", "Electrolysis (Faraday)"),
    ("Energía libre y potencial", r"\Delta G^{\circ} = -n F E^{\circ}", "Free energy and potential"),
], "Chemistry: equilibrium, acids and electrochemistry")
P.formulas_in(G, "Química: reacciones de ejemplo", [
    ("Combustión del metano", r"\text{CH}_{4} + 2\text{O}_{2} \to \text{CO}_{2} + 2\text{H}_{2}\text{O}", "Methane combustion"),
    ("Neutralización", r"\text{HCl} + \text{NaOH} \to \text{NaCl} + \text{H}_{2}\text{O}", "Neutralization"),
    ("Síntesis de amoniaco", r"\text{N}_{2} + 3\text{H}_{2} \rightleftharpoons 2\text{NH}_{3}", "Ammonia synthesis"),
    ("Fotosíntesis", r"6\text{CO}_{2} + 6\text{H}_{2}\text{O} \to \text{C}_{6}\text{H}_{12}\text{O}_{6} + 6\text{O}_{2}", "Photosynthesis"),
    ("Precipitación", r"\text{Ag}^{+} + \text{Cl}^{-} \to \text{AgCl} \downarrow", "Precipitation"),
    ("Óxido-reducción", r"\text{Zn} + \text{Cu}^{2+} \to \text{Zn}^{2+} + \text{Cu}", "Redox"),
], "Chemistry: sample reactions")

P.labels = [["Reactivo", "#2563eb"], ["Producto", "#16a34a"], ["Catalizador", "#7c3aed"], ["Precipitado", "#334155"],
            ["Ácido", "#dc2626"], ["Base", "#0891b2"], ["Oxidación", "#ea580c"], ["Reducción", "#4f46e5"],
            ["Exotérmica", "#b91c1c"], ["Endotérmica", "#1d4ed8"], ["Corrosivo", "#ca8a04"], ["Inflamable", "#c2410c"]]
P.en.update({"Reactivo": "Reactant", "Producto": "Product", "Catalizador": "Catalyst", "Precipitado": "Precipitate", "Ácido": "Acid", "Base": "Base",
             "Oxidación": "Oxidation", "Reducción": "Reduction", "Exotérmica": "Exothermic", "Endotérmica": "Endothermic", "Corrosivo": "Corrosive", "Inflamable": "Flammable"})
P.emoji = {"Química": "🧪 ⚗️ 🔬 🧫 🧬 🌡️ 💧 🔥 ☢️ ☣️ ⚠️ 🧯 🥼 🥽 🧤 💎"}
