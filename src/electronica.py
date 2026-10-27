import math
from wgpack import Pack

pack = Pack("electronica", "Electrónica y eléctrica", "Símbolos de circuitos, compuertas lógicas, instrumentos y formulario de circuitos, AC, analógica, digital y potencia.",
            "Ingenierías", "⚡", en={"Electrónica y eléctrica": "Electronics and electrical",
            "Símbolos de circuitos, compuertas lógicas, instrumentos y formulario de circuitos, AC, analógica, digital y potencia.":
            "Circuit symbols, logic gates, instruments and formulas for circuits, AC, analog, digital and power."})
P = pack
PAS, SRC, SEM, DIG, INS = "Electrónica: pasivos", "Electrónica: fuentes y conexiones", "Electrónica: semiconductores", "Electrónica: digital", "Electrónica: instrumentos y otros"
P.en.update({PAS: "Electronics: passive", SRC: "Electronics: sources and wiring", SEM: "Electronics: semiconductors", DIG: "Electronics: digital", INS: "Electronics: instruments and more"})


def leads(g, a=0.3, b=0.7):
    g.line(0, 0, a, 0); g.line(b, 0, 1, 0)

# --- Pasivos ----------------------------------------------------------------------------------

@P.figure(PAS, "resistor", "Resistencia", "Resistor")
def _(g): g.line(0, 0, 0.25, 0, 0.29, 0.1, 0.37, -0.1, 0.45, 0.1, 0.53, -0.1, 0.61, 0.1, 0.69, -0.1, 0.73, 0, 1, 0)

@P.figure(PAS, "resistor-iec", "Resistencia (IEC)", "Resistor (IEC)")
def _(g): leads(g, 0.25, 0.75); g.rect(0.25, -0.08, 0.75, 0.08)

@P.figure(PAS, "potentiometer", "Potenciómetro", "Potentiometer")
def _(g):
    g.line(0, 0, 0.25, 0, 0.29, 0.1, 0.37, -0.1, 0.45, 0.1, 0.53, -0.1, 0.61, 0.1, 0.69, -0.1, 0.73, 0, 1, 0)
    g.arrow(0.49, 0.4, 0.49, 0.13, 0.04)

@P.figure(PAS, "variable-resistor", "Resistencia variable", "Variable resistor")
def _(g):
    g.line(0, 0, 0.25, 0, 0.29, 0.1, 0.37, -0.1, 0.45, 0.1, 0.53, -0.1, 0.61, 0.1, 0.69, -0.1, 0.73, 0, 1, 0)
    g.arrow(0.3, -0.2, 0.7, 0.22, 0.04)

@P.figure(PAS, "capacitor", "Capacitor", "Capacitor")
def _(g): g.line(0, 0, 0.45, 0); g.line(0.45, -0.18, 0.45, 0.18); g.line(0.55, -0.18, 0.55, 0.18); g.line(0.55, 0, 1, 0)

@P.figure(PAS, "capacitor-pol", "Capacitor electrolítico", "Electrolytic capacitor")
def _(g):
    g.line(0, 0, 0.45, 0); g.line(0.45, -0.18, 0.45, 0.18); g.arc(0.68, 0, 0.12, 0.2, 125, 235); g.line(0.56, 0, 1, 0)
    g.label(0.38, 0.22, "+", 0.7)

@P.figure(PAS, "inductor", "Inductor", "Inductor")
def _(g):
    g.line(0, 0, 0.2, 0)
    for k in range(4): g.arc(0.275 + k * 0.15, 0, 0.075, 0.1, 180, 0)
    g.line(0.8, 0, 1, 0)

@P.figure(PAS, "transformer", "Transformador", "Transformer")
def _(g):
    for k in range(4): g.arc(0.38, 0.27 - k * 0.15, 0.08, 0.075, 90, -90)
    for k in range(4): g.arc(0.62, 0.27 - k * 0.15, 0.08, 0.075, 90, 270)
    g.line(0.47, 0.35, 0.47, -0.35); g.line(0.53, 0.35, 0.53, -0.35)
    g.line(0, 0.345, 0.38, 0.345); g.line(0, -0.255, 0.38, -0.255); g.line(0.62, 0.345, 1, 0.345); g.line(0.62, -0.255, 1, -0.255)

@P.figure(PAS, "fuse", "Fusible", "Fuse")
def _(g): leads(g, 0.25, 0.75); g.rect(0.25, -0.08, 0.75, 0.08); g.line(0.25, 0, 0.75, 0)

@P.figure(PAS, "crystal", "Cristal (oscilador)", "Crystal")
def _(g): g.line(0, 0, 0.4, 0); g.line(0.4, -0.15, 0.4, 0.15); g.rect(0.45, -0.12, 0.55, 0.12); g.line(0.6, -0.15, 0.6, 0.15); g.line(0.6, 0, 1, 0)

# --- Fuentes y conexiones ------------------------------------------------------------------------

@P.figure(SRC, "battery", "Batería", "Battery")
def _(g):
    g.line(0, 0, 0.42, 0); g.line(0.42, -0.2, 0.42, 0.2); g.line(0.5, -0.1, 0.5, 0.1); g.line(0.58, -0.2, 0.58, 0.2); g.line(0.66, -0.1, 0.66, 0.1)
    g.line(0.66, 0, 1, 0); g.label(0.38, 0.27, "+", 0.7); g.label(0.7, 0.27, "−", 0.7)

@P.figure(SRC, "cell", "Pila", "Cell")
def _(g): g.line(0, 0, 0.46, 0); g.line(0.46, -0.2, 0.46, 0.2); g.line(0.54, -0.1, 0.54, 0.1); g.line(0.54, 0, 1, 0)

@P.figure(SRC, "dc-source", "Fuente DC", "DC source")
def _(g): leads(g); g.circle(0.5, 0, 0.2); g.label(0.42, 0, "+", 0.7); g.label(0.58, 0, "−", 0.7)

@P.figure(SRC, "ac-source", "Fuente AC", "AC source")
def _(g):
    leads(g); g.circle(0.5, 0, 0.2)
    g.curve(lambda u: 0.07 * math.sin((u - 0.38) / 0.24 * 2 * math.pi), 0.38, 0.62, 24)

@P.figure(SRC, "current-source", "Fuente de corriente", "Current source")
def _(g): leads(g); g.circle(0.5, 0, 0.2); g.arrow(0.4, 0, 0.6, 0, 0.05)

@P.figure(SRC, "dep-voltage", "Fuente dependiente de voltaje", "Dependent voltage source")
def _(g): leads(g); g.poly(0.3, 0, 0.5, 0.2, 0.7, 0, 0.5, -0.2); g.label(0.42, 0, "+", 0.6); g.label(0.58, 0, "−", 0.6)

@P.figure(SRC, "dep-current", "Fuente dependiente de corriente", "Dependent current source")
def _(g): leads(g); g.poly(0.3, 0, 0.5, 0.2, 0.7, 0, 0.5, -0.2); g.arrow(0.4, 0, 0.6, 0, 0.04)

@P.figure(SRC, "ground", "Tierra", "Ground")
def _(g): g.line(0.5, 0.4, 0.5, 0); g.line(0.25, 0, 0.75, 0); g.line(0.33, -0.08, 0.67, -0.08); g.line(0.42, -0.16, 0.58, -0.16)

@P.figure(SRC, "chassis", "Tierra de chasis", "Chassis ground")
def _(g):
    g.line(0.5, 0.4, 0.5, 0); g.line(0.25, 0, 0.75, 0)
    for k in range(4): u = 0.28 + k * 0.15; g.line(u, 0, u - 0.08, -0.12)

@P.figure(SRC, "vcc", "Alimentación (Vcc)", "Supply (Vcc)")
def _(g): g.line(0.5, -0.3, 0.5, 0.1); g.line(0.35, 0.1, 0.65, 0.1); g.label(0.5, 0.22, "Vcc", 0.7)

@P.figure(SRC, "node", "Nodo", "Node")
def _(g): g.line(0, 0, 1, 0); g.circle(0.5, 0, 0.03, fill=True)

@P.figure(SRC, "tee", "Unión en T", "T junction")
def _(g): g.line(0, 0, 1, 0); g.line(0.5, 0, 0.5, -0.5); g.circle(0.5, 0, 0.03, fill=True)

@P.figure(SRC, "crossing", "Cruce sin conexión", "Crossing (no connection)")
def _(g): g.line(0, 0, 0.44, 0); g.arc(0.5, 0, 0.06, 0.06, 180, 0); g.line(0.56, 0, 1, 0); g.line(0.5, 0.5, 0.5, -0.5)

@P.figure(SRC, "terminal", "Borne", "Terminal")
def _(g): g.line(0, 0, 0.85, 0); g.circle(0.9, 0, 0.05)

@P.figure(SRC, "switch", "Interruptor", "Switch")
def _(g): g.line(0, 0, 0.3, 0); g.circle(0.32, 0, 0.02, fill=True); g.line(0.32, 0, 0.66, 0.18); g.circle(0.68, 0, 0.02, fill=True); g.line(0.7, 0, 1, 0)

@P.figure(SRC, "pushbutton", "Pulsador", "Push button")
def _(g):
    g.line(0, 0, 0.3, 0); g.circle(0.32, 0, 0.02, fill=True); g.circle(0.68, 0, 0.02, fill=True); g.line(0.7, 0, 1, 0)
    g.line(0.28, 0.08, 0.72, 0.08); g.line(0.5, 0.08, 0.5, 0.25); g.line(0.42, 0.25, 0.58, 0.25)

@P.figure(SRC, "switch-spdt", "Conmutador", "SPDT switch")
def _(g):
    g.line(0, 0, 0.3, 0); g.circle(0.32, 0, 0.02, fill=True); g.line(0.32, 0, 0.66, 0.12)
    g.circle(0.68, 0.15, 0.02, fill=True); g.circle(0.68, -0.15, 0.02, fill=True); g.line(0.7, 0.15, 1, 0.15); g.line(0.7, -0.15, 1, -0.15)

@P.figure(SRC, "relay", "Relevador", "Relay")
def _(g):
    g.rect(0.1, -0.35, 0.4, -0.1); g.line(0.1, -0.35, 0.4, -0.1)
    g.line(0.55, 0.1, 0.62, 0.1); g.line(0.62, 0.1, 0.9, 0.25); g.line(0.88, 0.1, 1, 0.1); g.line(0.25, -0.1, 0.75, 0.17, dashed=True)

# --- Semiconductores ------------------------------------------------------------------------------

def diode(g):
    g.line(0, 0, 0.38, 0); g.poly(0.38, 0.15, 0.38, -0.15, 0.6, 0); g.line(0.6, 0, 1, 0)

@P.figure(SEM, "diode", "Diodo", "Diode")
def _(g): diode(g); g.line(0.6, -0.15, 0.6, 0.15)

@P.figure(SEM, "zener", "Diodo Zener", "Zener diode")
def _(g): diode(g); g.line(0.55, -0.18, 0.6, -0.15, 0.6, 0.15, 0.65, 0.18)

@P.figure(SEM, "schottky", "Diodo Schottky", "Schottky diode")
def _(g): diode(g); g.line(0.65, -0.12, 0.65, -0.15, 0.6, -0.15, 0.6, 0.15, 0.55, 0.15, 0.55, 0.12)

@P.figure(SEM, "led", "LED", "LED")
def _(g): diode(g); g.line(0.6, -0.15, 0.6, 0.15); g.arrow(0.5, 0.2, 0.62, 0.32, 0.04); g.arrow(0.58, 0.16, 0.7, 0.28, 0.04)

@P.figure(SEM, "photodiode", "Fotodiodo", "Photodiode")
def _(g): diode(g); g.line(0.6, -0.15, 0.6, 0.15); g.arrow(0.62, 0.32, 0.5, 0.2, 0.04); g.arrow(0.7, 0.28, 0.58, 0.16, 0.04)

@P.figure(SEM, "npn", "Transistor NPN", "NPN transistor")
def _(g):
    g.circle(0.55, 0, 0.3); g.line(0, 0, 0.45, 0); g.line(0.45, -0.17, 0.45, 0.17)
    g.line(0.45, 0.08, 0.7, 0.25, 0.7, 0.5); g.arrow(0.45, -0.08, 0.7, -0.25, 0.05); g.line(0.7, -0.25, 0.7, -0.5)
    g.label(0.82, 0.38, "C", 0.6); g.label(0.82, -0.38, "E", 0.6); g.label(0.12, 0.08, "B", 0.6)

@P.figure(SEM, "pnp", "Transistor PNP", "PNP transistor")
def _(g):
    g.circle(0.55, 0, 0.3); g.line(0, 0, 0.45, 0); g.line(0.45, -0.17, 0.45, 0.17)
    g.line(0.45, 0.08, 0.7, 0.25, 0.7, 0.5); g.line(0.7, -0.25, 0.45, -0.08); g.head(0.7, -0.25, 0.47, -0.095, 0.05); g.line(0.7, -0.25, 0.7, -0.5)

@P.figure(SEM, "nmos", "MOSFET canal N", "N-channel MOSFET")
def _(g):
    g.line(0, 0, 0.4, 0); g.line(0.4, -0.2, 0.4, 0.2)
    for v in (0.15, 0, -0.15): g.line(0.46, v - 0.05, 0.46, v + 0.05)
    g.line(0.46, 0.15, 0.7, 0.15, 0.7, 0.5); g.line(0.46, -0.15, 0.7, -0.15, 0.7, -0.5); g.line(0.7, 0, 0.7, -0.15); g.arrow(0.7, 0, 0.47, 0, 0.04)
    g.label(0.8, 0.4, "D", 0.6); g.label(0.8, -0.4, "S", 0.6); g.label(0.15, 0.08, "G", 0.6)

@P.figure(SEM, "pmos", "MOSFET canal P", "P-channel MOSFET")
def _(g):
    g.line(0, 0, 0.4, 0); g.line(0.4, -0.2, 0.4, 0.2)
    for v in (0.15, 0, -0.15): g.line(0.46, v - 0.05, 0.46, v + 0.05)
    g.line(0.46, 0.15, 0.7, 0.15, 0.7, 0.5); g.line(0.46, -0.15, 0.7, -0.15, 0.7, -0.5); g.line(0.7, 0, 0.7, -0.15); g.arrow(0.48, 0, 0.7, 0, 0.04)

@P.figure(SEM, "opamp", "Amplificador operacional", "Operational amplifier")
def _(g):
    g.poly(0.25, 0.35, 0.25, -0.35, 0.8, 0); g.line(0, 0.18, 0.25, 0.18); g.line(0, -0.18, 0.25, -0.18); g.line(0.8, 0, 1, 0)
    g.label(0.31, 0.18, "−", 0.7); g.label(0.31, -0.18, "+", 0.7)

@P.figure(SEM, "comparator", "Comparador", "Comparator")
def _(g):
    g.poly(0.25, 0.35, 0.25, -0.35, 0.8, 0); g.line(0, 0.18, 0.25, 0.18); g.line(0, -0.18, 0.25, -0.18); g.line(0.8, 0, 1, 0)
    g.line(0.42, -0.06, 0.48, -0.06, 0.48, 0.06, 0.54, 0.06)

@P.figure(SEM, "thyristor", "Tiristor (SCR)", "Thyristor (SCR)")
def _(g): diode(g); g.line(0.6, -0.15, 0.6, 0.15); g.line(0.6, -0.08, 0.72, -0.25, 0.72, -0.4)

# --- Digital ----------------------------------------------------------------------------------------

def gate_inputs(g, x):
    g.line(0, 0.15, x, 0.15); g.line(0, -0.15, x, -0.15)

def and_body(g):
    g.line(0.5, 0.3, 0.25, 0.3, 0.25, -0.3, 0.5, -0.3); g.arc(0.5, 0, 0.3, 0.3, -90, 90)

def or_body(g):
    g.arc(0.08, 0, 0.25, 0.3, -90, 90); g.line(0.08, 0.3, 0.4, 0.3); g.line(0.08, -0.3, 0.4, -0.3)
    g.arc(0.4, -0.3, 0.42, 0.6, 90, 45); g.arc(0.4, 0.3, 0.42, 0.6, -90, -45)

@P.figure(DIG, "gate-and", "Compuerta AND", "AND gate")
def _(g): gate_inputs(g, 0.25); and_body(g); g.line(0.8, 0, 1, 0)

@P.figure(DIG, "gate-nand", "Compuerta NAND", "NAND gate")
def _(g): gate_inputs(g, 0.25); and_body(g); g.circle(0.84, 0, 0.04); g.line(0.88, 0, 1, 0)

@P.figure(DIG, "gate-or", "Compuerta OR", "OR gate")
def _(g): gate_inputs(g, 0.3); or_body(g); g.line(0.7, 0, 1, 0)

@P.figure(DIG, "gate-nor", "Compuerta NOR", "NOR gate")
def _(g): gate_inputs(g, 0.3); or_body(g); g.circle(0.74, 0, 0.04); g.line(0.78, 0, 1, 0)

@P.figure(DIG, "gate-xor", "Compuerta XOR", "XOR gate")
def _(g): gate_inputs(g, 0.27); or_body(g); g.arc(0.0, 0, 0.25, 0.3, -90, 90); g.line(0.7, 0, 1, 0)

@P.figure(DIG, "gate-not", "Compuerta NOT", "NOT gate")
def _(g): g.line(0, 0, 0.3, 0); g.poly(0.3, 0.25, 0.3, -0.25, 0.68, 0); g.circle(0.72, 0, 0.04); g.line(0.76, 0, 1, 0)

@P.figure(DIG, "buffer", "Buffer", "Buffer")
def _(g): g.line(0, 0, 0.3, 0); g.poly(0.3, 0.25, 0.3, -0.25, 0.7, 0); g.line(0.7, 0, 1, 0)

@P.figure(DIG, "flipflop-d", "Flip-flop D", "D flip-flop")
def _(g):
    g.rect(0.3, -0.35, 0.7, 0.35); g.line(0, 0.2, 0.3, 0.2); g.line(0, -0.2, 0.3, -0.2); g.line(0.7, 0.2, 1, 0.2); g.line(0.7, -0.2, 1, -0.2)
    g.line(0.3, -0.13, 0.36, -0.2, 0.3, -0.27); g.label(0.38, 0.2, "D", 0.6); g.label(0.63, 0.2, "Q", 0.6); g.label(0.63, -0.2, "Q̄", 0.6)

@P.figure(DIG, "mux", "Multiplexor", "Multiplexer")
def _(g):
    g.poly(0.35, 0.4, 0.65, 0.25, 0.65, -0.25, 0.35, -0.4)
    for v in (0.25, 0.08, -0.08, -0.25): g.line(0, v, 0.35, v)
    g.line(0.65, 0, 1, 0); g.line(0.5, -0.33, 0.5, -0.5); g.label(0.5, 0, "MUX", 0.5)

@P.figure(DIG, "ic", "Circuito integrado", "Integrated circuit")
def _(g):
    g.rect(0.25, -0.3, 0.75, 0.3); g.arc(0.25, 0, 0.05, 0.06, -90, 90)
    for k in range(4): v = 0.22 - k * 0.147; g.line(0.1, v, 0.25, v); g.line(0.75, v, 0.9, v)

@P.figure(DIG, "clock", "Señal de reloj", "Clock signal")
def _(g):
    pts = []; x = 0.0; hi = False
    while x < 0.99:
        y = 0.15 if hi else -0.15; pts += [x, y, min(1, x + 0.125), y]; x += 0.125; hi = not hi
    g.line(*pts)

# --- Instrumentos y otros -----------------------------------------------------------------------------

def meter(g, letter):
    leads(g); g.circle(0.5, 0, 0.2); g.label(0.5, 0, letter, 0.9)

@P.figure(INS, "ammeter", "Amperímetro", "Ammeter")
def _(g): meter(g, "A")

@P.figure(INS, "voltmeter", "Voltímetro", "Voltmeter")
def _(g): meter(g, "V")

@P.figure(INS, "ohmmeter", "Óhmetro", "Ohmmeter")
def _(g): meter(g, "Ω")

@P.figure(INS, "wattmeter", "Wattímetro", "Wattmeter")
def _(g): meter(g, "W")

@P.figure(INS, "galvanometer", "Galvanómetro", "Galvanometer")
def _(g): leads(g); g.circle(0.5, 0, 0.2); g.arrow(0.4, -0.12, 0.6, 0.12, 0.04)

@P.figure(INS, "oscilloscope", "Osciloscopio", "Oscilloscope")
def _(g):
    g.rect(0.15, -0.3, 0.85, 0.3); g.rect(0.2, -0.25, 0.65, 0.25)
    g.curve(lambda u: 0.15 * math.sin((u - 0.2) / 0.45 * 4 * math.pi), 0.2, 0.65, 48)
    for v in (0.15, 0, -0.15): g.circle(0.75, v, 0.03)

@P.figure(INS, "lamp", "Foco", "Lamp")
def _(g): leads(g); g.circle(0.5, 0, 0.2); g.line(0.36, 0.14, 0.64, -0.14); g.line(0.36, -0.14, 0.64, 0.14)

@P.figure(INS, "motor", "Motor", "Motor")
def _(g): meter(g, "M")

@P.figure(INS, "generator", "Generador", "Generator")
def _(g): meter(g, "G")

@P.figure(INS, "speaker", "Bocina", "Speaker")
def _(g): g.line(0, 0.08, 0.3, 0.08); g.line(0, -0.08, 0.3, -0.08); g.rect(0.3, -0.12, 0.42, 0.12); g.poly(0.42, 0.12, 0.62, 0.3, 0.62, -0.3, 0.42, -0.12)

@P.figure(INS, "microphone", "Micrófono", "Microphone")
def _(g): g.circle(0.6, 0, 0.18); g.line(0.42, -0.18, 0.42, 0.18); g.line(0, 0, 0.42, 0)

@P.figure(INS, "antenna", "Antena", "Antenna")
def _(g): g.line(0.5, -0.4, 0.5, 0.3); g.line(0.3, 0.45, 0.5, 0.3, 0.7, 0.45); g.line(0.5, 0.3, 0.5, 0.45)

@P.figure(INS, "buzzer", "Zumbador", "Buzzer")
def _(g): g.line(0, 0.1, 0.35, 0.1); g.line(0, -0.1, 0.35, -0.1); g.arc(0.55, -0.15, 0.22, 0.35, 0, 180); g.line(0.33, -0.15, 0.77, -0.15)

# --- Fórmulas -------------------------------------------------------------------------------------------

G = "Ingenierías"
P.formulas_in(G, "Circuitos eléctricos", [
    ("Ley de Ohm", r"V = I R", "Ohm's law"),
    ("Potencia eléctrica", r"P = V I = I^{2} R = \frac{V^{2}}{R}", "Electric power"),
    ("Resistencias en serie", r"R_{eq} = R_{1} + R_{2} + \cdots + R_{n}", "Resistors in series"),
    ("Resistencias en paralelo", r"\frac{1}{R_{eq}} = \frac{1}{R_{1}} + \frac{1}{R_{2}} + \cdots", "Resistors in parallel"),
    ("Dos en paralelo", r"R_{eq} = \frac{R_{1} R_{2}}{R_{1} + R_{2}}", "Two in parallel"),
    ("Divisor de voltaje", r"V_{out} = V_{in} \frac{R_{2}}{R_{1} + R_{2}}", "Voltage divider"),
    ("Divisor de corriente", r"I_{1} = I \frac{R_{2}}{R_{1} + R_{2}}", "Current divider"),
    ("Kirchhoff (corrientes)", r"\sum_{k} I_{k} = 0", "Kirchhoff (currents)"),
    ("Kirchhoff (voltajes)", r"\sum_{k} V_{k} = 0", "Kirchhoff (voltages)"),
    ("Resistividad", r"R = \rho \frac{L}{A}", "Resistivity"),
    ("Thévenin", r"R_{th} = \frac{V_{oc}}{I_{sc}}", "Thévenin"),
    ("Máxima transferencia", r"P_{max} = \frac{V_{th}^{2}}{4 R_{th}}", "Maximum power transfer"),
    ("Capacitores en serie", r"\frac{1}{C_{eq}} = \sum \frac{1}{C_{i}}", "Capacitors in series"),
    ("Capacitores en paralelo", r"C_{eq} = \sum C_{i}", "Capacitors in parallel"),
], "Electric circuits")
P.formulas_in(G, "Circuitos transitorios y AC", [
    ("Carga RC", r"v(t) = V_{0} \left( 1 - e^{-t/RC} \right)", "RC charging"),
    ("Descarga RC", r"v(t) = V_{0} e^{-t/RC}", "RC discharge"),
    ("Constante de tiempo", r"\tau = R C, \quad \tau = \frac{L}{R}", "Time constant"),
    ("Corriente en inductor", r"v = L \frac{di}{dt}", "Inductor current"),
    ("Corriente en capacitor", r"i = C \frac{dv}{dt}", "Capacitor current"),
    ("Reactancia capacitiva", r"X_{C} = \frac{1}{2 \pi f C}", "Capacitive reactance"),
    ("Reactancia inductiva", r"X_{L} = 2 \pi f L", "Inductive reactance"),
    ("Impedancia", r"Z = R + j \left( \omega L - \frac{1}{\omega C} \right)", "Impedance"),
    ("Magnitud de impedancia", r"|Z| = \sqrt{R^{2} + (X_{L} - X_{C})^{2}}", "Impedance magnitude"),
    ("Frecuencia de resonancia", r"f_{0} = \frac{1}{2 \pi \sqrt{L C}}", "Resonant frequency"),
    ("Valor eficaz", r"V_{rms} = \frac{V_{p}}{\sqrt{2}}", "RMS value"),
    ("Potencia activa", r"P = V_{rms} I_{rms} \cos\varphi", "Active power"),
    ("Potencia aparente", r"S = V_{rms} I_{rms}, \quad S^{2} = P^{2} + Q^{2}", "Apparent power"),
    ("Factor de potencia", r"FP = \cos\varphi = \frac{P}{S}", "Power factor"),
    ("Potencia trifásica", r"P = \sqrt{3} V_{L} I_{L} \cos\varphi", "Three-phase power"),
    ("Fasor", r"v(t) = V_{m} \cos(\omega t + \theta) \leftrightarrow V_{m} \angle \theta", "Phasor"),
], "Transient and AC circuits")
P.formulas_in(G, "Electrónica analógica", [
    ("Amplificador inversor", r"V_{out} = -\frac{R_{f}}{R_{in}} V_{in}", "Inverting amplifier"),
    ("Amplificador no inversor", r"V_{out} = \left( 1 + \frac{R_{f}}{R_{1}} \right) V_{in}", "Non-inverting amplifier"),
    ("Sumador", r"V_{out} = -R_{f} \left( \frac{V_{1}}{R_{1}} + \frac{V_{2}}{R_{2}} \right)", "Summing amplifier"),
    ("Integrador", r"V_{out} = -\frac{1}{RC} \int V_{in} \, dt", "Integrator"),
    ("Derivador", r"V_{out} = -R C \frac{dV_{in}}{dt}", "Differentiator"),
    ("Diodo (Shockley)", r"I = I_{S} \left( e^{V_{D}/(n V_{T})} - 1 \right)", "Diode (Shockley)"),
    ("Voltaje térmico", r"V_{T} = \frac{k T}{q} \approx 25.9 \text{ mV}", "Thermal voltage"),
    ("Transistor BJT", r"I_{C} = \beta I_{B}, \quad I_{E} = I_{C} + I_{B}", "BJT transistor"),
    ("MOSFET en saturación", r"I_{D} = \frac{k}{2} (V_{GS} - V_{th})^{2}", "MOSFET in saturation"),
    ("Ganancia en decibeles", r"G_{dB} = 20 \log_{10} \frac{V_{out}}{V_{in}}", "Gain in decibels"),
    ("Filtro RC (corte)", r"f_{c} = \frac{1}{2 \pi R C}", "RC filter (cutoff)"),
    ("Rizo de un rectificador", r"V_{r} \approx \frac{I_{L}}{f C}", "Rectifier ripple"),
], "Analog electronics")
P.formulas_in(G, "Electrónica digital", [
    ("De Morgan (1)", r"\overline{A \cdot B} = \overline{A} + \overline{B}", "De Morgan (1)"),
    ("De Morgan (2)", r"\overline{A + B} = \overline{A} \cdot \overline{B}", "De Morgan (2)"),
    ("XOR", r"A \oplus B = A \overline{B} + \overline{A} B", "XOR"),
    ("Absorción", r"A + A B = A", "Absorption"),
    ("Binario a decimal", r"N = \sum_{i=0}^{n-1} b_{i} \, 2^{i}", "Binary to decimal"),
    ("Complemento a dos", r"-N = \overline{N} + 1", "Two's complement"),
    ("Resolución de un ADC", r"\Delta V = \frac{V_{ref}}{2^{n}}", "ADC resolution"),
    ("Frecuencia de reloj", r"f = \frac{1}{T}", "Clock frequency"),
    ("Ciclo de trabajo", r"D = \frac{t_{on}}{T} \times 100\%", "Duty cycle"),
    ("Timer 555 (astable)", r"f = \frac{1.44}{(R_{1} + 2 R_{2}) C}", "555 timer (astable)"),
], "Digital electronics")

P.labels = [["Vcc", "#dc2626"], ["GND", "#334155"], ["Entrada", "#2563eb"], ["Salida", "#16a34a"],
            ["Alto (1)", "#ea580c"], ["Bajo (0)", "#0891b2"], ["Medición", "#7c3aed"], ["¡Polaridad!", "#ca8a04"]]
P.en.update({"Entrada": "Input", "Salida": "Output", "Alto (1)": "High (1)", "Bajo (0)": "Low (0)", "Medición": "Measurement", "¡Polaridad!": "Polarity!"})
P.emoji = {"Electrónica": "⚡ 🔌 🔋 💡 🔦 📟 🖥️ 💻 📡 🎛️ 🧲 ⚙️ 🔊 📶"}
