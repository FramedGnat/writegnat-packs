import math
from wgpack import Pack

pack = Pack("industrial-computacion", "Industrial y computación", "UML, redes, estructuras de datos, procesos y calidad, con formulario de operaciones, calidad, algoritmos, IA y redes.",
            "Ingenierías", "💻", en={"Industrial y computación": "Industrial and computing",
            "UML, redes, estructuras de datos, procesos y calidad, con formulario de operaciones, calidad, algoritmos, IA y redes.":
            "UML, networks, data structures, processes and quality, with formulas for operations, quality, algorithms, AI and networking."})
P = pack
SW, NET, IND = "Computación: software y datos", "Computación: redes y hardware", "Industrial: procesos y calidad"
P.en.update({SW: "Computing: software and data", NET: "Computing: networks and hardware", IND: "Industrial: processes and quality"})

@P.figure(SW, "uml-class", "Clase UML", "UML class")
def _(g):
    g.rect(0.15, -0.4, 0.85, 0.4); g.line(0.15, 0.22, 0.85, 0.22); g.line(0.15, -0.08, 0.85, -0.08)
    g.label(0.5, 0.31, "Clase", 0.6); g.label(0.42, 0.12, "- atributo", 0.45); g.label(0.42, -0.2, "+ método()", 0.45)

@P.figure(SW, "uml-actor", "Actor", "Actor")
def _(g): g.circle(0.5, 0.35, 0.1); g.line(0.5, 0.25, 0.5, -0.1); g.line(0.3, 0.12, 0.7, 0.12); g.line(0.35, -0.4, 0.5, -0.1, 0.65, -0.4)

@P.figure(SW, "uml-usecase", "Caso de uso", "Use case")
def _(g): g.ellipse(0.5, 0, 0.45, 0.2); g.label(0.5, 0, "caso de uso", 0.5)

@P.figure(SW, "uml-inherit", "Herencia (UML)", "Inheritance (UML)")
def _(g): g.line(0, 0, 0.85, 0); g.poly(0.85, 0.07, 1, 0, 0.85, -0.07)

@P.figure(SW, "uml-compose", "Composición (UML)", "Composition (UML)")
def _(g): g.line(0.2, 0, 1, 0); g.poly(0, 0, 0.1, 0.06, 0.2, 0, 0.1, -0.06, fill=True)

@P.figure(SW, "uml-aggregate", "Agregación (UML)", "Aggregation (UML)")
def _(g): g.line(0.2, 0, 1, 0); g.poly(0, 0, 0.1, 0.06, 0.2, 0, 0.1, -0.06)

@P.figure(SW, "uml-depend", "Dependencia (UML)", "Dependency (UML)")
def _(g): g.arrow(0, 0, 1, 0, 0.06, dashed=True)

@P.figure(SW, "er-entity", "Entidad (E-R)", "Entity (E-R)")
def _(g): g.rect(0.2, -0.18, 0.8, 0.18); g.label(0.5, 0, "Entidad", 0.6)

@P.figure(SW, "er-relation", "Relación (E-R)", "Relationship (E-R)")
def _(g): g.poly(0.1, 0, 0.5, 0.25, 0.9, 0, 0.5, -0.25); g.label(0.5, 0, "relación", 0.5)

@P.figure(SW, "er-attribute", "Atributo (E-R)", "Attribute (E-R)")
def _(g): g.ellipse(0.5, 0, 0.35, 0.15); g.label(0.5, 0, "atributo", 0.5)

@P.figure(SW, "state", "Estado", "State")
def _(g):
    g.arc(0.25, 0, 0.15, 0.15, 90, 270); g.line(0.25, 0.15, 0.75, 0.15); g.arc(0.75, 0, 0.15, 0.15, -90, 90); g.line(0.75, -0.15, 0.25, -0.15)
    g.label(0.5, 0, "estado", 0.6)

@P.figure(SW, "state-machine", "Máquina de estados", "State machine")
def _(g):
    g.circle(0.2, 0, 0.13); g.circle(0.8, 0, 0.13); g.circle(0.8, 0, 0.1); g.label(0.2, 0, "q₀", 0.6); g.label(0.8, 0, "q₁", 0.6)
    g.arc(0.5, -0.05, 0.3, 0.2, 30, 150); g.head(0.5 + 0.3 * math.cos(math.radians(40)), -0.05 + 0.2 * math.sin(math.radians(40)), 0.5 + 0.3 * math.cos(math.radians(30)), -0.05 + 0.2 * math.sin(math.radians(30)), 0.04)
    g.arc(0.5, 0.05, 0.3, 0.2, 210, 330); g.head(0.5 + 0.3 * math.cos(math.radians(220)), 0.05 + 0.2 * math.sin(math.radians(220)), 0.5 + 0.3 * math.cos(math.radians(210)), 0.05 + 0.2 * math.sin(math.radians(210)), 0.04)
    g.arrow(-0.05, 0, 0.07, 0, 0.03); g.label(0.5, 0.22, "a", 0.6); g.label(0.5, -0.22, "b", 0.6)

@P.figure(SW, "array", "Arreglo", "Array")
def _(g):
    for k in range(6): g.rect(k / 6, -0.08, (k + 1) / 6, 0.08); g.label((k + 0.5) / 6, -0.15, str(k), 0.45)

@P.figure(SW, "linked-list", "Lista enlazada", "Linked list")
def _(g):
    for k in range(3):
        x = k * 0.35; g.rect(x, -0.08, x + 0.22, 0.08); g.line(x + 0.15, -0.08, x + 0.15, 0.08)
        g.arrow(x + 0.185, 0, x + 0.35, 0, 0.03) if k < 2 else g.label(x + 0.3, 0, "∅", 0.6)

@P.figure(SW, "stack", "Pila", "Stack")
def _(g):
    g.line(0.3, 0.45, 0.3, -0.35, 0.7, -0.35, 0.7, 0.45)
    for k in range(3): g.rect(0.33, -0.33 + k * 0.17, 0.67, -0.18 + k * 0.17)
    g.arrow(0.85, 0.45, 0.85, 0.22, 0.03); g.label(0.9, 0.33, "push", 0.4)

@P.figure(SW, "queue", "Cola", "Queue")
def _(g):
    g.line(0.1, 0.12, 0.9, 0.12); g.line(0.1, -0.12, 0.9, -0.12)
    for k in range(4): g.rect(0.15 + k * 0.17, -0.09, 0.29 + k * 0.17, 0.09)
    g.arrow(0.9, 0, 1.05, 0, 0.03); g.arrow(-0.1, 0, 0.08, 0, 0.03)

@P.figure(SW, "binary-tree", "Árbol binario", "Binary tree")
def _(g):
    nodes = {(0.5, 0.35): None, (0.25, 0.05): (0.5, 0.35), (0.75, 0.05): (0.5, 0.35), (0.12, -0.25): (0.25, 0.05), (0.38, -0.25): (0.25, 0.05), (0.88, -0.25): (0.75, 0.05)}
    for (x, y), p in nodes.items():
        g.circle(x, y, 0.07)
        if p:
            d = math.hypot(x - p[0], y - p[1]); ux, uy = (x - p[0]) / d, (y - p[1]) / d
            g.line(p[0] + ux * 0.07, p[1] + uy * 0.07, x - ux * 0.07, y - uy * 0.07)

@P.figure(SW, "graph", "Grafo", "Graph")
def _(g):
    pts = [(0.1, 0), (0.4, 0.3), (0.4, -0.3), (0.75, 0.15), (0.95, -0.2)]
    for a, b in ((0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)):
        (x1, y1), (x2, y2) = pts[a], pts[b]; d = math.hypot(x2 - x1, y2 - y1)
        g.line(x1 + (x2 - x1) / d * 0.05, y1 + (y2 - y1) / d * 0.05, x2 - (x2 - x1) / d * 0.05, y2 - (y2 - y1) / d * 0.05)
    for x, y in pts: g.circle(x, y, 0.05)

@P.figure(SW, "matrix-grid", "Matriz (cuadrícula)", "Matrix grid")
def _(g):
    for i in range(5): g.line(0.2 + i * 0.15, -0.3, 0.2 + i * 0.15, 0.3); g.line(0.2, -0.3 + i * 0.15, 0.8, -0.3 + i * 0.15)

@P.figure(SW, "neural-net", "Red neuronal", "Neural network")
def _(g):
    layers = [[-0.25, 0, 0.25], [-0.35, -0.12, 0.12, 0.35], [-0.12, 0.12]]
    xs = [0.1, 0.5, 0.9]
    for li in range(2):
        for a in layers[li]:
            for b in layers[li + 1]: g.line(xs[li] + 0.05, a, xs[li + 1] - 0.05, b)
    for li, ys in enumerate(layers):
        for y in ys: g.circle(xs[li], y, 0.05)

@P.figure(SW, "sequence", "Diagrama de secuencia", "Sequence diagram")
def _(g):
    for x, n in ((0.15, "A"), (0.85, "B")): g.rect(x - 0.1, 0.3, x + 0.1, 0.45); g.label(x, 0.375, n, 0.6); g.line(x, 0.3, x, -0.45, dashed=True)
    g.arrow(0.15, 0.15, 0.85, 0.15, 0.04); g.label(0.5, 0.21, "petición", 0.45); g.arrow(0.85, -0.15, 0.15, -0.15, 0.04, dashed=True); g.label(0.5, -0.09, "respuesta", 0.45)

# --- Redes y hardware -----------------------------------------------------------------------------------

@P.figure(NET, "computer", "Computadora", "Computer")
def _(g): g.rect(0.2, -0.05, 0.8, 0.4); g.rect(0.24, 0.0, 0.76, 0.36); g.line(0.5, -0.05, 0.5, -0.18); g.line(0.35, -0.18, 0.65, -0.18)

@P.figure(NET, "laptop", "Laptop", "Laptop")
def _(g): g.rect(0.25, 0.0, 0.75, 0.35); g.poly(0.18, -0.08, 0.82, -0.08, 0.75, 0.0, 0.25, 0.0)

@P.figure(NET, "server", "Servidor", "Server")
def _(g):
    for k in range(3): g.rect(0.3, -0.35 + k * 0.24, 0.7, -0.15 + k * 0.24); g.circle(0.62, -0.25 + k * 0.24, 0.02, fill=True); g.line(0.36, -0.25 + k * 0.24, 0.5, -0.25 + k * 0.24)

@P.figure(NET, "database", "Base de datos", "Database")
def _(g): g.ellipse(0.5, 0.25, 0.3, 0.08); g.line(0.2, 0.25, 0.2, -0.25); g.line(0.8, 0.25, 0.8, -0.25); g.arc(0.5, -0.25, 0.3, 0.08, 180, 360); g.arc(0.5, 0.0, 0.3, 0.08, 180, 360)

@P.figure(NET, "router", "Router", "Router")
def _(g):
    g.ellipse(0.5, 0.05, 0.3, 0.1); g.line(0.2, 0.05, 0.2, -0.1); g.line(0.8, 0.05, 0.8, -0.1); g.arc(0.5, -0.1, 0.3, 0.1, 180, 360)
    g.arrow(0.4, 0.05, 0.3, 0.05, 0.03); g.arrow(0.6, 0.05, 0.7, 0.05, 0.03)

@P.figure(NET, "switch-net", "Switch de red", "Network switch")
def _(g):
    g.rect(0.15, -0.12, 0.85, 0.12); g.arrow(0.3, 0.04, 0.5, 0.04, 0.03); g.arrow(0.7, -0.04, 0.5, -0.04, 0.03)
    for k in range(5): g.rect(0.2 + k * 0.13, -0.1, 0.27 + k * 0.13, -0.06)

@P.figure(NET, "cloud", "Nube", "Cloud")
def _(g):
    # Elipse con bordes ondulados hacia fuera.
    pts = []
    for i in range(121):
        t = 2 * math.pi * i / 120; k = 1 + 0.16 * abs(math.sin(4 * t)); pts += [0.5 + 0.42 * k * math.cos(t), 0.24 * k * math.sin(t)]
    g.line(*pts)

@P.figure(NET, "firewall", "Firewall", "Firewall")
def _(g):
    g.rect(0.2, -0.3, 0.8, 0.3)
    for k in range(1, 4): g.line(0.2, -0.3 + k * 0.15, 0.8, -0.3 + k * 0.15)
    for k in range(4):
        off = 0.1 if k % 2 else 0.0
        for j in range(3): x = 0.3 + off + j * 0.2; x <= 0.79 and g.line(x, -0.3 + k * 0.15, x, -0.15 + k * 0.15)

@P.figure(NET, "phone", "Teléfono inteligente", "Smartphone")
def _(g): g.rect(0.38, -0.4, 0.62, 0.4); g.rect(0.4, -0.3, 0.6, 0.33); g.circle(0.5, -0.35, 0.02)

@P.figure(NET, "wifi", "Wi-Fi", "Wi-Fi")
def _(g):
    g.circle(0.5, -0.2, 0.03, fill=True)
    for r in (0.15, 0.3, 0.45): g.arc(0.5, -0.2, r, r, 45, 135)

@P.figure(NET, "cpu", "Procesador", "Processor")
def _(g):
    g.rect(0.3, -0.2, 0.7, 0.2); g.rect(0.4, -0.1, 0.6, 0.1)
    for k in range(5): x = 0.34 + k * 0.08; g.line(x, 0.2, x, 0.28); g.line(x, -0.2, x, -0.28)

@P.figure(NET, "net-topology", "Topología estrella", "Star topology")
def _(g):
    g.rect(0.42, -0.06, 0.58, 0.06)
    for k in range(6):
        a = k * math.pi / 3; x, y = 0.5 + 0.4 * math.cos(a), 0.4 * math.sin(a)
        g.line(0.5 + 0.08 * math.cos(a), 0.08 * math.sin(a), x - 0.05 * math.cos(a), y - 0.05 * math.sin(a)); g.circle(x, y, 0.05)

# --- Industrial ---------------------------------------------------------------------------------------------

@P.figure(IND, "process-op", "Operación (ASME)", "Operation (ASME)")
def _(g): g.circle(0.5, 0, 0.2)

@P.figure(IND, "process-inspect", "Inspección (ASME)", "Inspection (ASME)")
def _(g): g.rect(0.3, -0.2, 0.7, 0.2)

@P.figure(IND, "process-transport", "Transporte (ASME)", "Transport (ASME)")
def _(g): g.poly(0.2, 0.08, 0.6, 0.08, 0.6, 0.18, 0.85, 0, 0.6, -0.18, 0.6, -0.08, 0.2, -0.08)

@P.figure(IND, "process-delay", "Demora (ASME)", "Delay (ASME)")
def _(g): g.line(0.35, 0.2, 0.35, -0.2, 0.55, -0.2); g.arc(0.55, 0, 0.2, 0.2, -90, 90); g.line(0.55, 0.2, 0.35, 0.2)

@P.figure(IND, "process-storage", "Almacenamiento (ASME)", "Storage (ASME)")
def _(g): g.poly(0.3, 0.2, 0.7, 0.2, 0.5, -0.2)

@P.figure(IND, "conveyor", "Banda transportadora", "Conveyor belt")
def _(g):
    g.circle(0.1, 0, 0.08); g.circle(0.9, 0, 0.08); g.line(0.1, 0.08, 0.9, 0.08); g.line(0.1, -0.08, 0.9, -0.08)
    g.rect(0.35, 0.08, 0.5, 0.2); g.rect(0.6, 0.08, 0.75, 0.2); g.arrow(0.4, 0.32, 0.7, 0.32, 0.03)

@P.figure(IND, "factory", "Fábrica", "Factory")
def _(g): g.line(0, -0.3, 0, 0.1, 0.25, 0.25, 0.25, 0.1, 0.5, 0.25, 0.5, 0.1, 0.75, 0.25, 0.75, -0.3, 0, -0.3); g.rect(0.82, -0.3, 0.92, 0.45)

@P.figure(IND, "ishikawa", "Diagrama de Ishikawa", "Ishikawa diagram")
def _(g):
    g.arrow(0, 0, 0.85, 0, 0.04); g.rect(0.85, -0.1, 1.05, 0.1)
    for x in (0.2, 0.45, 0.7):
        g.line(x - 0.15, 0.3, x, 0); g.line(x - 0.15, -0.3, x, 0)
        g.line(x - 0.12, 0.2, x - 0.02, 0.2); g.line(x - 0.12, -0.2, x - 0.02, -0.2)

@P.figure(IND, "pareto", "Gráfica de Pareto", "Pareto chart")
def _(g):
    g.line(0, 0.5, 0, -0.3, 1, -0.3)
    hs = [0.6, 0.38, 0.22, 0.12, 0.08, 0.05]
    for k, h in enumerate(hs): g.rect(0.03 + k * 0.155, -0.3, 0.15 + k * 0.155, -0.3 + h)
    acc = 0; pts = []
    for k, h in enumerate(hs): acc += h; pts += [0.09 + k * 0.155, -0.3 + 0.75 * acc / sum(hs)]
    g.line(*pts)

@P.figure(IND, "control-chart", "Gráfica de control", "Control chart")
def _(g):
    g.line(0, 0, 1, 0); g.line(0, 0.3, 1, 0.3, dashed=True); g.line(0, -0.3, 1, -0.3, dashed=True)
    g.label(1.06, 0.3, "LSC", 0.45); g.label(1.06, 0, "LC", 0.45); g.label(1.06, -0.3, "LIC", 0.45)
    ys = [0.05, -0.1, 0.12, 0.2, -0.05, -0.18, 0.08, 0.15, -0.02, 0.1]
    g.line(*[x for k, y in enumerate(ys) for x in (0.05 + k * 0.1, y)])
    for k, y in enumerate(ys): g.circle(0.05 + k * 0.1, y, 0.012, fill=True)

@P.figure(IND, "gantt", "Diagrama de Gantt", "Gantt chart")
def _(g):
    g.line(0.2, 0.4, 0.2, -0.4); g.line(0.2, -0.4, 1, -0.4)
    for k, (a, b) in enumerate(((0.2, 0.45), (0.35, 0.6), (0.55, 0.85), (0.8, 1.0))):
        y = 0.28 - k * 0.18; g.rect(a, y - 0.05, b, y + 0.05, fill=(k % 2 == 0)); g.label(0.1, y, f"T{k + 1}", 0.5)

@P.figure(IND, "pert", "Red PERT", "PERT network")
def _(g):
    pts = [(0.05, 0), (0.35, 0.25), (0.35, -0.25), (0.65, 0), (0.95, 0)]
    for a, b in ((0, 1), (0, 2), (1, 3), (2, 3), (3, 4)):
        (x1, y1), (x2, y2) = pts[a], pts[b]; d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
        g.arrow(x1 + ux * 0.05, y1 + uy * 0.05, x2 - ux * 0.05, y2 - uy * 0.05, 0.03)
    for i, (x, y) in enumerate(pts): g.circle(x, y, 0.05); g.label(x, y, str(i + 1), 0.5)

# --- Fórmulas -----------------------------------------------------------------------------------------------

G = "Ingenierías"
P.formulas_in(G, "Ingeniería industrial", [
    ("Lote económico (EOQ)", r"Q^{*} = \sqrt{\frac{2 D S}{H}}", "Economic order quantity (EOQ)"),
    ("Punto de reorden", r"ROP = d \cdot L + SS", "Reorder point"),
    ("Inventario de seguridad", r"SS = z \, \sigma_{d} \sqrt{L}", "Safety stock"),
    ("Productividad", r"P = \frac{\text{salidas}}{\text{entradas}}", "Productivity"),
    ("Takt time", r"TT = \frac{\text{tiempo disponible}}{\text{demanda}}", "Takt time"),
    ("Eficiencia de línea", r"E = \frac{\sum t_{i}}{n \cdot C} \times 100\%", "Line efficiency"),
    ("OEE", r"OEE = \text{Disponibilidad} \times \text{Rendimiento} \times \text{Calidad}", "OEE"),
    ("Disponibilidad", r"A = \frac{MTBF}{MTBF + MTTR}", "Availability"),
    ("Confiabilidad", r"R(t) = e^{-\lambda t}", "Reliability"),
    ("Little", r"L = \lambda W", "Little's law"),
    ("Cola M/M/1", r"\rho = \frac{\lambda}{\mu}, \quad L = \frac{\rho}{1 - \rho}, \quad W = \frac{1}{\mu - \lambda}", "M/M/1 queue"),
    ("Tiempo estándar", r"TS = TN \times (1 + \text{tolerancias})", "Standard time"),
    ("Pronóstico (suavizamiento)", r"F_{t+1} = \alpha D_{t} + (1 - \alpha) F_{t}", "Forecast (smoothing)"),
    ("Programación lineal", r"\max \; z = c^{T} x \quad \text{s.a.} \; A x \le b, \; x \ge 0", "Linear programming"),
], "Industrial engineering")
P.formulas_in(G, "Control de calidad", [
    ("Límites X̄", r"LSC = \bar{\bar{x}} + A_{2} \bar{R}, \quad LIC = \bar{\bar{x}} - A_{2} \bar{R}", "X̄ limits"),
    ("Límites p", r"p \pm 3 \sqrt{\frac{p (1 - p)}{n}}", "p limits"),
    ("Capacidad del proceso", r"C_{p} = \frac{LSE - LIE}{6 \sigma}", "Process capability"),
    ("Índice Cpk", r"C_{pk} = \min\left( \frac{LSE - \mu}{3\sigma}, \frac{\mu - LIE}{3\sigma} \right)", "Cpk index"),
    ("Defectos por millón", r"DPMO = \frac{\text{defectos}}{\text{unidades} \times \text{oportunidades}} \times 10^{6}", "Defects per million"),
    ("Nivel sigma", r"Z = \Phi^{-1}(1 - DPMO \cdot 10^{-6}) + 1.5", "Sigma level"),
], "Quality control")
P.formulas_in(G, "Computación: algoritmos e IA", [
    ("Teorema maestro", r"T(n) = a T\left( \frac{n}{b} \right) + f(n)", "Master theorem"),
    ("Notación O grande", r"f(n) = O(g(n)) \iff \exists c, n_{0}: f(n) \le c \, g(n), \; n \ge n_{0}", "Big-O notation"),
    ("Suma aritmética", r"\sum_{i=1}^{n} i = \frac{n(n + 1)}{2}", "Arithmetic sum"),
    ("Búsqueda binaria", r"T(n) = O(\log_{2} n)", "Binary search"),
    ("Ley de Amdahl", r"S = \frac{1}{(1 - p) + \frac{p}{n}}", "Amdahl's law"),
    ("Entropía de Shannon", r"H(X) = -\sum_{i} p_{i} \log_{2} p_{i}", "Shannon entropy"),
    ("Sigmoide", r"\sigma(x) = \frac{1}{1 + e^{-x}}", "Sigmoid"),
    ("Softmax", r"\text{softmax}(z)_{i} = \frac{e^{z_{i}}}{\sum_{j} e^{z_{j}}}", "Softmax"),
    ("ReLU", r"\text{ReLU}(x) = \max(0, x)", "ReLU"),
    ("Neurona artificial", r"y = \sigma\left( \sum_{i} w_{i} x_{i} + b \right)", "Artificial neuron"),
    ("Descenso de gradiente", r"\theta \leftarrow \theta - \eta \nabla_{\theta} J(\theta)", "Gradient descent"),
    ("Entropía cruzada", r"L = -\sum_{i} y_{i} \log \hat{y}_{i}", "Cross-entropy"),
    ("Error cuadrático medio", r"MSE = \frac{1}{n} \sum_{i=1}^{n} (y_{i} - \hat{y}_{i})^{2}", "Mean squared error"),
    ("Distancia euclidiana", r"d(p, q) = \sqrt{\sum_{i} (p_{i} - q_{i})^{2}}", "Euclidean distance"),
    ("Similitud coseno", r"\cos\theta = \frac{A \cdot B}{\|A\| \|B\|}", "Cosine similarity"),
    ("Precisión y exhaustividad", r"P = \frac{TP}{TP + FP}, \quad R = \frac{TP}{TP + FN}", "Precision and recall"),
    ("F1", r"F_{1} = 2 \frac{P R}{P + R}", "F1 score"),
], "Computing: algorithms and AI")
P.formulas_in(G, "Computación: redes y sistemas", [
    ("Capacidad de Shannon", r"C = B \log_{2}(1 + SNR)", "Shannon capacity"),
    ("Retardo de transmisión", r"d_{t} = \frac{L}{R}", "Transmission delay"),
    ("Retardo de propagación", r"d_{p} = \frac{d}{s}", "Propagation delay"),
    ("Hosts por subred", r"N = 2^{32 - n} - 2", "Hosts per subnet"),
    ("Throughput", r"T = \frac{\text{datos}}{\text{tiempo}}", "Throughput"),
    ("Tiempo de acceso efectivo", r"EAT = h \cdot t_{c} + (1 - h) \cdot t_{m}", "Effective access time"),
    ("CPU (tiempo)", r"T_{CPU} = \frac{IC \times CPI}{f}", "CPU time"),
], "Computing: networks and systems")

P.labels = [["TODO", "#dc2626"], ["Bug", "#b91c1c"], ["Entrada", "#2563eb"], ["Salida", "#16a34a"],
            ["Proceso", "#7c3aed"], ["Cuello de botella", "#ea580c"], ["Mejora", "#15803d"], ["KPI", "#0891b2"]]
P.en.update({"Entrada": "Input", "Salida": "Output", "Proceso": "Process", "Cuello de botella": "Bottleneck", "Mejora": "Improvement"})
P.emoji = {"Computación": "💻 🖥️ ⌨️ 🖱️ 💾 📱 🌐 🔒 🔑 🐛 🧩 🤖 📊 📈 📉 ⚙️ 🏭 📦 🚚 ⏱️"}
