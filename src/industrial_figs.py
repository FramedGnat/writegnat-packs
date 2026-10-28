"""Figuras de las materias de Computación e Industrial (estructuras de datos, algoritmos, SO y redes, UML, calidad e inventarios)."""
import math

CDS, CAL, COS, CUM = "Computación: estructuras de datos", "Computación: algoritmos", "Computación: SO y redes", "Computación: UML y software"
IME, ILO = "Industrial: métodos y calidad", "Industrial: logística e inventarios"


def link(g, a, b, r, arrow=False, size=0.035):
    d = math.hypot(b[0] - a[0], b[1] - a[1]); ux, uy = (b[0] - a[0]) / d, (b[1] - a[1]) / d
    p, q = (a[0] + ux * r, a[1] + uy * r), (b[0] - ux * r, b[1] - uy * r)
    g.arrow(*p, *q, size) if arrow else g.line(*p, *q)


def node(g, x, y, text, r=0.07, s=0.5):
    g.circle(x, y, r); g.label(x, y, text, s)


def extend(P):
    P.en.update({CDS: "Computing: data structures", CAL: "Computing: algorithms", COS: "Computing: OS and networks", CUM: "Computing: UML and software",
                 IME: "Industrial: methods and quality", ILO: "Industrial: logistics and inventory"})

    # --- Estructuras de datos ---------------------------------------------------------------------
    @P.figure(CDS, "x-dll", "Lista doblemente enlazada", "Doubly linked list")
    def _(g):
        for k in range(3):
            x = k * 0.36; g.rect(x, -0.08, x + 0.24, 0.08); g.line(x + 0.08, -0.08, x + 0.08, 0.08); g.line(x + 0.16, -0.08, x + 0.16, 0.08)
            g.label(x + 0.12, 0, str(k + 1), 0.45)
            if k < 2: g.arrow(x + 0.24, 0.035, x + 0.36, 0.035, 0.025); g.arrow(x + 0.36, -0.035, x + 0.24, -0.035, 0.025)
        g.label(0.02, 0.17, "∅", 0.5); g.label(0.96, 0.17, "∅", 0.5)

    @P.figure(CDS, "x-circular-queue", "Cola circular", "Circular queue")
    def _(g):
        n = 8
        g.circle(0.5, 0, 0.32); g.circle(0.5, 0, 0.16)
        for k in range(n):
            a = 2 * math.pi * k / n + math.pi / n; g.line(0.5 + 0.16 * math.cos(a), 0.16 * math.sin(a), 0.5 + 0.32 * math.cos(a), 0.32 * math.sin(a))
        for k in range(n):
            a = 2 * math.pi * (k + 0.5) / n + math.pi / n; g.label(0.5 + 0.24 * math.cos(a), 0.24 * math.sin(a), str(k), 0.4)
        g.arrow(0.5 + 0.55, 0.12, 0.5 + 0.36, 0.06, 0.03); g.label(1.14, 0.12, "frente", 0.4)
        g.arrow(0.5 - 0.55, 0.12, 0.5 - 0.36, 0.06, 0.03); g.label(-0.14, 0.12, "final", 0.4)

    @P.figure(CDS, "x-heap", "Montículo (heap) y arreglo", "Heap and array")
    def _(g):
        pts = {0: (0.5, 0.4), 1: (0.28, 0.2), 2: (0.72, 0.2), 3: (0.17, 0.0), 4: (0.39, 0.0), 5: (0.61, 0.0), 6: (0.83, 0.0)}
        vals = [1, 3, 2, 7, 4, 5, 6]
        for i in range(1, 7): link(g, pts[(i - 1) // 2], pts[i], 0.06)
        for i, (x, y) in pts.items(): node(g, x, y, str(vals[i]), 0.06)
        for k in range(7): g.rect(0.08 + k * 0.12, -0.3, 0.2 + k * 0.12, -0.18); g.label(0.14 + k * 0.12, -0.24, str(vals[k]), 0.42)

    @P.figure(CDS, "x-hash", "Tabla hash (encadenamiento)", "Hash table (chaining)")
    def _(g):
        chains = {0: 0, 1: 2, 2: 1, 3: 0, 4: 3}
        for k in range(5):
            y = 0.34 - k * 0.17; g.rect(0, y - 0.07, 0.14, y + 0.07); g.label(-0.07, y, str(k), 0.42)
            x = 0.14
            for j in range(chains[k]):
                g.arrow(x, y, x + 0.12, y, 0.03); g.rect(x + 0.12, y - 0.06, x + 0.3, y + 0.06); x += 0.3
            if chains[k] == 0: g.label(0.24, y, "∅", 0.45)
        g.label(0.55, 0.45, "h(k) = k mod 5", 0.5)

    @P.figure(CDS, "x-bst", "Árbol de búsqueda (BST)", "Binary search tree")
    def _(g):
        P_ = {8: (0.5, 0.36), 3: (0.28, 0.12), 10: (0.74, 0.12), 1: (0.16, -0.12), 6: (0.4, -0.12), 14: (0.88, -0.12)}
        par = {3: 8, 10: 8, 1: 3, 6: 3, 14: 10}
        for c, p in par.items(): link(g, P_[p], P_[c], 0.065)
        for v, (x, y) in P_.items(): node(g, x, y, str(v), 0.065)
        g.label(0.5, -0.32, "izq < raíz < der", 0.45)

    @P.figure(CDS, "x-avl", "Rotación AVL simple", "AVL rotation")
    def _(g):
        for (x, y), t in (((0.1, 0.3), "3"), ((0.0, 0.1), "2"), ((-0.1, -0.1), "1")): node(g, x, y, t, 0.06)
        link(g, (0.1, 0.3), (0.0, 0.1), 0.06); link(g, (0.0, 0.1), (-0.1, -0.1), 0.06)
        g.arrow(0.25, 0.1, 0.5, 0.1, 0.04); g.label(0.375, 0.2, "rotar", 0.42)
        for (x, y), t in (((0.78, 0.3), "2"), ((0.65, 0.05), "1"), ((0.91, 0.05), "3")): node(g, x, y, t, 0.06)
        link(g, (0.78, 0.3), (0.65, 0.05), 0.06); link(g, (0.78, 0.3), (0.91, 0.05), 0.06)

    @P.figure(CDS, "x-trie", "Trie (árbol de prefijos)", "Trie")
    def _(g):
        P_ = {"r": (0.5, 0.35), "c": (0.25, 0.1), "d": (0.75, 0.1), "a": (0.25, -0.15), "o": (0.75, -0.15), "t": (0.12, -0.38), "s": (0.38, -0.38)}
        for ch, p in (("c", "r"), ("d", "r"), ("a", "c"), ("o", "d"), ("t", "a"), ("s", "a")): link(g, P_[p], P_[ch], 0.055)
        for k, (x, y) in P_.items(): node(g, x, y, "" if k == "r" else k, 0.055, 0.5)
        g.label(1.0, -0.38, "cat, cas, do", 0.42)

    @P.figure(CDS, "x-digraph", "Grafo dirigido con pesos", "Weighted digraph")
    def _(g):
        P_ = [(0.1, 0.0), (0.45, 0.3), (0.45, -0.3), (0.9, 0.0)]
        for a, b, w, off in ((0, 1, "4", (-0.05, 0.08)), (0, 2, "2", (-0.05, -0.08)), (1, 3, "5", (0.06, 0.08)), (2, 3, "1", (0.06, -0.08)), (1, 2, "3", (0.07, 0))):
            link(g, P_[a], P_[b], 0.06, True)
            g.label((P_[a][0] + P_[b][0]) / 2 + off[0], (P_[a][1] + P_[b][1]) / 2 + off[1], w, 0.42)
        for i, (x, y) in enumerate(P_): node(g, x, y, "ABCD"[i], 0.06)

    # --- Algoritmos --------------------------------------------------------------------------------
    @P.figure(CAL, "x-sort", "Ordenamiento (barras)", "Sorting bars")
    def _(g):
        h = [0.5, 0.2, 0.4, 0.1, 0.3]
        for k, v in enumerate(h): g.rect(k * 0.2, 0, k * 0.2 + 0.16, v, fill=(k in (1, 3)))
        g.arrow(0.28, 0.58, 0.68, 0.58, 0.03); g.arrow(0.68, 0.62, 0.28, 0.62, 0.03) if False else None
        g.label(0.48, 0.67, "intercambio", 0.4); g.line(0, 0, 0.96, 0)

    @P.figure(CAL, "x-bigo", "Complejidad O(n)", "Big-O curves")
    def _(g):
        g.arrow(0, 0, 1.0, 0, 0.03); g.arrow(0, 0, 0, 0.75, 0.03)
        g.curve(lambda x: x * 0.4, 0, 0.95); g.curve(lambda x: min(0.7, 0.55 * x * math.log2(1 + 3 * x) / 2), 0, 0.95)
        g.curve(lambda x: min(0.7, 0.75 * x * x), 0, 0.95); g.curve(lambda x: min(0.7, 0.04 * (2 ** (6 * x) - 1) / 4), 0, 0.95)
        g.label(1.0, 0.36, "n", 0.45); g.label(1.0, 0.1, "log n", 0.0) if False else None
        g.label(0.98, 0.52, "n log n", 0.4); g.label(0.78, 0.74, "n²", 0.45); g.label(0.52, 0.74, "2ⁿ", 0.45); g.label(1.05, -0.07, "n", 0.4); g.label(-0.07, 0.75, "t", 0.4)

    @P.figure(CAL, "x-flowchart", "Diagrama de flujo (símbolos)", "Flowchart")
    def _(g):
        g.ellipse(0.5, 0.45, 0.2, 0.06); g.label(0.5, 0.45, "Inicio", 0.45); g.arrow(0.5, 0.39, 0.5, 0.33, 0.03)
        g.poly(0.32, 0.31, 0.74, 0.31, 0.68, 0.19, 0.26, 0.19); g.label(0.5, 0.25, "Leer n", 0.45); g.arrow(0.5, 0.19, 0.5, 0.13, 0.03)
        g.poly(0.5, 0.13, 0.72, -0.01, 0.5, -0.15, 0.28, -0.01); g.label(0.5, -0.01, "n>0?", 0.45)
        g.arrow(0.72, -0.01, 0.9, -0.01, 0.03); g.label(0.82, 0.04, "no", 0.35); g.label(0.55, -0.2, "sí", 0.35)
        g.arrow(0.5, -0.15, 0.5, -0.22, 0.03); g.rect(0.3, -0.22, 0.7, -0.34); g.label(0.5, -0.28, "Proceso", 0.45)
        g.ellipse(0.95, -0.01, 0.0, 0.0) if False else g.ellipse(1.0, -0.01, 0.1, 0.05); g.label(1.0, -0.01, "Fin", 0.4)

    @P.figure(CAL, "x-recursion", "Árbol de recursión (Fibonacci)", "Recursion tree")
    def _(g):
        P_ = {"4": (0.5, 0.38), "3": (0.28, 0.16), "2a": (0.72, 0.16), "2b": (0.14, -0.06), "1a": (0.42, -0.06), "1b": (0.62, -0.06), "0a": (0.82, -0.06)}
        T = {"4": "f(4)", "3": "f(3)", "2a": "f(2)", "2b": "f(2)", "1a": "f(1)", "1b": "f(1)", "0a": "f(0)"}
        for c, p in (("3", "4"), ("2a", "4"), ("2b", "3"), ("1a", "3"), ("1b", "2a"), ("0a", "2a")): link(g, P_[p], P_[c], 0.07)
        for k, (x, y) in P_.items(): g.ellipse(x, y, 0.075, 0.05); g.label(x, y, T[k], 0.38)

    # --- Sistemas operativos y redes -------------------------------------------------------------
    @P.figure(COS, "x-proc-states", "Estados de un proceso", "Process states")
    def _(g):
        P_ = {"Nuevo": (0.0, 0.2), "Listo": (0.45, 0.2), "Ejecución": (0.95, 0.2), "Terminado": (1.45, 0.2), "Espera": (0.7, -0.25)}
        for k, (x, y) in P_.items(): g.ellipse(x, y, 0.18, 0.075); g.label(x, y, k, 0.4)
        g.arrow(0.18, 0.2, 0.27, 0.2, 0.03); g.arrow(0.63, 0.23, 0.77, 0.23, 0.03); g.arrow(0.77, 0.17, 0.63, 0.17, 0.03)
        g.arrow(1.13, 0.2, 1.27, 0.2, 0.03); g.arrow(0.9, 0.13, 0.78, -0.18, 0.03); g.arrow(0.6, -0.18, 0.48, 0.13, 0.03)
        g.label(0.7, 0.3, "despacho / expiración", 0.3)

    @P.figure(COS, "x-paging", "Paginación de memoria", "Memory paging")
    def _(g):
        for k in range(4): g.rect(0, 0.3 - k * 0.14, 0.2, 0.42 - k * 0.14); g.label(0.1, 0.36 - k * 0.14, f"P{k}", 0.42)
        for k in range(4): g.rect(0.4, 0.3 - k * 0.14, 0.6, 0.42 - k * 0.14); g.label(0.5, 0.36 - k * 0.14, ["3", "0", "5", "1"][k], 0.42)
        for k in range(6): g.rect(0.8, 0.44 - k * 0.14, 1.0, 0.56 - k * 0.14 - 0.0); g.label(0.9, 0.5 - k * 0.14, f"M{k}", 0.4)
        g.label(0.1, 0.52, "lógica", 0.4); g.label(0.5, 0.52, "tabla", 0.4); g.label(0.9, 0.62, "física", 0.4)
        for k, f in enumerate((3, 0, 5, 1)): g.arrow(0.6, 0.36 - k * 0.14, 0.8, 0.5 - f * 0.14, 0.03); g.arrow(0.2, 0.36 - k * 0.14, 0.4, 0.36 - k * 0.14, 0.03)

    @P.figure(COS, "x-osi", "Modelo OSI (7 capas)", "OSI model")
    def _(g):
        for k, t in enumerate(("Aplicación", "Presentación", "Sesión", "Transporte", "Red", "Enlace", "Física")):
            y = 0.42 - k * 0.13; g.rect(0, y - 0.11, 0.7, y); g.label(0.35, y - 0.055, f"{7 - k}  {t}", 0.45)
        g.label(0.95, 0.3, "datos", 0.4); g.label(0.95, 0.0, "segmentos", 0.35); g.label(0.95, -0.08, "paquetes", 0.35); g.label(0.95, -0.2, "bits", 0.4)

    @P.figure(COS, "x-bus-ring", "Topologías bus y anillo", "Bus and ring topologies")
    def _(g):
        g.line(0, 0.1, 0.9, 0.1)
        for k in range(4): x = 0.1 + k * 0.23; g.line(x, 0.1, x, -0.05); g.rect(x - 0.07, -0.05, x + 0.07, -0.17)
        g.circle(0.5, -0.5, 0.2)
        for k in range(5):
            a = 2 * math.pi * k / 5 + math.pi / 2; g.circle(0.5 + 0.2 * math.cos(a), -0.5 + 0.2 * math.sin(a), 0.05, fill=True)

    @P.figure(COS, "x-client-server", "Cliente-servidor", "Client-server")
    def _(g):
        g.rect(0, -0.12, 0.25, 0.12); g.rect(0.03, -0.09, 0.22, 0.09); g.label(0.12, -0.2, "Cliente", 0.4)
        g.rect(0.75, -0.2, 0.95, 0.2); g.line(0.75, 0.07, 0.95, 0.07); g.line(0.75, -0.07, 0.95, -0.07); g.label(0.85, -0.29, "Servidor", 0.4)
        g.arrow(0.3, 0.06, 0.7, 0.06, 0.03); g.label(0.5, 0.13, "petición", 0.4); g.arrow(0.7, -0.06, 0.3, -0.06, 0.03); g.label(0.5, -0.13, "respuesta", 0.4)

    @P.figure(COS, "x-tcp", "Saludo de tres vías (TCP)", "TCP three-way handshake")
    def _(g):
        g.line(0.05, 0.4, 0.05, -0.4); g.line(0.95, 0.4, 0.95, -0.4); g.label(0.05, 0.47, "Cliente", 0.45); g.label(0.95, 0.47, "Servidor", 0.45)
        g.arrow(0.05, 0.25, 0.95, 0.1, 0.04); g.label(0.5, 0.25, "SYN", 0.45)
        g.arrow(0.95, -0.05, 0.05, -0.2, 0.04); g.label(0.5, -0.0, "SYN + ACK", 0.45)
        g.arrow(0.05, -0.3, 0.95, -0.45, 0.04) if False else g.arrow(0.05, -0.3, 0.95, -0.4, 0.04); g.label(0.5, -0.27, "ACK", 0.45)

    @P.figure(COS, "x-memory-pyramid", "Jerarquía de memoria", "Memory hierarchy")
    def _(g):
        g.poly(0.5, 0.45, 0.95, -0.4, 0.05, -0.4)
        for k, y in enumerate((0.2, -0.0, -0.2)):
            w = 0.5 - 0.5 * (y + 0.4) / 0.85 * 0.0
            xr = (0.45 * (0.45 - y) / 0.85)
            g.line(0.5 - xr, y, 0.5 + xr, y)
        for t, y in (("Registros", 0.3), ("Caché", 0.1), ("RAM", -0.1), ("Disco", -0.3)): g.label(0.5, y, t, 0.42)
        g.arrow(1.1, -0.35, 1.1, 0.35, 0.04); g.label(1.22, 0.0, "más rápida", 0.35)

    @P.figure(COS, "x-von-neumann", "Arquitectura de von Neumann", "Von Neumann architecture")
    def _(g):
        g.rect(0.0, 0.1, 0.4, 0.4); g.label(0.2, 0.3, "CPU", 0.5); g.rect(0.04, 0.14, 0.18, 0.24); g.label(0.11, 0.19, "ALU", 0.35); g.rect(0.22, 0.14, 0.36, 0.24); g.label(0.29, 0.19, "UC", 0.35)
        g.rect(0.6, 0.1, 1.0, 0.4); g.label(0.8, 0.25, "Memoria", 0.5)
        g.rect(0.0, -0.4, 0.4, -0.2); g.label(0.2, -0.3, "Entrada", 0.45); g.rect(0.6, -0.4, 1.0, -0.2); g.label(0.8, -0.3, "Salida", 0.45)
        g.line(0.0, -0.04, 1.0, -0.04); g.line(0.0, 0.0, 1.0, 0.0); g.label(0.5, -0.1, "buses", 0.38)
        for x in (0.2, 0.8): g.line(x, 0.0, x, 0.1)
        for x in (0.2, 0.8): g.line(x, -0.04, x, -0.2)

    # --- UML y software ---------------------------------------------------------------------------
    @P.figure(CUM, "x-activity", "Diagrama de actividades", "Activity diagram")
    def _(g):
        g.circle(0.5, 0.45, 0.04, fill=True); g.arrow(0.5, 0.41, 0.5, 0.36, 0.03)
        g.rect(0.33, 0.2, 0.67, 0.36); g.label(0.5, 0.28, "Acción", 0.45); g.arrow(0.5, 0.2, 0.5, 0.14, 0.03)
        g.poly(0.5, 0.14, 0.58, 0.07, 0.5, 0.0, 0.42, 0.07); g.arrow(0.58, 0.07, 0.8, 0.07, 0.03); g.arrow(0.42, 0.07, 0.2, 0.07, 0.03)
        g.rect(0.7, -0.07, 0.95, 0.07, fill=False) if False else None
        g.rect(0.62, -0.1, 0.98, 0.04) if False else None
        g.line(0.1, -0.12, 0.9, -0.12); g.line(0.1, -0.15, 0.9, -0.15)
        g.line(0.2, 0.07, 0.2, -0.12); g.line(0.8, 0.07, 0.8, -0.12)
        g.arrow(0.5, -0.15, 0.5, -0.24, 0.03); g.circle(0.5, -0.3, 0.05); g.circle(0.5, -0.3, 0.03, fill=True)

    @P.figure(CUM, "x-component", "Diagrama de componentes", "Component diagram")
    def _(g):
        for x0, t in ((0.0, "Interfaz"), (0.7, "Datos")):
            g.rect(x0, -0.12, x0 + 0.3, 0.12); g.rect(x0 - 0.04, 0.03, x0 + 0.04, 0.09); g.rect(x0 - 0.04, -0.09, x0 + 0.04, -0.03); g.label(x0 + 0.16, 0, t, 0.45)
        g.circle(0.5, 0.0, 0.04); g.line(0.3, 0.0, 0.46, 0.0); g.arc(0.7, 0.0, 0.08, 0.08, 90, 270); g.line(0.7, 0.0, 0.54, 0.0) if False else g.line(0.7, 0.0, 0.62, 0.0)
        g.label(0.5, 0.12, "API", 0.4)

    @P.figure(CUM, "x-package", "Paquete UML", "UML package")
    def _(g):
        g.rect(0, 0.2, 0.3, 0.3); g.rect(0, -0.25, 0.8, 0.2); g.label(0.4, 0.0, "Dominio", 0.55)
        g.rect(0.9, -0.05, 1.3, 0.1) if False else None
        g.line(1.0, -0.05, 0.8, -0.05) if False else None
        g.arrow(0.8, -0.1, 1.05, -0.1, 0.03, dashed=True); g.rect(1.05, -0.2, 1.4, 0.0); g.label(1.22, -0.1, "BD", 0.5)

    @P.figure(CUM, "x-crowfoot", "E-R con patas de gallo (1:N)", "ER crow's foot")
    def _(g):
        g.rect(0.0, -0.1, 0.3, 0.1); g.label(0.15, 0.0, "Cliente", 0.45); g.rect(0.7, -0.1, 1.0, 0.1); g.label(0.85, 0.0, "Pedido", 0.45)
        g.line(0.3, 0.0, 0.7, 0.0); g.line(0.35, 0.05, 0.35, -0.05); g.line(0.4, 0.05, 0.4, -0.05)
        g.line(0.7, 0.0, 0.6, 0.06); g.line(0.7, 0.0, 0.6, -0.06); g.line(0.7, 0.0, 0.6, 0.0); g.circle(0.55, 0.0, 0.03)
        g.label(0.5, 0.12, "realiza", 0.4)

    @P.figure(CUM, "x-dfd", "Diagrama de flujo de datos", "Data-flow diagram")
    def _(g):
        g.rect(0, -0.1, 0.22, 0.1); g.label(0.11, 0.0, "Usuario", 0.4)
        g.circle(0.55, 0.0, 0.14); g.label(0.55, 0.0, "1 Procesar", 0.38)
        g.line(0.8, 0.1, 1.15, 0.1); g.line(0.8, -0.1, 1.15, -0.1); g.line(0.8, 0.1, 0.8, -0.1); g.label(0.98, 0.0, "Datos", 0.4)
        g.arrow(0.22, 0.03, 0.41, 0.03, 0.03); g.label(0.32, 0.1, "pedido", 0.33); g.arrow(0.69, 0.0, 0.8, 0.0, 0.03)

    @P.figure(CUM, "x-3tier", "Arquitectura en capas", "Layered architecture")
    def _(g):
        for k, t in enumerate(("Presentación", "Lógica de negocio", "Acceso a datos", "Base de datos")):
            y = 0.35 - k * 0.2; g.rect(0, y - 0.15, 0.8, y); g.label(0.4, y - 0.075, t, 0.5)
            if k < 3: g.double_arrow(0.4, y - 0.15, 0.4, y - 0.2, 0.025)

    @P.figure(CUM, "x-mvc", "Patrón MVC", "MVC pattern")
    def _(g):
        for x, y, t in ((0.5, 0.35, "Controlador"), (0.1, -0.1, "Vista"), (0.9, -0.1, "Modelo")):
            g.rect(x - 0.17, y - 0.07, x + 0.17, y + 0.07); g.label(x, y, t, 0.4)
        g.arrow(0.3, -0.03, 0.4, 0.28, 0.03); g.arrow(0.6, 0.28, 0.75, -0.03, 0.03); g.arrow(0.73, -0.12, 0.27, -0.12, 0.03, dashed=True)
        g.label(0.15, 0.13, "evento", 0.3); g.label(0.85, 0.13, "actualiza", 0.3); g.label(0.5, -0.2, "notifica", 0.3)

    @P.figure(CUM, "x-git", "Ramas de Git", "Git branches")
    def _(g):
        g.line(0, 0.2, 1.0, 0.2); g.line(0.2, 0.2, 0.3, -0.05, 0.7, -0.05, 0.8, 0.2)
        for x in (0.0, 0.2, 0.5, 0.8, 1.0): g.circle(x, 0.2, 0.025, fill=True)
        for x in (0.3, 0.5, 0.7): g.circle(x, -0.05, 0.025, fill=True)
        g.label(0.05, 0.3, "main", 0.4); g.label(0.5, -0.17, "feature", 0.4); g.label(0.8, 0.3, "merge", 0.35)

    # --- Industrial: métodos y calidad -----------------------------------------------------------
    @P.figure(IME, "x-histogram", "Histograma", "Histogram")
    def _(g):
        h = [0.08, 0.2, 0.38, 0.5, 0.32, 0.16, 0.06]
        for k, v in enumerate(h): g.rect(k * 0.14, 0, (k + 1) * 0.14, v)
        g.arrow(0, 0, 1.05, 0, 0.03); g.arrow(0, 0, 0, 0.6, 0.03); g.label(0.5, -0.08, "clases", 0.4); g.label(-0.07, 0.6, "f", 0.4)

    @P.figure(IME, "x-spec", "Capacidad del proceso (LIE/LSE)", "Process capability")
    def _(g):
        g.curve(lambda x: 0.55 * math.exp(-((x - 0.5) ** 2) / (2 * 0.12 ** 2)), 0.05, 0.95); g.line(0, 0, 1, 0)
        for x, t in ((0.2, "LIE"), (0.8, "LSE")): g.line(x, -0.04, x, 0.5, dashed=True); g.label(x, -0.1, t, 0.45)
        g.line(0.5, 0.0, 0.5, 0.56, dashed=True); g.label(0.5, 0.64, "μ", 0.5); g.label(0.5, -0.2, "Cp = (LSE − LIE) / 6σ", 0.42)

    @P.figure(IME, "x-scatter", "Diagrama de dispersión", "Scatter plot")
    def _(g):
        g.arrow(0, 0, 1.0, 0, 0.03); g.arrow(0, 0, 0, 0.7, 0.03)
        for x, y in ((0.1, 0.12), (0.2, 0.2), (0.28, 0.18), (0.38, 0.33), (0.45, 0.3), (0.55, 0.42), (0.65, 0.45), (0.72, 0.55), (0.85, 0.58)): g.circle(x, y, 0.015, fill=True)
        g.line(0.05, 0.08, 0.92, 0.62, dashed=True); g.label(0.9, 0.7, "r > 0", 0.4)

    @P.figure(IME, "x-plant-u", "Distribución en U (celda)", "U-shaped cell layout")
    def _(g):
        g.line(0, 0, 1, 0, 1, 0.6, 0, 0.6, 0, 0.0)
        g.line(0.25, 0.2, 0.75, 0.2, 0.75, 0.4, 0.25, 0.4) if False else None
        for k, (x, y) in enumerate(((0.15, 0.1), (0.5, 0.1), (0.85, 0.1), (0.85, 0.5), (0.5, 0.5), (0.15, 0.5))):
            g.rect(x - 0.08, y - 0.07, x + 0.08, y + 0.07); g.label(x, y, str(k + 1), 0.5)
        for a, b in (((0.23, 0.1), (0.42, 0.1)), ((0.58, 0.1), (0.77, 0.1)), ((0.85, 0.17), (0.85, 0.43)), ((0.77, 0.5), (0.58, 0.5)), ((0.42, 0.5), (0.23, 0.5))): g.arrow(*a, *b, 0.03)
        g.label(0.5, 0.3, "operario", 0.45); g.circle(0.5, 0.25, 0.03)

    @P.figure(IME, "x-vsm", "Mapa de flujo de valor (VSM)", "Value stream map")
    def _(g):
        for k, t in enumerate(("Corte", "Soldar", "Pintar")):
            x = k * 0.4; g.rect(x, 0.0, x + 0.28, 0.2); g.label(x + 0.14, 0.12, t, 0.45); g.rect(x, -0.12, x + 0.28, 0.0); g.label(x + 0.14, -0.06, "CT 40 s", 0.3)
            if k < 2: g.poly(x + 0.3, 0.15, x + 0.36, 0.15, x + 0.33, 0.05); g.label(x + 0.33, 0.22, "I", 0.3)
        g.line(0, -0.3, 0.16, -0.3, 0.16, -0.38, 0.38, -0.38, 0.38, -0.3, 0.6, -0.3, 0.6, -0.38, 0.8, -0.38, 0.8, -0.3, 1.0, -0.3); g.label(0.5, -0.22, "línea de tiempo (lead time)", 0.35)

    @P.figure(IME, "x-kanban", "Tablero Kanban", "Kanban board")
    def _(g):
        for k, t in enumerate(("Por hacer", "En curso", "Hecho")):
            x = k * 0.36; g.rect(x, -0.3, x + 0.3, 0.35); g.line(x, 0.25, x + 0.3, 0.25); g.label(x + 0.15, 0.3, t, 0.4)
        for x, y in ((0.04, 0.12), (0.04, -0.02), (0.04, -0.16), (0.4, 0.12), (0.76, 0.12), (0.76, -0.02)): g.rect(x, y, x + 0.22, y + 0.1)

    @P.figure(IME, "x-man-machine", "Diagrama hombre-máquina", "Man-machine chart")
    def _(g):
        g.rect(0, -0.4, 0.4, 0.4); g.rect(0.4, -0.4, 0.8, 0.4); g.label(0.2, 0.46, "Operario", 0.4); g.label(0.6, 0.46, "Máquina", 0.4)
        g.rect(0, 0.2, 0.4, 0.4, fill=True); g.rect(0.4, 0.2, 0.8, 0.4, fill=False); g.rect(0, -0.1, 0.4, 0.2); g.rect(0.4, -0.4, 0.8, 0.2, fill=True)
        g.rect(0, -0.4, 0.4, -0.1, fill=True); g.label(0.2, 0.3, "carga", 0.3); g.label(0.6, 0.0, "opera", 0.3); g.label(0.2, 0.05, "espera", 0.3)

    @P.figure(IME, "x-ergo", "Ergonomía: zona de alcance", "Ergonomics reach zone")
    def _(g):
        g.circle(0.2, 0.42, 0.07); g.line(0.2, 0.35, 0.2, 0.05, 0.38, -0.02, 0.38, -0.3); g.line(0.2, 0.05, 0.05, -0.02, 0.05, -0.3)
        g.line(0.2, 0.3, 0.55, 0.15); g.line(0.0, -0.3, 0.45, -0.3)
        g.arc(0.2, 0.3, 0.55, 0.45, -50, 20, dashed=True); g.arc(0.2, 0.3, 0.3, 0.25, -60, 30, dashed=True)
        g.line(0.55, 0.0, 1.0, 0.0); g.line(0.55, 0.0, 0.55, -0.3); g.line(1.0, 0.0, 1.0, -0.3)
        g.label(0.85, 0.15, "área de trabajo", 0.35)

    @P.figure(IME, "x-learning", "Curva de aprendizaje", "Learning curve")
    def _(g):
        g.arrow(0, 0, 1.0, 0, 0.03); g.arrow(0, 0, 0, 0.7, 0.03)
        g.curve(lambda x: 0.12 + 0.5 * math.exp(-4 * x), 0, 0.95); g.line(0, 0.12, 0.95, 0.12, dashed=True)
        g.label(0.5, -0.08, "unidades acumuladas", 0.35); g.label(-0.1, 0.66, "tiempo", 0.35)

    # --- Industrial: logística e inventarios -----------------------------------------------------
    @P.figure(ILO, "x-eoq", "Inventario (diente de sierra)", "Inventory sawtooth")
    def _(g):
        g.arrow(0, 0, 1.05, 0, 0.03); g.arrow(0, 0, 0, 0.6, 0.03)
        for k in range(3): x = k * 0.32; g.line(x, 0.45, x + 0.32, 0.0)
        for k in range(1, 3): g.line(k * 0.32, 0.0, k * 0.32, 0.45)
        g.line(0, 0.2, 1.0, 0.2, dashed=True); g.label(1.08, 0.2, "ROP", 0.35); g.label(-0.1, 0.45, "Q", 0.4); g.label(0.5, -0.08, "tiempo", 0.4)

    @P.figure(ILO, "x-breakeven", "Punto de equilibrio", "Break-even point")
    def _(g):
        g.arrow(0, 0, 1.05, 0, 0.03); g.arrow(0, 0, 0, 0.8, 0.03)
        g.line(0, 0.2, 1.0, 0.45); g.line(0, 0, 1.0, 0.7); g.line(0, 0.2, 1.0, 0.2, dashed=True)
        g.circle(0.8, 0.56, 0.02, fill=True); g.label(1.1, 0.7, "ingresos", 0.35); g.label(1.1, 0.45, "costo total", 0.35); g.label(1.1, 0.2, "costo fijo", 0.35); g.label(0.8, -0.08, "Q*", 0.4)

    @P.figure(ILO, "x-supply-chain", "Cadena de suministro", "Supply chain")
    def _(g):
        for k, t in enumerate(("Proveedor", "Fábrica", "Almacén", "Tienda", "Cliente")):
            x = k * 0.27; g.rect(x, -0.1, x + 0.22, 0.1); g.label(x + 0.11, 0.0, t, 0.28)
            if k < 4: g.arrow(x + 0.22, 0.03, x + 0.27, 0.03, 0.025); g.arrow(x + 0.27, -0.04, x + 0.22, -0.04, 0.025) if False else None
        g.arrow(1.07, -0.18, 0.0, -0.18, 0.03, dashed=True); g.label(0.55, -0.26, "flujo de información", 0.35); g.label(0.55, 0.2, "flujo de producto →", 0.35)

    @P.figure(ILO, "x-queue-system", "Sistema de colas (M/M/1)", "Queueing system")
    def _(g):
        g.arrow(-0.1, 0, 0.1, 0, 0.03); g.label(-0.05, 0.1, "λ", 0.5)
        for k in range(4): g.circle(0.18 + k * 0.1, 0, 0.03)
        g.line(0.12, 0.06, 0.6, 0.06); g.line(0.12, -0.06, 0.6, -0.06); g.line(0.6, 0.06, 0.6, -0.06)
        g.circle(0.8, 0, 0.12); g.label(0.8, 0, "servidor", 0.3); g.arrow(0.92, 0, 1.12, 0, 0.03); g.label(1.05, 0.1, "μ", 0.5)

    @P.figure(ILO, "x-decision-tree", "Árbol de decisión", "Decision tree")
    def _(g):
        g.rect(0, -0.05, 0.1, 0.05); g.line(0.1, 0, 0.3, 0.25); g.line(0.1, 0, 0.3, -0.25)
        g.circle(0.35, 0.25, 0.05); g.circle(0.35, -0.25, 0.05)
        g.line(0.4, 0.25, 0.7, 0.4); g.line(0.4, 0.25, 0.7, 0.1); g.line(0.4, -0.25, 0.7, -0.1); g.line(0.4, -0.25, 0.7, -0.4)
        for y, t in ((0.4, "+80"), (0.1, "−20"), (-0.1, "+30"), (-0.4, "0")): g.label(0.82, y, t, 0.42)
        g.label(0.55, 0.38, "p", 0.3); g.label(0.55, 0.12, "1−p", 0.3)
