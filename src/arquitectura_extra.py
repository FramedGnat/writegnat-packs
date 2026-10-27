import math
from _common import M, W, H, header, title_block, badge


def extend(P):
    P.version = 2

    @P.template("sheet-a", "Lámina con cuadro de datos (horizontal)", "Drawing sheet with title block (landscape)", 842.0, 595.0)
    def _(a):
        a.rect(20, 20, 822, 575, w=1.6); a.rect(28, 28, 814, 567, w=0.6)
        title_block(a, 620, 455, 814, 567, ("Proyecto", "Plano", "Escala", "Fecha", "Clave"))
        a.rect(620, 395, 814, 450, w=0.6); a.text(624, 399, "Notas", 8); a.circle(780, 425, 16, w=0.6); a.text(776, 400, "N", 8)

    @P.template("sketch-plan", "Croquis de planta (cuadrícula 1 m)", "Plan sketch (1 m grid)")
    def _(a):
        y = header(a, "Croquis de planta", ["Proyecto", "Escala", "Fecha"])
        a.grid(M, y, W - M, H - M - 70, 9.45, color="#eef0f2", w=0.25); a.grid(M, y, W - M, H - M - 70, 47.25, color="#cbd5e1", w=0.5)
        title_block(a, W - M - 220, H - M - 62, W - M, H - M, ("Espacio", "Área (m²)", "Revisión", "Fecha"))

    @P.template("isometric-sheet", "Hoja isométrica", "Isometric sheet")
    def _(a):
        y = header(a, "Isométrico", ["Ejercicio", "Nombre", "Fecha"])
        step = 14.17; t = math.tan(math.radians(30))
        x = M
        while x <= W - M: a.line(x, y, x, H - M, color="#e5e7eb", w=0.3); x += step * math.cos(math.radians(30))
        for k in range(-60, 80):
            x0 = M + k * step / t * 0.5
            a.line(max(M, x0), y + max(0, (M - x0)) * t, min(W - M, x0 + (H - M - y) / t), min(H - M, y + (min(W - M, x0 + (H - M - y) / t) - x0) * t), color="#e5e7eb", w=0.3)
            a.line(max(M, x0), H - M - max(0, (M - x0)) * t, min(W - M, x0 + (H - M - y) / t), max(y, H - M - (min(W - M, x0 + (H - M - y) / t) - x0) * t), color="#e5e7eb", w=0.3)

    @P.sticker("house", "Casa", "House")
    def _(a):
        a.poly(30, 4, 56, 28, 4, 28, color="#dc2626", fill=True); a.rect(10, 28, 50, 56, color="#fde68a", fill=True)
        a.rect(25, 38, 35, 56, color="#92400e", fill=True); a.rect(14, 33, 22, 41, color="#60a5fa", fill=True); a.rect(38, 33, 46, 41, color="#60a5fa", fill=True)

    @P.sticker("ruler-color", "Escuadra", "Set square")
    def _(a): a.poly(4, 56, 56, 56, 4, 4, color="#facc15", fill=True); a.poly(14, 46, 34, 46, 14, 26, color="#ffffff", fill=True); a.poly(4, 56, 56, 56, 4, 4, color="#a16207", w=1.4)

    @P.sticker("tree-color", "Árbol", "Tree")
    def _(a): a.rect(26, 38, 34, 58, color="#92400e", fill=True); a.circle(30, 24, 20, color="#22c55e", fill=True); a.circle(22, 30, 12, color="#16a34a", fill=True)

    @P.sticker("north-color", "Norte", "North")
    def _(a): a.circle(30, 30, 26, color="#f1f5f9", fill=True); a.poly(30, 6, 38, 40, 30, 34, 22, 40, color="#dc2626", fill=True); a.text(26, 40, "N", 11, "#111111")

    @P.sticker("sun", "Asoleamiento", "Sun path")
    def _(a):
        a.circle(30, 30, 12, color="#facc15", fill=True)
        for k in range(12): t = 2 * math.pi * k / 12; a.line(30 + 16 * math.cos(t), 30 + 16 * math.sin(t), 30 + 26 * math.cos(t), 30 + 26 * math.sin(t), color="#f59e0b", w=2.4)

    @P.sticker("approved", "Aprobado", "Approved", 82, 26)
    def _(a): badge(a, "✓ Aprobado", "#16a34a")

    P.symbols_in("Arquitectura", [r"\text{m}^{2}", r"\text{m}^{3}", r"\text{cm}", r"1:100", r"1:50", r"\varphi", r"\pm 0.00", r"\text{N.P.T.}", r"\%",
                                  r"\angle", r"\perp", r"\parallel", r"\cong", r"\sim", r"\text{lx}", r"\text{dB}", r"\varnothing", r"\text{W/m}^{2}\text{K}"], "Architecture")
