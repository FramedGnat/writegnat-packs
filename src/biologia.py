import math
from wgpack import Pack

pack = Pack("biologia-salud", "Biología y salud", "Células, ADN, órganos y sistemas, microbiología y formulario de genética, ecología, fisiología, farmacología y epidemiología.",
            "Ciencias", "🧬", en={"Biología y salud": "Biology and health",
            "Células, ADN, órganos y sistemas, microbiología y formulario de genética, ecología, fisiología, farmacología y epidemiología.":
            "Cells, DNA, organs and systems, microbiology and formulas for genetics, ecology, physiology, pharmacology and epidemiology."})
P = pack
CEL, ORG = "Biología: células y moléculas", "Biología: organismos y anatomía"
P.en.update({CEL: "Biology: cells and molecules", ORG: "Biology: organisms and anatomy"})

@P.figure(CEL, "cell-animal", "Célula animal", "Animal cell")
def _(g):
    g.polar(0.5, 0, lambda t: 0.45 + 0.03 * math.sin(3 * t)); g.circle(0.55, 0.05, 0.13); g.circle(0.57, 0.07, 0.04, fill=True)
    g.ellipse(0.27, -0.12, 0.08, 0.04); g.ellipse(0.75, -0.2, 0.07, 0.035); g.ellipse(0.3, 0.2, 0.05, 0.03)
    g.label(0.55, -0.12, "núcleo", 0.45)

@P.figure(CEL, "cell-plant", "Célula vegetal", "Plant cell")
def _(g):
    g.rect(0.05, -0.35, 0.95, 0.35); g.rect(0.09, -0.31, 0.91, 0.31); g.rect(0.35, -0.22, 0.75, 0.18)
    g.circle(0.2, 0.15, 0.08); g.circle(0.21, 0.16, 0.03, fill=True)
    for x, y in ((0.2, -0.18), (0.83, 0.2), (0.85, -0.18)): g.ellipse(x, y, 0.06, 0.03)
    g.label(0.55, -0.02, "vacuola", 0.45)

@P.figure(CEL, "bacteria", "Bacteria", "Bacterium")
def _(g):
    g.arc(0.25, 0, 0.15, 0.15, 90, 270); g.line(0.25, -0.15, 0.75, -0.15); g.arc(0.75, 0, 0.15, 0.15, -90, 90); g.line(0.75, 0.15, 0.25, 0.15)
    g.curve(lambda u: 0.05 * math.sin(u * 40), 0.9, 1.0, 20)
    g.curve(lambda u: 0.04 * math.sin((u - 0.35) * 30), 0.35, 0.65, 30)

@P.figure(CEL, "virus", "Virus", "Virus")
def _(g):
    g.regular(0.5, 0, 0.25, 6, 0); g.circle(0.5, 0, 0.1, fill=False)
    for k in range(12):
        a = 2 * math.pi * k / 12; g.line(0.5 + 0.25 * math.cos(a), 0.25 * math.sin(a), 0.5 + 0.38 * math.cos(a), 0.38 * math.sin(a))
        g.circle(0.5 + 0.41 * math.cos(a), 0.41 * math.sin(a), 0.025, fill=True)

@P.figure(CEL, "mitochondrion", "Mitocondria", "Mitochondrion")
def _(g):
    g.ellipse(0.5, 0, 0.45, 0.2)
    g.line(*[x for k in range(13) for x in (0.12 + k * 0.065, 0.12 if k % 2 else -0.12)])

@P.figure(CEL, "chloroplast", "Cloroplasto", "Chloroplast")
def _(g):
    g.ellipse(0.5, 0, 0.45, 0.2)
    for x in (0.25, 0.42, 0.59, 0.76):
        for k in range(3): g.ellipse(x, -0.06 + k * 0.06, 0.06, 0.025)

@P.figure(CEL, "dna", "ADN (doble hélice)", "DNA (double helix)")
def _(g):
    g.curve(lambda u: 0.2 * math.sin(u * 4 * math.pi), 0, 1, 120); g.curve(lambda u: -0.2 * math.sin(u * 4 * math.pi), 0, 1, 120)
    for k in range(1, 16):
        u = k / 16; y = 0.2 * math.sin(u * 4 * math.pi)
        if abs(y) > 0.03: g.line(u, y, u, -y)

@P.figure(CEL, "chromosome", "Cromosoma", "Chromosome")
def _(g):
    for s in (-1, 1):
        g.ellipse(0.5 + s * 0.08, 0.22, 0.06, 0.22); g.ellipse(0.5 + s * 0.08, -0.28, 0.06, 0.18)
    g.circle(0.5, -0.04, 0.04, fill=True)

@P.figure(CEL, "membrane", "Membrana (bicapa lipídica)", "Membrane (lipid bilayer)")
def _(g):
    for k in range(10):
        u = 0.05 + k * 0.1
        g.circle(u, 0.25, 0.04, fill=True); g.line(u - 0.015, 0.21, u - 0.015, 0.03); g.line(u + 0.015, 0.21, u + 0.015, 0.03)
        g.circle(u, -0.25, 0.04, fill=True); g.line(u - 0.015, -0.21, u - 0.015, -0.03); g.line(u + 0.015, -0.21, u + 0.015, -0.03)

@P.figure(CEL, "mitosis", "Mitosis (esquema)", "Mitosis (diagram)")
def _(g):
    g.circle(0.15, 0, 0.13); g.circle(0.15, 0, 0.05, fill=True); g.arrow(0.3, 0, 0.45, 0, 0.03)
    g.ellipse(0.62, 0, 0.14, 0.11); g.line(0.62, 0.11, 0.62, -0.11, dashed=True); g.arrow(0.78, 0, 0.86, 0, 0.03)
    g.circle(0.94, 0.12, 0.07); g.circle(0.94, -0.12, 0.07)

@P.figure(CEL, "enzyme", "Enzima y sustrato", "Enzyme and substrate")
def _(g):
    g.line(0.1, -0.3, 0.1, 0.2, 0.35, 0.2, 0.35, 0.05, 0.5, 0.05, 0.5, 0.2, 0.75, 0.2, 0.75, -0.3, 0.1, -0.3)
    g.rect(0.36, 0.06, 0.49, 0.32); g.arrow(0.43, 0.55, 0.43, 0.35, 0.03)

@P.figure(CEL, "punnett", "Cuadro de Punnett", "Punnett square")
def _(g):
    g.rect(0.2, -0.4, 1.0, 0.4); g.line(0.6, -0.4, 0.6, 0.4); g.line(0.2, 0, 1.0, 0)
    g.label(0.4, 0.5, "A", 0.7); g.label(0.8, 0.5, "a", 0.7); g.label(0.1, 0.2, "A", 0.7); g.label(0.1, -0.2, "a", 0.7)
    g.label(0.4, 0.2, "AA", 0.7); g.label(0.8, 0.2, "Aa", 0.7); g.label(0.4, -0.2, "Aa", 0.7); g.label(0.8, -0.2, "aa", 0.7)

# --- Organismos y anatomía ---------------------------------------------------------------------------

@P.figure(ORG, "neuron", "Neurona", "Neuron")
def _(g):
    g.circle(0.15, 0, 0.08); g.circle(0.15, 0, 0.03, fill=True)
    for a in (100, 140, 200, 240, 160):
        r = math.radians(a); g.line(0.15 + 0.08 * math.cos(r), 0.08 * math.sin(r), 0.15 + 0.2 * math.cos(r), 0.2 * math.sin(r))
    g.line(0.23, 0, 0.85, 0)
    for k in range(4): g.rect(0.3 + k * 0.13, -0.03, 0.4 + k * 0.13, 0.03)
    for a in (-30, 0, 30): r = math.radians(a); g.line(0.85, 0, 0.85 + 0.12 * math.cos(r), 0.12 * math.sin(r)); g.circle(0.85 + 0.13 * math.cos(r), 0.13 * math.sin(r), 0.015, fill=True)

@P.figure(ORG, "heart", "Corazón (esquema)", "Heart (diagram)")
def _(g):
    pts = []
    for i in range(65):
        t = 2 * math.pi * i / 64
        pts += [0.5 + 0.028 * 16 * math.sin(t) ** 3, 0.028 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))]
    g.line(*pts); g.line(0.5, 0.25, 0.5, -0.3, dashed=True); g.line(0.3, 0.05, 0.7, 0.05, dashed=True)
    g.label(0.37, 0.15, "AD", 0.45); g.label(0.63, 0.15, "AI", 0.45); g.label(0.4, -0.1, "VD", 0.45); g.label(0.6, -0.1, "VI", 0.45)

@P.figure(ORG, "leaf", "Hoja", "Leaf")
def _(g):
    g.curve(lambda u: 0.28 * math.sin(math.pi * u) ** 0.8, 0, 1, 50); g.curve(lambda u: -0.28 * math.sin(math.pi * u) ** 0.8, 0, 1, 50)
    g.line(-0.1, 0, 1, 0)
    for k in range(1, 6): u = k / 6; h = 0.25 * math.sin(math.pi * u) ** 0.8; g.line(u, 0, u + 0.1, h * 0.8); g.line(u, 0, u + 0.1, -h * 0.8)

@P.figure(ORG, "flower", "Flor", "Flower")
def _(g):
    for k in range(6): a = k * math.pi / 3; g.ellipse(0.5 + 0.15 * math.cos(a), 0.15 + 0.15 * math.sin(a), 0.09, 0.09)
    g.circle(0.5, 0.15, 0.07, fill=True); g.line(0.5, 0.0, 0.5, -0.5); g.ellipse(0.62, -0.3, 0.1, 0.04)

@P.figure(ORG, "food-chain", "Cadena alimenticia", "Food chain")
def _(g):
    for k, t in enumerate(("Productor", "Herbívoro", "Carnívoro")):
        g.rect(0.0 + k * 0.38, -0.12, 0.26 + k * 0.38, 0.12); g.label(0.13 + k * 0.38, 0, t, 0.4)
        if k < 2: g.arrow(0.27 + k * 0.38, 0, 0.37 + k * 0.38, 0, 0.03)

@P.figure(ORG, "trophic-pyramid", "Pirámide trófica", "Trophic pyramid")
def _(g):
    g.poly(0, -0.4, 1, -0.4, 0.5, 0.45); g.line(0.18, -0.12, 0.82, -0.12); g.line(0.33, 0.14, 0.67, 0.14)
    g.label(0.5, -0.27, "productores", 0.45); g.label(0.5, 0.0, "consumidores 1°", 0.4); g.label(0.5, 0.24, "2°", 0.45)

@P.figure(ORG, "ecg", "Electrocardiograma", "ECG")
def _(g):
    pts = []
    for i in range(201):
        u = i / 200; x = (u * 2) % 1
        y = 0.05 * math.exp(-((x - 0.2) / 0.04) ** 2) - 0.06 * math.exp(-((x - 0.38) / 0.01) ** 2) + 0.4 * math.exp(-((x - 0.42) / 0.012) ** 2) - 0.1 * math.exp(-((x - 0.46) / 0.012) ** 2) + 0.1 * math.exp(-((x - 0.7) / 0.06) ** 2)
        pts += [u, y]
    g.line(*pts)

@P.figure(ORG, "lungs", "Pulmones (esquema)", "Lungs (diagram)")
def _(g):
    g.line(0.5, 0.5, 0.5, 0.15); g.line(0.5, 0.15, 0.38, 0.05); g.line(0.5, 0.15, 0.62, 0.05)
    g.polar(0.27, -0.12, lambda t: 0.2 + 0.06 * math.cos(t)); g.polar(0.73, -0.12, lambda t: 0.2 - 0.06 * math.cos(t))

@P.figure(ORG, "eye", "Ojo (esquema)", "Eye (diagram)")
def _(g):
    g.circle(0.55, 0, 0.35); g.arc(0.2, 0, 0.12, 0.2, -80, 80); g.ellipse(0.3, 0, 0.05, 0.12)
    g.line(0.0, 0.05, 0.3, 0.05, 0.9, -0.05); g.line(0.0, -0.05, 0.3, -0.05, 0.9, 0.05); g.label(0.88, 0.15, "retina", 0.45)

@P.figure(ORG, "syringe", "Jeringa", "Syringe")
def _(g):
    g.rect(0.2, -0.08, 0.7, 0.08); g.line(0.7, 0, 0.95, 0); g.rect(0.05, -0.03, 0.2, 0.03); g.line(0.05, -0.1, 0.05, 0.1)
    for k in range(1, 6): g.line(0.2 + k * 0.08, 0.08, 0.2 + k * 0.08, 0.03)

@P.figure(ORG, "pill", "Cápsula", "Capsule")
def _(g): g.arc(0.3, 0, 0.15, 0.15, 90, 270); g.line(0.3, 0.15, 0.7, 0.15); g.line(0.3, -0.15, 0.7, -0.15); g.arc(0.7, 0, 0.15, 0.15, -90, 90); g.line(0.5, 0.15, 0.5, -0.15)

# --- Fórmulas ---------------------------------------------------------------------------------------------

G = "Ciencias"
P.formulas_in(G, "Biología: genética y ecología", [
    ("Hardy-Weinberg", r"p^{2} + 2pq + q^{2} = 1, \quad p + q = 1", "Hardy–Weinberg"),
    ("Proporción mendeliana", r"3:1 \quad (F_{2}, \text{ monohíbrido})", "Mendelian ratio"),
    ("Dihíbrido", r"9:3:3:1", "Dihybrid"),
    ("Crecimiento exponencial", r"N(t) = N_{0} e^{r t}", "Exponential growth"),
    ("Crecimiento logístico", r"\frac{dN}{dt} = r N \left( 1 - \frac{N}{K} \right)", "Logistic growth"),
    ("Lotka-Volterra", r"\frac{dx}{dt} = \alpha x - \beta x y, \quad \frac{dy}{dt} = \delta x y - \gamma y", "Lotka–Volterra"),
    ("Tiempo de duplicación", r"t_{d} = \frac{\ln 2}{r}", "Doubling time"),
    ("Diversidad de Shannon", r"H' = -\sum_{i} p_{i} \ln p_{i}", "Shannon diversity"),
    ("Índice de Simpson", r"D = 1 - \sum_{i} p_{i}^{2}", "Simpson index"),
    ("Michaelis-Menten", r"v = \frac{V_{max} [S]}{K_{m} + [S]}", "Michaelis–Menten"),
    ("Lineweaver-Burk", r"\frac{1}{v} = \frac{K_{m}}{V_{max}} \frac{1}{[S]} + \frac{1}{V_{max}}", "Lineweaver–Burk"),
    ("Respiración celular", r"\text{C}_{6}\text{H}_{12}\text{O}_{6} + 6\text{O}_{2} \to 6\text{CO}_{2} + 6\text{H}_{2}\text{O} + \text{ATP}", "Cellular respiration"),
    ("Fotosíntesis", r"6\text{CO}_{2} + 6\text{H}_{2}\text{O} \xrightarrow{luz} \text{C}_{6}\text{H}_{12}\text{O}_{6} + 6\text{O}_{2}", "Photosynthesis"),
    ("Potencial de Nernst (membrana)", r"E = \frac{RT}{zF} \ln \frac{[\text{ion}]_{ext}}{[\text{ion}]_{int}}", "Nernst potential (membrane)"),
], "Biology: genetics and ecology")
P.formulas_in(G, "Ciencias de la salud", [
    ("Índice de masa corporal", r"IMC = \frac{\text{peso (kg)}}{\text{talla (m)}^{2}}", "Body mass index"),
    ("Superficie corporal (Mosteller)", r"SC = \sqrt{\frac{\text{talla (cm)} \times \text{peso (kg)}}{3600}}", "Body surface area (Mosteller)"),
    ("Gasto cardiaco", r"GC = FC \times VS", "Cardiac output"),
    ("Presión arterial media", r"PAM = PAD + \frac{PAS - PAD}{3}", "Mean arterial pressure"),
    ("Frecuencia cardiaca máxima", r"FC_{max} = 220 - \text{edad}", "Maximum heart rate"),
    ("Depuración de creatinina", r"CrCl = \frac{(140 - \text{edad}) \times \text{peso}}{72 \times Cr_{s}}", "Creatinine clearance"),
    ("Agua corporal total", r"ACT = 0.6 \times \text{peso (kg)}", "Total body water"),
    ("Dosis por peso", r"D = \text{dosis (mg/kg)} \times \text{peso (kg)}", "Weight-based dose"),
    ("Velocidad de goteo", r"\text{gotas/min} = \frac{V (mL) \times 20}{t (min)}", "Drip rate"),
    ("Concentración de un fármaco", r"C(t) = C_{0} e^{-k t}", "Drug concentration"),
    ("Vida media de un fármaco", r"t_{1/2} = \frac{0.693 \, V_{d}}{Cl}", "Drug half-life"),
    ("Regla de Clark", r"D_{niño} = \frac{\text{peso (lb)}}{150} \times D_{adulto}", "Clark's rule"),
], "Health sciences")
P.formulas_in(G, "Epidemiología", [
    ("Prevalencia", r"P = \frac{\text{casos existentes}}{\text{población}}", "Prevalence"),
    ("Incidencia", r"I = \frac{\text{casos nuevos}}{\text{población en riesgo} \times t}", "Incidence"),
    ("Sensibilidad", r"S = \frac{VP}{VP + FN}", "Sensitivity"),
    ("Especificidad", r"E = \frac{VN}{VN + FP}", "Specificity"),
    ("Valor predictivo positivo", r"VPP = \frac{VP}{VP + FP}", "Positive predictive value"),
    ("Riesgo relativo", r"RR = \frac{a/(a + b)}{c/(c + d)}", "Relative risk"),
    ("Razón de momios", r"OR = \frac{a d}{b c}", "Odds ratio"),
    ("Número básico de reproducción", r"R_{0} = \beta \cdot \kappa \cdot D", "Basic reproduction number"),
    ("Modelo SIR", r"\frac{dS}{dt} = -\beta S I, \; \frac{dI}{dt} = \beta S I - \gamma I, \; \frac{dR}{dt} = \gamma I", "SIR model"),
    ("Número necesario a tratar", r"NNT = \frac{1}{RAR}", "Number needed to treat"),
], "Epidemiology")

P.labels = [["Síntoma", "#dc2626"], ["Diagnóstico", "#2563eb"], ["Tratamiento", "#16a34a"], ["Dosis", "#7c3aed"],
            ["Contraindicación", "#b91c1c"], ["Signo vital", "#0891b2"], ["Especie", "#15803d"], ["Hipótesis", "#ca8a04"]]
P.en.update({"Síntoma": "Symptom", "Diagnóstico": "Diagnosis", "Tratamiento": "Treatment", "Dosis": "Dose", "Contraindicación": "Contraindication",
             "Signo vital": "Vital sign", "Especie": "Species", "Hipótesis": "Hypothesis"})
P.emoji = {"Biología y salud": "🧬 🦠 🧫 🔬 🫀 🫁 🧠 🦴 🦷 👁️ 🩺 💉 💊 🩸 🩹 🌱 🌿 🍃 🌳 🐛 🐝 🐟 🐸 🦋"}
