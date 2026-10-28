import math
from _draw import *


def extend(P):
    def st(sid, name, en):
        return P.sticker("ch-" + sid, name, en, 80, 80)

    @st("barras", "Barras con cara", "Bar chart buddy")
    def _(a):
        ln(a, 8, 8, 8, 72, w=2); ln(a, 8, 72, 74, 72, w=2)
        for k, (h, c) in enumerate(((22, "#fca5a5"), (34, "#fcd34d"), (48, "#86efac"), (60, "#4ade80"))):
            rr(a, 14 + k * 15, 72 - h, 26 + k * 15, 72, 2, c, w=1.6)
        eyes(a, 62, 46, 3.4, 1.5, "dot"); smile(a, 62, 48.4, 3, 1.3)
        ln(a, 16, 38, 34, 26, 48, 22, 66, 8, color="#ef4444", w=1.6)

    @st("alcancia", "Alcancía", "Piggy bank")
    def _(a):
        cc(a, 38, 44, 27, "#f9a8d4", ry=22); pg(a, 22, 26, 20, 14, 32, 22, fill="#f472b6", w=1.5)
        rr(a, 20, 58, 30, 72, 3, "#f472b6", w=1.5); rr(a, 46, 58, 56, 72, 3, "#f472b6", w=1.5)
        cc(a, 64, 46, 9, "#f472b6", ry=7.4); cc(a, 62, 46, 1.4, OL, w=0.4); cc(a, 67, 46, 1.4, OL, w=0.4)
        ln(a, 12, 44, 8, 40, 11, 36, color=OL, w=1.8)
        rr(a, 30, 21, 46, 25, 2, "#be185d", w=1.2); cc(a, 38, 10, 7, "#fbbf24", ry=7, w=1.6); a.text(35.5, 5.5, "$", 9, "#b45309")
        eyes(a, 50, 38, 4.8, 1.8, "dot")
        blush(a, 50, 46, 7)

    @st("billete", "Billete", "Banknote")
    def _(a):
        rr(a, 6, 20, 74, 60, 4, "#86efac"); rr(a, 11, 25, 69, 55, 2.5, "#bbf7d0", w=1.2)
        cc(a, 40, 40, 12, "#4ade80", w=1.6); face(a, 40, 39, "dot", "smile", 4.8, 1.9, my=44)
        for x, y in ((16, 31), (64, 31), (16, 49), (64, 49)): a.text(x - 3.4, y - 5, "$", 8, "#15803d")
        shine(a, 24, 27, 5, 1)

    @st("carrito", "Carrito de compras", "Shopping cart")
    def _(a):
        ln(a, 6, 14, 18, 14, 26, 50, 62, 50, color=OL, w=3.2)
        pg(a, 18, 20, 72, 20, 64, 46, 26, 46, fill="#bae6fd", w=1.8)
        for x in (34, 48, 60): ln(a, x, 20, x - 2, 46, color="#38bdf8", w=1)
        cc(a, 34, 62, 6, "#475569", w=1.6); cc(a, 34, 62, 2.4, "#cbd5e1", w=1); cc(a, 58, 62, 6, "#475569", w=1.6); cc(a, 58, 62, 2.4, "#cbd5e1", w=1)
        face(a, 46, 31, "dot", "smile", 8, 2.5, my=37, cheeks=True)
        pg(a, 48, 6, 54, 6, 58, 18, 44, 18, fill="#fbbf24", w=1.2)

    @st("balanza", "Balanza", "Scales")
    def _(a):
        rr(a, 20, 68, 60, 76, 3, "#94a3b8"); ln(a, 40, 14, 40, 68, color=OL, w=5.6); ln(a, 40, 14, 40, 68, color="#cbd5e1", w=3.2)
        ln(a, 10, 22, 70, 22, color=OL, w=4.4); ln(a, 10, 22, 70, 22, color="#fbbf24", w=2.4); cc(a, 40, 12, 4.4, "#fbbf24", w=1.5)
        for x in (14, 66):
            ln(a, x, 22, x - 8, 46, color=OL, w=1.2); ln(a, x, 22, x + 8, 46, color=OL, w=1.2)
            pg(a, x - 11, 46, x + 11, 46, x + 6, 54, x - 6, 54, fill="#fcd34d", w=1.6)
        cc(a, 14, 41, 5, "#fbbf24", w=1.4); a.text(11.4, 36.5, "$", 7.5, "#92400e")
        cc(a, 66, 41, 5, "#fde68a", w=1.4); smile(a, 66, 40.5, 2.2, 1.1); cc(a, 64, 39, 0.9, OL, w=0.2); cc(a, 68, 39, 0.9, OL, w=0.2)

    @st("lingote", "Lingote de oro", "Gold bar")
    def _(a):
        pg(a, 14, 34, 66, 34, 74, 56, 6, 56, fill="#fbbf24", w=1.8); pg(a, 20, 20, 60, 20, 66, 34, 14, 34, fill="#fde68a", w=1.8)
        pg(a, 24, 24, 56, 24, 60, 32, 20, 32, fill="#fef3c7", w=1)
        face(a, 40, 44, "dot", "smile", 8, 2.6, my=50, cheeks=True)
        shine(a, 24, 40, 5, 1.2); a.text(33, 25.5, "999", 6, "#b45309")
        for x, y in ((66, 14), (72, 24)): star(a, x, y, 3.6, "#fde047")

    @st("tarjeta", "Tarjeta bancaria", "Bank card")
    def _(a):
        rr(a, 6, 16, 74, 62, 6, "#6366f1"); rr(a, 6, 26, 74, 36, 0.5, "#312e81", w=1)
        rr(a, 12, 42, 26, 52, 2, "#fbbf24", w=1.3); ln(a, 12, 47, 26, 47, w=0.9); ln(a, 19, 42, 19, 52, w=0.9)
        for k in range(4): ln(a, 32 + k * 9, 56, 36 + k * 9, 56, color="#c7d2fe", w=1.6)
        cc(a, 58, 46, 6, "#f87171", w=0.1); cc(a, 65, 46, 6, "#fbbf24", w=0.1)
        cc(a, 60, 45, 1.1, OL, w=0.2); cc(a, 65, 45, 1.1, OL, w=0.2); smile(a, 62.5, 46, 2.4, 1.1)

    @st("toro", "Toro (mercado alcista)", "Bull market")
    def _(a):
        rr(a, 14, 38, 62, 62, 10, "#fb923c"); pg(a, 22, 62, 22, 74, 28, 74, 30, 62, fill="#c2410c", w=1.5); pg(a, 48, 62, 48, 74, 54, 74, 56, 62, fill="#c2410c", w=1.5)
        rr(a, 48, 22, 72, 50, 8, "#fdba74"); pg(a, 52, 24, 44, 10, 54, 18, fill="#fef3c7", w=1.6); pg(a, 68, 24, 74, 10, 64, 18, fill="#fef3c7", w=1.6)
        cc(a, 56, 33, 2, OL, w=0.4); cc(a, 65, 33, 2, OL, w=0.4); rr(a, 54, 40, 68, 48, 4, "#f472b6", w=1.4); cc(a, 58, 44, 1.1, OL, w=0.3); cc(a, 64, 44, 1.1, OL, w=0.3)
        ln(a, 14, 46, 6, 40, 8, 54, w=2); ln(a, 8, 12, 24, 20, 32, 10, 44, 18, color="#22c55e", w=2.2)

    @st("oso", "Oso (mercado bajista)", "Bear market")
    def _(a):
        cc(a, 22, 22, 9, "#a16207"); cc(a, 58, 22, 9, "#a16207"); cc(a, 22, 22, 4, "#fcd34d", w=1); cc(a, 58, 22, 4, "#fcd34d", w=1)
        cc(a, 40, 40, 26, "#a16207", ry=24); cc(a, 40, 50, 12, "#fcd34d", ry=9)
        cc(a, 29, 36, 3, OL, w=0.4); cc(a, 51, 36, 3, OL, w=0.4); a.circle(28.2, 35, 0.9, color=WH, fill=True); a.circle(50.2, 35, 0.9, color=WH, fill=True)
        cc(a, 40, 46, 3.6, OL, w=0.4, ry=2.8); frown(a, 40, 51, 4, 1.6)
        ln(a, 8, 70, 22, 58, 34, 66, 52, 76, color="#ef4444", w=2.4)

    @st("velas", "Velas japonesas", "Candlestick chart")
    def _(a):
        rr(a, 6, 8, 74, 72, 4, "#f1f5f9")
        for y in (24, 40, 56): ln(a, 10, y, 70, y, color="#cbd5e1", w=0.8)
        for x, top, bot, w0, c in ((18, 38, 56, 8, "#4ade80"), (32, 26, 50, 10, "#f87171"), (46, 20, 42, 10, "#4ade80"), (60, 14, 34, 10, "#4ade80")):
            ln(a, x, top - 6, x, bot + 6, w=1.6); rr(a, x - 5, top, x + 5, bot, 1.5, c, w=1.4)
        eyes(a, 60, 24, 2.6, 1.1, "dot"); smile(a, 60, 25.6, 2.2, 1.1)
        a.text(9, 61, "$", 9, "#16a34a")
