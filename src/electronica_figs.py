"""Figuras de Señales y sistemas, Comunicaciones y Sistemas embebidos (Electrónica, Biomédica, Robótica)."""
import math

SG = "Señales: sistemas"
EM = "Embebidos: bloques"


def blk(g, u0, v0, u1, v1, text, s=0.6):
    g.rect(u0, v0, u1, v1); g.label((u0 + u1) / 2, (v0 + v1) / 2, text, s)


def ar(g, u0, v0, u1, v1, size=0.035): g.arrow(u0, v0, u1, v1, size)


def dot(g, u, v): g.circle(u, v, 0.012, fill=True)


def axes(g, u0, v0, u1, v1, xl="t", yl="x", up=0.04):
    g.arrow(u0, v0, u1, v0, up); g.arrow(u0, v0, u0, v1, up)
    g.label(u1 - 0.02, v0 - 0.07, xl, 0.7); g.label(u0 - 0.06, v1 - 0.02, yl, 0.7)


def gnd(g, u, v):
    g.line(u, v, u, v - 0.05); g.line(u - 0.07, v - 0.05, u + 0.07, v - 0.05); g.line(u - 0.045, v - 0.085, u + 0.045, v - 0.085); g.line(u - 0.02, v - 0.12, u + 0.02, v - 0.12)


def state(g, u, v, r, text):
    g.circle(u, v, r); g.label(u, v, text, 0.7)


def link(g, a, b, r, text, bend=0.0):
    dx, dy = b[0] - a[0], b[1] - a[1]; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    p0 = (a[0] + ux * r, a[1] + uy * r); p1 = (b[0] - ux * r, b[1] - uy * r)
    g.arrow(p0[0], p0[1], p1[0], p1[1], 0.035)
    g.label((p0[0] + p1[0]) / 2 - uy * 0.07, (p0[1] + p1[1]) / 2 + ux * 0.07, text, 0.55)


def extend(P):
    P.en.update({SG: "Signals: systems", EM: "Embedded: blocks"})

    # ---------------- Señales y sistemas ----------------
    @P.figure(SG, "sig-continuous", "Señal continua x(t)", "Continuous signal")
    def _(g):
        axes(g, 0, 0, 1, 0.5, "t", "x(t)"); g.curve(lambda u: 0.3 * math.sin(2 * math.pi * 2.2 * u), 0, 0.96, 96)

    @P.figure(SG, "sig-discrete", "Señal discreta x[n]", "Discrete signal")
    def _(g):
        axes(g, 0, 0, 1, 0.5, "n", "x[n]")
        for k in range(1, 12):
            u = k / 12.5; v = 0.3 * math.sin(2 * math.pi * 2.2 * u); g.line(u, 0, u, v); g.circle(u, v, 0.014, fill=True)

    @P.figure(SG, "sig-sampling", "Muestreo de una señal", "Sampling")
    def _(g):
        axes(g, 0, 0, 1, 0.5, "t", "x")
        g.curve(lambda u: 0.3 * math.sin(2 * math.pi * 1.5 * u), 0, 0.96, 96, dashed=True)
        for k in range(1, 13):
            u = k / 13.5; v = 0.3 * math.sin(2 * math.pi * 1.5 * u); g.line(u, 0, u, v); g.circle(u, v, 0.014, fill=True)
        g.double_arrow(1 / 13.5, -0.12, 2 / 13.5, -0.12, 0.02); g.label(1.5 / 13.5, -0.2, "Ts", 0.6)

    def response(g, f, marks):
        axes(g, 0, 0, 1, 0.55, "ω", "|H|")
        g.curve(f, 0.02, 0.97, 96)
        for u, t in marks: g.line(u, 0, u, 0.32, dashed=True); g.label(u, -0.07, t, 0.6)
        g.line(0, 0.32, 1, 0.32, dashed=True); g.label(-0.08, 0.32, "1", 0.55)

    @P.figure(SG, "filter-lp", "Filtro pasa-bajas", "Low-pass filter")
    def _(g): response(g, lambda u: 0.32 / math.sqrt(1 + (u / 0.4) ** 6), [(0.4, "ωc")])

    @P.figure(SG, "filter-hp", "Filtro pasa-altas", "High-pass filter")
    def _(g): response(g, lambda u: 0.32 / math.sqrt(1 + (0.4 / max(u, 0.001)) ** 6), [(0.4, "ωc")])

    @P.figure(SG, "filter-bp", "Filtro pasa-banda", "Band-pass filter")
    def _(g): response(g, lambda u: 0.32 / math.sqrt(1 + (4 * (u - 0.5)) ** 4 * 4), [(0.5, "ω₀")])

    @P.figure(SG, "filter-bs", "Filtro rechaza-banda", "Band-stop filter")
    def _(g): response(g, lambda u: 0.32 * (1 - 1 / (1 + (4 * (u - 0.5)) ** 4 * 4)), [(0.5, "ω₀")])

    @P.figure(SG, "mod-am", "Modulación AM", "Amplitude modulation")
    def _(g):
        axes(g, 0, 0, 1, 0.55, "t", "s(t)")
        env = lambda u: 0.28 * (1 + 0.6 * math.cos(2 * math.pi * 1.4 * u)) / 1.6 + 0.04
        g.curve(lambda u: env(u) * math.sin(2 * math.pi * 16 * u), 0, 0.96, 400)
        g.curve(env, 0, 0.96, 64, dashed=True); g.curve(lambda u: -env(u), 0, 0.96, 64, dashed=True)
        g.label(0.7, 0.4, "envolvente m(t)", 0.45)

    @P.figure(SG, "mod-fm", "Modulación FM", "Frequency modulation")
    def _(g):
        axes(g, 0, 0, 1, 0.5, "t", "s(t)")
        g.curve(lambda u: 0.28 * math.sin(2 * math.pi * 12 * u + 5 * math.sin(2 * math.pi * 1.3 * u)), 0, 0.96, 400)

    @P.figure(SG, "sig-spectrum", "Espectro de frecuencia", "Frequency spectrum")
    def _(g):
        axes(g, 0, 0, 1, 0.55, "f", "|X(f)|")
        for f, a in ((0.3, 0.38), (0.6, 0.22), (0.8, 0.12)):
            g.line(f, 0, f, a); g.head(f, 0, f, a, 0.03); g.label(f, -0.07, "f" + "₁₂₃"[[0.3, 0.6, 0.8].index(f)], 0.55)

    @P.figure(SG, "sig-lti", "Sistema LTI: h(t) y convolución", "LTI system")
    def _(g):
        ar(g, 0, 0, 0.3, 0); blk(g, 0.3, -0.16, 0.7, 0.16, "h(t)", 0.9); ar(g, 0.7, 0, 1, 0)
        g.label(0.12, 0.08, "x(t)", 0.6); g.label(0.9, 0.08, "y(t)", 0.6)
        g.label(0.5, -0.3, "y(t) = x(t) * h(t)", 0.55); g.label(0.5, -0.42, "Y(s) = H(s) X(s)", 0.55)

    @P.figure(SG, "sig-adc", "Conversión A/D en bloques", "A/D conversion blocks")
    def _(g):
        xs = [(0.0, 0.2, "Filtro"), (0.27, 0.47, "S/H"), (0.54, 0.74, "Cuantiz."), (0.81, 1.0, "Codif.")]
        for k, (a, b, t) in enumerate(xs):
            blk(g, a, -0.1, b, 0.1, t, 0.45)
            if k: ar(g, xs[k - 1][1], 0, a, 0)
        g.label(0.1, 0.2, "x(t)", 0.55); g.label(0.9, 0.2, "bits", 0.55); g.label(0.5, -0.25, "fs ≥ 2·fmax", 0.5)

    @P.figure(SG, "sig-dac", "Conversión D/A en bloques", "D/A conversion blocks")
    def _(g):
        xs = [(0.0, 0.25, "DAC"), (0.375, 0.625, "ZOH"), (0.75, 1.0, "Filtro")]
        for k, (a, b, t) in enumerate(xs):
            blk(g, a, -0.1, b, 0.1, t, 0.5)
            if k: ar(g, xs[k - 1][1], 0, a, 0)
        g.label(0.0, 0.2, "bits", 0.55); g.label(0.95, 0.2, "y(t)", 0.55)

    @P.figure(SG, "comm-chain", "Sistema de comunicaciones", "Communication system")
    def _(g):
        xs = [(0.0, 0.2, "Fuente"), (0.25, 0.47, "Transm."), (0.62, 0.78, "Canal"), (0.82, 1.0, "Recep.")]
        blk(g, 0.0, -0.1, 0.2, 0.1, "Fuente", 0.45); ar(g, 0.2, 0, 0.25, 0)
        blk(g, 0.25, -0.1, 0.47, 0.1, "Transm.", 0.45); ar(g, 0.47, 0, 0.62, 0)
        blk(g, 0.62, -0.1, 0.78, 0.1, "Canal", 0.45); ar(g, 0.78, 0, 0.82, 0)
        blk(g, 0.82, -0.1, 1.0, 0.1, "Recep.", 0.45)
        ar(g, 0.7, 0.35, 0.7, 0.1); g.label(0.7, 0.42, "ruido n(t)", 0.45)

    # ---------------- Sistemas embebidos ----------------
    @P.figure(EM, "emb-mcu", "Microcontrolador (pines)", "Microcontroller pins")
    def _(g):
        g.rect(0.3, -0.42, 0.7, 0.42)
        for v, a, b in ((0.3, "VCC", "PB0"), (0.1, "GND", "PB1"), (-0.1, "RST", "PB2"), (-0.3, "PA0", "TX")):
            g.line(0.15, v, 0.3, v); g.line(0.7, v, 0.85, v); g.label(0.37, v, a, 0.42); g.label(0.63, v, b, 0.42)
        g.label(0.5, 0.0, "MCU", 0.9)

    @P.figure(EM, "emb-i2c", "Bus I²C", "I2C bus")
    def _(g):
        blk(g, 0.0, -0.14, 0.2, 0.14, "Maestro", 0.5)
        g.line(0.2, 0.07, 0.95, 0.07); g.line(0.2, -0.07, 0.95, -0.07); g.label(0.27, 0.15, "SDA", 0.45); g.label(0.27, -0.15, "SCL", 0.45)
        for u, t in ((0.45, "Esclavo 1"), (0.75, "Esclavo 2")):
            blk(g, u - 0.11, -0.48, u + 0.11, -0.28, t, 0.38)
            g.line(u - 0.04, -0.28, u - 0.04, 0.07); g.line(u + 0.04, -0.28, u + 0.04, -0.07); dot(g, u - 0.04, 0.07); dot(g, u + 0.04, -0.07)
        g.line(0.55, 0.5, 0.95, 0.5); g.label(0.75, 0.57, "VCC", 0.5)
        g.rect(0.855, 0.2, 0.895, 0.4); g.line(0.875, 0.5, 0.875, 0.4); g.line(0.875, 0.2, 0.875, 0.07); dot(g, 0.875, 0.07)
        g.label(0.81, 0.3, "Rp", 0.45)

    @P.figure(EM, "emb-spi", "Bus SPI", "SPI bus")
    def _(g):
        blk(g, 0.0, -0.38, 0.25, 0.38, "Maestro", 0.5); blk(g, 0.75, -0.38, 1.0, 0.38, "Esclavo", 0.5)
        for v, t, d in ((0.27, "SCK", 1), (0.09, "MOSI", 1), (-0.09, "MISO", -1), (-0.27, "CS", 1)):
            if d > 0: ar(g, 0.25, v, 0.75, v)
            else: ar(g, 0.75, v, 0.25, v)
            g.label(0.5, v + 0.06, t, 0.5)

    @P.figure(EM, "emb-uart", "Enlace UART", "UART link")
    def _(g):
        blk(g, 0.0, -0.3, 0.25, 0.3, "Disp. A", 0.5); blk(g, 0.75, -0.3, 1.0, 0.3, "Disp. B", 0.5)
        ar(g, 0.25, 0.14, 0.75, -0.06); ar(g, 0.75, 0.14, 0.25, -0.06)
        g.line(0.25, -0.2, 0.75, -0.2); g.label(0.5, -0.28, "GND", 0.45)
        g.label(0.31, 0.22, "TX", 0.45); g.label(0.69, 0.22, "TX", 0.45); g.label(0.31, -0.13, "RX", 0.45); g.label(0.69, -0.13, "RX", 0.45)

    @P.figure(EM, "emb-pwm", "Señal PWM", "PWM signal")
    def _(g):
        g.arrow(0, 0, 1, 0, 0.04); g.arrow(0, 0, 0, 0.55, 0.04); g.label(0.95, -0.07, "t", 0.7); g.label(-0.06, 0.5, "V", 0.7)
        pts = [(0.05, 0)]
        for k in range(3):
            u = 0.05 + 0.3 * k; pts += [(u, 0.4), (u + 0.12, 0.4), (u + 0.12, 0), (u + 0.3, 0)]
        g._add(pts)
        g.double_arrow(0.05, 0.47, 0.17, 0.47, 0.02); g.label(0.11, 0.54, "ton", 0.45)
        g.double_arrow(0.05, -0.12, 0.35, -0.12, 0.02); g.label(0.2, -0.2, "T", 0.5); g.label(0.7, -0.22, "D = ton / T", 0.5)

    @P.figure(EM, "emb-hbridge", "Puente H para motor", "H-bridge")
    def _(g):
        g.line(0.2, 0.45, 0.8, 0.45); g.line(0.2, -0.45, 0.8, -0.45); g.label(0.5, 0.53, "VCC", 0.5); g.label(0.5, -0.53, "GND", 0.5)
        for u in (0.2, 0.8):
            g.line(u, 0.45, u, 0.35); blk(g, u - 0.07, 0.15, u + 0.07, 0.35, "S1" if u < 0.5 else "S3", 0.45); g.line(u, 0.15, u, -0.15)
            blk(g, u - 0.07, -0.35, u + 0.07, -0.15, "S2" if u < 0.5 else "S4", 0.45); g.line(u, -0.35, u, -0.45)
        g.line(0.2, 0, 0.4, 0); g.line(0.6, 0, 0.8, 0); dot(g, 0.2, 0); dot(g, 0.8, 0); g.circle(0.5, 0, 0.1); g.label(0.5, 0, "M", 0.8)

    @P.figure(EM, "emb-divider", "Divisor de voltaje", "Voltage divider")
    def _(g):
        g.line(0.5, 0.45, 0.5, 0.3); g.label(0.5, 0.52, "Vin", 0.6); g.rect(0.45, 0.1, 0.55, 0.3); g.label(0.36, 0.2, "R1", 0.55)
        g.line(0.5, 0.1, 0.5, -0.1); dot(g, 0.5, 0); g.arrow(0.5, 0, 0.85, 0, 0.035); g.label(0.93, 0, "Vout", 0.55)
        g.rect(0.45, -0.3, 0.55, -0.1); g.label(0.36, -0.2, "R2", 0.55); g.line(0.5, -0.3, 0.5, -0.38); gnd(g, 0.5, -0.38)

    @P.figure(EM, "emb-opto", "Optoacoplador", "Optocoupler")
    def _(g):
        g.rect(0.1, -0.3, 0.9, 0.3, dashed=True)
        g.line(0.25, 0.45, 0.25, 0.15); g.poly(0.17, 0.15, 0.33, 0.15, 0.25, 0.0); g.line(0.17, 0.0, 0.33, 0.0); g.line(0.25, 0.0, 0.25, -0.45)
        g.line(0.7, 0.12, 0.7, -0.12); g.line(0.7, 0.05, 0.8, 0.14, 0.8, 0.45); g.line(0.7, -0.05, 0.8, -0.14, 0.8, -0.45)
        g.head(0.7, -0.05, 0.8, -0.14, 0.03)
        g.arrow(0.4, 0.1, 0.62, 0.1, 0.03); g.arrow(0.4, -0.04, 0.62, -0.04, 0.03)
        g.label(0.1, 0.4, "A", 0.5); g.label(0.38, -0.2, "LED", 0.5); g.label(0.97, 0.0, "FT", 0.5)

    @P.figure(EM, "emb-chain", "Sensor → ADC → MCU → actuador", "Sensor to actuator chain")
    def _(g):
        names = ["Sensor", "ADC", "MCU", "Driver", "Actuad."]
        w = 0.17; gap = (1 - 5 * w) / 4
        for k, t in enumerate(names):
            u = k * (w + gap); blk(g, u, -0.12, u + w, 0.12, t, 0.4)
            if k: ar(g, u - gap, 0, u, 0, 0.025)
        g.label(0.5, -0.3, "lazo de medición y control", 0.45)

    @P.figure(EM, "emb-fsm", "Máquina de estados", "State machine")
    def _(g):
        A, B, C = (0.22, 0.15), (0.78, 0.15), (0.5, -0.3); r = 0.12
        state(g, *A, r, "S0"); state(g, *B, r, "S1"); state(g, *C, r, "S2")
        g.arrow(0.0, 0.15, 0.1, 0.15, 0.03)
        link(g, A, B, r, "a"); link(g, B, C, r, "b"); link(g, C, A, r, "c")

    @P.figure(EM, "emb-timer", "Temporizador / contador", "Timer / counter")
    def _(g):
        ar(g, 0, 0, 0.08, 0, 0.03); g.label(0.03, 0.08, "clk", 0.4)
        blk(g, 0.08, -0.1, 0.3, 0.1, "Prescaler", 0.4); ar(g, 0.3, 0, 0.36, 0, 0.03)
        blk(g, 0.36, -0.1, 0.58, 0.1, "Contador", 0.4); ar(g, 0.58, 0, 0.64, 0, 0.03)
        blk(g, 0.64, -0.1, 0.88, 0.1, "Comparador", 0.4); ar(g, 0.88, 0, 1.0, 0, 0.03)
        blk(g, 0.64, -0.42, 0.88, -0.24, "OCR", 0.45); ar(g, 0.76, -0.24, 0.76, -0.1, 0.03); g.label(0.95, 0.08, "salida", 0.4)

    @P.figure(EM, "emb-pullup", "Botón con pull-up", "Pull-up button input")
    def _(g):
        g.line(0.4, 0.45, 0.6, 0.45); g.label(0.5, 0.52, "VCC", 0.5); g.line(0.5, 0.45, 0.5, 0.3); g.rect(0.45, 0.1, 0.55, 0.3); g.label(0.36, 0.2, "R", 0.55)
        g.line(0.5, 0.1, 0.5, 0.0); dot(g, 0.5, 0); g.arrow(0.5, 0, 0.72, 0, 0.03); blk(g, 0.72, -0.1, 1.0, 0.1, "Pin MCU", 0.4)
        g.line(0.5, 0, 0.5, -0.1); g.circle(0.5, -0.12, 0.012); g.line(0.5, -0.13, 0.4, -0.24); g.circle(0.5, -0.27, 0.012); g.line(0.5, -0.28, 0.5, -0.36)
        gnd(g, 0.5, -0.36); g.label(0.3, -0.18, "BTN", 0.45)

    @P.figure(EM, "emb-led", "Salida GPIO a LED", "GPIO to LED")
    def _(g):
        blk(g, 0.0, -0.12, 0.2, 0.12, "GPIO", 0.45); g.line(0.2, 0, 0.3, 0); g.zigzag(0.3, 0.6, 0.0, 0.06, 4, 0.04); g.label(0.45, 0.15, "R", 0.55)
        g.line(0.6, 0, 0.66, 0); g.poly(0.66, -0.1, 0.66, 0.1, 0.78, 0); g.line(0.78, -0.1, 0.78, 0.1); g.line(0.78, 0, 0.9, 0)
        g.line(0.9, 0, 0.9, -0.2); gnd(g, 0.9, -0.2)
        g.arrow(0.72, 0.15, 0.8, 0.27, 0.025); g.arrow(0.78, 0.12, 0.86, 0.24, 0.025); g.label(0.72, -0.14, "LED", 0.45)
