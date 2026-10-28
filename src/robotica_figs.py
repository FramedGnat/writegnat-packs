"""Figuras de Control, modelado y respuesta (Control I–IV, Teoría de sistemas, Modelado y simulación, Actuadores)."""
import math

BD = "Control: diagramas de bloques"
RS = "Control: respuesta y análisis"
SY = "Control: sistemas"


def blk(g, u0, v0, u1, v1, text, s=0.7):
    g.rect(u0, v0, u1, v1); g.label((u0 + u1) / 2, (v0 + v1) / 2, text, s)


def ar(g, u0, v0, u1, v1, size=0.035): g.arrow(u0, v0, u1, v1, size)


def sumj(g, u, v, r=0.045):
    g.circle(u, v, r); k = r * 0.68
    g.line(u - k, v - k, u + k, v + k); g.line(u - k, v + k, u + k, v - k)


def dot(g, u, v): g.circle(u, v, 0.012, fill=True)


def axes(g, u0, v0, u1, v1, xl="t", yl="y", up=0.04):
    g.arrow(u0, v0, u1, v0, up); g.arrow(u0, v0, u0, v1, up)
    g.label(u1 - 0.01, v0 - 0.06, xl, 0.7); g.label(u0 - 0.05, v1 - 0.01, yl, 0.7)


def extend(P):
    P.en.update({BD: "Control: block diagrams", RS: "Control: response and analysis", SY: "Control: systems"})

    # ---------------- Diagramas de bloques ----------------
    @P.figure(BD, "bd-block", "Bloque G(s)", "Block G(s)")
    def _(g):
        ar(g, 0, 0, 0.3, 0); blk(g, 0.3, -0.18, 0.7, 0.18, "G(s)", 1.0); ar(g, 0.7, 0, 1, 0)
        g.label(0.1, 0.07, "U(s)", 0.7); g.label(0.9, 0.07, "Y(s)", 0.7)

    @P.figure(BD, "bd-sum", "Sumador (comparador)", "Summing junction")
    def _(g):
        sumj(g, 0.5, 0, 0.12); ar(g, 0.05, 0, 0.38, 0); ar(g, 0.5, -0.4, 0.5, -0.12); ar(g, 0.62, 0, 0.98, 0)
        g.label(0.3, 0.1, "+", 0.9); g.label(0.58, -0.2, "−", 0.9); g.label(0.05, 0.1, "R(s)", 0.6); g.label(0.5, -0.46, "B(s)", 0.6); g.label(0.94, 0.1, "E(s)", 0.6)

    @P.figure(BD, "bd-branch", "Punto de bifurcación", "Branch point")
    def _(g):
        ar(g, 0, 0, 0.45, 0); dot(g, 0.45, 0); g.line(0.45, 0, 1, 0); g.head(0.45, 0, 1, 0, 0.035)
        g.arrow(0.45, 0, 0.45, -0.4, 0.035); g.label(0.08, 0.08, "Y(s)", 0.6); g.label(0.93, 0.08, "Y(s)", 0.6); g.label(0.6, -0.4, "Y(s)", 0.6)

    @P.figure(BD, "bd-open", "Lazo abierto", "Open loop")
    def _(g):
        ar(g, 0, 0, 0.14, 0); blk(g, 0.14, -0.16, 0.5, 0.16, "Gc(s)"); ar(g, 0.5, 0, 0.62, 0)
        blk(g, 0.62, -0.16, 0.88, 0.16, "Gp(s)"); ar(g, 0.88, 0, 1, 0)
        g.label(0.04, 0.09, "R", 0.7); g.label(0.57, 0.09, "U", 0.7); g.label(0.97, 0.09, "Y", 0.7)
        g.label(0.32, -0.26, "controlador", 0.5); g.label(0.75, -0.26, "planta", 0.5)

    @P.figure(BD, "bd-closed", "Lazo cerrado", "Closed loop")
    def _(g):
        ar(g, 0, 0, 0.19, 0); sumj(g, 0.235, 0); ar(g, 0.28, 0, 0.4, 0); blk(g, 0.4, -0.12, 0.64, 0.12, "G(s)"); g.line(0.64, 0, 0.93, 0); g.head(0.64, 0, 0.93, 0, 0.035)
        dot(g, 0.78, 0); g.line(0.78, 0, 0.78, -0.32); g.line(0.78, -0.32, 0.64, -0.32); blk(g, 0.4, -0.44, 0.64, -0.2, "H(s)")
        g.line(0.4, -0.32, 0.235, -0.32); g.arrow(0.235, -0.32, 0.235, -0.045, 0.035)
        g.label(0.03, 0.08, "R(s)", 0.6); g.label(0.96, 0.08, "Y(s)", 0.6); g.label(0.19, 0.09, "+", 0.7); g.label(0.285, -0.09, "−", 0.7); g.label(0.34, 0.08, "E", 0.6)

    @P.figure(BD, "bd-unity", "Realimentación unitaria", "Unity feedback")
    def _(g):
        ar(g, 0, 0, 0.19, 0); sumj(g, 0.235, 0); ar(g, 0.28, 0, 0.4, 0); blk(g, 0.4, -0.12, 0.64, 0.12, "G(s)"); g.line(0.64, 0, 0.93, 0); g.head(0.64, 0, 0.93, 0, 0.035)
        dot(g, 0.78, 0); g.line(0.78, 0, 0.78, -0.3); g.line(0.78, -0.3, 0.235, -0.3); g.arrow(0.235, -0.3, 0.235, -0.045, 0.035)
        g.label(0.03, 0.08, "R(s)", 0.6); g.label(0.96, 0.08, "Y(s)", 0.6); g.label(0.19, 0.09, "+", 0.7); g.label(0.285, -0.09, "−", 0.7); g.label(0.51, -0.38, "H(s) = 1", 0.55)

    @P.figure(BD, "bd-equivalent", "Lazo cerrado equivalente", "Equivalent closed loop")
    def _(g):
        ar(g, 0, 0, 0.2, 0); blk(g, 0.2, -0.17, 0.8, 0.17, "G / (1 + G·H)", 0.9); ar(g, 0.8, 0, 1, 0)
        g.label(0.07, 0.08, "R(s)", 0.6); g.label(0.92, 0.08, "Y(s)", 0.6)
        g.label(0.5, -0.3, "Y/R = G/(1+GH)", 0.6)

    @P.figure(BD, "bd-series", "Bloques en serie", "Blocks in series")
    def _(g):
        ar(g, 0, 0, 0.1, 0); blk(g, 0.1, -0.14, 0.3, 0.14, "G₁"); ar(g, 0.3, 0, 0.4, 0); blk(g, 0.4, -0.14, 0.6, 0.14, "G₂"); ar(g, 0.6, 0, 0.7, 0)
        blk(g, 0.7, -0.14, 0.9, 0.14, "G₃"); ar(g, 0.9, 0, 1, 0); g.label(0.5, -0.3, "G = G₁·G₂·G₃", 0.6)

    @P.figure(BD, "bd-parallel", "Bloques en paralelo", "Blocks in parallel")
    def _(g):
        ar(g, 0, 0, 0.1, 0); dot(g, 0.1, 0); g.line(0.1, 0, 0.1, 0.25); g.line(0.1, 0, 0.1, -0.25)
        ar(g, 0.1, 0.25, 0.3, 0.25); blk(g, 0.3, 0.13, 0.6, 0.37, "G₁"); g.line(0.6, 0.25, 0.8, 0.25)
        ar(g, 0.1, -0.25, 0.3, -0.25); blk(g, 0.3, -0.37, 0.6, -0.13, "G₂"); g.line(0.6, -0.25, 0.8, -0.25)
        g.line(0.8, 0.25, 0.8, 0.045); g.line(0.8, -0.25, 0.8, -0.045); g.arrow(0.8, 0.25, 0.8, 0.05, 0.03); g.arrow(0.8, -0.25, 0.8, -0.05, 0.03)
        sumj(g, 0.8, 0, 0.045); ar(g, 0.845, 0, 1, 0); g.label(0.5, -0.5, "G = G₁ + G₂", 0.6)

    @P.figure(BD, "bd-pid", "Controlador PID en bloques", "PID controller blocks")
    def _(g):
        ar(g, 0, 0, 0.1, 0); dot(g, 0.1, 0); g.line(0.1, 0.3, 0.1, -0.3)
        for v, t in ((0.3, "Kp"), (0, "Ki / s"), (-0.3, "Kd · s")):
            ar(g, 0.1, v, 0.28, v); blk(g, 0.28, v - 0.1, 0.62, v + 0.1, t, 0.65); g.line(0.62, v, 0.8, v)
        g.line(0.8, 0.3, 0.8, 0.05); g.line(0.8, -0.3, 0.8, -0.05); g.head(0.8, 0.3, 0.8, 0.05, 0.03); g.head(0.8, -0.3, 0.8, -0.05, 0.03)
        ar(g, 0.62, 0, 0.755, 0); sumj(g, 0.8, 0, 0.045); ar(g, 0.845, 0, 1, 0); g.label(0.04, 0.08, "E(s)", 0.6); g.label(0.94, 0.08, "U(s)", 0.6)

    @P.figure(BD, "bd-cascade", "Control en cascada", "Cascade control")
    def _(g):
        ar(g, 0, 0.1, 0.1, 0.1); sumj(g, 0.145, 0.1, 0.04); ar(g, 0.185, 0.1, 0.24, 0.1); blk(g, 0.24, 0.02, 0.4, 0.18, "C₁", 0.6)
        ar(g, 0.4, 0.1, 0.46, 0.1); sumj(g, 0.5, 0.1, 0.04); ar(g, 0.54, 0.1, 0.58, 0.1); blk(g, 0.58, 0.02, 0.72, 0.18, "C₂", 0.6)
        ar(g, 0.72, 0.1, 0.78, 0.1); blk(g, 0.78, 0.02, 0.92, 0.18, "P", 0.6); g.line(0.92, 0.1, 0.97, 0.1)
        dot(g, 0.75, 0.1); g.line(0.75, 0.1, 0.75, -0.08); g.line(0.75, -0.08, 0.5, -0.08); g.arrow(0.5, -0.08, 0.5, 0.055, 0.03)
        dot(g, 0.95, 0.1); g.line(0.95, 0.1, 0.95, -0.28); g.line(0.95, -0.28, 0.145, -0.28); g.arrow(0.145, -0.28, 0.145, 0.06, 0.03)
        g.label(0.4, -0.15, "lazo interno", 0.5); g.label(0.55, -0.35, "lazo externo", 0.5); g.label(0.03, 0.2, "R", 0.6); g.label(0.97, 0.2, "Y", 0.6)

    @P.figure(BD, "bd-disturbance", "Perturbación en la planta", "Plant disturbance")
    def _(g):
        ar(g, 0, 0, 0.12, 0); blk(g, 0.12, -0.12, 0.36, 0.12, "Gc"); ar(g, 0.36, 0, 0.5, 0); sumj(g, 0.545, 0, 0.04); ar(g, 0.585, 0, 0.64, 0)
        blk(g, 0.64, -0.12, 0.86, 0.12, "Gp"); ar(g, 0.86, 0, 1, 0); ar(g, 0.545, 0.38, 0.545, 0.045, 0.03)
        g.label(0.62, 0.3, "D(s)", 0.7); g.label(0.04, 0.08, "U", 0.6); g.label(0.96, 0.08, "Y", 0.6); g.label(0.5, -0.07, "+", 0.6); g.label(0.5, 0.07, "+", 0.6)

    @P.figure(BD, "bd-feedforward", "Prealimentación (feedforward)", "Feedforward")
    def _(g):
        ar(g, 0, 0, 0.1, 0); dot(g, 0.1, 0); ar(g, 0.1, 0, 0.18, 0); sumj(g, 0.22, 0, 0.04); ar(g, 0.26, 0, 0.3, 0); blk(g, 0.3, -0.1, 0.46, 0.1, "Gc", 0.6)
        ar(g, 0.46, 0, 0.55, 0); sumj(g, 0.59, 0, 0.04); ar(g, 0.63, 0, 0.68, 0); blk(g, 0.68, -0.1, 0.86, 0.1, "Gp", 0.6); g.line(0.86, 0, 0.94, 0); g.head(0.86, 0, 0.94, 0, 0.03)
        g.line(0.1, 0, 0.1, 0.3); g.line(0.1, 0.3, 0.17, 0.3); blk(g, 0.17, 0.2, 0.42, 0.4, "Gff", 0.6); g.line(0.42, 0.3, 0.59, 0.3); g.arrow(0.59, 0.3, 0.59, 0.045, 0.03)
        dot(g, 0.9, 0); g.line(0.9, 0, 0.9, -0.28); g.line(0.9, -0.28, 0.22, -0.28); g.arrow(0.22, -0.28, 0.22, -0.045, 0.03)
        g.label(0.03, 0.08, "R", 0.6); g.label(0.97, 0.08, "Y", 0.6)

    @P.figure(BD, "bd-digital", "Control digital (muestreo)", "Digital control")
    def _(g):
        ar(g, 0, 0, 0.07, 0); sumj(g, 0.105, 0, 0.035); ar(g, 0.14, 0, 0.19, 0); blk(g, 0.19, -0.1, 0.38, 0.1, "Gc(z)", 0.55)
        ar(g, 0.38, 0, 0.44, 0); blk(g, 0.44, -0.1, 0.6, 0.1, "ZOH", 0.55); ar(g, 0.6, 0, 0.66, 0); blk(g, 0.66, -0.1, 0.84, 0.1, "Gp(s)", 0.55)
        g.line(0.84, 0, 0.97, 0); g.head(0.84, 0, 0.97, 0, 0.03); dot(g, 0.9, 0); g.line(0.9, 0, 0.9, -0.28); g.line(0.9, -0.28, 0.56, -0.28)
        g.line(0.4, -0.28, 0.105, -0.28); g.arrow(0.105, -0.28, 0.105, -0.036, 0.03)
        g.line(0.56, -0.28, 0.5, -0.2); g.circle(0.56, -0.28, 0.012); g.circle(0.4, -0.28, 0.012); g.label(0.48, -0.38, "T (muestreo)", 0.5)
        g.label(0.03, 0.07, "r(k)", 0.55); g.label(0.96, 0.07, "y(t)", 0.55)

    @P.figure(BD, "bd-statespace", "Espacio de estados (bloques)", "State-space blocks")
    def _(g):
        ar(g, 0, 0, 0.1, 0); blk(g, 0.1, -0.09, 0.22, 0.09, "B", 0.6); ar(g, 0.22, 0, 0.3, 0); sumj(g, 0.335, 0, 0.035); ar(g, 0.37, 0, 0.44, 0)
        blk(g, 0.44, -0.09, 0.56, 0.09, "∫", 0.8); g.line(0.56, 0, 0.66, 0); g.head(0.56, 0, 0.66, 0, 0.03); dot(g, 0.66, 0)
        ar(g, 0.66, 0, 0.74, 0); blk(g, 0.74, -0.09, 0.86, 0.09, "C", 0.6); ar(g, 0.86, 0, 0.93, 0); sumj(g, 0.965, 0, 0.03)
        g.line(0.66, 0, 0.66, -0.25); g.line(0.66, -0.25, 0.5, -0.25); blk(g, 0.4, -0.33, 0.5, -0.17, "A", 0.6)
        g.line(0.4, -0.25, 0.335, -0.25); g.arrow(0.335, -0.25, 0.335, -0.035, 0.03)
        g.line(0.04, 0, 0.04, 0.32); g.line(0.04, 0.32, 0.5, 0.32); blk(g, 0.5, 0.24, 0.62, 0.4, "D", 0.6); g.line(0.62, 0.32, 0.965, 0.32); g.arrow(0.965, 0.32, 0.965, 0.035, 0.03)
        g.label(0.02, -0.08, "u", 0.6); g.label(0.5, 0.1, "x'", 0.55); g.label(0.7, 0.07, "x", 0.55); g.label(0.985, -0.1, "y", 0.6)

    # ---------------- Respuesta y análisis ----------------
    @P.figure(RS, "resp-first", "Escalón de 1.er orden", "First-order step")
    def _(g):
        axes(g, 0, 0, 1, 0.8, "t", "y")
        g.line(0, 0.6, 1, 0.6, dashed=True)
        g.curve(lambda u: 0.6 * (1 - math.exp(-u / 0.2)), 0, 0.97)
        g.line(0.2, 0, 0.2, 0.6 * 0.632, dashed=True); g.line(0, 0.6 * 0.632, 0.2, 0.6 * 0.632, dashed=True); dot(g, 0.2, 0.6 * 0.632)
        g.label(-0.1, 0.6, "K", 0.7); g.label(0.2, -0.07, "τ", 0.8); g.label(0.38, 0.14, "63.2 %", 0.5)
        g.line(0, 0, 0.2, 0.6, dashed=True)

    @P.figure(RS, "resp-second", "Escalón de 2.º orden (Mp, tr, ts)", "Second-order step")
    def _(g):
        axes(g, 0, 0, 1, 0.9, "t", "y")
        f = lambda u: 0.5 * (1 - math.exp(-5 * u) * (math.cos(18 * u) + 5 / 18 * math.sin(18 * u)))
        g.line(0, 0.5, 1, 0.5, dashed=True); g.curve(f, 0, 0.97, 96)
        g.line(0.0, 0.475, 1, 0.475, dashed=True); g.line(0.0, 0.525, 1, 0.525, dashed=True)
        tp = math.pi / 18; g.line(tp, 0, tp, f(tp), dashed=True); g.line(0, f(tp), tp, f(tp), dashed=True)
        g.line(0.45, 0, 0.45, 0.45, dashed=True)
        g.label(tp, -0.07, "tp", 0.6); g.label(-0.12, f(tp), "Mp", 0.7); g.label(0.45, -0.07, "ts", 0.7); g.label(-0.08, 0.5, "1", 0.6)

    @P.figure(RS, "resp-splane", "Plano s: polos y ceros", "s-plane poles and zeros")
    def _(g):
        g.arrow(0.5, -0.45, 0.5, 0.45, 0.04); g.arrow(0, 0, 1, 0, 0.04); g.label(0.9, -0.07, "σ", 0.8); g.label(0.58, 0.42, "jω", 0.8)
        for u, v in ((0.3, 0.22), (0.3, -0.22)):
            g.line(u - 0.03, v - 0.03, u + 0.03, v + 0.03); g.line(u - 0.03, v + 0.03, u + 0.03, v - 0.03)
        g.line(0.12, -0.03, 0.18, 0.03); g.line(0.12, 0.03, 0.18, -0.03)
        g.circle(0.38, 0, 0.03); g.label(0.38, -0.1, "cero", 0.5); g.label(0.3, 0.32, "polo", 0.5)

    @P.figure(RS, "resp-stability", "Plano s: regiones de estabilidad", "s-plane stability regions")
    def _(g):
        g.arrow(0.5, -0.45, 0.5, 0.45, 0.04); g.arrow(0, 0, 1, 0, 0.04); g.label(0.93, -0.07, "σ", 0.8); g.label(0.58, 0.42, "jω", 0.8)
        for k in range(1, 9):
            v = -0.4 + k * 0.088 - 0.044
            g.line(0.08 + (k % 2) * 0.03, v, 0.5, v, dashed=True)
        g.label(0.27, 0.3, "ESTABLE", 0.55); g.label(0.76, 0.3, "INESTABLE", 0.55); g.label(0.27, -0.3, "σ < 0", 0.5); g.label(0.76, -0.3, "σ > 0", 0.5)

    @P.figure(RS, "resp-damping", "Polos, ωn y amortiguamiento", "Poles, wn and damping")
    def _(g):
        g.arrow(0.5, -0.45, 0.5, 0.45, 0.04); g.arrow(0, 0, 1, 0, 0.04); g.label(0.93, -0.07, "σ", 0.8); g.label(0.58, 0.42, "jω", 0.8)
        c = (0.5, 0)
        g.arc(0.5, 0, 0.34, 0.34, 90, 270, dashed=True)
        ang = math.radians(135); p = (0.5 + 0.34 * math.cos(ang), 0.34 * math.sin(ang)); q = (p[0], -p[1])
        g.line(0.5, 0, *p); g.line(0.5, 0, *q)
        for x, y in (p, q): g.line(x - 0.03, y - 0.03, x + 0.03, y + 0.03); g.line(x - 0.03, y + 0.03, x + 0.03, y - 0.03)
        g.arc(0.5, 0, 0.12, 0.12, 135, 180); g.label(0.34, 0.07, "θ", 0.6); g.label(0.38, 0.2, "ωn", 0.6); g.label(0.12, 0.3, "ζ = cos θ", 0.5)
        g.line(p[0], p[1], p[0], 0, dashed=True); g.label(p[0], -0.07, "−ζωn", 0.45)

    @P.figure(RS, "resp-rlocus", "Lugar de las raíces", "Root locus")
    def _(g):
        g.arrow(0.92, -0.45, 0.92, 0.45, 0.04); g.arrow(-0.12, 0, 1, 0, 0.04); g.label(0.97, -0.07, "σ", 0.8); g.label(1.0, 0.42, "jω", 0.8)
        for x in (0.55, 0.78):
            g.line(x - 0.025, -0.025, x + 0.025, 0.025); g.line(x - 0.025, 0.025, x + 0.025, -0.025)
        g.circle(0.3, 0, 0.025)
        r = 0.365
        g.arc(0.3, 0, r, r, 0, 180); g.arc(0.3, 0, r, r, 180, 360)
        g.line(0.55, 0, 0.78, 0); g.line(-0.065, 0, 0.275, 0); g.arrow(-0.065, 0, -0.12, 0, 0.03)
        g.label(0.55, -0.09, "polo", 0.45); g.label(0.78, -0.09, "polo", 0.45); g.label(0.3, -0.09, "cero", 0.45); g.label(0.665, 0.07, "ruptura", 0.4)

    @P.figure(RS, "resp-bode-mag", "Bode: magnitud", "Bode magnitude")
    def _(g):
        g.arrow(0, -0.1, 0, 0.5, 0.04); g.arrow(0, 0.05, 1, 0.05, 0.04)
        g.label(0.94, -0.02, "log ω", 0.6); g.label(-0.1, 0.46, "dB", 0.6)
        g.line(0.02, 0.4, 0.4, 0.4, 0.7, 0.1, 0.97, -0.2)
        g.spline([(0.02, 0.4), (0.3, 0.4), (0.4, 0.37), (0.55, 0.25), (0.7, 0.1), (0.97, -0.2)], dashed=True)
        g.label(0.4, 0.46, "ω₁", 0.55); g.line(0.4, 0.05, 0.4, 0.4, dashed=True)
        g.label(0.84, 0.18, "−20 dB/déc", 0.5); g.label(0.17, 0.46, "K dB", 0.5)

    @P.figure(RS, "resp-bode-phase", "Bode: fase y margen", "Bode phase")
    def _(g):
        g.arrow(0, -0.4, 0, 0.3, 0.04); g.arrow(0, 0, 1, 0, 0.04); g.label(0.94, 0.07, "log ω", 0.6); g.label(-0.1, 0.26, "φ", 0.7)
        g.spline([(0.02, 0), (0.25, -0.03), (0.45, -0.18), (0.6, -0.3), (0.75, -0.34), (0.97, -0.36)])
        g.line(0, -0.36, 1, -0.36, dashed=True); g.label(-0.12, -0.36, "−180°", 0.55); g.label(-0.1, -0.18, "−90°", 0.55)
        g.line(0.64, 0, 0.64, -0.31, dashed=True); g.label(0.64, 0.07, "ωc", 0.6)
        g.double_arrow(0.7, -0.31, 0.7, -0.36, 0.02); g.label(0.78, -0.29, "MF", 0.5)

    @P.figure(RS, "resp-nyquist", "Diagrama de Nyquist", "Nyquist plot")
    def _(g):
        g.arrow(0, 0, 1, 0, 0.04); g.arrow(0.4, -0.45, 0.4, 0.45, 0.04); g.label(0.93, -0.07, "Re", 0.6); g.label(0.5, 0.42, "Im", 0.6)
        g.spline([(0.85, 0.01), (0.7, -0.2), (0.45, -0.32), (0.25, -0.2), (0.22, -0.03), (0.3, 0.0)])
        g.spline([(0.85, -0.01), (0.7, 0.2), (0.45, 0.32), (0.25, 0.2), (0.22, 0.03), (0.3, 0.0)], dashed=True)
        g.line(0.15, -0.025, 0.2, 0.025); g.line(0.15, 0.025, 0.2, -0.025); g.label(0.175, -0.1, "−1", 0.6)
        g.head(0.7, -0.2, 0.62, -0.25, 0.035); g.label(0.85, 0.07, "ω = 0", 0.45); g.label(0.28, 0.1, "ω → ∞", 0.4)

    @P.figure(RS, "resp-nichols", "Carta de Nichols", "Nichols chart")
    def _(g):
        g.arrow(0, -0.4, 1, -0.4, 0.04); g.arrow(0, -0.4, 0, 0.45, 0.04)
        g.label(0.9, -0.47, "φ (°)", 0.6); g.label(0.1, 0.42, "|G| dB", 0.6)
        g.spline([(0.92, -0.35), (0.7, -0.15), (0.55, 0.0), (0.4, 0.12), (0.25, 0.28), (0.1, 0.4)])
        g.line(0.55, -0.4, 0.55, 0.45, dashed=True); g.label(0.55, -0.47, "−180°", 0.5); g.line(0, 0, 1, 0, dashed=True); g.label(-0.07, 0, "0", 0.55)
        g.line(0.52, -0.03, 0.58, 0.03); g.line(0.52, 0.03, 0.58, -0.03); g.label(0.7, 0.1, "(−180°, 0 dB)", 0.4)

    @P.figure(RS, "resp-ess", "Error en estado estable", "Steady-state error")
    def _(g):
        axes(g, 0, 0, 1, 0.8, "t", "y")
        g.line(0, 0.55, 1, 0.55, dashed=True); g.curve(lambda u: 0.45 * (1 - math.exp(-u / 0.18)), 0, 0.97)
        g.double_arrow(0.9, 0.45, 0.9, 0.55, 0.03); g.label(0.78, 0.5, "e_ss", 0.65); g.label(-0.1, 0.55, "r", 0.7); g.label(0.9, 0.35, "y(∞)", 0.55)

    # ---------------- Sistemas (modelado) ----------------
    @P.figure(SY, "sys-msd", "Masa-resorte-amortiguador", "Mass-spring-damper")
    def _(g):
        g.line(0.05, -0.28, 0.05, 0.32); [g.line(0.05, v, 0.0, v - 0.05) for v in (0.3, 0.2, 0.1, 0.0, -0.1, -0.2)]
        g.line(0.05, 0.2, 0.12, 0.2); g.zigzag(0.12, 0.5, 0.2, 0.04, 6, 0.06)
        g.line(0.05, -0.05, 0.12, -0.05)
        g.line(0.12, -0.12, 0.12, 0.02); g.line(0.12, -0.05, 0.3, -0.05); g.line(0.3, -0.12, 0.3, 0.02); g.line(0.3, -0.12, 0.42, -0.12)
        g.line(0.3, -0.05, 0.5, -0.05)
        g.rect(0.5, -0.2, 0.8, 0.3); g.label(0.65, 0.05, "m", 1.1)
        g.circle(0.55, -0.26, 0.04); g.circle(0.75, -0.26, 0.04); g.line(0.0, -0.3, 1, -0.3)
        g.arrow(0.8, 0.05, 0.97, 0.05, 0.04); g.label(0.9, 0.12, "F", 0.8)
        g.label(0.3, 0.31, "k", 0.8); g.label(0.2, -0.17, "b", 0.8); g.arrow(0.65, 0.36, 0.8, 0.36, 0.03); g.label(0.72, 0.43, "x", 0.7)

    @P.figure(SY, "sys-rlc", "Circuito RLC serie", "Series RLC circuit")
    def _(g):
        g.line(0.1, 0.25, 0.2, 0.25); g.zigzag(0.2, 0.45, 0.25, 0.04, 4, 0.04)
        g.line(0.45, 0.25, 0.5, 0.25)
        for k in range(4): g.arc(0.52 + 0.06 * k, 0.25, 0.03, 0.04, 180, 0)
        g.line(0.76, 0.25, 0.9, 0.25); g.line(0.9, 0.25, 0.9, 0.04); g.line(0.86, 0.04, 0.94, 0.04); g.line(0.86, -0.04, 0.94, -0.04); g.line(0.9, -0.04, 0.9, -0.25)
        g.line(0.9, -0.25, 0.1, -0.25); g.line(0.1, -0.25, 0.1, -0.08); g.circle(0.1, 0, 0.08); g.line(0.1, 0.08, 0.1, 0.25)
        g.label(0.1, 0, "~", 0.9)
        g.label(0.32, 0.36, "R", 0.8); g.label(0.63, 0.36, "L", 0.8); g.label(0.99, 0.0, "C", 0.8); g.label(0.0, 0.0, "v", 0.8)
        g.arrow(0.3, 0.12, 0.6, 0.12, 0.03); g.label(0.45, 0.07, "i", 0.7)

    @P.figure(SY, "sys-dcmotor", "Motor de CD (circuito + mecánica)", "DC motor model")
    def _(g):
        g.line(0.05, 0.3, 0.12, 0.3); g.zigzag(0.12, 0.34, 0.3, 0.04, 4, 0.03)
        for k in range(3): g.arc(0.37 + 0.05 * k, 0.3, 0.025, 0.035, 180, 0)
        g.line(0.52, 0.3, 0.6, 0.3); g.line(0.6, 0.3, 0.6, 0.2); g.circle(0.6, 0.12, 0.08); g.label(0.6, 0.12, "M", 0.8)
        g.line(0.6, 0.04, 0.6, -0.3); g.line(0.6, -0.3, 0.05, -0.3); g.line(0.05, -0.3, 0.05, 0.3)
        g.label(0.2, 0.4, "Ra", 0.65); g.label(0.42, 0.4, "La", 0.65); g.label(0.0, 0.0, "va", 0.7);
        g.line(0.68, 0.12, 0.8, 0.12); g.circle(0.88, 0.12, 0.08); g.label(0.88, 0.12, "J", 0.8); g.line(0.88, 0.04, 0.88, -0.12); g.line(0.82, -0.12, 0.94, -0.12)
        g.label(0.88, -0.22, "b", 0.65); g.label(0.74, 0.22, "τ, ω", 0.5)

    @P.figure(SY, "sys-invpend", "Péndulo invertido sobre carro", "Inverted pendulum on cart")
    def _(g):
        g.rect(0.28, -0.12, 0.72, 0.04); g.circle(0.36, -0.17, 0.04); g.circle(0.64, -0.17, 0.04); g.line(0.0, -0.21, 1, -0.21)
        g.line(0.5, 0.04, 0.62, 0.44); g.circle(0.64, 0.5, 0.06, fill=True); g.line(0.5, 0.04, 0.5, 0.3, dashed=True)
        g.arc(0.5, 0.04, 0.2, 0.2, 73, 90); g.label(0.58, 0.33, "θ", 0.6); g.label(0.78, 0.5, "m", 0.7); g.label(0.5, -0.04, "M", 0.7)
        g.arrow(0.0, -0.04, 0.26, -0.04, 0.04); g.label(0.1, 0.03, "F", 0.7); g.arrow(0.5, -0.3, 0.7, -0.3, 0.03); g.label(0.6, -0.37, "x", 0.6)

    @P.figure(SY, "sys-tank", "Tanque con nivel", "Tank level")
    def _(g):
        g.line(0.28, 0.45, 0.28, -0.3, 0.72, -0.3, 0.72, 0.45)
        g.poly(0.28, 0.0, 0.72, 0.0, 0.72, -0.3, 0.28, -0.3, fill=False)
        g.line(0.28, 0.0, 0.34, 0.03, 0.4, 0.0, 0.46, 0.03, 0.52, 0.0, 0.58, 0.03, 0.64, 0.0, 0.72, 0.0)
        g.arrow(0.0, 0.38, 0.35, 0.38, 0.04); g.label(0.12, 0.46, "qin", 0.65); g.line(0.72, -0.2, 0.85, -0.2); g.arrow(0.9, -0.2, 1, -0.2, 0.04)
        g.label(0.95, -0.1, "qout", 0.6); g.double_arrow(0.2, 0.0, 0.2, -0.3, 0.03); g.label(0.1, -0.15, "h", 0.8); g.label(0.5, -0.15, "A", 0.8)

    @P.figure(SY, "sys-thermal", "Sistema térmico (C y R)", "Thermal system")
    def _(g):
        g.rect(0.3, -0.2, 0.7, 0.2); g.label(0.5, 0.0, "C", 1.0); g.label(0.5, 0.3, "T", 0.7)
        g.arrow(0.0, 0.0, 0.28, 0.0, 0.04); g.label(0.12, 0.08, "Q", 0.8)
        g.line(0.7, 0.0, 0.76, 0.0); g.zigzag(0.7, 1.0, 0.0, 0.05, 3, 0.06)
        g.label(0.85, 0.1, "R", 0.8); g.label(1.0, -0.12, "T∞", 0.6)
