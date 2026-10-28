"""Figuras de las materias de Ingeniería Biomédica y salud (la carrera): señales, instrumentación, fisiología, biomecánica e imagen."""
import math

SEN = "Biomédica: señales"
INS = "Biomédica: instrumentación"
FIS = "Biomédica: anatomía y fisiología"
IMG = "Biomédica: imagen"


def extend(P):
    P.en.update({SEN: "Biomedical: signals", INS: "Biomedical: instrumentation", FIS: "Biomedical: anatomy and physiology", IMG: "Biomedical: imaging"})

    def axes(g, u0, v0, u1, v1):
        g.arrow(u0, v0, u1, v0, 0.04); g.arrow(u0, v0, u0, v1, 0.04)

    def gauss(u, c, w, h): return h * math.exp(-((u - c) / w) ** 2)

    def block(g, u0, v0, u1, v1, text, s=0.7):
        g.rect(u0, v0, u1, v1); g.label((u0 + u1) / 2, (v0 + v1) / 2, text, s)

    # --- Señales --------------------------------------------------------------------------------

    @P.figure(SEN, "ecg-waves", "ECG con ondas e intervalos", "ECG waves and intervals")
    def _(g):
        def ecg(u):
            return (gauss(u, 0.2, 0.04, 0.1) - gauss(u, 0.36, 0.012, 0.08) + gauss(u, 0.39, 0.012, 0.42) - gauss(u, 0.42, 0.012, 0.12)
                    + gauss(u, 0.62, 0.06, 0.16))
        g.curve(lambda u: ecg(u) - 0.1, 0.0, 1.0, 200)
        g.line(0.0, -0.1, 1.0, -0.1, dashed=True)
        for u, v, t in ((0.2, 0.02, "P"), (0.34, -0.26, "Q"), (0.39, 0.4, "R"), (0.43, -0.28, "S"), (0.62, 0.1, "T")): g.label(u, v, t, 0.8)
        g.double_arrow(0.14, -0.36, 0.36, -0.36, 0.03); g.label(0.25, -0.43, "PR", 0.6)
        g.double_arrow(0.34, -0.5, 0.7, -0.5, 0.03); g.label(0.52, -0.57, "QT", 0.6)

    @P.figure(SEN, "eeg-bands", "EEG: ritmos cerebrales", "EEG brain rhythms")
    def _(g):
        for k, (name, f, a) in enumerate((("δ", 2.0, 0.09), ("θ", 4.5, 0.07), ("α", 8.0, 0.06), ("β", 16.0, 0.04))):
            v0 = 0.33 - 0.22 * k
            g.curve(lambda u, v0=v0, f=f, a=a: v0 + a * math.sin(2 * math.pi * f * u) * (0.7 + 0.3 * math.sin(2 * math.pi * 1.3 * u)), 0.1, 1.0, 160)
            g.label(0.03, v0, name, 0.9)
        g.arrow(0.1, -0.4, 1.0, -0.4, 0.03); g.label(0.55, -0.47, "t (s)", 0.6)

    @P.figure(SEN, "emg-burst", "EMG (contracción muscular)", "EMG (muscle contraction)")
    def _(g):
        env = lambda u: gauss(u, 0.5, 0.18, 1.0)
        g.curve(lambda u: 0.22 * env(u) * math.sin(2 * math.pi * 38 * u) * (math.sin(2 * math.pi * 11 * u + 1) * 0.6 + 0.6), 0.05, 0.95, 400)
        g.line(0.05, 0.0, 0.95, 0.0, dashed=True); g.curve(lambda u: 0.3 * env(u) - 0.0, 0.05, 0.95, 60, dashed=True)
        g.label(0.5, 0.42, "envolvente", 0.6); g.label(0.12, -0.12, "reposo", 0.55); g.label(0.5, -0.32, "contracción", 0.6)

    @P.figure(SEN, "ppg-pulse", "Fotopletismografía (PPG)", "Photoplethysmogram (PPG)")
    def _(g):
        beat = lambda u: gauss(u % 0.5, 0.12, 0.06, 0.32) + gauss(u % 0.5, 0.3, 0.07, 0.14)
        g.curve(lambda u: beat(u) - 0.15, 0.0, 1.0, 200)
        g.label(0.12, 0.2, "sístole", 0.6); g.label(0.3, -0.03, "muesca dicrota", 0.5); g.label(0.5, -0.32, "tiempo", 0.6)

    @P.figure(SEN, "action-potential", "Potencial de acción", "Action potential")
    def _(g):
        axes(g, 0.08, -0.38, 0.97, 0.45)
        g.spline([(0.1, -0.2), (0.25, -0.2), (0.31, -0.1), (0.36, 0.28), (0.4, 0.38), (0.46, 0.15), (0.54, -0.2), (0.62, -0.32), (0.72, -0.29), (0.85, -0.22), (0.95, -0.2)], 12)
        g.line(0.08, -0.1, 0.95, -0.1, dashed=True); g.label(1.02, -0.1, "umbral", 0.5)
        g.label(0.22, 0.3, "despolarización", 0.5); g.label(0.62, 0.22, "repolarización", 0.5); g.label(0.75, -0.4, "hiperpolarización", 0.5); g.label(0.17, -0.26, "reposo", 0.5)
        g.label(0.05, 0.45, "mV", 0.7); g.label(0.97, -0.45, "t", 0.7)

    # --- Instrumentación ------------------------------------------------------------------------

    @P.figure(INS, "acquisition-chain", "Cadena de adquisición de señales", "Signal acquisition chain")
    def _(g):
        names = ("Sensor", "Ampl.", "Filtro", "ADC", "PC")
        for k, t in enumerate(names):
            u0 = k * 0.21; block(g, u0, -0.1, u0 + 0.16, 0.1, t, 0.55)
            if k < 4: g.arrow(u0 + 0.16, 0.0, u0 + 0.21, 0.0, 0.03)
        g.label(0.4, 0.2, "analógico", 0.55); g.label(0.78, 0.2, "digital", 0.55)
        g.line(0.56, 0.15, 0.56, -0.15, dashed=True)

    @P.figure(INS, "instrumentation-amp", "Amplificador de instrumentación", "Instrumentation amplifier")
    def _(g):
        def op(u, v, s=0.14):
            g.poly(u, v + s, u, v - s, u + 1.6 * s, v)
        op(0.3, 0.25); op(0.3, -0.25); op(0.7, 0.0)
        g.line(0.0, 0.31, 0.3, 0.31); g.line(0.0, -0.31, 0.3, -0.31); g.label(0.04, 0.38, "V₁", 0.6); g.label(0.04, -0.38, "V₂", 0.6)
        g.line(0.22, 0.19, 0.18, 0.19, 0.18, 0.1); g.line(0.22, -0.19, 0.18, -0.19, 0.18, -0.1)
        g.rect(0.15, -0.1, 0.21, 0.1); g.label(0.26, 0.0, "R_G", 0.55)
        g.line(0.524, 0.25, 0.58, 0.25, 0.58, 0.07, 0.7, 0.07); g.line(0.524, -0.25, 0.58, -0.25, 0.58, -0.07, 0.7, -0.07)
        g.line(0.924, 0.0, 1.0, 0.0); g.label(0.96, 0.08, "V_out", 0.6)

    @P.figure(INS, "ecg-electrode", "Electrodo Ag/AgCl sobre la piel", "Ag/AgCl skin electrode")
    def _(g):
        g.line(0.0, -0.1, 1.0, -0.1); g.line(0.0, -0.3, 1.0, -0.3)
        g.label(0.1, -0.2, "piel", 0.6); g.label(0.1, -0.4, "tejido", 0.6)
        g.poly(0.3, 0.0, 0.7, 0.0, 0.7, -0.1, 0.3, -0.1, fill=False)
        g.rect(0.35, 0.02, 0.65, 0.12); g.label(0.5, 0.07, "Ag/AgCl", 0.5)
        g.line(0.5, 0.12, 0.5, 0.3); g.line(0.5, 0.3, 0.9, 0.3); g.label(0.8, 0.38, "al amplificador", 0.55)
        g.label(0.5, -0.05, "gel", 0.5)

    @P.figure(INS, "einthoven", "Triángulo de Einthoven", "Einthoven's triangle")
    def _(g):
        g.poly(0.1, 0.3, 0.9, 0.3, 0.5, -0.35)
        g.circle(0.1, 0.3, 0.03, fill=True); g.circle(0.9, 0.3, 0.03, fill=True); g.circle(0.5, -0.35, 0.03, fill=True)
        g.label(0.04, 0.39, "RA", 0.7); g.label(0.96, 0.39, "LA", 0.7); g.label(0.5, -0.45, "LL", 0.7)
        g.label(0.5, 0.37, "I", 0.8); g.label(0.24, -0.04, "II", 0.8); g.label(0.76, -0.04, "III", 0.8)
        g.label(0.5, 0.05, "corazón", 0.55)

    @P.figure(INS, "bandpass-filter", "Filtro pasa banda (respuesta)", "Band-pass filter response")
    def _(g):
        axes(g, 0.08, -0.3, 0.97, 0.4)
        g.curve(lambda u: -0.25 + 0.6 * (1 / (1 + ((u - 0.5) / 0.22) ** 8)), 0.1, 0.95, 120)
        g.line(0.08, 0.2, 0.95, 0.2, dashed=True); g.line(0.28, 0.2, 0.28, -0.3, dashed=True); g.line(0.72, 0.2, 0.72, -0.3, dashed=True)
        g.label(0.28, -0.37, "f_c1 (0.5 Hz)", 0.5); g.label(0.72, -0.37, "f_c2 (40 Hz)", 0.5); g.label(0.5, 0.3, "ECG: 0.5–40 Hz", 0.6); g.label(0.05, 0.4, "|H|", 0.7)

    # --- Anatomía y fisiología ------------------------------------------------------------------

    @P.figure(FIS, "heart-chambers", "Corazón: cámaras y flujo", "Heart: chambers and flow")
    def _(g):
        g.ellipse(0.5, 0.0, 0.4, 0.36)
        g.line(0.5, 0.36, 0.5, -0.36); g.line(0.1, 0.02, 0.9, 0.02)
        g.label(0.3, 0.18, "AD", 0.8); g.label(0.7, 0.18, "AI", 0.8); g.label(0.3, -0.18, "VD", 0.8); g.label(0.7, -0.18, "VI", 0.8)
        g.arrow(0.05, 0.4, 0.2, 0.3, 0.04); g.label(0.04, 0.47, "cava", 0.5)
        g.arrow(0.3, -0.36, 0.2, -0.5, 0.04); g.label(0.14, -0.55, "pulmonar", 0.5)
        g.arrow(0.9, 0.4, 0.78, 0.3, 0.04); g.label(0.94, 0.47, "pulm.", 0.5)
        g.arrow(0.7, -0.36, 0.8, -0.5, 0.04); g.label(0.86, -0.55, "aorta", 0.5)

    @P.figure(FIS, "nephron", "Nefrona (esquema)", "Nephron (diagram)")
    def _(g):
        g.circle(0.15, 0.2, 0.1); g.circle(0.15, 0.2, 0.04)
        g.spline([(0.25, 0.2), (0.33, 0.32), (0.42, 0.2), (0.36, 0.1), (0.46, 0.04), (0.5, -0.05)], 10)
        g.line(0.5, -0.05, 0.5, -0.28); g.arc(0.6, -0.28, 0.1, 0.09, 180, 360); g.line(0.7, -0.28, 0.7, 0.08)
        g.spline([(0.7, 0.08), (0.76, 0.3), (0.88, 0.22)], 10); g.line(0.88, 0.22, 0.88, -0.4); g.arrow(0.88, -0.25, 0.88, -0.4, 0.04)
        g.label(0.15, 0.35, "glomérulo", 0.5); g.label(0.4, 0.4, "t. proximal", 0.5); g.label(0.6, -0.45, "asa de Henle", 0.5); g.label(0.76, 0.4, "t. distal", 0.5)
        g.label(0.88, -0.48, "colector", 0.5); g.arrow(0.0, 0.2, 0.1, 0.2, 0.03); g.label(0.03, 0.1, "sangre", 0.45)

    @P.figure(FIS, "glucose-feedback", "Control de glucosa (lazo cerrado)", "Glucose control (feedback loop)")
    def _(g):
        block(g, 0.0, -0.1, 0.26, 0.1, "Glucosa ↑", 0.55); block(g, 0.37, -0.1, 0.63, 0.1, "Páncreas", 0.55); block(g, 0.74, -0.1, 1.0, 0.1, "Insulina", 0.55)
        g.arrow(0.26, 0.0, 0.37, 0.0, 0.03); g.arrow(0.63, 0.0, 0.74, 0.0, 0.03)
        g.line(0.87, -0.1, 0.87, -0.3, 0.13, -0.3); g.arrow(0.13, -0.3, 0.13, -0.1, 0.03)
        g.label(0.5, -0.38, "células y hígado: glucosa ↓", 0.55); g.label(0.5, 0.2, "retroalimentación negativa", 0.55)

    @P.figure(FIS, "alveolus-exchange", "Alvéolo e intercambio gaseoso", "Alveolus gas exchange")
    def _(g):
        g.arc(0.55, 0.0, 0.28, 0.28, 210, 510)
        g.line(0.0, 0.14, 0.3075, 0.14); g.line(0.0, -0.14, 0.3075, -0.14)
        g.circle(0.92, 0.0, 0.07); g.label(0.92, -0.14, "capilar", 0.45)
        g.arrow(0.6, 0.06, 0.82, 0.06, 0.035); g.label(0.7, 0.14, "O₂", 0.7)
        g.arrow(0.82, -0.06, 0.6, -0.06, 0.035); g.label(0.7, -0.14, "CO₂", 0.7)
        g.label(0.12, 0.24, "bronquiolo", 0.5); g.label(0.55, 0.38, "alvéolo", 0.55)

    @P.figure(FIS, "sarcomere", "Sarcómero (actina y miosina)", "Sarcomere (actin and myosin)")
    def _(g):
        for u in (0.05, 0.95): g.line(u, 0.3, u, -0.3)
        for v in (0.2, 0.0, -0.2):
            g.line(0.05, v, 0.55, v); g.line(0.95, v + 0.1, 0.45, v + 0.1)
        for v in (0.15, -0.05): g.rect(0.3, v - 0.015, 0.7, v + 0.015, fill=True)
        g.label(0.05, 0.38, "Z", 0.7); g.label(0.95, 0.38, "Z", 0.7); g.double_arrow(0.05, -0.38, 0.95, -0.38, 0.03); g.label(0.5, -0.46, "sarcómero", 0.6)
        g.label(0.18, 0.3, "actina", 0.5); g.label(0.5, 0.3, "miosina", 0.5)

    @P.figure(FIS, "elbow-lever", "Biomecánica: antebrazo como palanca", "Biomechanics: forearm lever")
    def _(g):
        g.line(0.05, 0.1, 0.35, 0.1); g.circle(0.35, 0.1, 0.03, fill=True)
        g.rect(0.35, 0.07, 0.95, 0.13)
        g.arrow(0.5, 0.07, 0.5, 0.38, 0.04); g.label(0.58, 0.32, "F_b", 0.7)
        g.arrow(0.95, 0.07, 0.95, -0.2, 0.04); g.label(0.9, -0.28, "W", 0.7)
        g.label(0.35, -0.02, "codo", 0.55)
        g.double_arrow(0.35, -0.12, 0.5, -0.12, 0.025); g.label(0.42, -0.2, "d₁", 0.5)
        g.double_arrow(0.35, -0.32, 0.95, -0.32, 0.025); g.label(0.65, -0.4, "d₂", 0.5)
        g.label(0.2, 0.25, "ΣM = 0 → F_b·d₁ = W·d₂", 0.5)

    # --- Imagen médica --------------------------------------------------------------------------

    @P.figure(IMG, "xray-chain", "Rayos X: tubo, paciente y detector", "X-ray: tube, patient and detector")
    def _(g):
        g.rect(0.0, -0.1, 0.2, 0.1); g.label(0.1, 0.0, "tubo", 0.55)
        g.ellipse(0.55, 0.0, 0.1, 0.22); g.label(0.55, 0.3, "paciente", 0.55)
        g.rect(0.85, -0.3, 0.95, 0.3, dashed=False); g.label(0.9, -0.38, "detector", 0.55)
        for v in (-0.2, 0.0, 0.2): g.arrow(0.2, v * 0.4, 0.85, v, 0.03, dashed=True)

    @P.figure(IMG, "mri-bore", "Resonancia magnética (esquema)", "MRI scanner (diagram)")
    def _(g):
        g.rect(0.0, -0.3, 1.0, 0.3); g.circle(0.5, 0.0, 0.22)
        g.circle(0.5, 0.0, 0.15, dashed=True); g.label(0.5, 0.0, "B₀", 0.9)
        g.arrow(0.1, -0.38, 0.9, -0.38, 0.03); g.label(0.5, -0.45, "campo magnético principal", 0.5)
        g.label(0.18, 0.2, "bobina de gradiente", 0.45); g.label(0.82, 0.2, "bobina RF", 0.45)

    @P.figure(IMG, "ultrasound-echo", "Ultrasonido (eco)", "Ultrasound (echo)")
    def _(g):
        g.rect(0.05, 0.25, 0.4, 0.33); g.label(0.22, 0.4, "transductor", 0.55)
        g.line(0.0, 0.2, 1.0, 0.2)
        for r in (0.14, 0.26, 0.38): g.arc(0.22, 0.25, r, r, -120, -60)
        g.line(0.1, -0.15, 0.9, -0.15, dashed=True); g.label(0.82, -0.08, "interfaz", 0.5)
        g.arrow(0.5, 0.2, 0.5, -0.12, 0.03); g.arrow(0.6, -0.15, 0.6, 0.17, 0.03)
        g.label(0.5, -0.3, "t = 2d / c", 0.6); g.label(0.84, 0.1, "tejido", 0.5)

    @P.figure(IMG, "ct-gantry", "Tomografía computarizada (gantry)", "CT scanner (gantry)")
    def _(g):
        g.circle(0.5, 0.0, 0.4); g.circle(0.5, 0.0, 0.2); g.ellipse(0.5, 0.0, 0.1, 0.07)
        g.circle(0.5, 0.4, 0.03, fill=True); g.label(0.5, 0.5, "fuente", 0.55)
        g.rect(0.35, -0.44, 0.65, -0.37); g.label(0.5, -0.52, "detectores", 0.55)
        g.line(0.5, 0.37, 0.4, -0.37, dashed=True); g.line(0.5, 0.37, 0.6, -0.37, dashed=True)
        g.arc(0.5, 0.0, 0.47, 0.47, 20, 60); g.head(0.5 + 0.47 * math.cos(math.radians(50)), 0.47 * math.sin(math.radians(50)), 0.5 + 0.47 * math.cos(math.radians(60)), 0.47 * math.sin(math.radians(60)), 0.04)
