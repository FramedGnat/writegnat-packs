import math
from _common import M, W, H, header, badge, gear


def extend(P):
    P.version = 2

    @P.template("gantt", "Gantt semanal (horizontal)", "Weekly Gantt (landscape)", 842.0, 595.0)
    def _(a):
        a.title(36, 34, "Diagrama de Gantt"); a.fields(36, 78, 806, ["Proyecto", "Responsable", "Inicio"])
        a.table(36, 92, 806, 559, [3] + [1] * 14, 18, ["Actividad"] + [f"S{k}" for k in range(1, 15)])

    @P.template("check-sheet", "Hoja de verificación", "Check sheet")
    def _(a):
        y = header(a, "Hoja de verificación", ["Proceso", "Inspector", "Fecha"])
        a.table(M, y, W - M, y + 380, [2.4, 1, 1, 1, 1, 1, 1, 1.2], 14, ["Defecto", "L", "M", "Mi", "J", "V", "S", "Total"])
        a.section(M, y + 390, W - M, H - M, "Análisis (Pareto / causas)")

    @P.template("algorithm", "Diseño de algoritmo", "Algorithm design")
    def _(a):
        y = header(a, "Algoritmo", ["Problema", "Nombre", "Fecha"])
        a.section(M, y, W / 2 - 4, y + 120, "Entrada"); a.section(W / 2 + 4, y, W - M, y + 120, "Salida")
        y += 128
        a.rect(M, y, W / 2 - 4, H - M - 130, w=0.9); a.text(M + 5, y + 4, "Diagrama de flujo", 9); a.dots(M + 10, y + 20, W / 2 - 12, H - M - 136, 14.17)
        a.rect(W / 2 + 4, y, W - M, H - M - 130, w=0.9); a.text(W / 2 + 9, y + 4, "Pseudocódigo", 9)
        for k in range(1, 30):
            yy = y + 14 + k * 18
            if yy > H - M - 136: break
            a.text(W / 2 + 8, yy - 9, str(k), 6.5); a.line(W / 2 + 22, yy, W - M - 6, yy, color="#e5e7eb", w=0.4)
        a.table(M, H - M - 120, W - M, H - M, [1, 1, 1, 2], 4, ["Prueba", "Entrada", "Esperado", "Resultado"])

    @P.sticker("bug", "Bug", "Bug")
    def _(a):
        a.circle(30, 34, 16, color="#16a34a", fill=True, ry=20); a.circle(30, 12, 8, color="#15803d", fill=True)
        for y in (26, 34, 42): a.line(14, y, 4, y - 4, color="#14532d", w=2); a.line(46, y, 56, y - 4, color="#14532d", w=2)
        a.line(30, 16, 30, 54, color="#14532d", w=1.2)

    @P.sticker("terminal", "Terminal", "Terminal", 64, 46)
    def _(a):
        a.round_rect(2, 2, 62, 44, 5, color="#111827", fill=True); a.text(8, 8, ">_", 14, "#22c55e")

    @P.sticker("gear-blue", "Proceso", "Process")
    def _(a): gear(a, 30, 30, 26, "#2563eb", 12)

    @P.sticker("todo", "Pendiente", "To do", 80, 26)
    def _(a): badge(a, "☐ Pendiente", "#ea580c")

    @P.sticker("done", "Hecho", "Done", 70, 26)
    def _(a): badge(a, "☑ Hecho", "#16a34a")

    @P.sticker("deadline", "Fecha límite", "Deadline", 92, 26)
    def _(a): badge(a, "⏰ Fecha límite", "#dc2626")

    @P.sticker("cloud-color", "Nube", "Cloud", 70, 44)
    def _(a):
        for cx, cy, r in ((22, 26, 14), (38, 20, 16), (52, 28, 12), (34, 30, 14)): a.circle(cx, cy, r, color="#93c5fd", fill=True)

    P.symbols_in("Computación", [r"O(n)", r"O(\log n)", r"O(n^{2})", r"O(n \log n)", r"\Theta(n)", r"\Omega(n)", r"\lceil x \rceil", r"\lfloor x \rfloor",
                                 r"\land", r"\lor", r"\neg", r"\oplus", r"\forall", r"\exists", r"\in", r"\mathbb{Z}", r"\mathbb{N}", r"\leftarrow",
                                 r"\mapsto", r"\hat{y}", r"\nabla J", r"\sigma(x)", r"\text{mod}", r"\{0, 1\}^{n}", r"2^{n}"], "Computing")
    P.symbols_in("Industrial", [r"\bar{x}", r"\bar{R}", r"\sigma", r"\lambda", r"\mu", r"\rho", r"C_{p}", r"C_{pk}", r"Q^{*}", r"LSC", r"LIC",
                                r"MTBF", r"MTTR", r"\max z", r"\text{s.a.}", r"x \ge 0"], "Industrial")
