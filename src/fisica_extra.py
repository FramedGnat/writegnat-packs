import math
from _common import M, W, H, header, lab_report, badge


def extend(P):
    P.version = 2

    @P.template("lab", "Reporte de laboratorio de física", "Physics lab report")
    def _(a): lab_report(a, "Reporte de laboratorio · Física", ["Medición", "x", "t (s)", "Incertidumbre"])

    @P.template("problems", "Resolución de problemas", "Problem solving")
    def _(a):
        y = header(a, "Resolución de problemas", ["Tema", "Nombre", "Fecha"])
        for k in range(3):
            h = (H - M - y) / 3 - 8; y0 = y + k * (h + 8)
            a.rect(M, y0, W - M, y0 + h, w=0.9); a.text(M + 5, y0 + 4, f"Problema {k + 1}", 9.5)
            a.line(M + 160, y0 + 18, M + 160, y0 + h, w=0.5); a.line(M, y0 + 18, W - M, y0 + 18, w=0.5)
            a.text(M + 5, y0 + 22, "Datos", 8.0); a.text(M + 165, y0 + 22, "Diagrama y planteamiento", 8.0)
            a.line(M, y0 + h - 34, M + 160, y0 + h - 34, w=0.5); a.text(M + 5, y0 + h - 30, "Incógnita", 8.0)
            a.rect(W - M - 150, y0 + h - 30, W - M - 6, y0 + h - 6, w=1.0); a.text(W - M - 146, y0 + h - 27, "Resultado", 7.5)
            a.grid(M + 166, y0 + 34, W - M - 160, y0 + h - 8, 14.17)

    @P.template("graph-paper", "Papel para gráficas (mm)", "Graph paper (mm)")
    def _(a):
        y = header(a, "Gráfica", ["Título", "Eje x", "Eje y"])
        a.grid(M, y + 6, W - M, H - M, 2.835, color="#e5e7eb", w=0.25); a.grid(M, y + 6, W - M, H - M, 28.35, color="#9ca3af", w=0.6)

    @P.sticker("units", "¡Unidades!", "Units!", 90, 30)
    def _(a): badge(a, "¡Unidades!", "#ca8a04")

    @P.sticker("key-formula", "Fórmula clave", "Key formula", 100, 30)
    def _(a): badge(a, "★ Fórmula clave", "#be185d")

    @P.sticker("result", "Resultado", "Result", 90, 30)
    def _(a): badge(a, "✓ Resultado", "#16a34a")

    @P.sticker("atom", "Átomo", "Atom")
    def _(a):
        for k in range(3):
            rot = k * math.pi / 3; pts = []
            for i in range(41):
                t = 2 * math.pi * i / 40; x, y = 26 * math.cos(t), 9 * math.sin(t)
                pts += [30 + x * math.cos(rot) - y * math.sin(rot), 30 + x * math.sin(rot) + y * math.cos(rot)]
            a.line(*pts, color=["#2563eb", "#7c3aed", "#0891b2"][k], w=2.0)
        a.circle(30, 30, 5, color="#dc2626", fill=True)

    @P.sticker("magnet", "Imán", "Magnet")
    def _(a):
        a.line(14, 8, 14, 34, color="#dc2626", w=9); a.line(46, 8, 46, 34, color="#2563eb", w=9)
        pts = []
        for k in range(21): t = math.pi * k / 20; pts += [30 - 16 * math.cos(t), 34 + 16 * math.sin(t)]
        a.line(*pts, color="#6b7280", w=9); a.text(10.5, 10, "N", 8, "#ffffff"); a.text(42.5, 10, "S", 8, "#ffffff")

    @P.sticker("bolt", "Rayo", "Lightning")
    def _(a): a.poly(34, 2, 12, 34, 28, 34, 22, 58, 48, 22, 32, 22, 40, 2, color="#facc15", w=1.2, fill=True); a.poly(34, 2, 12, 34, 28, 34, 22, 58, 48, 22, 32, 22, 40, 2, color="#a16207", w=1.2)

    @P.sticker("rocket", "Cohete", "Rocket")
    def _(a):
        a.poly(30, 2, 42, 18, 42, 42, 18, 42, 18, 18, color="#e5e7eb", w=1.0, fill=True); a.poly(30, 2, 42, 18, 42, 42, 18, 42, 18, 18, color="#374151", w=1.2)
        a.circle(30, 22, 5, color="#38bdf8", fill=True); a.poly(18, 30, 8, 46, 18, 42, color="#dc2626", fill=True); a.poly(42, 30, 52, 46, 42, 42, color="#dc2626", fill=True)
        a.poly(22, 42, 38, 42, 30, 58, color="#f97316", fill=True)

    P.symbols_in("Física", r"\vec{F} \vec{v} \vec{a} \hat{i} \hat{j} \hat{k} \hbar \nabla\times \nabla\cdot \partial_{t} \dot{x} \ddot{x} \omega \Delta{t} \propto \approx \mu_{0} \varepsilon_{0} \lambda \Phi_{B}".split() +
                  [r"\langle \psi |", r"| \psi \rangle", r"\text{m/s}^{2}", r"^{\circ}\text{C}", r"\text{N}", r"\text{J}", r"\text{W}", r"\text{Pa}", r"\text{eV}", r"\times 10^{n}"], "Physics")
