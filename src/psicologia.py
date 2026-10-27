import math
from wgpack import Pack

pack = Pack("psicologia-sociales", "Psicología y ciencias sociales", "Gráficas estadísticas, modelos y esquemas, y formulario de estadística descriptiva e inferencial, psicometría y demografía.",
            "Licenciaturas", "🧠", en={"Psicología y ciencias sociales": "Psychology and social sciences",
            "Gráficas estadísticas, modelos y esquemas, y formulario de estadística descriptiva e inferencial, psicometría y demografía.":
            "Statistical graphs, models and diagrams, and formulas for descriptive and inferential statistics, psychometrics and demography."})
P = pack
EST, MOD = "Sociales: gráficas estadísticas", "Sociales: modelos y esquemas"
P.en.update({EST: "Social: statistical graphs", MOD: "Social: models and diagrams"})

N = lambda u, m=0.5, s=0.13: math.exp(-((u - m) / s) ** 2 / 2)

@P.figure(EST, "normal", "Curva normal", "Normal curve")
def _(g):
    g.line(0, -0.35, 1, -0.35); g.curve(lambda u: -0.35 + 0.7 * N(u), 0.02, 0.98, 80); g.line(0.5, -0.35, 0.5, 0.35, dashed=True)
    for k in (-1, 1): x = 0.5 + 0.13 * k; g.line(x, -0.35, x, -0.35 + 0.7 * N(x), dashed=True)
    g.label(0.5, -0.42, "μ", 0.6); g.label(0.63, -0.42, "+σ", 0.5); g.label(0.37, -0.42, "−σ", 0.5)

@P.figure(EST, "normal-areas", "Normal con porcentajes", "Normal with percentages")
def _(g):
    g.line(0, -0.35, 1, -0.35); g.curve(lambda u: -0.35 + 0.7 * N(u, 0.5, 0.12), 0.02, 0.98, 80)
    for k in (-2, -1, 0, 1, 2): x = 0.5 + 0.12 * k; g.line(x, -0.35, x, -0.35 + 0.7 * N(x, 0.5, 0.12))
    g.label(0.44, -0.1, "34%", 0.4); g.label(0.56, -0.1, "34%", 0.4); g.label(0.32, -0.28, "13.5%", 0.35); g.label(0.68, -0.28, "13.5%", 0.35)

@P.figure(EST, "skewed", "Distribución sesgada", "Skewed distribution")
def _(g): g.line(0, -0.35, 1, -0.35); g.curve(lambda u: -0.35 + 2.2 * u * math.exp(-u / 0.22) * 1.3, 0.0, 1.0, 80)

@P.figure(EST, "histogram", "Histograma", "Histogram")
def _(g):
    g.line(0, 0.45, 0, -0.4, 1, -0.4)
    for k, h in enumerate((0.1, 0.25, 0.5, 0.7, 0.55, 0.3, 0.12)): g.rect(0.05 + k * 0.13, -0.4, 0.18 + k * 0.13, -0.4 + h)

@P.figure(EST, "boxplot", "Diagrama de caja", "Box plot")
def _(g):
    g.line(0.05, 0, 0.25, 0); g.rect(0.25, -0.15, 0.7, 0.15); g.line(0.45, -0.15, 0.45, 0.15); g.line(0.7, 0, 0.95, 0)
    g.line(0.05, -0.08, 0.05, 0.08); g.line(0.95, -0.08, 0.95, 0.08); g.circle(1.02, 0, 0.015)

@P.figure(EST, "scatter", "Diagrama de dispersión", "Scatter plot")
def _(g):
    g.line(0, 0.45, 0, -0.4, 1, -0.4)
    import random; r = random.Random(7)
    for k in range(18): x = 0.08 + k * 0.05; g.circle(x, -0.32 + 0.7 * (x - 0.05) + r.uniform(-0.12, 0.12), 0.015, fill=True)
    g.line(0.05, -0.36, 0.95, 0.31, dashed=True)

@P.figure(EST, "venn2", "Diagrama de Venn (2)", "Venn diagram (2)")
def _(g): g.circle(0.38, 0, 0.3); g.circle(0.62, 0, 0.3); g.label(0.25, 0, "A", 0.7); g.label(0.75, 0, "B", 0.7)

@P.figure(EST, "venn3", "Diagrama de Venn (3)", "Venn diagram (3)")
def _(g): g.circle(0.38, 0.1, 0.27); g.circle(0.62, 0.1, 0.27); g.circle(0.5, -0.13, 0.27)

@P.figure(EST, "likert", "Escala Likert", "Likert scale")
def _(g):
    g.line(0.05, 0, 0.95, 0)
    for k in range(5): x = 0.05 + k * 0.225; g.circle(x, 0, 0.04); g.label(x, -0.12, str(k + 1), 0.5)

@P.figure(EST, "pop-pyramid", "Pirámide de población", "Population pyramid")
def _(g):
    g.line(0.5, -0.4, 0.5, 0.45)
    for k, w in enumerate((0.38, 0.36, 0.33, 0.29, 0.24, 0.18, 0.11, 0.05)):
        y = -0.4 + k * 0.1; g.rect(0.5 - w, y, 0.5, y + 0.09); g.rect(0.5, y, 0.5 + w * 1.03, y + 0.09)
    g.label(0.2, 0.42, "H", 0.6); g.label(0.8, 0.42, "M", 0.6)

# --- Modelos y esquemas --------------------------------------------------------------------------------

@P.figure(MOD, "maslow", "Pirámide de Maslow", "Maslow's pyramid")
def _(g):
    g.poly(0.05, -0.42, 0.95, -0.42, 0.5, 0.45)
    names = ["Fisiológicas", "Seguridad", "Afiliación", "Reconocimiento", "Autorrealización"]
    for k in range(1, 5): v = -0.42 + k * 0.174; w = 0.45 * (1 - k * 0.174 / 0.87); g.line(0.5 - w, v, 0.5 + w, v)
    for k, n in enumerate(names): g.label(0.5, -0.42 + (k + 0.5) * 0.174, n, 0.32)

@P.figure(MOD, "concept-map", "Mapa conceptual", "Concept map")
def _(g):
    def box(x, y): g.rect(x - 0.13, y - 0.07, x + 0.13, y + 0.07)
    box(0.5, 0.33)
    for x in (0.18, 0.5, 0.82): box(x, -0.2); g.arrow(0.5, 0.26, x, -0.13, 0.03)

@P.figure(MOD, "mind-map", "Mapa mental", "Mind map")
def _(g):
    g.ellipse(0.5, 0, 0.16, 0.1)
    for k in range(6):
        a = k * math.pi / 3 + 0.3; x, y = 0.5 + 0.42 * math.cos(a), 0.36 * math.sin(a)
        g.line(0.5 + 0.16 * math.cos(a), 0.1 * math.sin(a), x - 0.09 * math.cos(a), y - 0.05 * math.sin(a))
        g.ellipse(x, y, 0.09, 0.05)

@P.figure(MOD, "process-cycle", "Ciclo de proceso", "Process cycle")
def _(g):
    for k in range(5):
        a = math.radians(90 - k * 72); g.circle(0.5 + 0.35 * math.cos(a), 0.35 * math.sin(a), 0.08)
        b1, b2 = math.radians(90 - k * 72 - 16), math.radians(90 - (k + 1) * 72 + 16)
        g.arc(0.5, 0, 0.35, 0.35, 90 - k * 72 - 16, 90 - (k + 1) * 72 + 16)
        g.head(0.5 + 0.35 * math.cos(b2 + 0.1), 0.35 * math.sin(b2 + 0.1), 0.5 + 0.35 * math.cos(b2), 0.35 * math.sin(b2), 0.04)

@P.figure(MOD, "communication", "Modelo de comunicación", "Communication model")
def _(g):
    g.rect(0, -0.1, 0.25, 0.1); g.label(0.125, 0, "emisor", 0.4); g.rect(0.75, -0.1, 1.0, 0.1); g.label(0.875, 0, "receptor", 0.4)
    g.arrow(0.25, 0, 0.75, 0, 0.04); g.label(0.5, 0.07, "mensaje", 0.4); g.curve(lambda u: 0.03 * math.sin(u * 60), 0.42, 0.58, 30)
    g.arrow(0.875, -0.1, 0.875, -0.25, 0.0); g.line(0.875, -0.25, 0.125, -0.25); g.arrow(0.125, -0.25, 0.125, -0.1, 0.03); g.label(0.5, -0.31, "retroalimentación", 0.4)

@P.figure(MOD, "sociogram", "Sociograma", "Sociogram")
def _(g):
    pts = [(0.5, 0.3), (0.15, 0.1), (0.85, 0.1), (0.3, -0.3), (0.7, -0.3)]
    for a, b in ((1, 0), (2, 0), (3, 0), (4, 2), (3, 1), (0, 2)):
        (x1, y1), (x2, y2) = pts[a], pts[b]; d = math.hypot(x2 - x1, y2 - y1)
        g.arrow(x1 + (x2 - x1) / d * 0.06, y1 + (y2 - y1) / d * 0.06, x2 - (x2 - x1) / d * 0.06, y2 - (y2 - y1) / d * 0.06, 0.03)
    for x, y in pts: g.circle(x, y, 0.06)

@P.figure(MOD, "brain", "Cerebro (lóbulos)", "Brain (lobes)")
def _(g):
    g.polar(0.5, 0.05, lambda t: (0.38 if math.sin(t) > -0.3 else 0.3) * (1 + 0.04 * math.sin(9 * t)))
    g.line(0.5, 0.42, 0.45, 0.1, 0.3, -0.15); g.line(0.45, 0.1, 0.75, -0.05); g.line(0.62, -0.25, 0.7, -0.4)
    g.label(0.3, 0.2, "frontal", 0.35); g.label(0.65, 0.22, "parietal", 0.35); g.label(0.82, -0.12, "occipital", 0.35); g.label(0.45, -0.15, "temporal", 0.35)

@P.figure(MOD, "timeline-hist", "Línea del tiempo histórica", "Historical timeline")
def _(g):
    g.arrow(0, 0, 1, 0, 0.03)
    for k in range(6):
        u = 0.08 + k * 0.17; up = k % 2 == 0; g.line(u, 0, u, 0.15 if up else -0.15); g.circle(u, 0, 0.015, fill=True)
        g.rect(u - 0.07, (0.15 if up else -0.25), u + 0.07, (0.25 if up else -0.15))

# --- Fórmulas ---------------------------------------------------------------------------------------------

G = "Licenciaturas"
P.formulas_in(G, "Estadística descriptiva", [
    ("Media", r"\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_{i}", "Mean"),
    ("Media ponderada", r"\bar{x}_{w} = \frac{\sum w_{i} x_{i}}{\sum w_{i}}", "Weighted mean"),
    ("Mediana (posición)", r"Me = x_{\left( \frac{n + 1}{2} \right)}", "Median (position)"),
    ("Varianza muestral", r"s^{2} = \frac{1}{n - 1} \sum_{i=1}^{n} (x_{i} - \bar{x})^{2}", "Sample variance"),
    ("Desviación estándar", r"s = \sqrt{s^{2}}", "Standard deviation"),
    ("Coeficiente de variación", r"CV = \frac{s}{\bar{x}} \times 100", "Coefficient of variation"),
    ("Puntuación z", r"z = \frac{x - \mu}{\sigma}", "z-score"),
    ("Puntuación T", r"T = 50 + 10 z", "T-score"),
    ("Rango intercuartil", r"RIC = Q_{3} - Q_{1}", "Interquartile range"),
    ("Asimetría", r"g_{1} = \frac{\frac{1}{n} \sum (x_{i} - \bar{x})^{3}}{s^{3}}", "Skewness"),
], "Descriptive statistics")
P.formulas_in(G, "Estadística inferencial", [
    ("Error estándar", r"SE = \frac{s}{\sqrt{n}}", "Standard error"),
    ("Intervalo de confianza", r"\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}", "Confidence interval"),
    ("Prueba t (una muestra)", r"t = \frac{\bar{x} - \mu_{0}}{s / \sqrt{n}}", "One-sample t-test"),
    ("Prueba t (independientes)", r"t = \frac{\bar{x}_{1} - \bar{x}_{2}}{s_{p} \sqrt{\frac{1}{n_{1}} + \frac{1}{n_{2}}}}", "Independent t-test"),
    ("Prueba z de proporciones", r"z = \frac{\hat{p} - p_{0}}{\sqrt{p_{0}(1 - p_{0})/n}}", "Proportion z-test"),
    ("Ji cuadrada", r"\chi^{2} = \sum \frac{(O_{i} - E_{i})^{2}}{E_{i}}", "Chi-square"),
    ("ANOVA", r"F = \frac{CM_{entre}}{CM_{dentro}}", "ANOVA"),
    ("Correlación de Pearson", r"r = \frac{\sum (x_{i} - \bar{x})(y_{i} - \bar{y})}{\sqrt{\sum (x_{i} - \bar{x})^{2} \sum (y_{i} - \bar{y})^{2}}}", "Pearson correlation"),
    ("Spearman", r"\rho = 1 - \frac{6 \sum d_{i}^{2}}{n(n^{2} - 1)}", "Spearman"),
    ("Regresión lineal", r"\hat{y} = \beta_{0} + \beta_{1} x", "Linear regression"),
    ("Pendiente de regresión", r"\beta_{1} = r \frac{s_{y}}{s_{x}}", "Regression slope"),
    ("Coeficiente de determinación", r"R^{2} = 1 - \frac{SC_{res}}{SC_{tot}}", "Coefficient of determination"),
    ("Tamaño del efecto (d)", r"d = \frac{\bar{x}_{1} - \bar{x}_{2}}{s_{p}}", "Effect size (d)"),
    ("Tamaño de muestra", r"n = \frac{Z^{2} p q}{e^{2}}", "Sample size"),
], "Inferential statistics")
P.formulas_in(G, "Psicometría y demografía", [
    ("Alfa de Cronbach", r"\alpha = \frac{k}{k - 1} \left( 1 - \frac{\sum s_{i}^{2}}{s_{T}^{2}} \right)", "Cronbach's alpha"),
    ("Spearman-Brown", r"r_{n} = \frac{n r}{1 + (n - 1) r}", "Spearman–Brown"),
    ("Error estándar de medida", r"EEM = s \sqrt{1 - r_{xx}}", "Standard error of measurement"),
    ("Índice de dificultad", r"p = \frac{A}{N}", "Difficulty index"),
    ("Índice de discriminación", r"D = p_{sup} - p_{inf}", "Discrimination index"),
    ("Cociente intelectual", r"CI = 100 + 15 z", "IQ score"),
    ("Tasa bruta de natalidad", r"TBN = \frac{\text{nacimientos}}{\text{población}} \times 1000", "Crude birth rate"),
    ("Tasa de crecimiento", r"r = \frac{\ln(P_{t} / P_{0})}{t}", "Growth rate"),
    ("Índice de Gini", r"G = 1 - \sum_{k} (X_{k} - X_{k-1})(Y_{k} + Y_{k-1})", "Gini index"),
    ("Razón de dependencia", r"RD = \frac{P_{0-14} + P_{65+}}{P_{15-64}} \times 100", "Dependency ratio"),
], "Psychometrics and demography")

P.labels = [["Hipótesis", "#2563eb"], ["Variable", "#7c3aed"], ["Muestra", "#0891b2"], ["Hallazgo", "#16a34a"],
            ["Autor", "#334155"], ["Cita", "#ca8a04"], ["Teoría", "#be185d"], ["Conclusión", "#ea580c"]]
P.en.update({"Hipótesis": "Hypothesis", "Muestra": "Sample", "Hallazgo": "Finding", "Autor": "Author", "Cita": "Quote", "Teoría": "Theory", "Conclusión": "Conclusion"})
P.emoji = {"Sociales": "🧠 💭 💬 🗣️ 👥 👪 🤝 🏫 📚 📖 🗳️ 🌍 🏛️ 📜 ⚖️ ❤️ 😊 😟"}
