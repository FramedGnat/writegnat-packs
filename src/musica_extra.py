import math
from _common import M, W, H, header, badge


def extend(P):
    def staves(a, y0, count, gap, x0=M, x1=W - M, sp=7.0):
        for k in range(count):
            y = y0 + k * gap
            for l in range(5): a.line(x0, y + l * sp, x1, y + l * sp, w=0.6, color="#6b7280")
            a.line(x0, y, x0, y + 4 * sp, w=0.9, color="#6b7280"); a.line(x1, y, x1, y + 4 * sp, w=0.9, color="#6b7280")

    @P.template("staff-sheet", "Hoja de pentagramas", "Staff paper")
    def _(a):
        y = header(a, "Pentagramas", ["Obra", "Compositor", "Fecha"])
        a.text(M, y + 4, "Tempo: ____", 9); a.text(W - M - 90, y + 4, "Tonalidad: ____", 9)
        staves(a, y + 28, 11, 62)

    @P.template("piano-sheet", "Hoja de piano (pentagrama doble)", "Piano sheet (grand staff)")
    def _(a):
        y = header(a, "Piano", ["Obra", "Compositor", "Fecha"])
        for k in range(6):
            y0 = y + 20 + k * 110
            staves(a, y0, 1, 0, M + 14, W - M); staves(a, y0 + 42, 1, 0, M + 14, W - M)
            a.line(M + 14, y0, M + 14, y0 + 70, w=1.0, color="#6b7280")
            a.text(M, y0 + 14, "Sol", 8); a.text(M, y0 + 56, "Fa", 8)

    @P.template("tab-sheet", "Hoja de tablatura (guitarra)", "Guitar tab sheet")
    def _(a):
        y = header(a, "Tablatura", ["Canción", "Afinación", "Fecha"])
        a.text(M, y + 4, "Afinación estándar: E A D G B e", 8.5)
        for k in range(9):
            y0 = y + 28 + k * 68
            for l in range(6): a.line(M + 18, y0 + l * 9, W - M, y0 + l * 9, w=0.6, color="#6b7280")
            a.text(M, y0 + 2, "T", 11); a.text(M, y0 + 16, "A", 11); a.text(M, y0 + 30, "B", 11)
            a.line(M + 18, y0, M + 18, y0 + 45, w=0.9, color="#6b7280"); a.line(W - M, y0, W - M, y0 + 45, w=0.9, color="#6b7280")

    @P.template("chord-grid", "Hoja de acordes (diagramas)", "Chord chart sheet")
    def _(a):
        y = header(a, "Diccionario de acordes", ["Instrumento", "Nombre", "Fecha"])
        cw = (W - 2 * M) / 5; ch = 118
        for r in range(6):
            for c in range(5):
                x0 = M + c * cw + 10; y0 = y + 22 + r * ch
                a.text(x0 + 12, y0 - 14, "____", 9)
                for s in range(6): a.line(x0 + s * 12, y0, x0 + s * 12, y0 + 60, w=0.6, color="#6b7280")
                for f in range(5): a.line(x0, y0 + f * 15, x0 + 60, y0 + f * 15, w=0.6 if f else 1.6, color="#6b7280")

    @P.template("lead-sheet", "Hoja de letra y acordes", "Lead sheet")
    def _(a):
        y = header(a, "Letra y acordes", ["Canción", "Tono", "BPM"])
        for k in range(7):
            y0 = y + 20 + k * 100
            a.line(M, y0 + 8, W - M, y0 + 8, w=0.5, color="#d4d4d8"); a.text(M, y0 - 4, "Acordes", 7.5)
            staves(a, y0 + 16, 1, 0, M, W - M, 6.0)
            a.line(M, y0 + 66, W - M, y0 + 66, w=0.5, color="#d4d4d8"); a.text(M, y0 + 54, "", 7)
            a.line(M, y0 + 80, W - M, y0 + 80, w=0.5, color="#d4d4d8")

    @P.template("dictation", "Dictado musical y solfeo", "Music dictation and solfège")
    def _(a):
        y = header(a, "Dictado", ["Ejercicio", "Alumno", "Fecha"])
        for k in range(8):
            y0 = y + 18 + k * 82
            a.text(M, y0 - 8, f"{k + 1}.", 9); staves(a, y0 + 6, 1, 0, M + 14, W - M, 6.0)
            a.line(M + 14, y0 + 40, W - M, y0 + 40, w=0.4, color="#d4d4d8")

    @P.sticker("treble-color", "Clave de sol", "Treble clef", 40, 70)
    def _(a):
        pts = [(20, 56), (24, 60), (28, 56), (27, 48), (23, 36), (19, 24), (18, 14), (20, 6), (25, 4), (28, 9), (27, 16), (23, 26), (19, 34), (16, 42), (17, 48), (22, 50), (27, 46), (26, 40), (21, 38)]
        a.line(*[x for p in pts for x in p], color="#7c3aed", w=3.0)
        a.circle(17, 56, 2.2, color="#7c3aed", fill=True)

    @P.sticker("notes-pair", "Corcheas", "Eighth notes", 56, 60)
    def _(a):
        for x, y in ((14, 46), (38, 40)):
            a.circle(x, y, 6, color="#2563eb", fill=True, ry=4.5); a.line(x + 5.5, y, x + 5.5, y - 34, color="#2563eb", w=2.2)
        a.poly(19.5, 12, 43.5, 6, 43.5, 12, 19.5, 18, color="#2563eb", fill=True)

    @P.sticker("note-single", "Nota", "Note", 36, 60)
    def _(a): a.circle(14, 46, 8, color="#dc2626", fill=True, ry=6); a.line(21, 46, 21, 8, color="#dc2626", w=2.6); a.poly(21, 8, 32, 16, 32, 26, 21, 20, color="#dc2626", fill=True)

    @P.sticker("keys", "Teclas de piano", "Piano keys", 70, 50)
    def _(a):
        for k in range(5): a.rect(2 + k * 13, 4, 15 + k * 13, 46, color="#374151", w=1.2, fill=False)
        for k in (0, 1, 3): a.rect(11 + k * 13, 4, 20 + k * 13, 28, color="#111827", fill=True)

    @P.sticker("guitar-color", "Guitarra", "Guitar", 40, 70)
    def _(a):
        a.rect(18, 2, 24, 34, color="#92400e", fill=True); a.circle(21, 52, 14, color="#f59e0b", fill=True, ry=16); a.circle(21, 46, 10, color="#fbbf24", fill=True, ry=8)
        a.circle(21, 50, 4, color="#451a03", fill=True); a.rect(15, 58, 27, 62, color="#92400e", fill=True)

    @P.sticker("drum-color", "Tambor", "Drum", 60, 50)
    def _(a):
        a.round_rect(6, 18, 54, 44, 6, color="#dc2626", fill=True); a.circle(30, 18, 24, color="#fecaca", fill=True, ry=7)
        a.line(14, 8, 26, 22, color="#78350f", w=2.4); a.line(46, 8, 34, 22, color="#78350f", w=2.4)

    @P.sticker("headphones-color", "Audífonos", "Headphones", 60, 54)
    def _(a):
        pts = [(10 + 40 * k / 20, 34 - 26 * math.sin(math.pi * k / 20)) for k in range(21)]
        a.line(*[x for p in pts for x in p], color="#334155", w=4)
        a.round_rect(5, 32, 17, 50, 4, color="#0ea5e9", fill=True); a.round_rect(43, 32, 55, 50, 4, color="#0ea5e9", fill=True)

    @P.sticker("mic-color", "Micrófono", "Microphone", 36, 64)
    def _(a):
        a.circle(18, 16, 11, color="#94a3b8", fill=True, ry=13); a.round_rect(12, 28, 24, 52, 5, color="#334155", fill=True); a.line(18, 52, 18, 62, color="#334155", w=3)

    @P.sticker("vinyl", "Disco", "Record", 56, 56)
    def _(a):
        a.circle(28, 28, 26, color="#111827", fill=True)
        for r in (20, 15, 10): a.circle(28, 28, r, color="#374151", w=0.8)
        a.circle(28, 28, 7, color="#dc2626", fill=True); a.circle(28, 28, 1.5, color="#ffffff", fill=True)

    @P.sticker("metronome-color", "Metrónomo", "Metronome", 44, 64)
    def _(a):
        a.poly(10, 60, 34, 60, 28, 6, 16, 6, color="#92400e", fill=True); a.line(22, 54, 28, 14, color="#fde68a", w=2.4); a.circle(26, 22, 3.4, color="#facc15", fill=True)

    @P.sticker("sharp-badge", "Sostenido", "Sharp", 32, 32)
    def _(a): badge(a, "♯", "#7c3aed", size=16)

    @P.sticker("flat-badge", "Bemol", "Flat", 32, 32)
    def _(a): badge(a, "♭", "#0891b2", size=16)

    @P.sticker("forte-badge", "f", "f", 32, 32)
    def _(a): badge(a, "f", "#dc2626", size=16)

    @P.sticker("piano-badge", "p", "p", 32, 32)
    def _(a): badge(a, "p", "#2563eb", size=16)

    P.symbols_in("Música", [r"\sharp", r"\flat", r"\natural", r"f_{0}", r"2^{1/12}", r"\sqrt[12]{2}", r"\frac{3}{2}", r"\frac{5}{4}", r"\frac{4}{3}",
                            r"\text{Hz}", r"\text{cents}", r"\text{BPM}", r"\text{dB}", r"\lambda", r"\Delta f", r"\log_{2}", r"\text{mf}", r"\text{pp}", r"\text{ff}",
                            r"\frac{f_{2}}{f_{1}}", r"\times 2^{n}", r"\bmod 12", r"\omega = 2\pi f", r"\sin(2\pi f t)"], "Music")
