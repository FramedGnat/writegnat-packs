import math
from wgpack import Pack

pack = Pack("musica", "Música", "Notación (claves, notas, silencios, compases), instrumentos, tablaturas, teoría y acústica con plantillas de pentagrama y fórmulas.",
            "Licenciaturas", "🎼", en={"Música": "Music",
            "Notación (claves, notas, silencios, compases), instrumentos, tablaturas, teoría y acústica con plantillas de pentagrama y fórmulas.":
            "Notation (clefs, notes, rests, time signatures), instruments, tablature, theory and acoustics with staff templates and formulas."})
P = pack
NOT, INS, TEO = "Música: notación", "Música: instrumentos", "Música: teoría y gráficos"
P.en.update({NOT: "Music: notation", INS: "Music: instruments", TEO: "Music: theory and charts"})

SP = 0.05    # separación entre líneas del pentagrama (en unidades del arrastre)

def staff(g, u0=0.0, u1=1.0, v0=0.0, sp=SP):
    for k in range(5): g.line(u0, v0 + k * sp, u1, v0 + k * sp)

def head(g, u, v, filled=True, whole=False, r=SP * 0.56, k=1.0):
    """Cabeza de nota: elipse inclinada (la redonda va hueca y más ancha)."""
    r *= k
    ru = r * (1.25 if whole else 1.05); rv = r * (0.8 if whole else 0.72); rot = math.radians(20 if not whole else 0)
    pts = []
    for i in range(25):
        t = 2 * math.pi * i / 24; x, y = ru * math.cos(t), rv * math.sin(t)
        pts.append((u + x * math.cos(rot) - y * math.sin(rot), v + x * math.sin(rot) + y * math.cos(rot)))
    g._add(pts, fill=filled)
    if whole: g.ellipse(u, v, ru * 0.45, rv * 0.9)

def stem(g, u, v, up=True, ln=SP * 3.4, r=SP * 0.56, k=1.0):
    ln *= k; r *= k
    x = u + (r * 1.0 if up else -r * 1.0)
    g.line(x, v, x, v + (ln if up else -ln))
    return x, v + (ln if up else -ln)

def flag(g, x, y, up=True, n=1, kk=1.0):
    for k in range(n):
        d = -SP * 0.9 * k * kk if up else SP * 0.9 * k * kk
        s = 1 if up else -1
        g.spline([(x, y + d), (x + SP * 0.9 * kk, y + d - s * SP * 0.8 * kk), (x + SP * 0.9 * kk, y + d - s * SP * 1.8 * kk)], 6)

# --- Notación ------------------------------------------------------------------------------

@P.figure(NOT, "staff", "Pentagrama", "Staff")
def _(g): staff(g, 0, 1, 0)

@P.figure(NOT, "grand-staff", "Pentagrama doble (piano)", "Grand staff (piano)")
def _(g):
    staff(g, 0.06, 1, 0.3); staff(g, 0.06, 1, 0)
    g.line(0.06, 0, 0.06, 0.5); g.line(1, 0, 1, 0.5)
    g.spline([(0.04, 0.5), (0.02, 0.45), (0.02, 0.3), (0.0, 0.25), (0.02, 0.2), (0.02, 0.05), (0.04, 0.0)], 8)

@P.figure(NOT, "treble-clef", "Clave de sol", "Treble clef")
def _(g):
    g.spline([(0.45, -0.075), (0.49, -0.095), (0.525, -0.075), (0.52, -0.03), (0.5, 0.04), (0.47, 0.12), (0.46, 0.2), (0.47, 0.26), (0.5, 0.3), (0.525, 0.27),
              (0.52, 0.22), (0.5, 0.15), (0.47, 0.08), (0.455, 0.03), (0.47, -0.01), (0.51, -0.015), (0.54, 0.02), (0.535, 0.06), (0.5, 0.075), (0.475, 0.05)], 8)
    g.circle(0.45, -0.075, 0.008, fill=True)

@P.figure(NOT, "bass-clef", "Clave de fa", "Bass clef")
def _(g):
    g.spline([(0.455, 0.15), (0.475, 0.19), (0.52, 0.2), (0.56, 0.17), (0.57, 0.12), (0.53, 0.05), (0.47, 0.0), (0.43, -0.03)], 8)
    g.circle(0.455, 0.15, 0.011, fill=True); g.circle(0.62, 0.17, 0.008, fill=True); g.circle(0.62, 0.12, 0.008, fill=True)

@P.figure(NOT, "note-whole", "Redonda", "Whole note")
def _(g): head(g, 0.5, 0.1, False, True, k=2.4)

@P.figure(NOT, "note-half", "Blanca", "Half note")
def _(g): head(g, 0.5, 0.0, False, k=2.4); stem(g, 0.5, 0.0, True, k=2.4)

@P.figure(NOT, "note-quarter", "Negra", "Quarter note")
def _(g): head(g, 0.5, 0.0, True, k=2.4); stem(g, 0.5, 0.0, True, k=2.4)

@P.figure(NOT, "note-eighth", "Corchea", "Eighth note")
def _(g): head(g, 0.5, 0.0, k=2.4); x, y = stem(g, 0.5, 0.0, k=2.4); flag(g, x, y, True, 1, 2.4)

@P.figure(NOT, "note-sixteenth", "Semicorchea", "Sixteenth note")
def _(g): head(g, 0.5, 0.0, k=2.4); x, y = stem(g, 0.5, 0.0, k=2.4); flag(g, x, y, True, 2, 2.4)

@P.figure(NOT, "beamed-eighths", "Corcheas ligadas", "Beamed eighth notes")
def _(g):
    head(g, 0.35, 0.0); head(g, 0.65, 0.04)
    x1, y1 = stem(g, 0.35, 0.0, ln=SP * 3.6); x2, y2 = stem(g, 0.65, 0.04, ln=SP * 3.6)
    g.poly(x1, y1, x2, y2, x2, y2 - SP * 0.45, x1, y1 - SP * 0.45, fill=True)

@P.figure(NOT, "beamed-sixteenths", "Cuatro semicorcheas ligadas", "Four beamed sixteenths")
def _(g):
    us = [0.2, 0.4, 0.6, 0.8]
    for u in us: head(g, u, 0.0); stem(g, u, 0.0, ln=SP * 3.5)
    x1 = us[0] + SP * 0.56; x2 = us[-1] + SP * 0.56; y = SP * 3.5
    for k in range(2): g.poly(x1, y - k * SP * 0.8, x2, y - k * SP * 0.8, x2, y - k * SP * 0.8 - SP * 0.4, x1, y - k * SP * 0.8 - SP * 0.4, fill=True)

@P.figure(NOT, "dotted-note", "Negra con puntillo", "Dotted quarter note")
def _(g): head(g, 0.5, 0.0, k=2.4); stem(g, 0.5, 0.0, k=2.4); g.circle(0.5 + SP * 1.4 * 2.4, 0.0, 0.012, fill=True)

@P.figure(NOT, "rest-whole", "Silencio de redonda", "Whole rest")
def _(g): staff(g, 0.25, 0.75, 0); g.rect(0.45, SP * 3 - SP * 0.5, 0.55, SP * 3, fill=True)

@P.figure(NOT, "rest-half", "Silencio de blanca", "Half rest")
def _(g): staff(g, 0.25, 0.75, 0); g.rect(0.45, SP * 2, 0.55, SP * 2 + SP * 0.5, fill=True)

@P.figure(NOT, "rest-quarter", "Silencio de negra", "Quarter rest")
def _(g): g.spline([(0.5, 0.17), (0.54, 0.13), (0.49, 0.1), (0.54, 0.06), (0.49, 0.03), (0.53, 0.0), (0.5, -0.02)], 8)

@P.figure(NOT, "rest-eighth", "Silencio de corchea", "Eighth rest")
def _(g): g.circle(0.47, 0.11, 0.012, fill=True); g.spline([(0.485, 0.105), (0.53, 0.115), (0.5, 0.03), (0.47, -0.04)], 8)

@P.figure(NOT, "sharp", "Sostenido", "Sharp")
def _(g):
    for u in (0.47, 0.53): g.line(u, -0.045, u, 0.125)
    for v in (0.0, 0.05): g.poly(0.43, v + 0.0, 0.57, v + 0.02, 0.57, v + 0.045, 0.43, v + 0.025, fill=True)

@P.figure(NOT, "flat", "Bemol", "Flat")
def _(g): g.line(0.47, -0.02, 0.47, 0.17); g.spline([(0.47, 0.02), (0.53, 0.05), (0.54, 0.08), (0.5, 0.1), (0.47, 0.075)], 8)

@P.figure(NOT, "natural", "Becuadro", "Natural")
def _(g):
    g.line(0.48, 0.06, 0.48, 0.18); g.line(0.52, -0.05, 0.52, 0.07)
    g.poly(0.48, 0.07, 0.52, 0.055, 0.52, 0.015, 0.48, 0.03); g.poly(0.48, 0.1, 0.52, 0.085, 0.52, 0.06, 0.48, 0.075)

@P.figure(NOT, "barline", "Línea divisoria", "Barline")
def _(g): staff(g, 0, 1, 0); g.line(0.5, 0, 0.5, 4 * SP)

@P.figure(NOT, "double-bar", "Doble barra", "Double barline")
def _(g): staff(g, 0.2, 0.8, 0); g.line(0.7, 0, 0.7, 4 * SP); g.line(0.75, 0, 0.75, 4 * SP)

@P.figure(NOT, "final-bar", "Barra final", "Final barline")
def _(g): staff(g, 0.2, 0.8, 0); g.line(0.7, 0, 0.7, 4 * SP); g.poly(0.74, 0, 0.78, 0, 0.78, 4 * SP, 0.74, 4 * SP, fill=True)

@P.figure(NOT, "repeat-start", "Inicio de repetición", "Repeat start")
def _(g):
    staff(g, 0.2, 0.8, 0); g.poly(0.3, 0, 0.34, 0, 0.34, 4 * SP, 0.3, 4 * SP, fill=True); g.line(0.37, 0, 0.37, 4 * SP)
    g.circle(0.42, SP * 1.5, 0.007, fill=True); g.circle(0.42, SP * 2.5, 0.007, fill=True)

@P.figure(NOT, "repeat-end", "Fin de repetición", "Repeat end")
def _(g):
    staff(g, 0.2, 0.8, 0); g.line(0.63, 0, 0.63, 4 * SP); g.poly(0.66, 0, 0.7, 0, 0.7, 4 * SP, 0.66, 4 * SP, fill=True)
    g.circle(0.58, SP * 1.5, 0.007, fill=True); g.circle(0.58, SP * 2.5, 0.007, fill=True)

@P.figure(NOT, "time-44", "Compás 4/4", "Time 4/4")
def _(g): staff(g, 0.2, 0.8, 0); g.label(0.4, SP * 3, "4", 1.3); g.label(0.4, SP, "4", 1.3)

@P.figure(NOT, "time-34", "Compás 3/4", "Time 3/4")
def _(g): staff(g, 0.2, 0.8, 0); g.label(0.4, SP * 3, "3", 1.3); g.label(0.4, SP, "4", 1.3)

@P.figure(NOT, "time-68", "Compás 6/8", "Time 6/8")
def _(g): staff(g, 0.2, 0.8, 0); g.label(0.4, SP * 3, "6", 1.3); g.label(0.4, SP, "8", 1.3)

@P.figure(NOT, "common-time", "Compás común (C)", "Common time (C)")
def _(g): staff(g, 0.2, 0.8, 0); g.arc(0.45, SP * 2, SP * 1.1, SP * 1.3, 55, 305)

@P.figure(NOT, "crescendo", "Crescendo", "Crescendo")
def _(g): g.line(1, 0.045, 0, 0.0); g.line(1, -0.045, 0, 0.0)

@P.figure(NOT, "decrescendo", "Decrescendo", "Decrescendo")
def _(g): g.line(0, 0.045, 1, 0.0); g.line(0, -0.045, 1, 0.0)

@P.figure(NOT, "dynamics", "Dinámicas (pp p mf f ff)", "Dynamics (pp p mf f ff)")
def _(g):
    for k, t in enumerate(("pp", "p", "mp", "mf", "f", "ff")): g.label(0.08 + k * 0.17, 0.0, t, 1.6)

@P.figure(NOT, "fermata", "Calderón", "Fermata")
def _(g): g.arc(0.5, 0.0, 0.07, 0.07, 0, 180); g.circle(0.5, 0.012, 0.008, fill=True)

@P.figure(NOT, "slur", "Ligadura", "Slur")
def _(g): g.spline([(0.1, 0.0), (0.3, 0.05), (0.7, 0.05), (0.9, 0.0)], 12); g.spline([(0.1, 0.0), (0.3, 0.035), (0.7, 0.035), (0.9, 0.0)], 12)

@P.figure(NOT, "staccato", "Staccato y acento", "Staccato and accent")
def _(g): g.circle(0.3, 0.0, 0.01, fill=True); g.line(0.6, 0.03, 0.7, 0.0, 0.6, -0.03)

@P.figure(NOT, "triplet", "Tresillo", "Triplet")
def _(g): g.line(0.1, 0.0, 0.1, 0.03, 0.4, 0.03); g.line(0.6, 0.03, 0.9, 0.03, 0.9, 0.0); g.label(0.5, 0.03, "3", 1.0)

@P.figure(NOT, "tempo-mark", "Indicación de tempo (♩ = 120)", "Tempo mark (♩ = 120)")
def _(g): head(g, 0.2, 0.0); stem(g, 0.2, 0.0); g.label(0.55, 0.0, "= 120", 1.2)

@P.figure(NOT, "chord-triad", "Acorde (tríada)", "Chord (triad)")
def _(g):
    staff(g, 0.2, 0.8, 0)
    for k in range(3): head(g, 0.5, k * SP * 2)
    stem(g, 0.5, SP * 4, False, SP * 3.4)

@P.figure(NOT, "ledger-notes", "Notas con líneas adicionales", "Notes with ledger lines")
def _(g):
    staff(g, 0.1, 0.9, 0)
    head(g, 0.3, -SP); g.line(0.3 - SP * 0.9, -SP * 0.0 - SP * 0.0, 0.3 + SP * 0.9, 0.0)
    head(g, 0.5, SP * 2.5); head(g, 0.7, SP * 5.5); g.line(0.7 - SP * 0.9, SP * 5, 0.7 + SP * 0.9, SP * 5)

# --- Instrumentos ---------------------------------------------------------------------------

@P.figure(INS, "piano-octave", "Teclado (una octava)", "Keyboard (one octave)")
def _(g):
    w = 1 / 7; h = 0.35
    for k in range(7): g.rect(k * w, 0, (k + 1) * w, h)
    for k in (0, 1, 3, 4, 5): g.rect((k + 1) * w - w * 0.3, h * 0.38, (k + 1) * w + w * 0.3, h, fill=True)
    for k, t in enumerate("CDEFGAB"): g.label((k + 0.5) * w, -0.03, t, 0.7)

@P.figure(INS, "piano-keyboard", "Teclado (dos octavas)", "Keyboard (two octaves)")
def _(g):
    w = 1 / 14; h = 0.3
    for k in range(14): g.rect(k * w, 0, (k + 1) * w, h)
    for k in (0, 1, 3, 4, 5, 7, 8, 10, 11, 12): g.rect((k + 1) * w - w * 0.3, h * 0.38, (k + 1) * w + w * 0.3, h, fill=True)

@P.figure(INS, "guitar-chord-box", "Diagrama de acorde de guitarra", "Guitar chord diagram")
def _(g):
    for k in range(6): g.line(0.2 + k * 0.12, 0.0, 0.2 + k * 0.12, 0.5)
    for k in range(6): g.line(0.2, k * 0.1, 0.8, k * 0.1)
    g.line(0.2, 0.5, 0.8, 0.5, 0.8, 0.5); g.line(0.2, 0.505, 0.8, 0.505)
    g.circle(0.44, 0.35, 0.02, fill=True); g.circle(0.56, 0.25, 0.02, fill=True); g.circle(0.68, 0.15, 0.02, fill=True)
    g.label(0.2, 0.56, "X", 0.6); g.label(0.32, 0.56, "O", 0.6)

@P.figure(INS, "ukulele-chord-box", "Diagrama de acorde de ukulele", "Ukulele chord diagram")
def _(g):
    for k in range(4): g.line(0.3 + k * 0.13, 0.0, 0.3 + k * 0.13, 0.5)
    for k in range(6): g.line(0.3, k * 0.1, 0.69, k * 0.1)
    g.line(0.3, 0.505, 0.69, 0.505); g.circle(0.43, 0.35, 0.02, fill=True); g.circle(0.56, 0.25, 0.02, fill=True)

@P.figure(INS, "guitar-tab", "Tablatura de guitarra", "Guitar tab")
def _(g):
    for k in range(6): g.line(0.1, k * 0.04, 1, k * 0.04)
    g.label(0.03, 0.1, "T", 0.9); g.label(0.03, 0.06, "A", 0.9); g.label(0.03, 0.02, "B", 0.9)
    g.label(0.3, 0.12, "0", 0.7); g.label(0.5, 0.04, "2", 0.7); g.label(0.7, 0.16, "3", 0.7)

@P.figure(INS, "fretboard", "Mástil de guitarra", "Guitar fretboard")
def _(g):
    for k in range(6): g.line(0.0, k * 0.04, 1.0, k * 0.04)
    for k in range(13): g.line(k / 12, 0.0, k / 12, 0.2, )
    g.line(0.0, 0.0, 0.0, 0.2); g.line(0.005, 0.0, 0.005, 0.2)
    for k in (3, 5, 7, 9): g.circle((k - 0.5) / 12, 0.1, 0.008, fill=True)

@P.figure(INS, "guitar", "Guitarra", "Guitar")
def _(g):
    g.rect(0.0, -0.015, 0.45, 0.015); g.rect(0.45, -0.03, 0.55, 0.03)
    g.spline([(0.5, 0.03), (0.6, 0.12), (0.72, 0.08), (0.78, 0.12), (0.95, 0.12), (1.0, 0.0), (0.95, -0.12), (0.78, -0.12), (0.72, -0.08), (0.6, -0.12), (0.5, -0.03)], 8)
    g.circle(0.78, 0.0, 0.05)

@P.figure(INS, "drum-kit", "Batería", "Drum kit")
def _(g):
    g.circle(0.5, 0.0, 0.2); g.circle(0.5, 0.0, 0.15)
    g.ellipse(0.25, 0.22, 0.12, 0.05); g.ellipse(0.75, 0.22, 0.12, 0.05); g.ellipse(0.12, 0.05, 0.1, 0.04)
    g.line(0.12, 0.05, 0.12, -0.2); g.ellipse(0.88, 0.1, 0.1, 0.04); g.line(0.88, 0.1, 0.88, -0.2); g.ellipse(0.5, 0.42, 0.09, 0.03)

@P.figure(INS, "metronome", "Metrónomo", "Metronome")
def _(g):
    g.poly(0.3, 0.0, 0.7, 0.0, 0.58, 0.55, 0.42, 0.55); g.line(0.5, 0.08, 0.58, 0.5); g.circle(0.55, 0.38, 0.03, fill=True)
    g.line(0.34, 0.15, 0.66, 0.15)

@P.figure(INS, "tuning-fork", "Diapasón", "Tuning fork")
def _(g): g.line(0.42, 0.4, 0.42, 0.08); g.line(0.58, 0.4, 0.58, 0.08); g.arc(0.5, 0.08, 0.08, 0.08, 180, 360); g.line(0.5, 0.0, 0.5, -0.2)

@P.figure(INS, "microphone", "Micrófono", "Microphone")
def _(g): g.circle(0.5, 0.18, 0.1); g.rect(0.46, -0.1, 0.54, 0.08); g.line(0.4, 0.22, 0.6, 0.22, dashed=True); g.line(0.5, -0.1, 0.5, -0.25)

@P.figure(INS, "headphones", "Audífonos", "Headphones")
def _(g): g.arc(0.5, 0.0, 0.3, 0.28, 0, 180); g.rect(0.16, -0.1, 0.26, 0.05, fill=True); g.rect(0.74, -0.1, 0.84, 0.05, fill=True)

@P.figure(INS, "speaker", "Bocina", "Speaker")
def _(g): g.rect(0.3, -0.3, 0.7, 0.3); g.circle(0.5, 0.1, 0.15); g.circle(0.5, 0.1, 0.05); g.circle(0.5, -0.17, 0.07)

@P.figure(INS, "violin", "Violín", "Violin")
def _(g):
    g.spline([(0.5, 0.0), (0.6, 0.04), (0.62, 0.1), (0.57, 0.14), (0.6, 0.2), (0.7, 0.25), (0.7, 0.33), (0.5, 0.37), (0.3, 0.33), (0.3, 0.25), (0.4, 0.2),
              (0.43, 0.14), (0.38, 0.1), (0.4, 0.04)], 8, closed=True)
    g.line(0.5, 0.37, 0.5, 0.6); g.rect(0.47, 0.6, 0.53, 0.7); g.line(0.45, 0.2, 0.55, 0.2)

@P.figure(INS, "trumpet", "Trompeta", "Trumpet")
def _(g):
    g.line(0.05, 0.03, 0.7, 0.03); g.line(0.05, -0.03, 0.7, -0.03); g.line(0.7, 0.03, 0.95, 0.12); g.line(0.7, -0.03, 0.95, -0.12); g.line(0.95, 0.12, 0.95, -0.12)
    for u in (0.3, 0.4, 0.5): g.line(u, 0.03, u, 0.12); g.circle(u, 0.13, 0.012)

# --- Teoría y gráficos -------------------------------------------------------------------------

@P.figure(TEO, "circle-fifths", "Círculo de quintas", "Circle of fifths")
def _(g):
    g.circle(0.5, 0.0, 0.46); g.circle(0.5, 0.0, 0.32); g.circle(0.5, 0.0, 0.17)
    maj = ["C", "G", "D", "A", "E", "B", "F♯", "D♭", "A♭", "E♭", "B♭", "F"]; mi = ["Am", "Em", "Bm", "F♯m", "C♯m", "G♯m", "E♭m", "B♭m", "Fm", "Cm", "Gm", "Dm"]
    for k in range(12):
        a = math.radians(90 - 30 * k)
        g.label(0.5 + 0.39 * math.cos(a), 0.39 * math.sin(a), maj[k], 0.9); g.label(0.5 + 0.245 * math.cos(a), 0.245 * math.sin(a), mi[k], 0.6)
        b = math.radians(90 - 30 * k + 15); g.line(0.5 + 0.32 * math.cos(b), 0.32 * math.sin(b), 0.5 + 0.46 * math.cos(b), 0.46 * math.sin(b))

@P.figure(TEO, "major-scale-steps", "Escala mayor (tonos y semitonos)", "Major scale (whole and half steps)")
def _(g):
    steps = ["T", "T", "S", "T", "T", "T", "S"]
    for k in range(8): g.circle(0.06 + k * 0.125, 0.0, 0.03, fill=(k in (0, 7))); g.label(0.06 + k * 0.125, -0.07, str(k + 1), 0.6)
    for k, t in enumerate(steps): g.arc(0.1225 + k * 0.125, 0.0, 0.0625, 0.07, 0, 180); g.label(0.1225 + k * 0.125, 0.1, t, 0.8)

@P.figure(TEO, "note-values", "Valores de las figuras", "Note values")
def _(g):
    for r, (n, c) in enumerate((("1", 1), ("1/2", 2), ("1/4", 4), ("1/8", 8))):
        v = 0.3 - r * 0.1; g.label(0.04, v, n, 0.7)
        for k in range(c): g.rect(0.1 + k * 0.9 / c, v - 0.03, 0.1 + (k + 1) * 0.9 / c - 0.005, v + 0.03)

@P.figure(TEO, "waveforms", "Formas de onda", "Waveforms")
def _(g):
    g.curve(lambda u: 0.06 * math.sin(u * 4 * math.pi), 0, 1, 60); g.label(1.07, 0.0, "seno", 0.6)
    sq = []
    for k in range(4): y = -0.2 + (0.05 if k % 2 == 0 else -0.05); sq += [k / 4, y, (k + 1) / 4, y]
    g.line(*sq); g.label(1.07, -0.2, "cuadrada", 0.6)
    g.line(*[x for k in range(5) for x in (k / 4, -0.4 + (0.05 if k % 2 == 0 else -0.05))]); g.label(1.07, -0.4, "triangular", 0.6)

@P.figure(TEO, "adsr", "Envolvente ADSR", "ADSR envelope")
def _(g):
    g.arrow(0, 0, 1, 0, 0.03); g.arrow(0, 0, 0, 0.45, 0.03)
    g.line(0, 0, 0.2, 0.4, 0.35, 0.25, 0.7, 0.25, 0.95, 0)
    for u, t in ((0.1, "A"), (0.28, "D"), (0.52, "S"), (0.83, "R")): g.label(u, -0.06, t, 0.7)

@P.figure(TEO, "harmonics", "Armónicos de una cuerda", "String harmonics")
def _(g):
    for n in range(1, 5):
        v = 0.45 - (n - 1) * 0.15
        g.curve(lambda u, n=n, v=v: v + 0.05 * math.sin(n * math.pi * u), 0, 1, 40); g.circle(0, v, 0.012, fill=True); g.circle(1, v, 0.012, fill=True)
        g.label(1.06, v, f"{n}f", 0.6)

@P.figure(TEO, "sound-wave", "Onda sonora (compresiones)", "Sound wave (compressions)")
def _(g):
    for k in range(12): u = 0.1 + k * 0.07 + 0.02 * math.sin(k * 0.8); g.line(u, -0.1, u, 0.1)
    g.arrow(0.0, 0.2, 0.3, 0.2, 0.03); g.label(0.5, 0.25, "λ", 0.8)

@P.figure(TEO, "pitch-lines", "Altura: grave y agudo", "Pitch: low and high")
def _(g):
    g.curve(lambda u: 0.06 * math.sin(u * 2 * math.pi), 0, 1, 40); g.curve(lambda u: -0.2 + 0.06 * math.sin(u * 8 * math.pi), 0, 1, 80)
    g.label(1.1, 0.0, "grave", 0.6); g.label(1.1, -0.2, "agudo", 0.6)

# --- Fórmulas -------------------------------------------------------------------------------------

G = "Licenciaturas"
P.formulas_in(G, "Música: teoría y afinación", [
    ("Frecuencia de una nota (MIDI)", r"f = 440 \cdot 2^{\frac{n - 69}{12}}", "Note frequency (MIDI)"),
    ("Razón del semitono", r"r = 2^{1/12} \approx 1.05946", "Semitone ratio"),
    ("Frecuencia tras n semitonos", r"f_{n} = f_{0} \cdot 2^{n/12}", "Frequency after n semitones"),
    ("Cents entre dos frecuencias", r"c = 1200 \log_{2} \frac{f_{2}}{f_{1}}", "Cents between two frequencies"),
    ("Octava", r"f_{2} = 2 f_{1}", "Octave"),
    ("Quinta justa (afinación pitagórica)", r"\frac{f_{2}}{f_{1}} = \frac{3}{2}", "Perfect fifth (Pythagorean)"),
    ("Cuarta justa", r"\frac{f_{2}}{f_{1}} = \frac{4}{3}", "Perfect fourth"),
    ("Tercera mayor (entonación justa)", r"\frac{f_{2}}{f_{1}} = \frac{5}{4}", "Major third (just intonation)"),
    ("Coma pitagórica", r"\left( \frac{3}{2} \right)^{12} / 2^{7} \approx 1.01364", "Pythagorean comma"),
    ("Tempo (BPM) a milisegundos", r"t_{\text{negra}} = \frac{60\,000}{BPM} \text{ ms}", "Tempo (BPM) to milliseconds"),
    ("Duración de una redonda", r"t = 4 \cdot \frac{60}{BPM} \text{ s}", "Length of a whole note"),
    ("Compás: pulsos por minuto", r"BPM = \frac{\text{pulsos}}{\text{minutos}}", "Beats per minute"),
    ("Número MIDI de una nota", r"n = 69 + 12 \log_{2} \frac{f}{440}", "MIDI number of a note"),
    ("Transposición", r"n' = (n + k) \bmod 12", "Transposition"),
], "Music: theory and tuning")
P.formulas_in(G, "Música: acústica", [
    ("Velocidad del sonido en el aire", r"v \approx 331.3 + 0.6\,T \text{ m/s}", "Speed of sound in air"),
    ("Longitud de onda", r"\lambda = \frac{v}{f}", "Wavelength"),
    ("Armónicos de una cuerda", r"f_{n} = \frac{n}{2L} \sqrt{\frac{T}{\mu}}", "String harmonics"),
    ("Tubo abierto", r"f_{n} = \frac{n\,v}{2L}", "Open tube"),
    ("Tubo cerrado", r"f_{n} = \frac{(2n - 1)\,v}{4L}", "Closed tube"),
    ("Batimientos", r"f_{b} = |f_{1} - f_{2}|", "Beats"),
    ("Nivel de intensidad", r"\beta = 10 \log_{10} \frac{I}{I_{0}}, \quad I_{0} = 10^{-12} \text{ W/m}^{2}", "Intensity level"),
    ("Nivel de presión sonora", r"L_{p} = 20 \log_{10} \frac{p}{p_{0}}", "Sound pressure level"),
    ("Suma de dos fuentes", r"L = 10 \log_{10} \left( 10^{L_{1}/10} + 10^{L_{2}/10} \right)", "Sum of two sources"),
    ("Efecto Doppler", r"f' = f \frac{v \pm v_{o}}{v \mp v_{s}}", "Doppler effect"),
    ("Tiempo de reverberación (Sabine)", r"T_{60} = \frac{0.161\,V}{A}", "Reverberation time (Sabine)"),
    ("Frecuencia de muestreo (Nyquist)", r"f_{s} \ge 2 f_{max}", "Sampling rate (Nyquist)"),
    ("Tasa de bits digital", r"R = f_{s} \cdot n \cdot c", "Digital bit rate"),
    ("Serie de Fourier de una onda", r"x(t) = \sum_{n=1}^{\infty} A_{n} \sin(2\pi n f t + \phi_{n})", "Fourier series of a wave"),
], "Music: acoustics")

P.labels = [["Forte", "#dc2626"], ["Piano", "#2563eb"], ["Crescendo", "#ea580c"], ["Allegro", "#16a34a"], ["Adagio", "#7c3aed"],
            ["Staccato", "#0891b2"], ["Legato", "#be185d"], ["Tema", "#334155"], ["Coda", "#ca8a04"], ["Repetir", "#15803d"]]
P.en.update({"Forte": "Forte", "Piano": "Piano", "Crescendo": "Crescendo", "Tema": "Theme", "Coda": "Coda", "Repetir": "Repeat"})
P.emoji = {"Música": "🎵 🎶 🎼 🎹 🎸 🥁 🎺 🎻 🎷 🎤 🎧 📻 🔔 🪕 🪗 🎙️ 🎚️ 🎛️ 💿 📀"}
