import math
from _common import M, W, H, header, badge


def extend(P):
    P.version = 2

    @P.template("income", "Estado de resultados", "Income statement")
    def _(a):
        y = header(a, "Estado de resultados", ["Empresa", "Periodo", "Elaboró"])
        rows = ["Ventas netas", "(−) Costo de ventas", "= Utilidad bruta", "(−) Gastos de venta", "(−) Gastos de administración", "= Utilidad de operación",
                "(+/−) Resultado financiero", "= Utilidad antes de impuestos", "(−) Impuestos", "= Utilidad neta"]
        a.table(M, y, W - M, y + 26 + 30 * len(rows), [3, 1, 1], len(rows), ["Concepto", "Parcial", "Total"])
        for k, r in enumerate(rows): a.text(M + 6, y + 30 + k * 30, r, 9)
        a.section(M, y + 40 + 30 * len(rows), W - M, H - M, "Análisis (márgenes, razones)")

    @P.template("cashflow", "Flujo de efectivo (horizontal)", "Cash flow (landscape)", 842.0, 595.0)
    def _(a):
        a.title(36, 34, "Flujo de efectivo"); a.fields(36, 78, 806, ["Proyecto", "Año", "Moneda"])
        months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic", "Total"]
        rows = ["Saldo inicial", "Ingresos", "  Ventas", "  Otros", "Egresos", "  Costos", "  Gastos", "  Impuestos", "  Inversión", "Flujo neto", "Saldo final"]
        a.table(36, 92, 806, 92 + 22 + 36 * len(rows), [2.2] + [1] * 13, len(rows), ["Concepto"] + months)
        for k, r in enumerate(rows): a.text(40, 118 + k * 36, r, 8.5)

    @P.template("balance", "Balance general", "Balance sheet")
    def _(a):
        y = header(a, "Balance general", ["Empresa", "Al", "Elaboró"])
        h = (H - M - y - 40)
        a.table(M, y, W / 2 - 4, y + h, [2.2, 1], 18, ["Activo", "$"]); a.table(W / 2 + 4, y, W - M, y + h * 0.6, [2.2, 1], 10, ["Pasivo", "$"])
        a.table(W / 2 + 4, y + h * 0.6 + 8, W - M, y + h, [2.2, 1], 7, ["Capital", "$"])
        a.rect(M, H - M - 30, W / 2 - 4, H - M, w=1); a.text(M + 5, H - M - 22, "Total activo", 9)
        a.rect(W / 2 + 4, H - M - 30, W - M, H - M, w=1); a.text(W / 2 + 9, H - M - 22, "Total pasivo + capital", 9)

    @P.sticker("coin", "Moneda", "Coin")
    def _(a): a.circle(30, 30, 26, color="#facc15", fill=True); a.circle(30, 30, 26, color="#a16207", w=2); a.circle(30, 30, 20, color="#ca8a04", w=1); a.text(22, 16, "$", 22, "#a16207")

    @P.sticker("up", "Sube", "Up")
    def _(a): a.poly(30, 4, 54, 30, 40, 30, 40, 56, 20, 56, 20, 30, 6, 30, color="#16a34a", fill=True)

    @P.sticker("down", "Baja", "Down")
    def _(a): a.poly(30, 56, 54, 30, 40, 30, 40, 4, 20, 4, 20, 30, 6, 30, color="#dc2626", fill=True)

    @P.sticker("chart-color", "Gráfica", "Chart")
    def _(a):
        for k, (h, c) in enumerate(((18, "#60a5fa"), (30, "#34d399"), (24, "#fbbf24"), (44, "#f472b6"))): a.rect(6 + k * 13, 54 - h, 16 + k * 13, 54, color=c, fill=True)
        a.line(4, 4, 4, 55, 58, 55, color="#374151", w=1.6)

    @P.sticker("money-bag", "Bolsa de dinero", "Money bag")
    def _(a):
        a.circle(30, 38, 20, color="#a3e635", fill=True); a.poly(22, 18, 38, 18, 34, 10, 26, 10, color="#84cc16", fill=True); a.text(24, 26, "$", 18, "#365314")

    @P.sticker("goal", "Meta", "Goal", 64, 26)
    def _(a): badge(a, "🎯 Meta", "#0891b2")

    @P.sticker("risk", "Riesgo", "Risk", 64, 26)
    def _(a): badge(a, "⚠ Riesgo", "#b91c1c")

    P.symbols_in("Economía y finanzas", [r"\$", r"\%", r"\Delta P", r"\Delta Q", r"\bar{x}", r"\sum", r"\prod", r"\pi", r"\text{IVA}", r"\text{PIB}",
                                         r"(1+i)^{n}", r"\frac{1}{(1+r)^{t}}", r"Q^{*}", r"P^{*}", r"\partial", r"\uparrow", r"\downarrow", r"\beta",
                                         r"r_{f}", r"E(R)", r"\text{VPN}", r"\text{TIR}"], "Economics and finance")
