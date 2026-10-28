"""Figuras de las materias de Física (la carrera): mecánica avanzada, cuántica y moderna, termodinámica y estadística, campos."""
import math

MAV = "Física: mecánica avanzada"
CUA = "Física: cuántica y moderna"
EM = "Física: electricidad y magnetismo"
TES = "Física: termodinámica y estadística"
HER = "Física: herramientas matemáticas"


def extend(P):
    P.en.update({MAV: "Physics: advanced mechanics", CUA: "Physics: quantum and modern", TES: "Physics: thermodynamics and statistics",
                 HER: "Physics: mathematical tools"})

    def axes(g, u0, v0, u1, v1):
        g.arrow(u0, v0, u1, v0, 0.04); g.arrow(u0, v0, u0, v1, 0.04)

    def wavy(g, u0, v0, u1, v1, amp=0.03, n=4):
        """Línea ondulada (fotón) de (u0, v0) a (u1, v1)."""
        L = math.hypot(u1 - u0, v1 - v0); ex, ey = (u1 - u0) / L, (v1 - v0) / L; m = n * 12
        pts = []
        for k in range(m + 1):
            s = amp * math.sin(2 * math.pi * k / 12)
            pts.append((u0 + ex * L * k / m - ey * s, v0 + ey * L * k / m + ex * s))
        g._add(pts)

    # --- Mecánica avanzada ----------------------------------------------------------------------

    @P.figure(MAV, "effective-potential", "Potencial efectivo (fuerza central)", "Effective potential (central force)")
    def _(g):
        axes(g, 0.1, -0.33, 0.95, 0.42)
        g.curve(lambda r: 5 * (0.009 / (r * r) - 0.045 / r), 0.165, 0.95, 90)
        g.line(0.1, -0.1, 0.95, -0.1, dashed=True); g.label(1.02, -0.1, "E₁", 0.7)
        g.line(0.1, -0.25, 0.95, -0.25, dashed=True); g.label(1.02, -0.25, "E₂", 0.7)
        g.label(0.97, -0.4, "r", 0.8); g.label(0.04, 0.42, "V", 0.8); g.label(0.62, 0.3, "V_ef = L²/2mr² − k/r", 0.6)

    @P.figure(MAV, "coupled-oscillators", "Osciladores acoplados", "Coupled oscillators")
    def _(g):
        for u in (0.0, 1.0): g.line(u, -0.2, u, 0.25)
        g.zigzag(0.0, 0.3, 0.02, 0.05, 6, 0.04); g.rect(0.3, -0.06, 0.48, 0.1); g.label(0.39, 0.02, "m", 0.8)
        g.zigzag(0.48, 0.72, 0.02, 0.05, 5, 0.04)
        g.rect(0.72, -0.06, 0.88, 0.1); g.label(0.8, 0.02, "m", 0.8)
        g.zigzag(0.88, 1.0, 0.02, 0.05, 2, 0.02)
        g.hatch(0.0, 1.0, -0.06, 12, 0.04)
        g.label(0.15, 0.14, "k", 0.8); g.label(0.6, 0.14, "k_c", 0.8); g.label(0.94, 0.14, "k", 0.8)
        g.arrow(0.39, -0.22, 0.52, -0.22, 0.04); g.label(0.39, -0.3, "x₁", 0.7); g.arrow(0.8, -0.22, 0.93, -0.22, 0.04); g.label(0.8, -0.3, "x₂", 0.7)

    @P.figure(MAV, "kepler-orbit", "Órbita elíptica (Kepler)", "Elliptical orbit (Kepler)")
    def _(g):
        a, b = 0.46, 0.3; c = math.sqrt(a * a - b * b)
        g.ellipse(0.5, 0, a, b); g.circle(0.5 + c, 0, 0.03, fill=True)
        g.label(0.5 + c + 0.07, -0.07, "F", 0.7); g.circle(0.5 - c, 0, 0.012, fill=True); g.label(0.5 - c, -0.07, "F'", 0.7)
        t = math.radians(125); px, py = 0.5 + a * math.cos(t), b * math.sin(t)
        g.circle(px, py, 0.025, fill=True); g.line(0.5 + c, 0, px, py, dashed=True); g.label(px - 0.05, py + 0.06, "m", 0.7)
        g.label(0.5, -0.38, "a (semieje mayor)", 0.6); g.label((0.5 + c + px) / 2 + 0.07, py / 2 + 0.03, "r", 0.7)

    @P.figure(MAV, "noninertial-cart", "Marco no inercial (péndulo en vagón)", "Non-inertial frame (pendulum in cart)")
    def _(g):
        g.rect(0.15, -0.3, 0.85, -0.12); g.circle(0.3, -0.34, 0.04); g.circle(0.7, -0.34, 0.04); g.hatch(0.0, 1.0, -0.38, 10, 0.04)
        g.line(0.25, -0.12, 0.25, 0.3, 0.5, 0.3)
        th = math.radians(25); bx, by = 0.5 + 0.38 * math.sin(th), 0.3 - 0.38 * math.cos(th)
        g.line(0.5, 0.3, 0.5, -0.12, dashed=True); g.line(0.5, 0.3, bx, by); g.circle(bx, by, 0.035, fill=True)
        g.arrow(0.88, -0.2, 1.0, -0.2, 0.04); g.label(0.94, -0.12, "a", 0.8)
        g.arrow(bx, by, bx - 0.2, by, 0.04); g.label(bx - 0.17, by + 0.06, "−ma", 0.7)
        g.arrow(bx, by, bx, by - 0.2, 0.04); g.label(bx + 0.07, by - 0.17, "mg", 0.7)
        g.label(0.56, 0.18, "θ", 0.7)

    # --- Cuántica y moderna ---------------------------------------------------------------------

    @P.figure(CUA, "infinite-well", "Pozo de potencial infinito", "Infinite potential well")
    def _(g):
        g.line(0.15, 0.4, 0.15, -0.3, 0.85, -0.3, 0.85, 0.4)
        for n, v in ((1, -0.18), (2, 0.0), (3, 0.2)):
            g.line(0.15, v, 0.85, v, dashed=True); g.label(0.93, v, f"n={n}", 0.6)
            g.curve(lambda u, n=n, v=v: v + 0.055 * math.sin(n * math.pi * (u - 0.15) / 0.7), 0.15, 0.85, 60)
        g.label(0.5, -0.4, "L", 0.7); g.double_arrow(0.15, -0.34, 0.85, -0.34, 0.03); g.label(0.04, 0.0, "E", 0.7)

    @P.figure(CUA, "tunnel-effect", "Efecto túnel", "Quantum tunneling")
    def _(g):
        g.rect(0.42, -0.25, 0.58, 0.25); g.label(0.5, 0.32, "V₀", 0.7)
        g.curve(lambda u: 0.1 * math.sin(2 * math.pi * 7 * u), 0.0, 0.42, 80)
        g.curve(lambda u: 0.1 * math.exp(-9 * (u - 0.42)), 0.42, 0.58, 20)
        g.curve(lambda u: 0.035 * math.sin(2 * math.pi * 7 * u), 0.58, 1.0, 60)
        g.label(0.2, -0.17, "incidente", 0.55); g.label(0.8, -0.17, "transmitida", 0.55); g.label(0.5, -0.32, "barrera", 0.55)

    @P.figure(CUA, "qho-levels", "Oscilador armónico cuántico", "Quantum harmonic oscillator")
    def _(g):
        g.curve(lambda u: 1.6 * (u - 0.5) ** 2 - 0.3, 0.1, 0.9, 60)
        for n in range(5):
            v = -0.21 + 0.12 * n; w = math.sqrt((v + 0.3) / 1.6)
            g.line(0.5 - w, v, 0.5 + w, v)
            if n < 4: g.label(0.5 + w + 0.08, v, f"n={n}", 0.5)
        g.label(0.5, -0.38, "E_n = ħω(n + ½)", 0.65); g.label(0.14, 0.2, "V = ½kx²", 0.6)

    @P.figure(CUA, "orbitals-spd", "Orbitales s, p y d", "s, p and d orbitals")
    def _(g):
        g.circle(0.17, 0.05, 0.14); g.label(0.17, -0.2, "s", 0.8)
        g.circle(0.5, 0.2, 0.09); g.circle(0.5, -0.04, 0.09); g.label(0.5, -0.2, "p", 0.8)
        for k in range(4):
            a = math.radians(45 + 90 * k); g.circle(0.83 + 0.09 * math.cos(a), 0.08 + 0.09 * math.sin(a), 0.065)
        g.label(0.83, -0.2, "d", 0.8)

    @P.figure(CUA, "double-slit", "Doble rendija", "Double slit")
    def _(g):
        g.line(0.3, 0.4, 0.3, 0.12); g.line(0.3, 0.06, 0.3, -0.06); g.line(0.3, -0.12, 0.3, -0.4)
        g.line(0.88, 0.4, 0.88, -0.4)
        g.arrow(0.0, 0.0, 0.26, 0.0, 0.04)
        for r in (0.14, 0.24, 0.34):
            g.arc(0.3, 0.09, r, r, -60, 60); g.arc(0.3, -0.09, r, r, -60, 60)
        g._add([(0.88 + 0.1 * (math.cos(11 * v) ** 2) * math.exp(-6 * v * v), v) for v in [-0.4 + 0.8 * i / 100 for i in range(101)]])
        g.label(0.93, -0.44, "pantalla", 0.55); g.label(0.3, -0.44, "rendijas", 0.55)

    @P.figure(CUA, "hydrogen-levels", "Niveles del hidrógeno", "Hydrogen energy levels")
    def _(g):
        vs = {1: -0.36, 2: -0.05, 3: 0.12, 4: 0.23, 5: 0.31}
        for n, v in vs.items():
            g.line(0.2, v, 0.8, v); g.label(0.11, v, f"n={n}", 0.5)
        g.line(0.2, 0.38, 0.8, 0.38, dashed=True); g.label(0.9, 0.38, "n=∞", 0.5)
        g.arrow(0.3, -0.05, 0.3, -0.36, 0.04); g.arrow(0.4, 0.12, 0.4, -0.36, 0.04); g.arrow(0.5, 0.23, 0.5, -0.36, 0.04)
        g.label(0.4, -0.43, "Lyman", 0.55)
        g.arrow(0.62, 0.12, 0.62, -0.05, 0.035); g.arrow(0.7, 0.23, 0.7, -0.05, 0.035); g.label(0.66, -0.12, "Balmer", 0.55)

    @P.figure(CUA, "feynman-annihilation", "Diagrama de Feynman (aniquilación)", "Feynman diagram (annihilation)")
    def _(g):
        g.arrow(0.0, 0.35, 0.35, 0.0, 0.05); g.arrow(0.35, 0.0, 0.0, -0.35, 0.05)
        wavy(g, 0.35, 0.0, 0.65, 0.0)
        g.arrow(0.65, 0.0, 1.0, 0.35, 0.05); g.arrow(1.0, -0.35, 0.65, 0.0, 0.05)
        g.label(0.05, 0.4, "e⁻", 0.8); g.label(0.05, -0.4, "e⁺", 0.8); g.label(0.5, 0.1, "γ", 0.9); g.label(0.97, 0.4, "μ⁻", 0.8); g.label(0.97, -0.4, "μ⁺", 0.8)

    @P.figure(CUA, "light-cone", "Cono de luz (relatividad)", "Light cone (relativity)")
    def _(g):
        g.arrow(0.0, 0.0, 1.0, 0.0, 0.04); g.arrow(0.5, -0.4, 0.5, 0.4, 0.04)
        g.line(0.1, -0.4, 0.9, 0.4); g.line(0.1, 0.4, 0.9, -0.4)
        g.label(0.5, 0.28, "futuro", 0.7); g.label(0.5, -0.28, "pasado", 0.7); g.label(0.15, 0.06, "otro lugar", 0.55); g.label(0.85, 0.06, "otro lugar", 0.55)
        g.label(1.0, -0.06, "x", 0.8); g.label(0.56, 0.42, "ct", 0.8)

    # --- Electricidad y magnetismo (se suman a la categoría existente) ---------------------------

    @P.figure(EM, "faraday-loop", "Ley de Faraday (espira)", "Faraday's law (loop)")
    def _(g):
        g.rect(0.3, -0.2, 0.7, 0.2)
        for u in (0.38, 0.5, 0.62):
            for v in (-0.1, 0.1): g.circle(u, v, 0.02); g.circle(u, v, 0.006, fill=True)
        g.arrow(0.7, 0.05, 0.7, -0.08, 0.04); g.label(0.78, 0.0, "I", 0.8)
        g.label(0.5, 0.3, "ε = −dΦ/dt", 0.7); g.label(0.5, -0.3, "B(t) creciente", 0.6)

    @P.figure(EM, "em-wave", "Onda electromagnética", "Electromagnetic wave")
    def _(g):
        g.arrow(0.0, 0.0, 1.0, 0.0, 0.04)
        g.curve(lambda u: 0.3 * math.sin(2 * math.pi * 2 * u), 0.0, 0.95, 80)
        g.curve(lambda u: 0.15 * math.sin(2 * math.pi * 2 * u), 0.0, 0.95, 80, dashed=True)
        g.label(0.12, 0.34, "E", 0.8); g.label(0.12, -0.1, "B", 0.8); g.label(1.0, -0.08, "k", 0.8)

    @P.figure(EM, "lc-circuit", "Circuito LC", "LC circuit")
    def _(g):
        g.line(0.2, 0.25, 0.2, 0.1); g.line(0.2, -0.1, 0.2, -0.25); g.line(0.8, 0.25, 0.8, 0.12); g.line(0.8, -0.12, 0.8, -0.25)
        g.line(0.2, 0.25, 0.8, 0.25); g.line(0.2, -0.25, 0.8, -0.25)
        g.line(0.1, 0.1, 0.3, 0.1); g.line(0.1, -0.1, 0.3, -0.1); g.label(0.04, 0.0, "C", 0.9)
        for k in range(4): g.arc(0.8, 0.09 - 0.06 * k, 0.045, 0.03, -90, 90)
        g.label(0.9, 0.0, "L", 0.9); g.arrow(0.45, 0.32, 0.58, 0.32, 0.04); g.label(0.5, 0.0, "ω = 1/√(LC)", 0.6)

    # --- Termodinámica y estadística ------------------------------------------------------------

    @P.figure(TES, "carnot-cycle", "Ciclo de Carnot (P–V)", "Carnot cycle (P–V)")
    def _(g):
        axes(g, 0.1, -0.35, 0.95, 0.4)
        p = lambda P_: 1.5 * P_ - 0.3                      # presión → v
        P1, P2, P3, P4 = (0.25, 0.35), (0.45, 0.0875 / 0.45), (0.65, 0.0644), (0.362, 0.1157)
        g.curve(lambda u: p(0.0875 / u), 0.25, 0.45, 30)          # isoterma T_h
        g.curve(lambda u: p(P2[1] * (0.45 / u) ** 3), 0.45, 0.65, 30)   # adiabática
        g.curve(lambda u: p(0.0418 / u), 0.362, 0.65, 30)         # isoterma T_c
        g.curve(lambda u: p(0.35 * (0.25 / u) ** 3), 0.25, 0.362, 30)   # adiabática
        for (u, P_), t, du, dv in ((P1, "1", -0.05, 0.03), (P2, "2", 0.04, 0.05), (P3, "3", 0.05, 0.03), (P4, "4", -0.05, -0.04)): g.label(u + du, p(P_) + dv, t, 0.7)
        g.label(0.42, p(0.0875 / 0.4) + 0.07, "T_h", 0.6); g.label(0.55, p(0.0418 / 0.55) - 0.07, "T_c", 0.6)
        g.label(0.04, 0.42, "P", 0.8); g.label(0.97, -0.42, "V", 0.8)

    @P.figure(TES, "otto-cycle", "Ciclo Otto (P–V)", "Otto cycle (P–V)")
    def _(g):
        axes(g, 0.1, -0.35, 0.95, 0.4)
        p = lambda P_: P_ - 0.3
        g.curve(lambda u: p(0.06 * (0.65 / u) ** 2.5), 0.4, 0.65, 30)
        g.curve(lambda u: p(0.45 * (0.4 / u) ** 2.5), 0.4, 0.65, 30)
        g.line(0.4, p(0.2), 0.4, p(0.45)); g.line(0.65, p(0.06), 0.65, p(0.134))
        for (u, P_), t, du, dv in (((0.65, 0.06), "1", 0.05, -0.02), ((0.4, 0.2), "2", -0.05, 0.0), ((0.4, 0.45), "3", -0.05, 0.02), ((0.65, 0.134), "4", 0.05, 0.02)): g.label(u + du, p(P_) + dv, t, 0.7)
        g.label(0.04, 0.42, "P", 0.8); g.label(0.97, -0.42, "V", 0.8); g.label(0.7, 0.3, "2 adiabáticas + 2 isocoras", 0.55)

    @P.figure(TES, "maxwell-boltzmann", "Distribución de Maxwell–Boltzmann", "Maxwell–Boltzmann distribution")
    def _(g):
        axes(g, 0.05, -0.3, 0.97, 0.42)
        for s, t in ((0.12, "T₁"), (0.2, "T₂"), (0.32, "T₃")):
            A = 0.6 * 0.12 / s
            f = lambda u, s=s, A=A: -0.3 + A * (u * u / (2 * s * s)) * math.exp(1 - u * u / (2 * s * s))
            g.curve(f, 0.05, 0.95, 100); g.label(s * 1.41 + 0.05 + (0.04 if s > 0.2 else 0), f(s * 1.41) + 0.07, t, 0.7)
        g.label(0.97, -0.37, "v", 0.8); g.label(0.04, 0.45, "f(v)", 0.7)

    @P.figure(TES, "phase-diagram", "Diagrama de fases (P–T)", "Phase diagram (P–T)")
    def _(g):
        axes(g, 0.05, -0.35, 0.97, 0.42)
        g.line(0.08, -0.33, 0.3, -0.12)                                                   # sublimación
        g.curve(lambda u: -0.12 + 0.32 * ((u - 0.3) / 0.45) ** 0.8, 0.3, 0.75, 40)       # vaporización
        g.line(0.3, -0.12, 0.27, 0.4)                                                    # fusión
        g.circle(0.3, -0.12, 0.015, fill=True); g.circle(0.75, 0.2, 0.015, fill=True)
        g.label(0.14, 0.15, "sólido", 0.7); g.label(0.55, 0.28, "líquido", 0.7); g.label(0.68, -0.15, "gas", 0.7)
        g.label(0.38, -0.2, "PT", 0.55); g.label(0.83, 0.2, "PC", 0.55); g.label(0.04, 0.45, "P", 0.8); g.label(0.97, -0.42, "T", 0.8)

    # --- Herramientas matemáticas (cálculo vectorial y álgebra lineal) --------------------------

    @P.figure(HER, "cross-product", "Producto cruz (regla de la mano derecha)", "Cross product (right-hand rule)")
    def _(g):
        g.poly(0.1, -0.25, 0.65, -0.25, 0.8, -0.05, 0.25, -0.05, dashed=True)
        g.arrow(0.1, -0.25, 0.65, -0.25, 0.05); g.arrow(0.1, -0.25, 0.25, -0.05, 0.05); g.arrow(0.1, -0.25, 0.1, 0.35, 0.05)
        g.label(0.7, -0.33, "a", 0.8); g.label(0.17, -0.07, "b", 0.8); g.label(0.2, 0.33, "a × b", 0.8); g.label(0.55, -0.15, "|a×b| = área", 0.55)

    @P.figure(HER, "div-curl-fields", "Divergencia y rotacional", "Divergence and curl")
    def _(g):
        for k in range(8):
            a = math.radians(45 * k); g.arrow(0.27 + 0.05 * math.cos(a), 0.05 * math.sin(a), 0.27 + 0.2 * math.cos(a), 0.2 * math.sin(a), 0.04)
        g.circle(0.27, 0, 0.015, fill=True); g.label(0.27, -0.33, "div F > 0", 0.65)
        for r in (0.08, 0.16, 0.24):
            g.arc(0.76, 0, r, r, 20, 330)
            g.head(0.76 + r * math.cos(math.radians(322)), r * math.sin(math.radians(322)), 0.76 + r * math.cos(math.radians(330)), r * math.sin(math.radians(330)), 0.04)
        g.label(0.76, -0.33, "rot F ≠ 0", 0.65)

    @P.figure(HER, "gradient-surface", "Gradiente y curvas de nivel", "Gradient and level curves")
    def _(g):
        for r in (0.1, 0.2, 0.3): g.ellipse(0.4, 0.0, r * 1.4, r)
        g.circle(0.4, 0, 0.012, fill=True)
        px, py = 0.4 + 0.2 * 1.4 * math.cos(math.radians(30)), 0.2 * math.sin(math.radians(30))
        g.circle(px, py, 0.012, fill=True); g.arrow(px, py, px - 0.15, py - 0.09, 0.04)
        g.label(px + 0.1, py + 0.06, "∇f", 0.8); g.label(0.4, -0.38, "∇f ⟂ curva de nivel", 0.6)
