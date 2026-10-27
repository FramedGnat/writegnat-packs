import math
from wgpack import Pack

pack = Pack("fisica", "Física", "Mecánica, ondas, óptica, electromagnetismo, termodinámica y física moderna: diagramas y formulario.",
            "Ciencias", "⚛️", en={"Física": "Physics",
            "Mecánica, ondas, óptica, electromagnetismo, termodinámica y física moderna: diagramas y formulario.":
            "Mechanics, waves, optics, electromagnetism, thermodynamics and modern physics: diagrams and formula sheet."})
P = pack
MEC, OPT, EM, TER = "Física: mecánica", "Física: ondas y óptica", "Física: electricidad y magnetismo", "Física: calor y fluidos"
P.en.update({MEC: "Physics: mechanics", OPT: "Physics: waves and optics", EM: "Physics: electricity and magnetism", TER: "Physics: heat and fluids"})

# --- Mecánica -------------------------------------------------------------------------------

@P.figure(MEC, "vector", "Vector", "Vector")
def _(g): g.arrow(0, 0, 1, 0, 0.08)

@P.figure(MEC, "spring", "Resorte", "Spring")
def _(g): g.zigzag(0, 1, 0, 0.08, 8, 0.15)

@P.figure(MEC, "spring-wall", "Resorte con bloque", "Spring and block")
def _(g):
    g.line(0, -0.25, 0, 0.35)
    for k in range(6): v = -0.2 + k * 0.1; g.line(0, v, -0.06, v - 0.06)
    g.zigzag(0, 0.6, 0.06, 0.06, 8, 0.05); g.rect(0.6, -0.08, 0.88, 0.2); g.label(0.74, 0.06, "m")
    g.hatch(-0.05, 1.0, -0.08, 8, 0.05)

@P.figure(MEC, "mass", "Bloque (masa)", "Block (mass)")
def _(g): g.rect(0.2, 0, 0.8, 0.45); g.hatch(0, 1, 0); g.label(0.5, 0.22, "m")

@P.figure(MEC, "fbd", "Diagrama de cuerpo libre", "Free-body diagram")
def _(g):
    g.rect(0.35, -0.15, 0.65, 0.15); g.circle(0.5, 0, 0.015, fill=True)
    g.arrow(0.5, 0.15, 0.5, 0.5); g.label(0.56, 0.45, "N", 0.8)
    g.arrow(0.5, -0.15, 0.5, -0.5); g.label(0.57, -0.47, "mg", 0.8)
    g.arrow(0.65, 0, 1.0, 0); g.label(0.95, 0.07, "F", 0.8)
    g.arrow(0.35, 0, 0.05, 0); g.label(0.1, 0.07, "f", 0.8)

@P.figure(MEC, "incline", "Plano inclinado", "Inclined plane")
def _(g):
    g.poly(0, 0, 1, 0, 1, 0.55); g.arc(0, 0, 0.2, 0.2, 0, 28.8); g.label(0.27, 0.06, "θ", 0.8)
    c, s = math.cos(0.5028), math.sin(0.5028)
    at = lambda a, b: (0.45 * c + a * c - b * s, 0.45 * s + a * s + b * c)
    pts = [at(0, 0), at(0.2, 0), at(0.2, 0.15), at(0, 0.15)]
    g.poly(*[x for p in pts for x in p])

@P.figure(MEC, "pulley", "Polea", "Pulley")
def _(g):
    g.hatch(0.3, 0.7, 0.5, 4, 0.05); g.line(0.5, 0.5, 0.5, 0.2); g.circle(0.5, 0, 0.2); g.circle(0.5, 0, 0.02, fill=True)
    g.line(0.3, 0, 0.3, -0.5); g.line(0.7, 0, 0.7, -0.35); g.rect(0.62, -0.5, 0.78, -0.35)

@P.figure(MEC, "atwood", "Máquina de Atwood", "Atwood machine")
def _(g):
    g.hatch(0.3, 0.7, 0.55, 4, 0.05); g.line(0.5, 0.55, 0.5, 0.2); g.circle(0.5, 0, 0.2); g.circle(0.5, 0, 0.02, fill=True)
    g.line(0.3, 0, 0.3, -0.45); g.line(0.7, 0, 0.7, -0.25)
    g.rect(0.22, -0.62, 0.38, -0.45); g.label(0.3, -0.535, "m₁", 0.6)
    g.rect(0.62, -0.42, 0.78, -0.25); g.label(0.7, -0.335, "m₂", 0.6)

@P.figure(MEC, "pendulum", "Péndulo", "Pendulum")
def _(g):
    g.hatch(0.3, 0.7, 0, 4, 0.05); g.line(0.5, 0, 0.72, -0.6); g.circle(0.75, -0.66, 0.07)
    g.line(0.5, 0, 0.5, -0.6, dashed=True); g.arc(0.5, 0, 0.25, 0.25, 270, 290); g.label(0.55, -0.35, "θ", 0.7)

@P.figure(MEC, "projectile", "Tiro parabólico", "Projectile motion")
def _(g):
    g.arrow(0, 0, 1, 0, 0.04); g.arrow(0, 0, 0, 0.6, 0.04)
    g.curve(lambda u: 2.0 * u * (0.9 - u) / 0.9 * 0.55 / 0.5, 0, 0.9, dashed=True)
    g.arrow(0, 0, 0.18, 0.22, 0.04); g.label(0.22, 0.2, "v₀", 0.7); g.arc(0, 0, 0.1, 0.1, 0, 50); g.label(0.14, 0.04, "θ", 0.6)
    g.label(0.98, -0.06, "x", 0.8); g.label(-0.06, 0.58, "y", 0.8)

@P.figure(MEC, "circular", "Movimiento circular", "Circular motion")
def _(g):
    g.circle(0.5, 0, 0.4, dashed=True); g.circle(0.5, 0, 0.015, fill=True); g.line(0.5, 0, 0.9, 0); g.label(0.7, 0.05, "r", 0.7)
    g.circle(0.9, 0, 0.04, fill=True); g.arrow(0.9, 0, 0.9, 0.35, 0.04); g.label(0.95, 0.3, "v", 0.7)
    g.arrow(0.86, 0, 0.62, 0, 0.04); g.label(0.72, -0.06, "a", 0.6)

@P.figure(MEC, "lever", "Palanca", "Lever")
def _(g):
    g.line(0, 0.05, 1, 0.05); g.poly(0.35, 0.05, 0.28, -0.12, 0.42, -0.12); g.hatch(0.2, 0.5, -0.12, 4, 0.04)
    g.arrow(0.02, 0.35, 0.02, 0.07, 0.04); g.label(0.07, 0.3, "F₁", 0.7)
    g.arrow(0.98, 0.35, 0.98, 0.07, 0.04); g.label(0.9, 0.3, "F₂", 0.7)

@P.figure(MEC, "cart", "Carro", "Cart")
def _(g):
    g.rect(0.15, 0.08, 0.85, 0.35); g.circle(0.3, 0.06, 0.06); g.circle(0.7, 0.06, 0.06); g.line(0, 0, 1, 0)
    g.arrow(0.85, 0.22, 1.05, 0.22, 0.04)

@P.figure(MEC, "balance", "Balanza", "Balance")
def _(g):
    g.poly(0.5, 0.5, 0.45, 0.0, 0.55, 0.0); g.line(0.3, 0, 0.7, 0); g.line(0.1, 0.5, 0.9, 0.5)
    for c in (0.15, 0.85):
        g.line(c - 0.05, 0.5, c - 0.12, 0.25); g.line(c + 0.05, 0.5, c + 0.12, 0.25); g.arc(c, 0.25, 0.12, 0.05, 180, 360)

@P.figure(MEC, "dynamometer", "Dinamómetro", "Spring scale")
def _(g):
    g.line(0, 0, 0.08, 0); g.rect(0.08, -0.08, 0.7, 0.08)
    for k in range(1, 9): g.line(0.08 + k * 0.07, 0.08, 0.08 + k * 0.07, 0.03)
    g.zigzag(0.12, 0.55, 0, 0.04, 8, 0.02); g.line(0.55, 0, 1, 0); g.head(0.8, 0, 1, 0, 0.04)

@P.figure(MEC, "torque", "Torque (brazo de palanca)", "Torque (lever arm)")
def _(g):
    g.circle(0, 0, 0.03, fill=True); g.line(0, 0, 0.8, 0); g.label(0.4, -0.07, "r", 0.7)
    g.arrow(0.8, 0, 0.95, 0.4, 0.05); g.label(0.98, 0.35, "F", 0.7)
    g.arc(0, 0, 0.18, 0.18, 0, 70); g.head(0.18 * math.cos(math.radians(60)), 0.18 * math.sin(math.radians(60)), 0.18 * math.cos(math.radians(70)), 0.18 * math.sin(math.radians(70)), 0.04)
    g.label(0.24, 0.13, "τ", 0.7)

# --- Ondas y óptica ---------------------------------------------------------------------------

@P.figure(OPT, "wave", "Onda", "Wave")
def _(g):
    g.curve(lambda u: 0.2 * math.sin(u * 4 * math.pi), 0, 1, 96); g.line(0, 0, 1, 0, dashed=True)
    g.double_arrow(0.125, 0.26, 0.625, 0.26, 0.03); g.label(0.375, 0.32, "λ", 0.7)
    g.double_arrow(0.875, 0, 0.875, 0.2, 0.03); g.label(0.93, 0.1, "A", 0.6)

@P.figure(OPT, "standing-wave", "Onda estacionaria", "Standing wave")
def _(g):
    g.curve(lambda u: 0.2 * math.sin(u * 3 * math.pi), 0, 1, 96); g.curve(lambda u: -0.2 * math.sin(u * 3 * math.pi), 0, 1, 96, dashed=True)
    g.line(0, 0, 1, 0)
    for k in range(4): g.circle(k / 3, 0, 0.015, fill=True)

@P.figure(OPT, "lens-conv", "Lente convergente", "Converging lens")
def _(g):
    half = math.degrees(math.asin(math.sqrt(0.25 - 0.42 ** 2) / 0.5))
    g.arc(0.92, 0, 0.5, 0.5, 180 - half, 180 + half); g.arc(0.08, 0, 0.5, 0.5, -half, half); g.line(0, 0, 1, 0, dashed=True)

@P.figure(OPT, "lens-div", "Lente divergente", "Diverging lens")
def _(g):
    g.arc(0.3, 0, 0.17, 0.3, -60, 60); g.arc(0.7, 0, 0.17, 0.3, 120, 240)
    g.line(0.385, 0.26, 0.615, 0.26); g.line(0.385, -0.26, 0.615, -0.26); g.line(0, 0, 1, 0, dashed=True)

@P.figure(OPT, "ray-diagram", "Diagrama de rayos (lente)", "Ray diagram (lens)")
def _(g):
    g.line(0, 0, 1, 0, dashed=True); g.double_arrow(0.5, -0.35, 0.5, 0.35, 0.04)
    g.arrow(0.15, 0, 0.15, 0.2, 0.04); g.line(0.15, 0.2, 0.5, 0.2, 0.75, 0, 1, -0.2); g.line(0.15, 0.2, 1, -0.2 * 0.85 / 0.35)
    for f in (0.25, 0.75): g.circle(f, 0, 0.012, fill=True)
    g.label(0.25, -0.06, "F", 0.6); g.label(0.75, -0.06, "F", 0.6)

@P.figure(OPT, "mirror-concave", "Espejo cóncavo", "Concave mirror")
def _(g):
    g.arc(0.0, 0, 0.6, 0.6, -35, 35); g.line(0, 0, 0.6, 0, dashed=True)
    for k in range(-3, 4): a = math.radians(k * 9); x, y = 0.6 * math.cos(a), 0.6 * math.sin(a); g.line(x, y, x + 0.05, y + 0.03)
    g.circle(0.3, 0, 0.012, fill=True); g.label(0.3, -0.06, "F", 0.6)

@P.figure(OPT, "mirror-plane", "Espejo plano y reflexión", "Plane mirror and reflection")
def _(g):
    g.line(0, 0, 1, 0); g.hatch(0, 1, 0, 8, 0.05); g.line(0.5, 0, 0.5, 0.5, dashed=True)
    g.arrow(0.15, 0.45, 0.5, 0, 0.04); g.arrow(0.5, 0, 0.85, 0.45, 0.04)
    g.label(0.42, 0.2, "θᵢ", 0.6); g.label(0.6, 0.2, "θᵣ", 0.6)

@P.figure(OPT, "refraction", "Refracción", "Refraction")
def _(g):
    g.line(0, 0, 1, 0); g.line(0.5, 0.45, 0.5, -0.45, dashed=True)
    g.arrow(0.2, 0.4, 0.5, 0, 0.04); g.arrow(0.5, 0, 0.65, -0.4, 0.04)
    g.label(0.1, 0.06, "n₁", 0.7); g.label(0.1, -0.08, "n₂", 0.7); g.label(0.42, 0.22, "θ₁", 0.6); g.label(0.6, -0.22, "θ₂", 0.6)

@P.figure(OPT, "prism", "Prisma óptico", "Optical prism")
def _(g):
    g.poly(0.3, -0.3, 0.7, -0.3, 0.5, 0.35); g.line(0, 0.0, 0.4, 0.02)
    for k, d in enumerate((-0.12, -0.06, 0.0)): g.line(0.6, 0.0 + d * 0.3, 1.0, -0.15 + d * 2.2, dashed=(k == 1))

@P.figure(OPT, "doppler", "Efecto Doppler", "Doppler effect")
def _(g):
    for k in range(4): g.circle(0.35 + k * 0.05, 0, 0.1 + 0.11 * k)
    g.circle(0.55, 0, 0.02, fill=True); g.arrow(0.55, 0, 0.8, 0, 0.04)

# --- Electricidad y magnetismo ------------------------------------------------------------------

@P.figure(EM, "charge-pos", "Carga positiva", "Positive charge")
def _(g):
    g.circle(0.5, 0, 0.12); g.label(0.5, 0, "+")
    for k in range(8): a = k * math.pi / 4; g.arrow(0.5 + 0.17 * math.cos(a), 0.17 * math.sin(a), 0.5 + 0.45 * math.cos(a), 0.45 * math.sin(a), 0.04)

@P.figure(EM, "charge-neg", "Carga negativa", "Negative charge")
def _(g):
    g.circle(0.5, 0, 0.12); g.label(0.5, 0, "−")
    for k in range(8): a = k * math.pi / 4; g.arrow(0.5 + 0.45 * math.cos(a), 0.45 * math.sin(a), 0.5 + 0.17 * math.cos(a), 0.17 * math.sin(a), 0.04)

@P.figure(EM, "dipole", "Dipolo eléctrico", "Electric dipole")
def _(g):
    g.circle(0.2, 0, 0.07); g.label(0.2, 0, "+", 0.8); g.circle(0.8, 0, 0.07); g.label(0.8, 0, "−", 0.8)
    for h in (0.12, 0.25, 0.38):
        g.curve(lambda u, h=h: h * math.sin(math.pi * (u - 0.27) / 0.46), 0.27, 0.73); g.curve(lambda u, h=h: -h * math.sin(math.pi * (u - 0.27) / 0.46), 0.27, 0.73)
    g.line(0.27, 0, 0.73, 0); g.head(0.45, 0, 0.55, 0, 0.03)

@P.figure(EM, "capacitor-plates", "Capacitor de placas", "Parallel-plate capacitor")
def _(g):
    g.line(0.3, -0.35, 0.3, 0.35); g.line(0.7, -0.35, 0.7, 0.35)
    for k in range(5): v = -0.28 + k * 0.14; g.arrow(0.32, v, 0.68, v, 0.03); g.label(0.25, v, "+", 0.6); g.label(0.75, v, "−", 0.6)
    g.double_arrow(0.3, -0.42, 0.7, -0.42, 0.03); g.label(0.5, -0.48, "d", 0.7)

@P.figure(EM, "magnet", "Imán y campo", "Magnet and field")
def _(g):
    g.rect(0.3, -0.08, 0.5, 0.08); g.rect(0.5, -0.08, 0.7, 0.08, fill=True); g.label(0.4, 0, "N", 0.7)
    for h in (0.2, 0.32, 0.44):
        g.arc(0.5, 0, 0.3 + h * 0.4, h, 20, 160); g.arc(0.5, 0, 0.3 + h * 0.4, h, 200, 340)

@P.figure(EM, "solenoid", "Solenoide", "Solenoid")
def _(g):
    for k in range(8): g.ellipse(0.15 + k * 0.1, 0, 0.05, 0.2)
    g.line(0, -0.2, 0.1, -0.2); g.line(0.9, -0.2, 1.0, -0.2); g.arrow(0.1, 0.32, 0.9, 0.32, 0.04); g.label(0.5, 0.38, "B", 0.7)

@P.figure(EM, "wire-field", "Corriente y campo magnético", "Current and magnetic field")
def _(g):
    g.arrow(0.5, -0.45, 0.5, 0.5, 0.04); g.label(0.56, 0.45, "I", 0.7)
    for r in (0.12, 0.22): g.ellipse(0.5, 0, r * 1.6, r * 0.5); g.head(0.5 - 0.01, -r * 0.5, 0.5 + 0.03, -r * 0.5, 0.03)
    g.label(0.9, 0.1, "B", 0.7)

@P.figure(EM, "field-into", "Campo hacia dentro (×)", "Field into page (×)")
def _(g):
    for i in range(5):
        for j in range(3): u, v = 0.1 + i * 0.2, -0.2 + j * 0.2; g.line(u - 0.03, v - 0.03, u + 0.03, v + 0.03); g.line(u - 0.03, v + 0.03, u + 0.03, v - 0.03)

@P.figure(EM, "field-out", "Campo hacia fuera (·)", "Field out of page (·)")
def _(g):
    for i in range(5):
        for j in range(3): u, v = 0.1 + i * 0.2, -0.2 + j * 0.2; g.circle(u, v, 0.035); g.circle(u, v, 0.008, fill=True)

# --- Calor y fluidos ----------------------------------------------------------------------------

@P.figure(TER, "piston", "Cilindro con pistón", "Piston cylinder")
def _(g):
    g.line(0.2, 0.5, 0.2, -0.3, 0.8, -0.3, 0.8, 0.5); g.rect(0.2, 0.15, 0.8, 0.25, fill=True); g.line(0.5, 0.25, 0.5, 0.55)
    g.label(0.5, -0.07, "gas", 0.7); g.arrow(0.5, 0.75, 0.5, 0.58, 0.04)

@P.figure(TER, "thermometer", "Termómetro", "Thermometer")
def _(g):
    g.line(0.45, 0.5, 0.45, -0.25); g.line(0.55, 0.5, 0.55, -0.25); g.arc(0.5, 0.5, 0.05, 0.05, 0, 180)
    g.circle(0.5, -0.32, 0.09); g.circle(0.5, -0.32, 0.06, fill=True); g.rect(0.48, -0.25, 0.52, 0.15, fill=True)
    for k in range(7): g.line(0.55, -0.2 + k * 0.1, 0.6, -0.2 + k * 0.1)

@P.figure(TER, "heat-engine", "Máquina térmica", "Heat engine")
def _(g):
    g.rect(0.3, 0.35, 0.7, 0.55); g.label(0.5, 0.45, "T₁", 0.7); g.rect(0.3, -0.55, 0.7, -0.35); g.label(0.5, -0.45, "T₂", 0.7)
    g.circle(0.5, 0, 0.13); g.arrow(0.5, 0.35, 0.5, 0.13, 0.04); g.label(0.56, 0.24, "Q₁", 0.6)
    g.arrow(0.5, -0.13, 0.5, -0.35, 0.04); g.label(0.57, -0.24, "Q₂", 0.6); g.arrow(0.63, 0, 0.95, 0, 0.04); g.label(0.85, 0.06, "W", 0.7)

@P.figure(TER, "pv-diagram", "Diagrama P-V", "P–V diagram")
def _(g):
    g.arrow(0, 0, 1, 0, 0.04); g.arrow(0, 0, 0, 0.7, 0.04); g.label(0.98, -0.06, "V", 0.7); g.label(-0.06, 0.68, "P", 0.7)
    g.curve(lambda u: 0.12 / u, 0.2, 0.85); g.curve(lambda u: 0.06 / u, 0.2, 0.85, dashed=True)
    g.label(0.3, 0.5, "T₂", 0.6); g.label(0.25, 0.18, "T₁", 0.6)

@P.figure(TER, "tank", "Depósito con fluido", "Fluid tank")
def _(g):
    g.line(0.1, 0.6, 0.1, -0.3, 0.9, -0.3, 0.9, 0.6); g.line(0.1, 0.35, 0.9, 0.35, dashed=True)
    g.poly(0.45, 0.42, 0.55, 0.42, 0.5, 0.36); g.double_arrow(0.75, 0.35, 0.75, -0.1, 0.03); g.label(0.8, 0.12, "h", 0.7)
    g.circle(0.75, -0.1, 0.012, fill=True)

@P.figure(TER, "pipe-flow", "Tubo de Venturi", "Venturi tube")
def _(g):
    g.line(0, 0.25, 0.3, 0.25, 0.45, 0.1, 0.55, 0.1, 0.7, 0.25, 1, 0.25)
    g.line(0, -0.25, 0.3, -0.25, 0.45, -0.1, 0.55, -0.1, 0.7, -0.25, 1, -0.25)
    g.arrow(0.05, 0, 0.25, 0, 0.04); g.label(0.15, 0.07, "v₁", 0.6); g.arrow(0.42, 0, 0.6, 0, 0.04); g.label(0.5, 0.05, "v₂", 0.6)

@P.figure(TER, "buoyancy", "Empuje (Arquímedes)", "Buoyancy (Archimedes)")
def _(g):
    g.line(0, 0.25, 1, 0.25, dashed=True); g.rect(0.35, -0.15, 0.65, 0.35)
    g.arrow(0.5, -0.15, 0.5, -0.45, 0.04); g.label(0.56, -0.4, "W", 0.7); g.arrow(0.5, 0.1, 0.5, 0.55, 0.04); g.label(0.57, 0.5, "E", 0.7)

# --- Fórmulas -----------------------------------------------------------------------------------

G = "Ciencias"
P.formulas_in(G, "Física: cinemática y dinámica", [
    ("Velocidad media", r"\bar{v} = \frac{\Delta x}{\Delta t}", "Average velocity"),
    ("MRUA: posición", r"x = x_{0} + v_{0} t + \frac{1}{2} a t^{2}", "Uniform acceleration: position"),
    ("MRUA: velocidad", r"v = v_{0} + a t", "Uniform acceleration: velocity"),
    ("MRUA: sin tiempo", r"v^{2} = v_{0}^{2} + 2 a \Delta x", "Uniform acceleration: timeless"),
    ("Caída libre", r"y = y_{0} + v_{0} t - \frac{1}{2} g t^{2}", "Free fall"),
    ("Alcance de un proyectil", r"R = \frac{v_{0}^{2} \sin 2\theta}{g}", "Projectile range"),
    ("Altura máxima", r"H = \frac{v_{0}^{2} \sin^{2} \theta}{2g}", "Maximum height"),
    ("Segunda ley de Newton", r"\sum \vec{F} = m \vec{a}", "Newton's second law"),
    ("Peso", r"W = m g", "Weight"),
    ("Fricción", r"f = \mu N", "Friction"),
    ("Aceleración centrípeta", r"a_{c} = \frac{v^{2}}{r} = \omega^{2} r", "Centripetal acceleration"),
    ("Periodo y frecuencia", r"T = \frac{1}{f} = \frac{2\pi}{\omega}", "Period and frequency"),
    ("Gravitación universal", r"F = G \frac{m_{1} m_{2}}{r^{2}}", "Universal gravitation"),
    ("Tercera ley de Kepler", r"T^{2} = \frac{4\pi^{2}}{G M} a^{3}", "Kepler's third law"),
], "Physics: kinematics and dynamics")
P.formulas_in(G, "Física: energía y momento", [
    ("Trabajo", r"W = \int \vec{F} \cdot d\vec{r} = F d \cos\theta", "Work"),
    ("Energía cinética", r"E_{k} = \frac{1}{2} m v^{2}", "Kinetic energy"),
    ("Energía potencial", r"E_{p} = m g h", "Potential energy"),
    ("Energía elástica", r"E_{e} = \frac{1}{2} k x^{2}", "Elastic energy"),
    ("Teorema trabajo-energía", r"W_{neto} = \Delta E_{k}", "Work–energy theorem"),
    ("Conservación de la energía", r"E_{k,i} + E_{p,i} = E_{k,f} + E_{p,f}", "Conservation of energy"),
    ("Potencia", r"P = \frac{dW}{dt} = \vec{F} \cdot \vec{v}", "Power"),
    ("Momento lineal", r"\vec{p} = m \vec{v}", "Linear momentum"),
    ("Impulso", r"\vec{J} = \int \vec{F} \, dt = \Delta \vec{p}", "Impulse"),
    ("Conservación del momento", r"m_{1} v_{1} + m_{2} v_{2} = m_{1} v_{1}' + m_{2} v_{2}'", "Conservation of momentum"),
    ("Centro de masa", r"x_{cm} = \frac{\sum m_{i} x_{i}}{\sum m_{i}}", "Center of mass"),
    ("Ley de Hooke", r"F = -k x", "Hooke's law"),
], "Physics: energy and momentum")
P.formulas_in(G, "Física: rotación y oscilaciones", [
    ("Torque", r"\vec{\tau} = \vec{r} \times \vec{F}", "Torque"),
    ("Dinámica rotacional", r"\sum \tau = I \alpha", "Rotational dynamics"),
    ("Momento angular", r"\vec{L} = I \vec{\omega}", "Angular momentum"),
    ("Energía rotacional", r"E_{r} = \frac{1}{2} I \omega^{2}", "Rotational energy"),
    ("Teorema de ejes paralelos", r"I = I_{cm} + M d^{2}", "Parallel axis theorem"),
    ("Relación lineal-angular", r"v = \omega r, \quad a_{t} = \alpha r", "Linear–angular relation"),
    ("Oscilador armónico", r"x(t) = A \cos(\omega t + \phi)", "Harmonic oscillator"),
    ("Masa-resorte", r"\omega = \sqrt{\frac{k}{m}}", "Mass–spring"),
    ("Péndulo simple", r"T = 2\pi \sqrt{\frac{L}{g}}", "Simple pendulum"),
    ("Oscilador amortiguado", r"x(t) = A e^{-\gamma t} \cos(\omega_{d} t + \phi)", "Damped oscillator"),
], "Physics: rotation and oscillations")
P.formulas_in(G, "Física: ondas y óptica", [
    ("Velocidad de onda", r"v = \lambda f", "Wave speed"),
    ("Onda viajera", r"y(x, t) = A \sin(k x - \omega t)", "Travelling wave"),
    ("Cuerda tensa", r"v = \sqrt{\frac{T}{\mu}}", "Taut string"),
    ("Armónicos", r"f_{n} = \frac{n v}{2L}", "Harmonics"),
    ("Nivel de intensidad", r"\beta = 10 \log_{10} \frac{I}{I_{0}}", "Intensity level"),
    ("Efecto Doppler", r"f' = f \frac{v \pm v_{o}}{v \mp v_{s}}", "Doppler effect"),
    ("Ley de Snell", r"n_{1} \sin\theta_{1} = n_{2} \sin\theta_{2}", "Snell's law"),
    ("Índice de refracción", r"n = \frac{c}{v}", "Refractive index"),
    ("Lente delgada", r"\frac{1}{f} = \frac{1}{d_{o}} + \frac{1}{d_{i}}", "Thin lens"),
    ("Aumento", r"M = -\frac{d_{i}}{d_{o}} = \frac{h_{i}}{h_{o}}", "Magnification"),
    ("Doble rendija", r"d \sin\theta = m \lambda", "Double slit"),
    ("Ley de Malus", r"I = I_{0} \cos^{2}\theta", "Malus's law"),
], "Physics: waves and optics")
P.formulas_in(G, "Física: electromagnetismo", [
    ("Ley de Coulomb", r"F = k \frac{|q_{1} q_{2}|}{r^{2}}", "Coulomb's law"),
    ("Campo eléctrico", r"\vec{E} = \frac{\vec{F}}{q} = k \frac{q}{r^{2}} \hat{r}", "Electric field"),
    ("Potencial eléctrico", r"V = k \frac{q}{r}", "Electric potential"),
    ("Capacitor de placas", r"C = \varepsilon_{0} \frac{A}{d}", "Parallel-plate capacitor"),
    ("Energía en un capacitor", r"U = \frac{1}{2} C V^{2}", "Energy in a capacitor"),
    ("Gauss", r"\oint \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\varepsilon_{0}}", "Gauss's law"),
    ("Gauss magnético", r"\oint \vec{B} \cdot d\vec{A} = 0", "Gauss's law for magnetism"),
    ("Faraday", r"\varepsilon = -\frac{d\Phi_{B}}{dt}", "Faraday's law"),
    ("Ampère-Maxwell", r"\oint \vec{B} \cdot d\vec{l} = \mu_{0} I + \mu_{0} \varepsilon_{0} \frac{d\Phi_{E}}{dt}", "Ampère–Maxwell law"),
    ("Fuerza de Lorentz", r"\vec{F} = q (\vec{E} + \vec{v} \times \vec{B})", "Lorentz force"),
    ("Biot-Savart", r"d\vec{B} = \frac{\mu_{0}}{4\pi} \frac{I \, d\vec{l} \times \hat{r}}{r^{2}}", "Biot–Savart law"),
    ("Campo de un hilo", r"B = \frac{\mu_{0} I}{2 \pi r}", "Field of a wire"),
    ("Solenoide", r"B = \mu_{0} n I", "Solenoid"),
    ("Flujo magnético", r"\Phi_{B} = \int \vec{B} \cdot d\vec{A}", "Magnetic flux"),
], "Physics: electromagnetism")
P.formulas_in(G, "Física: termodinámica y fluidos", [
    ("Gas ideal", r"P V = n R T", "Ideal gas"),
    ("Primera ley", r"\Delta U = Q - W", "First law"),
    ("Calor sensible", r"Q = m c \Delta T", "Sensible heat"),
    ("Calor latente", r"Q = m L", "Latent heat"),
    ("Dilatación lineal", r"\Delta L = \alpha L_{0} \Delta T", "Linear expansion"),
    ("Trabajo de un gas", r"W = \int_{V_{1}}^{V_{2}} P \, dV", "Work of a gas"),
    ("Entropía", r"\Delta S = \int \frac{dQ_{rev}}{T}", "Entropy"),
    ("Eficiencia de Carnot", r"\eta = 1 - \frac{T_{C}}{T_{H}}", "Carnot efficiency"),
    ("Conducción (Fourier)", r"\dot{Q} = -k A \frac{dT}{dx}", "Conduction (Fourier)"),
    ("Stefan-Boltzmann", r"P = \varepsilon \sigma A T^{4}", "Stefan–Boltzmann"),
    ("Presión hidrostática", r"P = P_{0} + \rho g h", "Hydrostatic pressure"),
    ("Principio de Arquímedes", r"E = \rho_{f} g V_{d}", "Archimedes' principle"),
    ("Continuidad", r"A_{1} v_{1} = A_{2} v_{2}", "Continuity"),
    ("Bernoulli", r"P + \frac{1}{2} \rho v^{2} + \rho g h = \text{cte}", "Bernoulli"),
    ("Torricelli", r"v = \sqrt{2 g h}", "Torricelli"),
], "Physics: thermodynamics and fluids")
P.formulas_in(G, "Física moderna", [
    ("Equivalencia masa-energía", r"E = m c^{2}", "Mass–energy equivalence"),
    ("Factor de Lorentz", r"\gamma = \frac{1}{\sqrt{1 - v^{2}/c^{2}}}", "Lorentz factor"),
    ("Dilatación del tiempo", r"\Delta t = \gamma \Delta t_{0}", "Time dilation"),
    ("Energía del fotón", r"E = h f = \frac{h c}{\lambda}", "Photon energy"),
    ("Efecto fotoeléctrico", r"E_{k,max} = h f - \phi", "Photoelectric effect"),
    ("De Broglie", r"\lambda = \frac{h}{p}", "De Broglie"),
    ("Incertidumbre de Heisenberg", r"\Delta x \, \Delta p \ge \frac{\hbar}{2}", "Heisenberg uncertainty"),
    ("Schrödinger", r"i \hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi", "Schrödinger"),
    ("Niveles de Bohr", r"E_{n} = -\frac{13.6 \text{ eV}}{n^{2}}", "Bohr levels"),
    ("Decaimiento radiactivo", r"N(t) = N_{0} e^{-\lambda t}", "Radioactive decay"),
    ("Vida media", r"t_{1/2} = \frac{\ln 2}{\lambda}", "Half-life"),
], "Modern physics")

P.labels = [["Datos", "#2563eb"], ["Incógnita", "#dc2626"], ["Diagrama de cuerpo libre", "#7c3aed"], ["Resultado", "#16a34a"],
            ["Unidades SI", "#0891b2"], ["Suposición", "#ca8a04"], ["Ley", "#be185d"], ["Experimento", "#ea580c"]]
P.en.update({"Datos": "Data", "Incógnita": "Unknown", "Diagrama de cuerpo libre": "Free-body diagram", "Resultado": "Result",
             "Unidades SI": "SI units", "Suposición": "Assumption", "Ley": "Law", "Experimento": "Experiment"})
P.emoji = {"Física": "⚛️ 🧲 🔭 🌡️ ⚡ 💡 🪐 🌍 🚀 🎯 ⏱️ 📏 ⚖️ 🔋 🌈 🔊 ❄️ 🔥"}
