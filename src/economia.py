import math
from wgpack import Pack

pack = Pack("economia-finanzas", "Economía, finanzas y administración", "Gráficas económicas, diagramas de negocio y formulario de micro y macroeconomía, finanzas, contabilidad, mercadotecnia y estadística aplicada.",
            "Licenciaturas", "📈", en={"Economía, finanzas y administración": "Economics, finance and business",
            "Gráficas económicas, diagramas de negocio y formulario de micro y macroeconomía, finanzas, contabilidad, mercadotecnia y estadística aplicada.":
            "Economic graphs, business diagrams and formulas for micro and macroeconomics, finance, accounting, marketing and applied statistics."})
P = pack
GRA, NEG = "Economía: gráficas", "Negocios: diagramas"
P.en.update({GRA: "Economics: graphs", NEG: "Business: diagrams"})


def axes(g, xl="Q", yl="P"):
    g.arrow(0, -0.4, 1, -0.4, 0.03); g.arrow(0, -0.4, 0, 0.5, 0.03); g.label(0.97, -0.47, xl, 0.6); g.label(-0.07, 0.46, yl, 0.6)

@P.figure(GRA, "supply-demand", "Oferta y demanda", "Supply and demand")
def _(g):
    axes(g); g.line(0.1, 0.4, 0.9, -0.3); g.line(0.1, -0.3, 0.9, 0.4); g.label(0.92, -0.24, "D", 0.6); g.label(0.93, 0.45, "O", 0.6)
    g.line(0.5, 0.05, 0.5, -0.4, dashed=True); g.line(0, 0.05, 0.5, 0.05, dashed=True); g.circle(0.5, 0.05, 0.015, fill=True)
    g.label(0.5, -0.47, "Q*", 0.5); g.label(-0.06, 0.05, "P*", 0.5)

@P.figure(GRA, "demand-shift", "Desplazamiento de la demanda", "Demand shift")
def _(g):
    axes(g); g.line(0.1, 0.3, 0.7, -0.3); g.line(0.3, 0.4, 0.9, -0.2, dashed=True); g.arrow(0.45, 0.0, 0.6, 0.08, 0.03)
    g.label(0.72, -0.34, "D₁", 0.5); g.label(0.92, -0.24, "D₂", 0.5)

@P.figure(GRA, "cost-curves", "Curvas de costos", "Cost curves")
def _(g):
    axes(g, "Q", "$")
    g.curve(lambda u: -0.35 + 1.4 * (u - 0.4) ** 2 + 0.02, 0.1, 0.85); g.label(0.88, 0.17, "CMg", 0.45)
    g.curve(lambda u: -0.28 + 0.9 * (u - 0.5) ** 2 + 0.02, 0.12, 0.92); g.label(0.95, -0.05, "CTMe", 0.45)
    g.curve(lambda u: -0.32 + 0.9 * (u - 0.45) ** 2, 0.1, 0.85, dashed=True); g.label(0.86, -0.1, "CVMe", 0.45)

@P.figure(GRA, "break-even", "Punto de equilibrio", "Break-even point")
def _(g):
    axes(g, "Q", "$"); g.line(0, -0.4, 0.9, 0.45); g.line(0, -0.1, 0.9, 0.3); g.line(0, -0.1, 0.9, -0.1, dashed=True)
    g.circle(0.48, 0.055, 0.015, fill=True); g.label(0.93, 0.48, "IT", 0.5); g.label(0.93, 0.33, "CT", 0.5); g.label(0.94, -0.13, "CF", 0.5)

@P.figure(GRA, "ppf", "Frontera de posibilidades", "Production possibility frontier")
def _(g):
    axes(g, "X", "Y"); g.arc(0, -0.4, 0.8, 0.8, 0, 90); g.circle(0.35, -0.05, 0.015, fill=True); g.circle(0.6, 0.25, 0.015, fill=True)
    g.label(0.4, -0.08, "A", 0.5); g.label(0.65, 0.3, "B", 0.5)

@P.figure(GRA, "indifference", "Curvas de indiferencia", "Indifference curves")
def _(g):
    axes(g, "X", "Y")
    for k in (0.04, 0.09, 0.16): g.curve(lambda u, k=k: -0.4 + k / u, 0.08 + k * 0.3, 0.95)
    g.line(0, 0.25, 0.75, -0.4)

@P.figure(GRA, "lorenz", "Curva de Lorenz", "Lorenz curve")
def _(g):
    g.rect(0.1, -0.4, 0.9, 0.4); g.line(0.1, -0.4, 0.9, 0.4, dashed=True); g.curve(lambda u: -0.4 + 0.8 * ((u - 0.1) / 0.8) ** 2.4, 0.1, 0.9)
    g.label(0.6, 0.1, "igualdad", 0.4)

@P.figure(GRA, "laffer", "Curva de Laffer", "Laffer curve")
def _(g): axes(g, "t", "R"); g.curve(lambda u: -0.4 + 3.2 * u * (1 - u) * 0.8 / 0.8 * 0.85 if u <= 1 else 0, 0.0, 1.0)

@P.figure(GRA, "business-cycle", "Ciclo económico", "Business cycle")
def _(g):
    axes(g, "t", "PIB"); g.line(0, -0.25, 1, 0.25, dashed=True)
    g.curve(lambda u: -0.25 + 0.5 * u + 0.12 * math.sin(u * 4 * math.pi), 0.02, 0.98)

@P.figure(GRA, "bar-chart", "Gráfica de barras", "Bar chart")
def _(g):
    g.line(0, 0.5, 0, -0.4, 1, -0.4)
    for k, h in enumerate((0.4, 0.65, 0.3, 0.8, 0.55)): g.rect(0.08 + k * 0.18, -0.4, 0.2 + k * 0.18, -0.4 + h)

@P.figure(GRA, "pie-chart", "Gráfica de pastel", "Pie chart")
def _(g):
    g.circle(0.5, 0, 0.4)
    for a in (90, 200, 290, 350): r = math.radians(a); g.line(0.5, 0, 0.5 + 0.4 * math.cos(r), 0.4 * math.sin(r))

@P.figure(GRA, "line-chart", "Gráfica de líneas", "Line chart")
def _(g):
    g.line(0, 0.5, 0, -0.4, 1, -0.4); ys = [-0.3, -0.1, -0.15, 0.1, 0.05, 0.3, 0.4]
    g.line(*[x for k, y in enumerate(ys) for x in (0.05 + k * 0.15, y)])
    for k, y in enumerate(ys): g.circle(0.05 + k * 0.15, y, 0.015, fill=True)

@P.figure(GRA, "growth-arrow", "Flecha de crecimiento", "Growth arrow")
def _(g): g.arrow(0, -0.3, 0.25, -0.05, 0.0); g.line(0.25, -0.05, 0.45, -0.18, 0.95, 0.35); g.head(0.75, 0.15, 0.95, 0.35, 0.08)

# --- Diagramas de negocio ----------------------------------------------------------------------------

@P.figure(NEG, "swot", "Matriz FODA", "SWOT matrix")
def _(g):
    g.rect(0.1, -0.4, 0.9, 0.4); g.line(0.5, -0.4, 0.5, 0.4); g.line(0.1, 0, 0.9, 0)
    g.label(0.3, 0.32, "Fortalezas", 0.45); g.label(0.7, 0.32, "Debilidades", 0.45); g.label(0.3, -0.08, "Oportunidades", 0.45); g.label(0.7, -0.08, "Amenazas", 0.45)

@P.figure(NEG, "bcg", "Matriz BCG", "BCG matrix")
def _(g):
    g.rect(0.1, -0.4, 0.9, 0.4); g.line(0.5, -0.4, 0.5, 0.4); g.line(0.1, 0, 0.9, 0)
    g.label(0.3, 0.2, "★ Estrella", 0.45); g.label(0.7, 0.2, "? Interrogante", 0.45); g.label(0.3, -0.2, "$ Vaca", 0.45); g.label(0.7, -0.2, "✕ Perro", 0.45)

@P.figure(NEG, "org-chart", "Organigrama", "Org chart")
def _(g):
    g.rect(0.38, 0.25, 0.62, 0.42); g.line(0.5, 0.25, 0.5, 0.1); g.line(0.15, 0.1, 0.85, 0.1)
    for x in (0.15, 0.5, 0.85): g.line(x, 0.1, x, 0.0); g.rect(x - 0.12, -0.17, x + 0.12, 0.0)
    for x in (0.08, 0.22): g.line(0.15, -0.17, 0.15, -0.24); g.line(0.08, -0.24, 0.22, -0.24); g.line(x, -0.24, x, -0.28); g.rect(x - 0.06, -0.4, x + 0.06, -0.28)

@P.figure(NEG, "funnel", "Embudo de ventas", "Sales funnel")
def _(g):
    g.poly(0.05, 0.4, 0.95, 0.4, 0.62, -0.4, 0.38, -0.4)
    for v in (0.13, -0.13): w = 0.45 - (0.4 - v) / 0.8 * 0.33; g.line(0.5 - w, v, 0.5 + w, v)

@P.figure(NEG, "pyramid", "Pirámide de niveles", "Level pyramid")
def _(g):
    g.poly(0.05, -0.4, 0.95, -0.4, 0.5, 0.45)
    for k in range(1, 5): v = -0.4 + k * 0.17; w = 0.45 * (1 - k * 0.17 / 0.85); g.line(0.5 - w, v, 0.5 + w, v)

@P.figure(NEG, "cycle", "Ciclo (PDCA)", "Cycle (PDCA)")
def _(g):
    for k, t in enumerate(("Planear", "Hacer", "Verificar", "Actuar")):
        a1, a2 = 90 - k * 90 - 10, 90 - (k + 1) * 90 + 10
        g.arc(0.5, 0, 0.35, 0.35, a1, a2); r = math.radians(a2); r0 = math.radians(a2 + 5)
        g.head(0.5 + 0.35 * math.cos(r0), 0.35 * math.sin(r0), 0.5 + 0.35 * math.cos(r), 0.35 * math.sin(r), 0.04)
        m = math.radians(90 - k * 90 - 45); g.label(0.5 + 0.5 * math.cos(m), 0.5 * math.sin(m), t, 0.45)

@P.figure(NEG, "timeline", "Línea de tiempo", "Timeline")
def _(g):
    g.arrow(0, 0, 1, 0, 0.03)
    for k in range(5): u = 0.1 + k * 0.2; g.line(u, -0.05, u, 0.05); g.circle(u, 0, 0.015, fill=True)

@P.figure(NEG, "canvas", "Lienzo de modelo de negocio", "Business model canvas")
def _(g):
    g.rect(0, -0.4, 1, 0.4); g.line(0, -0.15, 1, -0.15)
    for x in (0.2, 0.4, 0.6, 0.8): g.line(x, -0.15, x, 0.4)
    g.line(0.2, 0.12, 0.4, 0.12); g.line(0.6, 0.12, 0.8, 0.12); g.line(0.5, -0.4, 0.5, -0.15)

# --- Fórmulas ------------------------------------------------------------------------------------------

G = "Licenciaturas"
P.formulas_in(G, "Microeconomía", [
    ("Elasticidad precio", r"E_{p} = \frac{\% \Delta Q}{\% \Delta P} = \frac{\Delta Q / Q}{\Delta P / P}", "Price elasticity"),
    ("Elasticidad arco", r"E = \frac{(Q_{2} - Q_{1}) / (Q_{2} + Q_{1})}{(P_{2} - P_{1}) / (P_{2} + P_{1})}", "Arc elasticity"),
    ("Ingreso total", r"IT = P \cdot Q", "Total revenue"),
    ("Ingreso marginal", r"IMg = \frac{\Delta IT}{\Delta Q}", "Marginal revenue"),
    ("Costo total", r"CT = CF + CV", "Total cost"),
    ("Costo medio", r"CTMe = \frac{CT}{Q}", "Average cost"),
    ("Costo marginal", r"CMg = \frac{\Delta CT}{\Delta Q}", "Marginal cost"),
    ("Maximización de beneficio", r"IMg = CMg", "Profit maximization"),
    ("Utilidad", r"\pi = IT - CT", "Profit"),
    ("Cobb-Douglas", r"Y = A K^{\alpha} L^{1-\alpha}", "Cobb–Douglas"),
    ("Tasa marginal de sustitución", r"TMS = -\frac{\Delta Y}{\Delta X} = \frac{UMg_{X}}{UMg_{Y}}", "Marginal rate of substitution"),
    ("Excedente del consumidor", r"EC = \int_{0}^{Q^{*}} D(Q) \, dQ - P^{*} Q^{*}", "Consumer surplus"),
], "Microeconomics")
P.formulas_in(G, "Macroeconomía", [
    ("PIB (gasto)", r"PIB = C + I + G + (X - M)", "GDP (expenditure)"),
    ("PIB real", r"PIB_{real} = \frac{PIB_{nominal}}{\text{deflactor}} \times 100", "Real GDP"),
    ("Inflación", r"\pi = \frac{IPC_{t} - IPC_{t-1}}{IPC_{t-1}} \times 100", "Inflation"),
    ("Tasa de desempleo", r"u = \frac{\text{desempleados}}{\text{PEA}} \times 100", "Unemployment rate"),
    ("Ecuación cuantitativa", r"M V = P Y", "Quantity theory of money"),
    ("Multiplicador", r"k = \frac{1}{1 - PMgC}", "Multiplier"),
    ("Multiplicador monetario", r"m = \frac{1}{r}", "Money multiplier"),
    ("Ecuación de Fisher", r"i \approx r + \pi", "Fisher equation"),
    ("Ley de Okun", r"\frac{Y - Y^{*}}{Y^{*}} = -\beta (u - u^{*})", "Okun's law"),
    ("Regla de Taylor", r"i = r^{*} + \pi + 0.5(\pi - \pi^{*}) + 0.5 \, y", "Taylor rule"),
    ("Crecimiento compuesto", r"g = \left( \frac{X_{t}}{X_{0}} \right)^{1/t} - 1", "Compound growth"),
    ("Regla del 70", r"t_{dup} \approx \frac{70}{g (\%)}", "Rule of 70"),
], "Macroeconomics")
P.formulas_in(G, "Finanzas", [
    ("Interés simple", r"I = C \, i \, t", "Simple interest"),
    ("Interés compuesto", r"M = C (1 + i)^{n}", "Compound interest"),
    ("Capitalización continua", r"M = C e^{r t}", "Continuous compounding"),
    ("Tasa efectiva", r"i_{e} = \left( 1 + \frac{j}{m} \right)^{m} - 1", "Effective rate"),
    ("Valor presente", r"VP = \frac{VF}{(1 + i)^{n}}", "Present value"),
    ("VPN", r"VPN = \sum_{t=0}^{n} \frac{F_{t}}{(1 + r)^{t}}", "NPV"),
    ("TIR", r"\sum_{t=0}^{n} \frac{F_{t}}{(1 + TIR)^{t}} = 0", "IRR"),
    ("Anualidad (valor presente)", r"VP = A \frac{1 - (1 + i)^{-n}}{i}", "Annuity (present value)"),
    ("Anualidad (valor futuro)", r"VF = A \frac{(1 + i)^{n} - 1}{i}", "Annuity (future value)"),
    ("Perpetuidad", r"VP = \frac{A}{i}", "Perpetuity"),
    ("Amortización (pago)", r"A = P \frac{i (1 + i)^{n}}{(1 + i)^{n} - 1}", "Loan payment"),
    ("CAPM", r"E(R_{i}) = R_{f} + \beta_{i} (E(R_{m}) - R_{f})", "CAPM"),
    ("WACC", r"WACC = \frac{E}{V} R_{e} + \frac{D}{V} R_{d} (1 - T)", "WACC"),
    ("Gordon (dividendos)", r"P_{0} = \frac{D_{1}}{r - g}", "Gordon (dividends)"),
    ("Rendimiento", r"R = \frac{P_{1} - P_{0} + D}{P_{0}}", "Return"),
    ("ROI", r"ROI = \frac{\text{ganancia} - \text{inversión}}{\text{inversión}} \times 100", "ROI"),
], "Finance")
P.formulas_in(G, "Contabilidad y administración", [
    ("Ecuación contable", r"\text{Activo} = \text{Pasivo} + \text{Capital}", "Accounting equation"),
    ("Utilidad neta", r"UN = \text{Ventas} - \text{Costos} - \text{Gastos} - \text{Impuestos}", "Net income"),
    ("Punto de equilibrio", r"Q_{e} = \frac{CF}{P - CV_{u}}", "Break-even point"),
    ("Margen de contribución", r"MC = P - CV_{u}", "Contribution margin"),
    ("Margen de utilidad", r"\text{Margen} = \frac{\text{Utilidad neta}}{\text{Ventas}} \times 100", "Profit margin"),
    ("Razón circulante", r"RC = \frac{\text{Activo circulante}}{\text{Pasivo circulante}}", "Current ratio"),
    ("Prueba ácida", r"PA = \frac{AC - \text{Inventarios}}{PC}", "Quick ratio"),
    ("Endeudamiento", r"E = \frac{\text{Pasivo total}}{\text{Activo total}}", "Debt ratio"),
    ("ROE", r"ROE = \frac{\text{Utilidad neta}}{\text{Capital}}", "ROE"),
    ("ROA", r"ROA = \frac{\text{Utilidad neta}}{\text{Activo total}}", "ROA"),
    ("Rotación de inventario", r"R = \frac{\text{Costo de ventas}}{\text{Inventario promedio}}", "Inventory turnover"),
    ("Depreciación en línea recta", r"D = \frac{C - VR}{n}", "Straight-line depreciation"),
], "Accounting and management")
P.formulas_in(G, "Mercadotecnia", [
    ("Participación de mercado", r"PM = \frac{V_{empresa}}{V_{mercado}} \times 100", "Market share"),
    ("Valor del cliente (CLV)", r"CLV = \sum_{t=1}^{n} \frac{m \, r^{t}}{(1 + d)^{t}}", "Customer lifetime value (CLV)"),
    ("Costo de adquisición", r"CAC = \frac{\text{gasto en marketing}}{\text{clientes nuevos}}", "Customer acquisition cost"),
    ("Tasa de conversión", r"TC = \frac{\text{conversiones}}{\text{visitas}} \times 100", "Conversion rate"),
    ("ROAS", r"ROAS = \frac{\text{ingresos por anuncios}}{\text{gasto en anuncios}}", "ROAS"),
    ("Precio con margen", r"P = \frac{C}{1 - m}", "Price with margin"),
    ("Tamaño de muestra", r"n = \frac{Z^{2} p q}{e^{2}}", "Sample size"),
    ("Población finita", r"n = \frac{N Z^{2} p q}{e^{2} (N - 1) + Z^{2} p q}", "Finite population"),
], "Marketing")

P.labels = [["Ingreso", "#16a34a"], ["Egreso", "#dc2626"], ["Activo", "#2563eb"], ["Pasivo", "#ea580c"], ["Capital", "#7c3aed"],
            ["Meta", "#0891b2"], ["KPI", "#be185d"], ["Riesgo", "#b91c1c"], ["Oportunidad", "#15803d"], ["Presupuesto", "#334155"]]
P.en.update({"Ingreso": "Income", "Egreso": "Expense", "Activo": "Asset", "Pasivo": "Liability", "Capital": "Equity", "Meta": "Goal",
             "Riesgo": "Risk", "Oportunidad": "Opportunity", "Presupuesto": "Budget"})
P.emoji = {"Negocios": "📈 📉 📊 💰 💵 💳 🏦 🧾 💼 📑 🗂️ 🤝 🎯 🛒 🏷️ 📦 🌎 ⚖️"}
