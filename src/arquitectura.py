import math
from wgpack import Pack

pack = Pack("arquitectura", "Arquitectura y dibujo técnico", "Símbolos de planos, mobiliario, cotas, vistas y formulario de diseño, iluminación, acústica y confort térmico.",
            "Licenciaturas", "📐", en={"Arquitectura y dibujo técnico": "Architecture and technical drawing",
            "Símbolos de planos, mobiliario, cotas, vistas y formulario de diseño, iluminación, acústica y confort térmico.":
            "Floor plan symbols, furniture, dimensions, views and formulas for design, lighting, acoustics and thermal comfort."})
P = pack
PLA, MOB, DIB = "Arquitectura: planos", "Arquitectura: mobiliario", "Dibujo técnico"
P.en.update({PLA: "Architecture: plans", MOB: "Architecture: furniture", DIB: "Technical drawing"})

@P.figure(PLA, "wall-plan", "Muro (planta)", "Wall (plan)")
def _(g): g.rect(0, -0.05, 1, 0.05, fill=True)

@P.figure(PLA, "door", "Puerta", "Door")
def _(g): g.line(0, 0, 0.1, 0); g.line(0.9, 0, 1, 0); g.line(0.1, 0, 0.1, 0.8); g.arc(0.1, 0, 0.8, 0.8, 0, 90, dashed=True)

@P.figure(PLA, "double-door", "Puerta doble", "Double door")
def _(g): g.line(0.1, 0, 0.1, 0.4); g.line(0.9, 0, 0.9, 0.4); g.arc(0.1, 0, 0.4, 0.4, 0, 90, dashed=True); g.arc(0.9, 0, 0.4, 0.4, 90, 180, dashed=True)

@P.figure(PLA, "sliding-door", "Puerta corrediza", "Sliding door")
def _(g): g.line(0, 0, 0.1, 0); g.line(0.9, 0, 1, 0); g.line(0.1, 0.03, 0.55, 0.03); g.line(0.45, -0.03, 0.9, -0.03); g.arrow(0.3, 0.12, 0.6, 0.12, 0.03)

@P.figure(PLA, "window", "Ventana", "Window")
def _(g): g.rect(0, -0.05, 1, 0.05); g.line(0, 0, 1, 0)

@P.figure(PLA, "stairs", "Escalera", "Stairs")
def _(g):
    g.rect(0, -0.25, 1, 0.25)
    for k in range(1, 10): g.line(k / 10, -0.25, k / 10, 0.25)
    g.arrow(0.05, 0, 0.95, 0, 0.04); g.label(0.08, 0.1, "sube", 0.4)

@P.figure(PLA, "column-plan", "Columna (planta)", "Column (plan)")
def _(g): g.rect(0.4, -0.1, 0.6, 0.1, fill=True); g.line(0, 0, 1, 0, dashed=True); g.line(0.5, -0.4, 0.5, 0.4, dashed=True)

@P.figure(PLA, "grid-axis", "Eje de proyecto", "Grid axis")
def _(g): g.line(0, 0, 0.82, 0, dashed=True); g.circle(0.9, 0, 0.08); g.label(0.9, 0, "A", 0.6)

@P.figure(PLA, "north", "Norte", "North arrow")
def _(g): g.circle(0.5, 0, 0.35); g.poly(0.5, 0.42, 0.6, -0.2, 0.5, -0.1, fill=True); g.poly(0.5, 0.42, 0.4, -0.2, 0.5, -0.1); g.label(0.5, 0.52, "N", 0.7)

@P.figure(PLA, "wind-rose", "Rosa de los vientos", "Compass rose")
def _(g):
    for k in range(8):
        a = math.radians(90 - k * 45); r = 0.45 if k % 2 == 0 else 0.25; b1, b2 = a + math.radians(12), a - math.radians(12)
        g.poly(0.5 + r * math.cos(a), r * math.sin(a), 0.5 + 0.06 * math.cos(b1), 0.06 * math.sin(b1), 0.5, 0, fill=(k % 2 == 0))
        g.poly(0.5 + r * math.cos(a), r * math.sin(a), 0.5 + 0.06 * math.cos(b2), 0.06 * math.sin(b2), 0.5, 0)
    for k, t in enumerate("NESO"): a = math.radians(90 - k * 90); g.label(0.5 + 0.55 * math.cos(a), 0.55 * math.sin(a), t, 0.6)

@P.figure(PLA, "scale-bar", "Escala gráfica", "Scale bar")
def _(g):
    for k in range(5): g.rect(k * 0.2, -0.04, (k + 1) * 0.2, 0.04, fill=(k % 2 == 0)); g.label(k * 0.2, -0.12, str(k), 0.5)
    g.label(1.0, -0.12, "5 m", 0.5)

@P.figure(PLA, "section-cut", "Línea de corte", "Section cut line")
def _(g): g.line(0.1, 0, 0.9, 0, dashed=True); g.line(0.1, 0, 0.1, 0.12); g.line(0.9, 0, 0.9, 0.12); g.arrow(0.1, 0.12, 0.25, 0.12, 0.03); g.arrow(0.9, 0.12, 0.75, 0.12, 0.03); g.label(0.0, 0, "A", 0.6); g.label(1.0, 0, "A'", 0.6)

@P.figure(PLA, "level", "Nivel (N.P.T.)", "Floor level")
def _(g): g.line(0, 0, 0.8, 0); g.circle(0.88, 0, 0.07); g.line(0.81, 0, 0.95, 0); g.line(0.88, -0.07, 0.88, 0.07); g.label(0.88, 0.16, "+0.00", 0.5)

@P.figure(PLA, "slope", "Pendiente", "Slope")
def _(g): g.arrow(0, 0, 1, 0, 0.04); g.label(0.5, 0.08, "2%", 0.6)

@P.figure(PLA, "tree-plan", "Árbol (planta)", "Tree (plan)")
def _(g): g.polar(0.5, 0, lambda t: 0.35 + 0.05 * math.sin(7 * t)); g.circle(0.5, 0, 0.03, fill=True)

@P.figure(PLA, "person-scale", "Persona a escala", "Human scale figure")
def _(g): g.circle(0.5, 0.42, 0.06); g.line(0.5, 0.36, 0.5, 0.0); g.line(0.38, 0.22, 0.5, 0.3, 0.62, 0.22); g.line(0.42, -0.42, 0.5, 0.0, 0.58, -0.42)

@P.figure(PLA, "car-plan", "Automóvil (planta)", "Car (plan)")
def _(g): g.rect(0.05, -0.2, 0.95, 0.2); g.rect(0.3, -0.16, 0.65, 0.16); g.line(0.3, -0.16, 0.22, -0.2); g.line(0.3, 0.16, 0.22, 0.2)

# --- Mobiliario ------------------------------------------------------------------------------------------

@P.figure(MOB, "bed", "Cama", "Bed")
def _(g): g.rect(0.1, -0.3, 0.9, 0.3); g.rect(0.12, -0.25, 0.3, -0.03); g.rect(0.12, 0.03, 0.3, 0.25); g.line(0.4, -0.3, 0.4, 0.3)

@P.figure(MOB, "table-chairs", "Mesa con sillas", "Table and chairs")
def _(g):
    g.rect(0.25, -0.2, 0.75, 0.2)
    for x in (0.35, 0.65): g.rect(x - 0.08, 0.25, x + 0.08, 0.38); g.rect(x - 0.08, -0.38, x + 0.08, -0.25)

@P.figure(MOB, "sofa", "Sofá", "Sofa")
def _(g): g.rect(0.05, -0.2, 0.95, 0.2); g.rect(0.05, 0.08, 0.95, 0.2); g.rect(0.05, -0.2, 0.15, 0.08); g.rect(0.85, -0.2, 0.95, 0.08); g.line(0.5, -0.2, 0.5, 0.08)

@P.figure(MOB, "toilet", "Inodoro", "Toilet")
def _(g): g.rect(0.35, 0.18, 0.65, 0.32); g.ellipse(0.5, -0.05, 0.13, 0.2)

@P.figure(MOB, "sink", "Lavabo", "Sink")
def _(g): g.rect(0.25, -0.2, 0.75, 0.2); g.ellipse(0.5, -0.02, 0.17, 0.12); g.circle(0.5, 0.15, 0.02, fill=True)

@P.figure(MOB, "shower", "Regadera", "Shower")
def _(g): g.rect(0.2, -0.3, 0.8, 0.3); g.line(0.2, -0.3, 0.8, 0.3); g.line(0.2, 0.3, 0.8, -0.3); g.circle(0.5, 0, 0.04)

@P.figure(MOB, "stove", "Estufa", "Stove")
def _(g):
    g.rect(0.25, -0.25, 0.75, 0.25)
    for x in (0.38, 0.62):
        for y in (0.11, -0.11): g.circle(x, y, 0.07)

@P.figure(MOB, "desk", "Escritorio", "Desk")
def _(g): g.rect(0.1, 0, 0.9, 0.25); g.circle(0.5, -0.12, 0.09); g.rect(0.42, 0.05, 0.58, 0.2)

# --- Dibujo técnico ------------------------------------------------------------------------------------------

@P.figure(DIB, "dimension", "Cota", "Dimension")
def _(g):
    g.line(0, -0.15, 0, 0.12); g.line(1, -0.15, 1, 0.12); g.double_arrow(0, 0.06, 1, 0.06, 0.04)
    for x in (0, 1): g.line(x - 0.03, 0.03, x + 0.03, 0.09)
    g.label(0.5, 0.14, "L", 0.7)

@P.figure(DIB, "radius-dim", "Cota de radio", "Radius dimension")
def _(g): g.circle(0.5, 0, 0.35); g.circle(0.5, 0, 0.012, fill=True); g.arrow(0.5, 0, 0.75, 0.25, 0.04); g.label(0.6, 0.22, "R", 0.6)

@P.figure(DIB, "diameter-dim", "Cota de diámetro", "Diameter dimension")
def _(g): g.circle(0.5, 0, 0.35); g.double_arrow(0.25, -0.25, 0.75, 0.25, 0.04); g.label(0.6, 0.06, "Ø", 0.7)

@P.figure(DIB, "angle-dim", "Cota angular", "Angle dimension")
def _(g): g.line(0, 0, 1, 0); g.line(0, 0, 0.8, 0.55); g.arc(0, 0, 0.5, 0.5, 0, 34.5); g.head(0.5 * math.cos(math.radians(28)), 0.5 * math.sin(math.radians(28)), 0.5 * math.cos(math.radians(34.5)), 0.5 * math.sin(math.radians(34.5)), 0.04); g.label(0.6, 0.18, "α", 0.6)

@P.figure(DIB, "center-line", "Línea de centro", "Center line")
def _(g): g.line(0, 0, 1, 0, dashed=True); g.label(0.5, 0.08, "℄", 0.7)

@P.figure(DIB, "hidden-line", "Línea oculta", "Hidden line")
def _(g): g.line(0, 0, 1, 0, dashed=True)

@P.figure(DIB, "hatch-section", "Achurado de corte", "Section hatching")
def _(g):
    g.rect(0.1, -0.3, 0.9, 0.3)
    for k in range(-3, 9): x0 = 0.1 + k * 0.1; g.line(max(0.1, x0), -0.3 + max(0, 0.1 - x0), min(0.9, x0 + 0.6), -0.3 + min(0.6, 0.9 - x0))

@P.figure(DIB, "ortho-views", "Vistas ortogonales", "Orthographic views")
def _(g):
    g.rect(0.05, -0.4, 0.4, -0.1); g.rect(0.05, 0.05, 0.4, 0.35); g.rect(0.55, -0.4, 0.75, -0.1)
    g.line(0.05, -0.25, 0.4, -0.25, dashed=True); g.label(0.22, -0.48, "frente", 0.4); g.label(0.22, 0.42, "planta", 0.4); g.label(0.65, -0.48, "lateral", 0.4)

@P.figure(DIB, "isometric-box", "Caja isométrica", "Isometric box")
def _(g):
    c, s = math.cos(math.radians(30)), math.sin(math.radians(30)); a, b, h = 0.5, 0.35, 0.4
    p0 = (0.15, -0.3); px = (p0[0] + a * c, p0[1] + a * s); py = (p0[0] - b * c * 0.0 + b * c, p0[1] - b * s * 0 + 0)
    pts = [(0.5, -0.4), (0.5 + a * c, -0.4 + a * s), (0.5 - b * c, -0.4 + b * s)]
    (o, x, y) = pts; top = lambda p: (p[0], p[1] + h); xy = (x[0] + y[0] - o[0], x[1] + y[1] - o[1])
    g.line(*y, *o, *x); g.line(*o, *top(o)); g.line(*x, *top(x)); g.line(*y, *top(y))
    g.poly(*top(o), *top(x), *top(xy), *top(y))

@P.figure(DIB, "title-block", "Cuadro de datos", "Title block")
def _(g):
    g.rect(0, -0.3, 1, 0.3); g.line(0.6, -0.3, 0.6, 0.3); g.line(0, 0.1, 1, 0.1); g.line(0.6, -0.1, 1, -0.1)
    g.label(0.3, 0.2, "Proyecto", 0.45); g.label(0.8, 0.2, "Escala", 0.45); g.label(0.8, 0.0, "Fecha", 0.45); g.label(0.8, -0.2, "Lámina", 0.45)

@P.figure(DIB, "roughness", "Acabado superficial", "Surface finish")
def _(g): g.line(0.2, 0.1, 0.35, -0.15, 0.6, 0.35, 0.95, 0.35); g.line(0.0, -0.15, 0.6, -0.15)

@P.figure(DIB, "weld-symbol", "Símbolo de soldadura", "Weld symbol")
def _(g): g.arrow(0.6, 0, 0.1, -0.3, 0.04); g.line(0.6, 0, 1, 0); g.poly(0.72, 0, 0.8, 0.08, 0.8, 0)

# --- Fórmulas -------------------------------------------------------------------------------------------------

G = "Licenciaturas"
P.formulas_in(G, "Arquitectura y diseño", [
    ("Proporción áurea", r"\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618", "Golden ratio"),
    ("Escala", r"E = \frac{\text{medida en plano}}{\text{medida real}}", "Scale"),
    ("Pendiente (%)", r"p = \frac{\Delta h}{d} \times 100", "Slope (%)"),
    ("Regla de escaleras", r"2h + b = 63 \text{ a } 64 \text{ cm}", "Stair rule"),
    ("Número de escalones", r"n = \frac{H}{h}", "Number of steps"),
    ("Área de un polígono (Gauss)", r"A = \frac{1}{2} \left| \sum_{i} (x_{i} y_{i+1} - x_{i+1} y_{i}) \right|", "Polygon area (shoelace)"),
    ("Coeficiente de ocupación", r"COS = \frac{\text{área de desplante}}{\text{área del terreno}}", "Site coverage ratio"),
    ("Coeficiente de utilización", r"CUS = \frac{\text{área construida}}{\text{área del terreno}}", "Floor area ratio"),
    ("Iluminancia", r"E = \frac{\Phi}{A}", "Illuminance"),
    ("Método de lúmenes", r"N = \frac{E \cdot A}{\Phi \cdot CU \cdot FM}", "Lumen method"),
    ("Tiempo de reverberación (Sabine)", r"T_{60} = \frac{0.161 \, V}{\sum S_{i} \alpha_{i}}", "Reverberation time (Sabine)"),
    ("Transmitancia térmica", r"U = \frac{1}{R_{si} + \sum \frac{e_{i}}{\lambda_{i}} + R_{se}}", "Thermal transmittance"),
    ("Pérdida de calor", r"Q = U A \Delta T", "Heat loss"),
    ("Factor de luz diurna", r"FLD = \frac{E_{int}}{E_{ext}} \times 100", "Daylight factor"),
    ("Captación pluvial", r"V = P \cdot A \cdot C", "Rainwater harvesting"),
], "Architecture and design")

P.labels = [["Planta", "#2563eb"], ["Corte", "#7c3aed"], ["Fachada", "#16a34a"], ["Detalle", "#ea580c"],
            ["Croquis", "#ca8a04"], ["Norte", "#334155"], ["Escala 1:100", "#0891b2"], ["Revisión", "#dc2626"]]
P.en.update({"Planta": "Plan", "Corte": "Section", "Fachada": "Elevation", "Detalle": "Detail", "Croquis": "Sketch", "Norte": "North",
             "Escala 1:100": "Scale 1:100", "Revisión": "Revision"})
P.emoji = {"Arquitectura": "📐 📏 🏛️ 🏠 🏡 🏢 🏗️ 🧱 🪟 🚪 🛋️ 🛏️ 🪴 🌳 ☀️ 🌧️ 🖌️ ✏️"}
