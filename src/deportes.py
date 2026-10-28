import math
from wgpack import Pack
from _draw_gen import *

pack = Pack("deportes", "Deportes y juegos", "Balones, medallas, raquetas, bicis, dados, cartas, ajedrez y videojuegos con carita para tus apuntes.",
            "General", "⚽", en={"Deportes y juegos": "Sports and games",
            "Balones, medallas, raquetas, bicis, dados, cartas, ajedrez y videojuegos con carita para tus apuntes.":
            "Balls, medals, rackets, bikes, dice, cards, chess and video games with a face for your notes."})
P = pack
S = 80.0


def st(sid, name, en):
    return P.sticker("deportes-" + sid, name, en, S, S)


def seam(a, pts, col, tick=3.0, w=1.6, n=9):
    """Costura con puntadas cruzadas a lo largo de una curva."""
    a._add(pts, col, w)
    for k in range(n):
        t = (k + 0.5) / n * (len(pts) - 1); i = min(int(t), len(pts) - 2); f = t - i
        x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f; y = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f
        dx, dy = pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]; d = math.hypot(dx, dy) or 1
        nx, ny = -dy / d * tick, dx / d * tick
        a.line(x - nx, y - ny, x + nx, y + ny, color=col, w=w)


@st("futbol", "Balón de fútbol", "Soccer ball")
def _(a):
    cc(a, 40, 40, 30, "#ffffff")
    regpoly(a, 40, 24, 8.5, 5, "#1e293b", w=1.2)
    for k in range(5):
        t = math.radians(-90 + 72 * k); ln(a, 40 + 8.5 * math.cos(t), 24 + 8.5 * math.sin(t), 40 + 15 * math.cos(t), 24 + 15 * math.sin(t), w=1.4)
    for x, y in ((15, 44), (65, 44)): regpoly(a, x, y, 6, 5, "#1e293b", rot=0 if x < 40 else 180, w=1.2)
    regpoly(a, 29, 66, 5, 5, "#1e293b", rot=90, w=1.2); regpoly(a, 51, 66, 5, 5, "#1e293b", rot=90, w=1.2)
    shine(a, 28, 18, 4, 1.8); a.circle(40, 40, 30, color=OL, w=1.8)
    face(a, 40, 46, "dot", "smile", 7, 2.6, my=52, cheeks=True)


@st("basquet", "Balón de basquetbol", "Basketball")
def _(a):
    cc(a, 40, 40, 30, "#fb923c")
    ln(a, 11, 40, 28, 40, color="#7c2d12", w=1.8); ln(a, 52, 40, 69, 40, color="#7c2d12", w=1.8)
    a._add([(21, 14), (28, 26), (29, 40), (28, 54), (21, 66)], "#7c2d12", 1.8); a._add([(59, 14), (52, 26), (51, 40), (52, 54), (59, 66)], "#7c2d12", 1.8)
    a._add([(40, 10), (40, 18)], "#7c2d12", 1.8); a._add([(40, 62), (40, 70)], "#7c2d12", 1.8)
    shine(a, 27, 22, 3.6, 1.6); face(a, 40, 40, "dot", "smile", 5.6, 2.5, my=47, cheeks=False)


@st("beisbol", "Pelota de béisbol", "Baseball")
def _(a):
    cc(a, 40, 40, 30, "#ffffff")
    L = [(20, 15), (27, 24), (30, 33), (31, 40), (30, 47), (27, 56), (20, 65)]
    seam(a, L, "#ef4444", 3.2, 1.5, 9); seam(a, [(80 - x, y) for x, y in L], "#ef4444", 3.2, 1.5, 9)
    shine(a, 30, 18, 3.6, 1.6); face(a, 40, 40, "dot", "smile", 5.3, 2.4, my=47)


@st("tenis", "Pelota de tenis", "Tennis ball")
def _(a):
    cc(a, 40, 40, 30, "#bef264")
    for pts in ([(18, 16), (30, 26), (31, 40), (30, 54), (18, 64)], [(62, 16), (50, 26), (49, 40), (50, 54), (62, 64)]):
        a._add(pts, OL, 4.8); a._add(pts, "#ffffff", 2.8)
    shine(a, 28, 20, 3.6, 1.6); face(a, 40, 40, "dot", "smile", 5.2, 2.4, my=47)
    a.circle(40, 40, 30, color=OL, w=1.8)


@st("voleibol", "Balón de voleibol", "Volleyball")
def _(a):
    cc(a, 40, 40, 30, "#ffffff")
    for pts, col in (([(13, 28), (26, 19), (40, 16), (54, 19), (67, 28)], "#3b82f6"), ([(13, 52), (26, 61), (40, 64), (54, 61), (67, 52)], "#fbbf24")):
        a._add(pts, OL, 7.4); a._add(pts, col, 5)
    a._add([(40, 13), (40, 20)], "#3b82f6", 3); a._add([(40, 60), (40, 67)], "#fbbf24", 3)
    shine(a, 28, 28, 3, 1.4); face(a, 40, 40, "dot", "smile", 6, 2.4, my=47, cheeks=True)
    a.circle(40, 40, 30, color=OL, w=1.8)


@st("americano", "Balón de americano", "American football")
def _(a):
    ell(a, 40, 42, 33, 20, -22, "#92400e", 1.8)
    for u in (-21, 21):
        r = math.radians(-22); pts = [(40 + u * math.cos(r) - v * math.sin(r), 42 + u * math.sin(r) + v * math.cos(r)) for v in (-12, 12)]
        a.line(pts[0][0], pts[0][1], pts[1][0], pts[1][1], color="#ffffff", w=2.6)
    r = math.radians(-22)
    def P_(u, v): return (40 + u * math.cos(r) - v * math.sin(r), 42 + u * math.sin(r) + v * math.cos(r))
    p0, p1 = P_(-9, -9), P_(9, -9); a.line(p0[0], p0[1], p1[0], p1[1], color="#ffffff", w=2)
    for u in (-6, -2, 2, 6): q0, q1 = P_(u, -12), P_(u, -6); a.line(q0[0], q0[1], q1[0], q1[1], color="#ffffff", w=1.6)
    shine(a, 28, 36, 5, 1.6); face(a, 40, 47, "dot", "flat", 6, 2.4, my=53, cheeks=False, col="#ffffff"); arc(a, 40, 50, 4.4, 25, 155, color="#ffffff", w=1.8)


@st("raqueta", "Raqueta", "Racket")
def _(a):
    a.circle(40, 30, 21, color="#ffffff", fill=True, ry=25)
    for x in range(26, 55, 7):
        d = math.sqrt(max(0, 1 - ((x - 40) / 21) ** 2)); ln(a, x, 30 - 25 * d, x, 30 + 25 * d, color="#94a3b8", w=0.8)
    for y in range(12, 49, 7):
        d = math.sqrt(max(0, 1 - ((y - 30) / 25) ** 2)); ln(a, 40 - 21 * d, y, 40 + 21 * d, y, color="#94a3b8", w=0.8)
    a.circle(40, 30, 21, color=OL, w=6, ry=25); a.circle(40, 30, 21, color="#ef4444", w=3.6, ry=25)
    pg(a, 33, 52, 47, 52, 43, 62, 37, 62, fill="#ef4444", w=1.5); rr(a, 36, 60, 44, 77, 3, "#92400e", w=1.6)
    a.circle(40, 29, 12, color="#ffffff", fill=True, ry=10); face(a, 40, 28, "dot", "smile", 5.2, 2.3, my=34, cheeks=False)


@st("bici-carreras", "Bici de carreras", "Racing bike")
def _(a):
    for cx in (19, 61): ring(a, cx, 54, 14, "#64748b", 2.4); a.circle(cx, 54, 2, color="#cbd5e1", fill=True)
    for pts in ((19, 54, 38, 54), (38, 54, 34, 33), (34, 33, 55, 33), (38, 54, 55, 33), (19, 54, 34, 33), (55, 33, 61, 54)): thick(a, *pts, color="#ef4444", w=2.6)
    rr(a, 26, 28, 42, 32, 2, "#1e293b", w=1.2); ln(a, 34, 32, 34, 33, w=2)
    ln(a, 55, 33, 55, 26, 61, 24, w=2.4); cc(a, 38, 54, 3.4, "#fbbf24", w=1.3)
    face(a, 43, 42, "dot", "smile", 3.4, 1.4, my=46.5)
    ln(a, 4, 28, 12, 28, color="#94a3b8", w=1.4); ln(a, 2, 36, 10, 36, color="#94a3b8", w=1.4)


@st("patineta", "Patineta", "Skateboard")
def _(a):
    for x in (22, 58):
        rr(a, x - 4, 20, x + 4, 28, 2, "#94a3b8", w=1.3); rr(a, x - 4, 52, x + 4, 60, 2, "#94a3b8", w=1.3)
    rr(a, 6, 28, 74, 52, 12, "#ec4899"); rr(a, 10, 32, 70, 48, 9, "#f472b6", w=1.0)
    for x in (22, 58): cc(a, x, 17, 4, "#fde047", w=1.3); cc(a, x, 63, 4, "#fde047", w=1.3)
    shine(a, 24, 33, 7, 1.2); face(a, 40, 40, "dot", "smile", 6, 2.3, my=45.5, cheeks=True)


@st("pesas", "Pesas", "Dumbbell")
def _(a):
    rr(a, 28, 31, 52, 49, 4, "#cbd5e1")
    for x0, x1 in ((6, 18), (62, 74)): rr(a, x0, 18, x1, 62, 3, "#475569")
    for x0, x1 in ((18, 28), (52, 62)): rr(a, x0, 25, x1, 55, 2.5, "#64748b")
    shine(a, 12, 28, 1.6, 6); shine(a, 68, 28, 1.6, 6)
    face(a, 40, 38, "dot", "smile", 4.6, 1.8, my=44.5)
    ln(a, 8, 66, 18, 66, color="#94a3b8", w=1.4)


@st("medalla", "Medalla", "Medal")
def _(a):
    pg(a, 24, 3, 38, 3, 48, 36, 36, 36, fill="#ef4444", w=1.6); pg(a, 56, 3, 42, 3, 32, 36, 44, 36, fill="#3b82f6", w=1.6)
    cc(a, 40, 53, 21, "#fbbf24"); cc(a, 40, 53, 16, "#fcd34d", w=1.2); shine(a, 30, 42, 4, 1.8)
    face(a, 40, 52, "dot", "smile", 5.6, 2.4, my=58, cheeks=True); star(a, 40, 35, 3.6, "#f59e0b")


@st("copa", "Copa de campeón", "Champion cup")
def _(a):
    for s in (-1, 1):
        arc(a, 40 + s * 19, 24, 9, 90 if s < 0 else 270, 270 if s < 0 else 450, color=OL, w=6); arc(a, 40 + s * 19, 24, 9, 90 if s < 0 else 270, 270 if s < 0 else 450, color="#fbbf24", w=3.4)
    pg(a, 20, 6, 60, 6, 56, 32, 48, 44, 32, 44, 24, 32, fill="#fbbf24", w=1.8)
    rr(a, 35, 43, 45, 56, 2, "#f59e0b", w=1.6); rr(a, 25, 55, 55, 66, 3, "#16a34a"); rr(a, 30, 65, 50, 73, 3, "#15803d")
    pg(a, 20, 66, 12, 60, 14, 70, fill="#4ade80", w=1.1); pg(a, 60, 66, 68, 60, 66, 70, fill="#4ade80", w=1.1)
    shine(a, 29, 14, 2.6, 6); face(a, 40, 24, "dot", "smile", 7, 2.5, my=30.5, cheeks=True)


@st("silbato", "Silbato", "Whistle")
def _(a):
    ring(a, 14, 36, 8, "#ef4444", 2.4)
    rr(a, 26, 28, 76, 44, 6, "#60a5fa"); rr(a, 52, 24, 63, 32, 1.5, "#1e293b", w=1.2)
    cc(a, 38, 52, 19, "#60a5fa"); cc(a, 38, 55, 3.4, "#ffffff", w=1.0)
    shine(a, 30, 42, 4, 1.8); face(a, 38, 50, "dot", "smile", 5.4, 2.3, my=56, cheeks=False)
    ln(a, 66, 18, 72, 12, w=1.4); ln(a, 70, 24, 77, 20, w=1.4)


@st("dado", "Dado", "Die")
def _(a):
    rr(a, 12, 12, 68, 68, 13, "#ffffff"); shine(a, 22, 20, 5, 1.8)
    for x in (29, 51): cc(a, x, 33, 4.6, OL, w=0.4); a.circle(x - 1.4, 31.6, 1.3, color="#ffffff", fill=True)
    smile(a, 40, 45, 9, 2.4); blush(a, 40, 46, 18, 3, "#fb7185")
    cc(a, 20, 60, 2, "#e2e8f0", w=0.8); cc(a, 60, 60, 2, "#e2e8f0", w=0.8)


@st("cartas", "Cartas", "Playing cards")
def _(a):
    rotpoly(a, 46, 40, 38, 54, 18, "#3b82f6", 1.8); rotpoly(a, 46, 40, 30, 46, 18, "#93c5fd", 1.0)
    rotpoly(a, 34, 42, 38, 54, -10, "#ffffff", 1.8)
    heart(a, 34, 44, 16, "#ef4444"); a.text(19, 19, "A", 9, "#ef4444")
    face(a, 34, 42, "dot", "smile", 5.4, 2, my=48, cheeks=False, col="#ffffff")


@st("peon", "Peón de ajedrez", "Chess pawn")
def _(a):
    rr(a, 20, 64, 60, 74, 4, "#e2e8f0"); pg(a, 28, 64, 52, 64, 46, 44, 34, 44, fill="#f1f5f9", w=1.8)
    rr(a, 26, 40, 54, 47, 3.4, "#e2e8f0"); cc(a, 40, 28, 12, "#f1f5f9"); shine(a, 35, 22, 3, 1.5)
    face(a, 40, 28, "dot", "smile", 4.2, 1.8, my=34.4); ln(a, 32, 56, 48, 56, color="#cbd5e1", w=1.2)


@st("rey", "Rey de ajedrez", "Chess king")
def _(a):
    rr(a, 18, 64, 62, 74, 4, "#64748b"); pg(a, 26, 64, 54, 64, 48, 36, 32, 36, fill="#94a3b8", w=1.8)
    rr(a, 24, 33, 56, 40, 3.4, "#64748b"); pg(a, 26, 33, 22, 19, 31, 25, 40, 15, 49, 25, 58, 19, 54, 33, fill="#fbbf24", w=1.7)
    ln(a, 40, 15, 40, 5, w=2.2); ln(a, 35, 9, 45, 9, w=2.2); cc(a, 22, 19, 2, "#f59e0b", w=1.0); cc(a, 58, 19, 2, "#f59e0b", w=1.0)
    face(a, 40, 49, "dot", "smile", 5.4, 2.1, my=56, cheeks=False, col="#ffffff")


@st("come-puntos", "Come-puntos", "Dot muncher")
def _(a):
    pts = [(36, 40)] + [(36 + 28 * math.cos(math.radians(t)), 40 + 28 * math.sin(math.radians(t))) for t in range(38, 323, 10)]
    ps = []
    for x, y in pts: ps += [x, y]
    pg(a, *ps, fill="#fde047", w=1.9)
    cc(a, 36, 23, 3.4, OL, w=0.4); a.circle(35, 22, 1.1, color="#ffffff", fill=True)
    a.circle(20, 44, 3, color="#fb7185", fill=True, ry=2)
    for x in (58, 68, 77): cc(a, x, 40, 2.6, "#fda4af", w=1.1)
    shine(a, 24, 20, 3, 1.4)


@st("control", "Control de videojuegos", "Game controller")
def _(a):
    blob(a, rects=[(8, 22, 72, 52, 14)], circles=[(19, 54, 13), (61, 54, 13)], fill="#6366f1", w=3.4)
    shine(a, 26, 28, 10, 1.4)
    rr(a, 14, 31, 18, 47, 1.5, "#1e293b", w=0.1); rr(a, 11, 36, 27, 42, 1.5, "#1e293b", w=0.1); a.rect(18, 36, 22, 42, color="#1e293b", fill=True)
    rr(a, 18, 30, 24, 48, 1.5, "#1e293b", w=0.1); rr(a, 12, 36, 30, 42, 1.5, "#1e293b", w=0.1)
    for x, y, c in ((62, 31, "#22c55e"), (70, 38, "#ef4444"), (62, 45, "#3b82f6"), (54, 38, "#fbbf24")): cc(a, x, y, 3.6, c, w=1.2)
    face(a, 41, 35, "dot", "smile", 4.6, 1.9, my=41, cheeks=False, col="#ffffff")
    for x in (26, 54): cc(a, x, 57, 4.4, "#312e81", w=1.2)


@st("rompecabezas", "Rompecabezas", "Jigsaw")
def _(a):
    blob(a, rects=[(8, 14, 44, 50, 4)], circles=[(48, 32, 6.5), (26, 54, 6.5)], fill="#3b82f6", w=3.4)
    blob(a, rects=[(40, 38, 72, 70, 4)], circles=[(56, 34, 6), (36, 56, 6)], fill="#f43f5e", w=3.4)
    rr(a, 8, 14, 44, 50, 4, "#3b82f6", w=1.8); cc(a, 48, 32, 6.5, "#3b82f6", w=1.8); cc(a, 26, 54, 6.5, "#3b82f6", w=0.1)
    a.round_rect(8, 14, 44, 50, 4, color="#3b82f6", fill=True)
    shine(a, 16, 20, 4, 1.4); face(a, 26, 32, "dot", "smile", 6, 2.4, my=38.5, cheeks=True)


@st("diana", "Diana", "Target")
def _(a):
    cc(a, 40, 42, 31, "#ef4444"); cc(a, 40, 42, 24, "#ffffff", w=1.4); cc(a, 40, 42, 17, "#ef4444", w=1.4); cc(a, 40, 42, 10, "#ffffff", w=1.4)
    face(a, 40, 42, "dot", "smile", 3.4, 1.4, my=46.5)
    thick(a, 42, 40, 72, 10, color="#92400e", w=2.2)
    pg(a, 66, 6, 74, 4, 76, 12, 70, 10, fill="#3b82f6", w=1.2); pg(a, 70, 14, 74, 16, 76, 12, fill="#3b82f6", w=0.1)
    pg(a, 62, 12, 68, 18, 62, 18, fill="#93c5fd", w=1.0)


@st("yoyo", "Yoyo", "Yo-yo")
def _(a):
    ring(a, 40, 9, 5, "#cbd5e1", 1.8); ln(a, 40, 14, 40, 34, w=1.8)
    cc(a, 40, 53, 22, "#ef4444"); cc(a, 40, 53, 17, "#fca5a5", w=1.2); a.circle(40, 53, 5.2, color="#ffffff", fill=True, w=1.4)
    a.circle(40, 53, 5.2, color=OL, w=1.2); shine(a, 28, 42, 4, 1.8)
    face(a, 40, 55, "dot", "smile", 7, 2.4, my=62, cheeks=False)
    arc(a, 40, 53, 28, 200, 250, color="#94a3b8", w=1.6); arc(a, 40, 53, 28, 290, 340, color="#94a3b8", w=1.6)


@st("pingpong", "Raqueta de ping-pong", "Table tennis paddle")
def _(a):
    thick(a, 52, 54, 66, 72, color="#d97706", w=6.4)
    cc(a, 36, 36, 23, "#ef4444"); a.circle(36, 36, 19, color="#dc2626", w=1.0); a.circle(36, 36, 19, color="#fca5a5", w=0.6)
    shine(a, 24, 24, 4, 1.8); face(a, 36, 36, "dot", "smile", 7, 2.5, my=43, cheeks=True)
    cc(a, 68, 14, 6, "#ffffff", w=1.5); shine(a, 66, 12, 1.8, 1.2); ln(a, 58, 20, 52, 26, color="#94a3b8", w=1.2); ln(a, 62, 24, 58, 30, color="#94a3b8", w=1.2)
