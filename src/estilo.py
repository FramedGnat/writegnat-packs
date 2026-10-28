import math
from wgpack import Pack
from _draw import *

pack = Pack("estilo", "Estilo urbano y emo", "Corazones rotos, cadenas, murciélagos, calaveras lindas, mariposas Y2K, banners con frases y accesorios de estética emo y urbana.",
            "General", "🖤", en={"Estilo urbano y emo": "Urban and emo style",
            "Corazones rotos, cadenas, murciélagos, calaveras lindas, mariposas Y2K, banners con frases y accesorios de estética emo y urbana.":
            "Broken hearts, chains, bats, cute skulls, Y2K butterflies, phrase banners and emo/urban accessories."})
P = pack
S = 80.0

K = "#111827"; NEON = "#ff2e93"; ROSA = "#f472b6"; MOR = "#8b5cf6"; LILA = "#c4b5fd"; RED = "#ef4444"; CHR = "#cbd5e1"; ORO = "#fbbf24"


def st(sid, name, en, w=S, h=S):
    return P.sticker("estilo-" + sid, name, en, w, h)


def sparkle(a, x, y, r, fill=WH):
    pg(a, x, y - r, x + r * 0.28, y - r * 0.28, x + r, y, x + r * 0.28, y + r * 0.28, x, y + r, x - r * 0.28, y + r * 0.28, x - r, y, x - r * 0.28, y - r * 0.28, fill=fill, w=0.9)


def chain(a, x0, y0, x1, y1, n, r=3.8, fill=CHR):
    for k in range(n):
        t = k / (n - 1)
        x = x0 + (x1 - x0) * t; y = y0 + (y1 - y0) * t
        cc(a, x, y, r, fill, ry=r * 0.7, w=1.3) if k % 2 == 0 else cc(a, x, y, r * 0.7, fill, ry=r, w=1.3)


def tear(a, x, y, s=1.0, fill="#7dd3fc"):
    pg(a, x, y - 6 * s, x + 4 * s, y, x + 3.4 * s, y + 4.2 * s, x, y + 5.6 * s, x - 3.4 * s, y + 4.2 * s, x - 4 * s, y, fill=fill, w=1.2)


@st("corazon-roto", "Corazón roto", "Broken heart")
def _(a):
    heart(a, 40, 34, 30, NEON); shine(a, 22, 22, 4, 2)
    a._add([(41, 15), (36, 27), (45, 35), (37, 47), (43, 56), (40, 64)], WH, 3.8)
    a._add([(41, 15), (36, 27), (45, 35), (37, 47), (43, 56), (40, 64)], OL, 1.6)
    rr(a, 47, 32, 60, 44, 2, "#fde68a", w=1.4)
    for x, y in ((50, 35), (57, 41)): ln(a, x - 2, y - 2, x + 2, y + 2, w=1.4); ln(a, x - 2, y + 2, x + 2, y - 2, w=1.4)
    tear(a, 24, 52, 0.9)


@st("corazon-candado", "Corazón con candado", "Locked heart")
def _(a):
    heart(a, 40, 34, 30, RED); shine(a, 22, 22, 4, 2)
    chain(a, 10, 22, 70, 46, 7)
    arc(a, 40, 50, 6.5, 180, 360, color=OL, w=4.4); arc(a, 40, 50, 6.5, 180, 360, color=CHR, w=2.2)
    rr(a, 31, 50, 49, 66, 3, ORO); cc(a, 40, 57, 2.2, K, w=0.4); ln(a, 40, 58, 40, 62, color=K, w=1.6)


@st("murcielago", "Murciélago", "Bat")
def _(a):
    for s in (-1, 1):
        pg(a, 40 + s * 4, 34, 40 + s * 18, 18, 40 + s * 33, 22, 40 + s * 37, 32, 40 + s * 31, 42, 40 + s * 26, 38, 40 + s * 21, 50, 40 + s * 14, 42, 40 + s * 8, 52, fill=K)
        ln(a, 40 + s * 8, 34, 40 + s * 30, 26, color=NEON, w=1.2); ln(a, 40 + s * 10, 40, 40 + s * 24, 40, color=NEON, w=1.2)
    pg(a, 30, 24, 28, 10, 36, 20, fill=K); pg(a, 50, 24, 52, 10, 44, 20, fill=K)
    pg(a, 30.5, 21, 29.7, 14, 34, 19.5, fill=NEON, w=0.5); pg(a, 49.5, 21, 50.3, 14, 46, 19.5, fill=NEON, w=0.5)
    cc(a, 40, 36, 13, K)
    eyes(a, 40, 34, 6, 2.8, "big", NEON)
    pg(a, 36, 41, 38, 46, 39.4, 41.4, fill=WH, w=0.8); pg(a, 44, 41, 42, 46, 40.6, 41.4, fill=WH, w=0.8)
    shine(a, 33, 28, 3, 1.2)


@st("calavera", "Calavera linda", "Cute skull")
def _(a):
    rr(a, 29, 48, 51, 68, 5, WH); cc(a, 40, 34, 22, WH)
    for x in (34, 40, 46): ln(a, x, 56, x, 68, w=1.2)
    ln(a, 29, 60, 51, 60, w=1.2)
    for x in (30, 50): cc(a, x, 35, 6.4, K, w=0.8); heart(a, x, 35, 4.4, NEON)
    pg(a, 40, 43, 37, 49, 43, 49, fill=K, w=0.8)
    shine(a, 28, 22, 3.2, 1.4)
    pg(a, 56, 16, 50, 6, 51, 22, fill=NEON); pg(a, 56, 16, 70, 8, 68, 24, fill=NEON); cc(a, 56, 16, 3.6, "#be185d", w=1.4)
    blush(a, 40, 46, 17, 2.6, ROSA)


@st("estrella-cadenas", "Estrella con cadenas", "Star with chains")
def _(a):
    star(a, 40, 42, 33, NEON); shine(a, 30, 26, 3, 1.6)
    chain(a, 8, 62, 72, 24, 7)
    sparkle(a, 66, 62, 8); sparkle(a, 12, 20, 6, ORO); sparkle(a, 70, 10, 4)


@st("rayo", "Rayo", "Lightning")
def _(a):
    bolt(a, 40, 40, 36, NEON); sparkle(a, 14, 18, 7); sparkle(a, 66, 62, 6, ORO); sparkle(a, 66, 14, 4)
    bolt(a, 40, 40, 20, "#fde047")


@st("flama-rosa", "Flama rosa", "Pink flame")
def _(a):
    pg(a, 40, 4, 50, 20, 60, 34, 64, 50, 56, 66, 40, 75, 24, 66, 16, 50, 21, 36, 30, 26, 32, 40, 38, 24, fill=NEON)
    pg(a, 40, 34, 48, 46, 52, 58, 46, 68, 40, 71, 33, 68, 28, 58, 32, 46, fill="#f9a8d4", w=1.2)
    face(a, 40, 56, "dot", "smile", 6, 2.4, my=62, cheeks=True)


@st("mariposa", "Mariposa Y2K", "Y2K butterfly")
def _(a):
    for s in (-1, 1):
        pg(a, 40 + s * 3, 36, 40 + s * 28, 8, 40 + s * 36, 22, 40 + s * 30, 40, fill=ROSA)
        pg(a, 40 + s * 3, 42, 40 + s * 30, 46, 40 + s * 24, 68, 40 + s * 4, 56, fill=MOR)
        cc(a, 40 + s * 22, 24, 5, WH, w=1.2); cc(a, 40 + s * 22, 24, 2.2, NEON, w=0.6)
        arc(a, 40 + s * 16, 56, 6, 200, 340, color=WH, w=1.6)
        ln(a, 40 + s * 8, 40, 40 + s * 26, 18, color=WH, w=1.2)
    rr(a, 37, 24, 43, 66, 3, K)
    arc(a, 36, 22, 8, 200, 330, color=OL, w=1.6); arc(a, 44, 22, 8, 210, 340, color=OL, w=1.6)
    sparkle(a, 10, 66, 5, ORO); sparkle(a, 70, 70, 4)


@st("tijeras", "Tijeras", "Scissors")
def _(a):
    for x0, x1 in ((56, 26), (24, 54)):
        ln(a, x0, 52, x1, 6, color=OL, w=7); ln(a, x0, 52, x1, 6, color=CHR, w=4.4)
    for x in (24, 56): cc(a, x, 62, 10, NEON); cc(a, x, 62, 4.6, WH, w=1.4)
    cc(a, 40, 36, 2.6, "#64748b", w=1.2); sparkle(a, 66, 16, 5, ORO)


@st("esposas", "Esposas rosa", "Pink cuffs")
def _(a):
    for x in (24, 56): cc(a, x, 44, 16, NEON); cc(a, x, 44, 8.4, WH, w=1.4); rr(a, x - 5, 22, x + 5, 30, 2, "#be185d", w=1.4)
    for k in range(3): cc(a, 40, 44 + (k - 1) * 0, 0.1, CHR, w=0.1)
    cc(a, 40, 44, 5, CHR, ry=3.2, w=1.4)
    for x, y in ((16, 38), (30, 50), (50, 38), (64, 50)): a.circle(x, y, 1.6, color=WH, fill=True)


@st("labios", "Labios", "Lips")
def _(a):
    pg(a, 6, 40, 20, 26, 32, 28, 40, 34, 48, 28, 60, 26, 74, 40, 40, 44, fill=RED)
    pg(a, 6, 40, 40, 44, 74, 40, 62, 60, 40, 66, 18, 60, fill=NEON)
    ln(a, 6, 40, 40, 44, 74, 40, w=1.8); shine(a, 28, 54, 6, 2); shine(a, 22, 31, 4, 1.2)


@st("gafas", "Gafas oscuras", "Dark shades", 80, 40)
def _(a):
    for x0 in (5, 43): rr(a, x0, 8, x0 + 32, 32, 9, K)
    ln(a, 37, 14, 43, 14, w=3.2); ln(a, 5, 14, 1, 10, w=2.4); ln(a, 75, 14, 79, 10, w=2.4)
    for x0 in (5, 43):
        ln(a, x0 + 8, 12, x0 + 18, 12, color=NEON, w=1.4); shine(a, x0 + 10, 14, 4, 1.4); a.circle(x0 + 24, 24, 2, color=MOR, fill=True)


@st("corona", "Corona", "Crown")
def _(a):
    pg(a, 10, 62, 8, 26, 24, 42, 40, 14, 56, 42, 72, 26, 70, 62, fill=ORO)
    rr(a, 9, 58, 71, 68, 2, "#f59e0b")
    for x, y, c in ((8, 24, NEON), (40, 12, NEON), (72, 24, NEON)): cc(a, x, y, 3.8, c, w=1.4)
    cc(a, 40, 46, 4.6, RED, w=1.3); cc(a, 22, 51, 3, MOR, w=1.2); cc(a, 58, 51, 3, MOR, w=1.2); shine(a, 30, 38, 3, 1.2)


@st("cadena-oro", "Cadena dorada", "Gold chain", 100, 40)
def _(a):
    for k in range(6):
        x = 10 + k * 16
        if k % 2 == 0: cc(a, x, 20, 11, ORO, ry=7.4, w=1.8); cc(a, x, 20, 5.5, WH, ry=2.8, w=0.1); a.circle(x, 20, 5.5, color=OL, w=1.1, ry=2.8)
        else: cc(a, x, 20, 7.4, ORO, ry=11, w=1.8); a.circle(x, 20, 3, color=OL, w=1.1, ry=6)
    shine(a, 12, 15, 3, 1)


@st("ojo-lagrima", "Ojo con lágrima", "Teary eye")
def _(a):
    top = [(8 + 64 * k / 20, 36 - 22 * math.sin(math.pi * k / 20)) for k in range(21)]
    bot = [(72 - 64 * k / 20, 36 + 16 * math.sin(math.pi * k / 20)) for k in range(21)]
    a._add(top + bot, WH, 1, True); a._add(top + bot, OL, 2.2)
    cc(a, 40, 36, 13, MOR); cc(a, 40, 36, 6, K, w=0.8); a.circle(35, 31, 2.6, color=WH, fill=True)
    for x, y, x2, y2 in ((16, 28, 10, 20), (28, 18, 24, 8), (52, 18, 56, 8), (64, 28, 70, 20)): ln(a, x, y, x2, y2, w=2)
    tear(a, 52, 60, 1.5)


@st("gotas", "Gotas negras", "Black drips")
def _(a):
    rr(a, 6, 6, 74, 18, 5, K)
    for x, hh in ((14, 34), (26, 22), (38, 50), (50, 28), (62, 40)):
        a.rect(x - 4, 14, x + 4, 14 + hh, color=K, fill=True); cc(a, x, 14 + hh, 4.8, K, w=0.8)
        ln(a, x - 1.8, 24, x - 1.8, 10 + hh, color=NEON, w=1.2)
    shine(a, 20, 10, 5, 1.2)


@st("mano-paz", "Mano de paz", "Peace hand")
def _(a):
    skin = "#fcd5b5"
    rr(a, 26, 40, 58, 74, 11, skin)
    rr(a, 29, 6, 39, 46, 5, skin); rr(a, 43, 8, 53, 46, 5, skin)
    rr(a, 53, 38, 62, 56, 4, skin); rr(a, 58, 42, 66, 58, 4, skin)
    rr(a, 18, 50, 32, 62, 5, skin)
    for x in (29, 43): pg(a, x + 1.2, 6.8, x + 8.8, 6.8, x + 8.8, 17, x + 1.2, 17, fill=NEON, w=1.2)
    a.rect(30, 44, 38, 47, color=skin, fill=True)
    ln(a, 41, 46, 41, 38, color=OL, w=1.2)
    cc(a, 36, 66, 3, ORO, w=1.2)


@st("cruz", "Cruz gótica", "Gothic cross")
def _(a):
    rr(a, 32, 6, 48, 74, 4, NEON); rr(a, 14, 22, 66, 38, 4, NEON)
    rr(a, 35, 9, 45, 71, 3, K); rr(a, 17, 25, 63, 35, 3, K)
    cc(a, 40, 30, 4.4, RED, w=1.3); shine(a, 39, 28, 1.4, 1.4)
    for x, y in ((40, 8), (40, 72), (16, 30), (64, 30)): heart(a, x, y, 3.4, NEON) if False else cc(a, x, y, 2.4, NEON, w=1.1)


@st("telarana", "Telaraña", "Cobweb")
def _(a):
    g = "#64748b"
    for k in range(8):
        t = math.radians(45 * k); ln(a, 40, 40, 40 + 34 * math.cos(t), 40 + 34 * math.sin(t), color=g, w=1.4)
    for r in (10, 20, 30):
        pts = []
        for k in range(9):
            t = math.radians(45 * k); rr_ = r * (0.86 if k % 1 == 0 and k < 8 else 1.0)
            pts.append((40 + rr_ * math.cos(t), 40 + rr_ * math.sin(t)))
        a._add(pts, g, 1.4)
    ln(a, 56, 56, 66, 70, color=OL, w=1)
    cc(a, 66, 70, 5, K, w=1.2); eyes(a, 66, 69, 2, 1.3, "dot", NEON)
    for s in (-1, 1):
        for dy in (-3, 0, 3): ln(a, 66 + s * 4, 70 + dy * 0.6, 66 + s * 10, 70 + dy * 2.2, w=1.2)
    pg(a, 66, 64, 62, 60, 70, 60, fill=NEON, w=1)


@st("luna-triste", "Luna triste", "Sad moon")
def _(a):
    outer = [(44 + 30 * math.cos(math.radians(t)), 40 + 30 * math.sin(math.radians(t))) for t in range(35, 326, 10)]
    inner = [(54 + 25 * math.cos(math.radians(t)), 40 + 25 * math.sin(math.radians(t))) for t in range(320, 40, -10)]
    pts = outer + inner
    a._add(pts, ORO, 1, True); a._add(pts, OL, 1.8)
    eyes(a, 24, 38, 0, 0, "dot") if False else None
    cc(a, 22, 34, 2.4, OL, w=0.4); a.circle(21.4, 33.4, 0.8, color=WH, fill=True)
    frown(a, 24, 46, 4, 1.8); tear(a, 28, 42, 0.8); blush(a, 24, 40, 0, 0) if False else None
    sparkle(a, 62, 18, 6, ORO); sparkle(a, 68, 56, 4, LILA); sparkle(a, 58, 40, 3, WH)


@st("gato-negro", "Gato negro", "Black cat")
def _(a):
    arc(a, 58, 60, 13, -90, 70, color=OL, w=8); arc(a, 58, 60, 13, -90, 70, color=K, w=5.6)
    cc(a, 40, 56, 19, K, ry=17); cc(a, 40, 30, 16, K)
    pg(a, 26, 24, 24, 8, 36, 17, fill=K); pg(a, 54, 24, 56, 8, 44, 17, fill=K)
    pg(a, 27, 21, 26, 12, 33, 18, fill=ROSA, w=0.5); pg(a, 53, 21, 54, 12, 47, 18, fill=ROSA, w=0.5)
    for x in (33, 47): cc(a, x, 30, 4.4, ORO, w=1); a.rect(x - 0.7, 26.4, x + 0.7, 33.6, color=K, fill=True)
    pg(a, 40, 36, 37.6, 33.6, 42.4, 33.6, fill=NEON, w=0.8)
    for s in (-1, 1):
        for dy in (-2, 2): ln(a, 40 + s * 7, 36 + dy * 0.4, 40 + s * 17, 36 + dy * 2, color=CHR, w=1)
    arc(a, 40, 40, 14, 200, 340, color=NEON, w=3.4, ry=3)
    heart(a, 40, 47, 3.4, ORO)
    rr(a, 29, 70, 37, 76, 3, K, w=1.2); rr(a, 43, 70, 51, 76, 3, K, w=1.2)


@st("ataud", "Ataúd rosa", "Pink coffin")
def _(a):
    pg(a, 31, 6, 49, 6, 63, 30, 53, 74, 27, 74, 17, 30, fill=NEON)
    pg(a, 34, 12, 46, 12, 56, 31, 48, 68, 32, 68, 24, 31, fill="#f9a8d4", w=1.2)
    heart(a, 40, 42, 11, K); sparkle(a, 36, 36, 3); shine(a, 28, 26, 2, 4)


def banner(a, text, bg, fg, size=11.0, border=None):
    rr(a, 2, 2, a.w - 2, a.h - 2, 8, bg, w=1.8)
    if border: rr(a, 5, 5, a.w - 5, a.h - 5, 5, bg, w=0.1); a.round_rect(5, 5, a.w - 5, a.h - 5, 5, color=border, w=1.0)
    a.text(a.w / 2 - len(text) * size * 0.29, a.h / 2 - size * 0.62, text, size, fg)


@st("te-amo-pero-no", "«Te amo pero no»", "Banner: love you but no", 110, 30)
def _(a): banner(a, "te amo pero no", K, "#ffffff", 11.0, NEON)


@st("sad-era", "«Sad era»", "Banner: sad era", 90, 30)
def _(a): banner(a, "sad era", NEON, K, 12.0); star(a, 12, 15, 4.2, "#ffffff"); star(a, 78, 15, 4.2, "#ffffff")


@st("perreo", "«Perreo»", "Banner: perreo", 86, 40)
def _(a):
    pg(a, 20, 30, 14, 38, 30, 30, fill=MOR, w=1.4); rr(a, 2, 2, 84, 31, 13, MOR, w=1.8)
    a.text(43 - 6 * 14 * 0.29, 16.5 - 14 * 0.62, "perreo", 14.0, "#ffffff"); sparkle(a, 10, 10, 4, ORO); sparkle(a, 76, 22, 3.4, ORO)


@st("modo-on", "«Modo calavera on»", "Banner: skull mode on", 110, 30)
def _(a):
    rr(a, 2, 2, 108, 28, 8, K, w=1.8)
    a.text(8, 8.6, "modo", 11.0, "#ffffff"); a.text(80, 8.6, "on", 11.0, NEON)
    cc(a, 55, 14, 8, WH, w=1.2); rr(a, 51, 18, 59, 26, 2, WH, w=1.2)
    for x in (52, 58): cc(a, x, 13, 2.4, K, w=0.4)
    pg(a, 55, 17, 54, 19, 56, 19, fill=K, w=0.5)


@st("no-me-hablen", "«No me hablen»", "Banner: don't talk to me", 112, 34)
def _(a):
    rr(a, 2, 2, 110, 32, 8, "#ffffff", w=1.8); a.round_rect(5, 5, 107, 29, 5, color=NEON, w=1.2)
    a.text(56 - 12 * 11 * 0.29, 17 - 11 * 0.62, "no me hablen", 11.0, K)
    cc(a, 12, 17, 3.6, NEON, w=1.2); cc(a, 100, 17, 3.6, NEON, w=1.2)


@st("mono", "Moño negro", "Black bow")
def _(a):
    pg(a, 40, 40, 8, 18, 6, 62, fill=K); pg(a, 40, 40, 72, 18, 74, 62, fill=K)
    ln(a, 12, 28, 30, 38, color=NEON, w=1.2); ln(a, 12, 52, 30, 44, color=NEON, w=1.2); ln(a, 68, 28, 50, 38, color=NEON, w=1.2); ln(a, 68, 52, 50, 44, color=NEON, w=1.2)
    pg(a, 36, 52, 30, 74, 38, 68, fill=K); pg(a, 44, 52, 50, 74, 42, 68, fill=K)
    cc(a, 40, 40, 8, K); cc(a, 40, 40, 3, NEON, w=1); shine(a, 37, 36, 2, 1.2)


@st("rosa-negra", "Rosa negra", "Black rose")
def _(a):
    ln(a, 40, 40, 40, 76, color=OL, w=5); ln(a, 40, 40, 40, 76, color="#166534", w=3)
    pg(a, 40, 62, 56, 52, 58, 64, fill="#22c55e"); pg(a, 40, 54, 24, 46, 22, 58, fill="#22c55e")
    cc(a, 40, 28, 22, K); cc(a, 31, 26, 11, "#1f2937", w=1.2); cc(a, 49, 26, 11, "#1f2937", w=1.2); cc(a, 40, 36, 11, "#1f2937", w=1.2)
    arc(a, 40, 28, 12, 20, 340, color=NEON, w=1.6); arc(a, 40, 28, 6, 30, 330, color=NEON, w=1.4); a.circle(40, 28, 1.6, color=NEON, fill=True)
    shine(a, 28, 16, 3, 1.4); sparkle(a, 66, 14, 4, NEON)


@st("casete", "Casete", "Cassette")
def _(a):
    rr(a, 6, 16, 74, 64, 5, K); rr(a, 12, 22, 68, 42, 3, "#ffffff", w=1.3)
    a.rect(14, 24, 66, 29, color=NEON, fill=True)
    for x in (28, 52): cc(a, x, 34, 5, K, w=1.2); cc(a, x, 34, 2, "#ffffff", w=0.8)
    ln(a, 28, 34, 52, 34, color="#94a3b8", w=1)
    pg(a, 20, 64, 26, 50, 54, 50, 60, 64, fill="#475569", w=1.4)
    for x in (32, 40, 48): cc(a, x, 57, 1.6, K, w=0.5)
    cc(a, 14, 58, 1.6, "#94a3b8", w=0.6); cc(a, 66, 58, 1.6, "#94a3b8", w=0.6); heart(a, 40, 47, 2.4, NEON) if False else None
    ln(a, 18, 44, 38, 44, color=NEON, w=1.2)


@st("vinilo", "Disco de vinilo", "Vinyl record")
def _(a):
    cc(a, 40, 40, 33, K)
    for r in (28, 23, 18): a.circle(40, 40, r, color="#374151", w=0.9)
    arc(a, 40, 40, 26, 200, 260, color=WH, w=1.4); arc(a, 40, 40, 26, 20, 80, color=WH, w=1.4)
    cc(a, 40, 40, 12, NEON); a.circle(40, 40, 1.8, color=WH, fill=True)
    eyes(a, 40, 36, 4.4, 1.5, "dot"); smile(a, 40, 39, 3.2, 1.4)


@st("audifonos", "Audífonos", "Headphones")
def _(a):
    arc(a, 40, 40, 26, 180, 360, color=OL, w=9, n=18); arc(a, 40, 40, 26, 180, 360, color=K, w=6, n=18)
    for x in (12, 68):
        rr(a, x - 8, 38, x + 8, 66, 6, K); rr(a, x - 5, 42, x + 5, 62, 4, NEON, w=1.2)
    heart(a, 12, 52, 3.6, "#ffffff"); heart(a, 68, 52, 3.6, "#ffffff"); shine(a, 40, 16, 8, 1.2)
    sparkle(a, 40, 62, 5, ORO)


@st("camara", "Cámara desechable", "Disposable camera")
def _(a):
    rr(a, 6, 24, 74, 66, 7, ROSA); rr(a, 6, 24, 74, 36, 6, NEON)
    rr(a, 12, 14, 28, 24, 3, "#e5e7eb"); rr(a, 52, 16, 66, 24, 2, "#fde68a")
    cc(a, 40, 47, 14, K); cc(a, 40, 47, 9, MOR, w=1.2); cc(a, 40, 47, 4, K, w=0.8); a.circle(36, 43, 2.4, color=WH, fill=True)
    cc(a, 15, 30, 2.4, WH, w=1); rr(a, 58, 40, 68, 46, 2, "#e5e7eb", w=1.2)
    for x in (14, 20, 26): ln(a, x, 58, x, 62, color=K, w=1.2)
    sparkle(a, 66, 12, 5, ORO); sparkle(a, 14, 8, 3, WH)
