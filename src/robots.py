import math
from wgpack import Pack
from _draw import *

pack = Pack("robots", "Robots y máquinas", "26 robots con personalidad: amigos, cíclopes, drones, rovers, brazos, perros robot y cuadrúpedos, listos para decorar tus apuntes.",
            "General", "🤖", en={"Robots y máquinas": "Robots and machines",
            "26 robots con personalidad: amigos, cíclopes, drones, rovers, brazos, perros robot y cuadrúpedos, listos para decorar tus apuntes.":
            "26 robots with personality: friends, cyclops, drones, rovers, arms, robot dogs and quadrupeds, ready to decorate your notes."})
P = pack
S = 80.0


def bot(a, body, accent, head="box", eye="dot", mouth="smile", ant="ball", loco="legs", chest="heart", arms="down", cheeks=False, eyecol=OL):
    # antena
    if ant in ("ball", "bulb"):
        ln(a, 40, 11, 40, 5, w=1.8); cc(a, 40, 4.2, 2.8, accent if ant == "ball" else "#fde047", w=1.4)
    elif ant == "double":
        ln(a, 33, 12, 30, 5, w=1.8); ln(a, 47, 12, 50, 5, w=1.8); cc(a, 30, 4.4, 2.2, accent, w=1.3); cc(a, 50, 4.4, 2.2, accent, w=1.3)
    elif ant == "dish":
        ln(a, 40, 11, 40, 6, w=1.8); a.poly(34, 3, 46, 3, 40, 8, color=accent, fill=True); a.poly(34, 3, 46, 3, 40, 8, color=OL, w=1.3)
    # brazos (detrás del cuerpo)
    for s in (-1, 1):
        if arms == "down": p = (40 + s * 13, 43, 40 + s * 22, 56)
        elif arms == "up": p = (40 + s * 13, 43, 40 + s * 21, 33)
        elif arms == "wave" and s == 1: p = (53, 43, 62, 31)
        else: p = (40 + s * 13, 43, 40 + s * 21, 55)
        ln(a, *p, color=OL, w=5.8); ln(a, *p, color=body, w=3.6); cc(a, p[2], p[3], 3.1, accent, w=1.4)
    # locomoción
    if loco == "legs":
        for s in (-1, 1):
            rr(a, 40 + s * 9 - 3, 62, 40 + s * 9 + 3, 72, 2, body, w=1.4); rr(a, 40 + s * 9 - 5.5, 71, 40 + s * 9 + 5.5, 76, 2, accent, w=1.4)
    elif loco == "wheel":
        cc(a, 40, 69, 8, "#475569"); cc(a, 40, 69, 3, "#cbd5e1", w=1.2)
    elif loco == "tracks":
        rr(a, 24, 63, 56, 76, 6.5, "#475569"); 
        for x in (31, 40, 49): cc(a, x, 69.5, 3, "#cbd5e1", w=1.1)
    elif loco == "hover":
        pg(a, 33, 64, 47, 64, 43, 78, 37, 78, fill="#fb923c", w=1.2); pg(a, 36.5, 64, 43.5, 64, 41, 74, 39, 74, fill="#fde047", w=0.8)
    # cuerpo
    rr(a, 37, 36, 43, 40, 1, "#94a3b8", w=1.3)
    rr(a, 27, 38, 53, 64, 6, body)
    rr(a, 33, 43, 47, 57, 3, WH, w=1.3)
    if chest == "heart": heart(a, 40, 50, 6.5)
    elif chest == "bolt": bolt(a, 40, 50, 6.5)
    elif chest == "gear": gear(a, 40, 50, 5.6, accent, 6, 0.3)
    elif chest == "star": star(a, 40, 50.5, 6)
    elif chest == "screen":
        a.rect(35, 45, 45, 55, color="#0f172a", fill=True); ln(a, 36.5, 52, 39, 48, 41, 53, 43.5, 47, color="#4ade80", w=1.3)
    elif chest == "dots":
        for k, c in enumerate(("#ef4444", "#fbbf24", "#22c55e")): cc(a, 36.5 + k * 3.5, 50, 1.4, c, w=0.6)
    # cabeza
    if head == "box": rr(a, 23, 10, 57, 37, 8, body)
    elif head == "round": cc(a, 40, 23, 15.5, body)
    elif head == "wide": cc(a, 40, 24, 19, body, ry=13.5)
    elif head == "tv": rr(a, 22, 10, 58, 37, 5, body); rr(a, 26, 13.5, 54, 33.5, 3.5, "#0f172a", w=1.2)
    elif head == "visor": rr(a, 23, 10, 57, 37, 11, body); rr(a, 27, 17, 53, 30, 6.5, "#0f172a", w=1.2)
    shine(a, 29, 14.4, 3.6, 1.2) if head != "tv" else None
    # cara
    if head == "tv": face(a, 40, 22.5, "glow", "smile", 8, 2.3, my=29, col="#4ade80")
    elif head == "visor": eyes(a, 40, 23.5, 8, 2.4, "glow", "#38bdf8"); smile(a, 40, 24.5, 3.4, w=1.4) if mouth == "smile" else None
    else: face(a, 40, 22.5, eye, mouth, 7.5, 2.6, my=29, cheeks=cheeks, col=eyecol)
    for x, y in ((26, 13), (54, 13), (26, 34), (54, 34)): screw(a, x, y) if head == "box" else None


V = [  # id, nombre, inglés, cuerpo, acento, opciones
    ("amigo", "Robot amigo", "Friendly robot", "#93c5fd", "#f97316", dict(head="box", eye="dot", mouth="smile", ant="ball", chest="heart", cheeks=True)),
    ("ciclope", "Robot cíclope", "Cyclops robot", "#a7f3d0", "#ef4444", dict(head="round", eye="dot", mouth="grill", ant="bulb", chest="bolt")),
    ("tele", "Robot pantalla", "Screen robot", "#fca5a5", "#38bdf8", dict(head="tv", ant="dish", chest="screen")),
    ("visor", "Robot con visor", "Visor robot", "#c4b5fd", "#22d3ee", dict(head="visor", ant="double", chest="dots", loco="wheel")),
    ("feliz", "Robot feliz", "Happy robot", "#fde68a", "#ef4444", dict(head="wide", eye="happy", mouth="big", ant="ball", chest="star", arms="up", cheeks=True)),
    ("dormido", "Robot dormido", "Sleepy robot", "#cbd5e1", "#6366f1", dict(head="round", eye="sleep", mouth="flat", ant="bulb", chest="dots", loco="wheel")),
    ("saludo", "Robot saluda", "Waving robot", "#bbf7d0", "#16a34a", dict(head="box", eye="big", mouth="smile", ant="double", chest="heart", arms="wave")),
    ("oruga", "Robot oruga", "Tracked robot", "#fdba74", "#475569", dict(head="box", eye="dot", mouth="grill", ant="dish", chest="gear", loco="tracks")),
    ("jet", "Robot volador", "Flying robot", "#bae6fd", "#f43f5e", dict(head="round", eye="big", mouth="o", ant="ball", chest="bolt", loco="hover", arms="up")),
    ("retro", "Robot retro", "Retro robot", "#d6d3d1", "#b45309", dict(head="box", eye="big", mouth="grill", ant="double", chest="gear")),
    ("curioso", "Robot curioso", "Curious robot", "#f9a8d4", "#7c3aed", dict(head="wide", eye="big", mouth="o", ant="bulb", chest="screen", loco="wheel", cheeks=True)),
    ("serio", "Robot serio", "Serious robot", "#94a3b8", "#0ea5e9", dict(head="visor", ant="dish", chest="dots", loco="tracks")),
    ("enamorado", "Robot enamorado", "Robot in love", "#fecdd3", "#e11d48", dict(head="round", eye="happy", mouth="smile", ant="ball", chest="heart", arms="wave", cheeks=True)),
    ("heroe", "Robot héroe", "Hero robot", "#fca5a5", "#2563eb", dict(head="box", eye="glow", mouth="flat", ant="ball", chest="star", arms="up", eyecol="#38bdf8")),
    ("mini", "Mini robot", "Tiny robot", "#99f6e4", "#f59e0b", dict(head="wide", eye="dot", mouth="smile", ant="bulb", chest="bolt", loco="wheel", cheeks=True)),
    ("estudioso", "Robot estudioso", "Studious robot", "#bfdbfe", "#1d4ed8", dict(head="tv", ant="ball", chest="screen", arms="up")),
]
for sid, name, en, body, acc, kw in V:
    P.sticker("bot-" + sid, name, en, S, S)(lambda a, body=body, acc=acc, kw=kw: bot(a, body, acc, **kw))


@P.sticker("bot-dron", "Dron", "Drone", S, S)
def _(a):
    for s in (-1, 1):
        ln(a, 40 + s * 12, 36, 40 + s * 26, 28, color=OL, w=4.6); ln(a, 40 + s * 12, 36, 40 + s * 26, 28, color="#94a3b8", w=2.6)
        a.circle(40 + s * 26, 24, 12, color="#7dd3fc", fill=True, ry=2.4); a.circle(40 + s * 26, 24, 12, color=OL, w=1.4, ry=2.4); cc(a, 40 + s * 26, 27.5, 2.2, "#475569", w=1.2)
    cc(a, 40, 40, 15, "#fcd34d", ry=11); shine(a, 33, 34, 4, 1.4)
    cc(a, 40, 41, 6.2, "#0f172a", w=1.4); cc(a, 40, 41, 3.1, "#38bdf8", w=1.0); a.circle(39, 40, 0.9, color=WH, fill=True)
    ln(a, 33, 52, 31, 62, w=1.8); ln(a, 47, 52, 49, 62, w=1.8); ln(a, 27, 62, 53, 62, w=2.2)
    a.text(30, 66, "· · ·", 8, "#94a3b8")


@P.sticker("bot-rover", "Rover explorador", "Exploration rover", S, S)
def _(a):
    rr(a, 21, 42, 59, 56, 4, "#e2e8f0"); rr(a, 28, 36, 52, 44, 3, "#cbd5e1")
    a.rect(55, 21, 56.4, 36, color=OL, fill=True); ln(a, 55.7, 36, 55.7, 22, w=2.2); rr(a, 51, 14, 62, 23, 3, "#cbd5e1", w=1.4); cc(a, 56.5, 18.5, 2.6, "#0f172a", w=1.2); a.circle(55.8, 17.8, 0.8, color=WH, fill=True)
    ln(a, 28, 36, 24, 26, w=1.6); a.poly(20, 22, 28, 22, 24, 27, color="#f97316", fill=True); a.poly(20, 22, 28, 22, 24, 27, color=OL, w=1.2)
    for x in (27, 40, 53): cc(a, x, 62, 7, "#475569", w=1.6); cc(a, x, 62, 2.8, "#cbd5e1", w=1.1)
    ln(a, 27, 55, 27, 58, w=1.6); ln(a, 53, 55, 53, 58, w=1.6)
    a.rect(26, 46, 38, 52, color="#1e3a8a", fill=True); a.rect(26, 46, 38, 52, color=OL, w=0.9); ln(a, 32, 46, 32, 52, w=0.8); ln(a, 44, 48, 55, 48, w=1.0); ln(a, 44, 52, 55, 52, w=1.0)


@P.sticker("bot-brazo", "Brazo industrial", "Industrial arm", S, S)
def _(a):
    rr(a, 14, 66, 52, 75, 2, "#475569"); rr(a, 25, 54, 41, 66, 2, "#f59e0b"); cc(a, 33, 52, 7.5, "#fbbf24")
    ln(a, 33, 52, 28, 30, color=OL, w=11); ln(a, 33, 52, 28, 30, color="#fb923c", w=8.4); cc(a, 28, 28, 6.5, "#fbbf24")
    ln(a, 28, 28, 54, 20, color=OL, w=9.4); ln(a, 28, 28, 54, 20, color="#fb923c", w=6.8); cc(a, 54, 20, 5.2, "#fbbf24")
    ln(a, 54, 20, 62, 31, color=OL, w=7); ln(a, 54, 20, 62, 31, color="#94a3b8", w=4.4)
    ln(a, 62, 31, 58, 38, w=2.4); ln(a, 62, 31, 67, 36, w=2.4); screw(a, 33, 52, 1.2); screw(a, 28, 28, 1.2); screw(a, 54, 20, 1.2)
    cc(a, 62, 10, 3, "#ef4444", w=1.3); ln(a, 62, 13, 62, 16, w=1.6)


@P.sticker("bot-perro", "Perro robot", "Robot dog", S, S)
def _(a):
    for x in (24, 31, 51, 58):
        rr(a, x - 2.2, 52, x + 2.2, 70, 2, "#94a3b8", w=1.4); rr(a, x - 3.4, 68, x + 3.4, 73, 2, "#475569", w=1.3)
    rr(a, 20, 38, 62, 56, 7, "#fcd34d"); ln(a, 62, 42, 71, 36, color=OL, w=4.6); ln(a, 62, 42, 71, 36, color="#fcd34d", w=2.6)
    a.rect(28, 42, 52, 52, color="#fde68a", fill=True); a.rect(28, 42, 52, 52, color=OL, w=1.1); heart(a, 40, 47.2, 3.8)
    rr(a, 8, 22, 36, 44, 7, "#fcd34d"); pg(a, 12, 24, 10, 14, 19, 22, fill="#f59e0b", w=1.3); pg(a, 30, 24, 33, 14, 25, 22, fill="#f59e0b", w=1.3)
    cc(a, 14, 37, 3.4, "#0f172a", w=1.2); a.circle(13.2, 36.2, 0.9, color=WH, fill=True)
    cc(a, 22.5, 31, 2.6, OL, w=0.4); cc(a, 31, 31, 2.6, OL, w=0.4); smile(a, 24, 35, 3.5, 1.5)
    ln(a, 36, 41, 44, 41, color="#ef4444", w=2.4)


@P.sticker("bot-cuadrupedo", "Robot cuadrúpedo", "Quadruped robot", S, S)
def _(a):
    for x, s in ((21, 1), (30, -1), (50, 1), (59, -1)):
        ln(a, x, 46, x + s * 6, 58, color=OL, w=6); ln(a, x, 46, x + s * 6, 58, color="#94a3b8", w=3.6)
        ln(a, x + s * 6, 58, x - s * 1, 70, color=OL, w=5.4); ln(a, x + s * 6, 58, x - s * 1, 70, color="#64748b", w=3.2)
        cc(a, x + s * 6, 58, 2.6, "#f97316", w=1.2); cc(a, x - s * 1, 71, 2.2, "#1e293b", w=1)
    rr(a, 17, 34, 63, 50, 6, "#38bdf8"); rr(a, 25, 38, 42, 46, 2.5, "#0f172a", w=1.1); ln(a, 27, 43, 31, 40, 35, 44, 40, 39, color="#4ade80", w=1.2)
    for k in range(3): ln(a, 49 + k * 4, 38, 49 + k * 4, 46, color="#0c4a6e", w=1.2)
    rr(a, 60, 30, 74, 42, 4, "#0ea5e9"); cc(a, 69, 35.5, 2.6, "#0f172a", w=1.1); a.circle(68.4, 34.8, 0.8, color=WH, fill=True); ln(a, 68, 28, 68, 22, w=1.6); cc(a, 68, 21, 2, "#ef4444", w=1.1)


@P.sticker("bot-humanoide", "Humanoide", "Humanoid", S, S)
def _(a):
    for s in (-1, 1):
        ln(a, 40 + s * 4, 55, 40 + s * 8, 66, color=OL, w=7.4); ln(a, 40 + s * 4, 55, 40 + s * 8, 66, color="#64748b", w=5)
        ln(a, 40 + s * 8, 66, 40 + s * 9, 76, color=OL, w=6.4); ln(a, 40 + s * 8, 66, 40 + s * 9, 76, color="#94a3b8", w=4); rr(a, 40 + s * 9 - 5, 75, 40 + s * 9 + 5, 79, 1.6, "#334155", w=1.3)
        ln(a, 40 + s * 15, 28, 40 + s * 23, 40, color=OL, w=6.4); ln(a, 40 + s * 15, 28, 40 + s * 23, 40, color="#94a3b8", w=4); cc(a, 40 + s * 23, 42, 3.1, "#334155", w=1.3)
    rr(a, 27, 24, 53, 56, 7, "#e2e8f0"); rr(a, 33, 31, 47, 43, 3, "#0f172a", w=1.2); ln(a, 35, 39, 38, 34, 41, 40, 45, 33, color="#38bdf8", w=1.3)
    ln(a, 33, 50, 47, 50, color="#94a3b8", w=1.4)
    rr(a, 31, 4, 49, 22, 6.5, "#e2e8f0"); rr(a, 34, 9.5, 46, 17, 3.2, "#0f172a", w=1.1); cc(a, 37.2, 13.2, 1.4, "#38bdf8", w=0.6); cc(a, 42.8, 13.2, 1.4, "#38bdf8", w=0.6); rr(a, 37, 21, 43, 25, 1, "#94a3b8", w=1.2)


@P.sticker("bot-esfera", "Robot esfera", "Ball robot", S, S)
def _(a):
    cc(a, 40, 44, 28, "#f8fafc"); a.circle(40, 44, 28, color="#fb923c", ry=9, w=2.4)
    arc(a, 40, 44, 28, 200, 340, color="#fb923c", w=0.1); cc(a, 40, 34, 13, "#0f172a", w=1.4)
    cc(a, 40, 34, 7, "#38bdf8", w=1.2); a.circle(37.8, 31.6, 2, color=WH, fill=True)
    shine(a, 24, 26, 5, 2.2); ln(a, 40, 16, 40, 8, w=1.8); cc(a, 40, 7, 2.8, "#ef4444", w=1.3)
    a.text(31, 53, "BB", 11, "#475569")


@P.sticker("bot-chat", "Robot asistente", "Assistant robot", S, S)
def _(a):
    rr(a, 8, 8, 72, 50, 11, "#e0f2fe"); pg(a, 22, 49, 20, 62, 36, 49, fill="#e0f2fe", w=1.6)
    rr(a, 12, 12, 68, 46, 8, "#e0f2fe", w=0.1)
    face(a, 40, 26, "big", "smile", 11, 2.6, my=36, cheeks=True)
    for x in (18, 62): ln(a, x, 18, x, 22, w=2.4)
    cc(a, 40, 70, 6.5, "#38bdf8", w=1.4); cc(a, 40, 70, 3, "#e0f2fe", w=1.1)
    for x in (22, 58): cc(a, x, 70, 2.2, "#fbbf24", w=1)


@P.sticker("bot-engranes", "Robot de engranes", "Gear robot", S, S)
def _(a):
    gear(a, 24, 30, 15, "#fbbf24", 9, 0.36); gear(a, 53, 22, 12, "#38bdf8", 8, 0.36); gear(a, 52, 52, 18, "#f87171", 10, 0.5)
    cc(a, 52, 52, 8.5, WH, w=1.4); eyes(a, 52, 51, 3.2, 1.7, "dot"); smile(a, 52, 52.5, 2.6, 1.4)
    a.circle(24, 30, 2.4, color="#fef3c7", fill=True); ln(a, 8, 60, 8, 72, w=1.6)


@P.sticker("bot-circuito", "Robot circuito", "Circuit robot", S, S)
def _(a):
    rr(a, 14, 14, 66, 66, 7, "#16a34a"); rr(a, 28, 28, 52, 52, 4, "#1e293b", w=1.4); a.text(33, 35, "CPU", 8, "#a7f3d0")
    for k in range(4):
        ln(a, 32 + k * 5, 28, 32 + k * 5, 20, color="#fbbf24", w=1.6); ln(a, 32 + k * 5, 52, 32 + k * 5, 60, color="#fbbf24", w=1.6)
        ln(a, 28, 32 + k * 5, 20, 32 + k * 5, color="#fbbf24", w=1.6); ln(a, 52, 32 + k * 5, 60, 32 + k * 5, color="#fbbf24", w=1.6)
    for x, y in ((19, 19), (61, 19), (19, 61), (61, 61)): cc(a, x, y, 2.6, "#fde68a", w=1.1)
    eyes(a, 40, 44, 4.6, 1.6, "glow", "#4ade80")
