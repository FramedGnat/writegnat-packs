import math
from wgpack import Pack
from _draw_gen import *

pack = Pack("transporte", "Transporte y ciudad", "Coches, trenes, aviones, barcos, globos, semáforos, edificios y más, todos con su carita.",
            "General", "🚗", en={"Transporte y ciudad": "Transport and city",
            "Coches, trenes, aviones, barcos, globos, semáforos, edificios y más, todos con su carita.":
            "Cars, trains, planes, boats, balloons, traffic lights, buildings and more, all with a little face."})
P = pack
S = 80.0


def st(sid, name, en):
    return P.sticker("transporte-" + sid, name, en, S, S)


def car_front(a, body, sign=None, kind=None):
    rr(a, 8, 54, 18, 69, 3, "#334155", w=1.4); rr(a, 62, 54, 72, 69, 3, "#334155", w=1.4)
    rr(a, 18, 16, 62, 46, 10, body); rr(a, 23, 21, 57, 36, 6, "#bae6fd", w=1.4); shine(a, 32, 25, 4, 1.4)
    rr(a, 10, 36, 70, 64, 9, body)
    cc(a, 24, 47, 6.6, "#ffffff", w=1.5); cc(a, 56, 47, 6.6, "#ffffff", w=1.5)
    cc(a, 25, 48, 3.1, OL, w=0.4); cc(a, 57, 48, 3.1, OL, w=0.4)
    a.circle(24, 46.5, 1, color="#ffffff", fill=True); a.circle(56, 46.5, 1, color="#ffffff", fill=True)
    rr(a, 32, 58, 48, 63, 2, "#f8fafc", w=1.2); smile(a, 40, 51, 4.6, 1.8)
    if sign == "taxi":
        rr(a, 31, 6, 49, 16, 3, "#ffffff", w=1.5); a.text(33.2, 8.6, "TAXI", 6.4, OL)
        for i in range(9): a.poly(11 + i * 6.5, 40, 17.5 + i * 6.5, 40, 17.5 + i * 6.5, 44, 11 + i * 6.5, 44, color=OL if i % 2 == 0 else "#ffffff", fill=True)
    elif sign == "amb":
        rr(a, 28, 6, 52, 16, 3, "#ffffff", w=1.5); rr(a, 38, 8, 42, 14, 0.8, "#ef4444", w=0.1); rr(a, 35, 10, 45, 12, 0.8, "#ef4444", w=0.1)
        cc(a, 24, 11, 3, "#ef4444", w=1.2); cc(a, 56, 11, 3, "#3b82f6", w=1.2); rr(a, 10, 61, 70, 64, 1, "#ef4444", w=0.1)


@st("coche", "Coche", "Car")
def _(a): car_front(a, "#ef4444")


@st("taxi", "Taxi", "Taxi")
def _(a): car_front(a, "#fbbf24", "taxi")


@st("ambulancia", "Ambulancia", "Ambulance")
def _(a): car_front(a, "#f8fafc", "amb")


@st("autobus", "Autobús", "Bus")
def _(a):
    rr(a, 5, 20, 75, 62, 8, "#fbbf24")
    for x in (10, 24, 38, 52): rr(a, x, 26, x + 11, 39, 2.5, "#bae6fd", w=1.4)
    rr(a, 66, 26, 72, 44, 2.5, "#bae6fd", w=1.4); ln(a, 6, 44, 74, 44, color="#f59e0b", w=1.4); shine(a, 14, 30, 3, 1.2)
    face(a, 38, 50, "dot", "smile", 7, 2.3, my=55.6, cheeks=True)
    wheel(a, 22, 62, 8); wheel(a, 58, 62, 8); cc(a, 72, 52, 2.2, "#ffffff", w=1.0)


@st("tren", "Tren", "Train")
def _(a):
    rr(a, 8, 72, 72, 76, 1.5, "#94a3b8", w=1.4)
    for x in (14, 26, 38, 50, 62): ln(a, x, 70, x - 2, 78, color="#64748b", w=1.2)
    rr(a, 18, 10, 62, 68, 14, "#3b82f6"); rr(a, 24, 17, 56, 36, 7, "#bae6fd", w=1.4); shine(a, 32, 21, 4, 1.4)
    rr(a, 18, 40, 62, 43, 1, "#fb923c", w=0.1); cc(a, 40, 13, 3, "#fde047", w=1.3)
    cc(a, 28, 52, 5.6, "#ffffff", w=1.4); cc(a, 52, 52, 5.6, "#ffffff", w=1.4); cc(a, 28.6, 52.6, 2.7, OL, w=0.4); cc(a, 52.6, 52.6, 2.7, OL, w=0.4)
    smile(a, 40, 55, 4.4, 1.8); rr(a, 34, 61, 46, 65, 1.5, "#1e293b", w=0.1)


@st("avion", "Avión", "Plane")
def _(a):
    pg(a, 15, 38, 8, 18, 20, 18, 28, 36, fill="#3b82f6", w=1.6)
    pg(a, 36, 44, 54, 44, 42, 68, 26, 68, fill="#3b82f6", w=1.6)
    cc(a, 38, 40, 32, "#ffffff", ry=11)
    for x in (16, 24, 32): cc(a, x, 37, 2.3, "#bae6fd", w=1.1)
    a._add(ellpts(38, 40, 31, 10, 0, 20, 160, 12), "#bfdbfe", 1.4)
    shine(a, 34, 34, 6, 1.2); face(a, 55, 38, "dot", "smile", 4.2, 1.8, my=44, cheeks=False); blush(a, 55, 42, 9, 1.6)


@st("barco", "Barco", "Ship")
def _(a):
    cc(a, 36, 10, 4.4, "#e2e8f0", w=1.2); cc(a, 31, 6, 3.2, "#e2e8f0", w=1.2)
    rr(a, 33, 14, 45, 31, 2, "#fbbf24"); rr(a, 33, 18, 45, 21, 0.5, "#ef4444", w=0.1)
    rr(a, 22, 30, 58, 46, 2.5, "#f8fafc")
    for x in (29, 51): cc(a, x, 38, 3.2, "#38bdf8", w=1.3)
    pg(a, 8, 46, 72, 46, 62, 66, 18, 66, fill="#dc2626", w=1.8); ln(a, 11, 51, 69, 51, color="#fca5a5", w=1.2)
    face(a, 40, 55, "dot", "smile", 7.5, 2.4, my=60.4, cheeks=False, col="#ffffff")
    for k in range(6): arc(a, 8 + k * 13, 66, 6.5, 180, 360, color="#38bdf8", w=2.6, ry=4)
    rr(a, 0, 68, 80, 78, 0, "#38bdf8", w=0.1)
    for k in range(8): arc(a, 6 + k * 10.5, 68, 5.2, 180, 360, color="#7dd3fc", w=1.6, ry=3)


@st("bici-urbana", "Bicicleta urbana", "City bike")
def _(a):
    for cx in (18, 62): ring(a, cx, 56, 13, "#64748b", 2.4); a.circle(cx, 56, 2, color="#cbd5e1", fill=True)
    for pts in ((18, 56, 36, 56), (36, 56, 30, 34), (30, 34, 54, 40), (36, 56, 54, 40), (54, 40, 62, 56), (18, 56, 30, 34)): thick(a, *pts, color="#14b8a6", w=2.6)
    rr(a, 20, 28, 36, 32, 2, "#92400e", w=1.3); ln(a, 54, 40, 54, 32, 58, 30, w=2.4); cc(a, 36, 56, 3.2, "#fbbf24", w=1.2)
    rr(a, 52, 14, 72, 30, 2.5, "#a16207"); ln(a, 58, 14, 58, 30, color="#78350f", w=0.9); ln(a, 66, 14, 66, 30, color="#78350f", w=0.9)
    cc(a, 62, 10, 3.2, "#f472b6", w=1.2); cc(a, 62, 10, 1.1, "#fde047", w=0.1)
    cc(a, 59, 21, 1.4, OL, w=0.1); cc(a, 65, 21, 1.4, OL, w=0.1); smile(a, 62, 23, 2.6, 1.2)


@st("moto", "Moto", "Scooter")
def _(a):
    wheel(a, 18, 62, 10, "#334155"); wheel(a, 62, 62, 10, "#334155")
    pg(a, 8, 56, 10, 40, 22, 34, 40, 36, 44, 54, 28, 60, fill="#ef4444", w=1.8)
    rr(a, 10, 29, 40, 36, 3.4, "#1e293b", w=1.5); rr(a, 36, 52, 56, 58, 3, "#b91c1c", w=1.6)
    pg(a, 50, 58, 52, 26, 60, 26, 62, 58, fill="#ef4444", w=1.8)
    ln(a, 54, 26, 54, 20, 66, 20, w=2.4); cc(a, 64, 31, 3.8, "#fde047", w=1.4)
    face(a, 27, 46, "dot", "smile", 5, 2.1, my=52, cheeks=False, col="#ffffff"); shine(a, 18, 40, 3, 1.2)


@st("camion", "Camión", "Truck")
def _(a):
    rr(a, 3, 16, 47, 58, 4, "#f8fafc"); ln(a, 4, 48, 46, 48, color="#cbd5e1", w=1.2)
    pg(a, 47, 30, 62, 30, 75, 44, 75, 58, 47, 58, fill="#3b82f6", w=1.8); pg(a, 51, 34, 60, 34, 69, 44, 51, 44, fill="#bae6fd", w=1.3)
    wheel(a, 16, 60, 8); wheel(a, 33, 60, 8); wheel(a, 62, 60, 8); rr(a, 70, 52, 77, 58, 2, "#94a3b8", w=1.3)
    shine(a, 12, 22, 3, 1.2); face(a, 25, 34, "dot", "smile", 7, 2.4, my=41, cheeks=True)


@st("bomberos", "Camión de bomberos", "Fire truck")
def _(a):
    ln(a, 8, 20, 46, 20, w=2); ln(a, 8, 26, 46, 26, w=2)
    for x in range(12, 46, 6): ln(a, x, 20, x, 26, color=OL, w=1.2)
    rr(a, 4, 28, 48, 58, 3, "#ef4444"); rr(a, 48, 24, 75, 58, 6, "#ef4444"); rr(a, 53, 29, 70, 42, 3, "#bae6fd", w=1.4)
    ln(a, 6, 50, 46, 50, color="#ffffff", w=1.8); cc(a, 61, 20, 3, "#3b82f6", w=1.3); rr(a, 55, 22, 67, 25, 1, "#94a3b8", w=1.2)
    wheel(a, 18, 60, 8); wheel(a, 60, 60, 8); cc(a, 14, 38, 5, "#fbbf24", w=1.3); cc(a, 14, 38, 1.8, "#f59e0b", w=0.8)
    face(a, 31, 39, "dot", "smile", 6, 2.2, my=45.5, cheeks=False, col="#ffffff")


@st("helicoptero", "Helicóptero", "Helicopter")
def _(a):
    ln(a, 12, 10, 68, 10, color=OL, w=3); ln(a, 40, 10, 40, 22, w=2.4); cc(a, 40, 10, 2.2, "#94a3b8", w=1.2)
    pg(a, 48, 36, 74, 31, 76, 38, 50, 45, fill="#ef4444", w=1.7); ln(a, 75, 24, 75, 44, color=OL, w=2.2)
    cc(a, 34, 38, 19, "#ef4444"); ln(a, 22, 60, 58, 60, w=2.4); ln(a, 28, 54, 28, 60, w=2); ln(a, 46, 54, 46, 60, w=2)
    cc(a, 29, 35, 11, "#bae6fd", w=1.5); shine(a, 24, 30, 3, 1.4)
    face(a, 29, 36, "dot", "smile", 4.2, 1.8, my=41.5, cheeks=False)


@st("globo", "Globo aerostático", "Hot air balloon")
def _(a):
    ln(a, 29, 53, 34, 62, w=1.5); ln(a, 51, 53, 46, 62, w=1.5); ln(a, 40, 55, 40, 62, w=1.3)
    rr(a, 32, 61, 48, 72, 2.5, "#a16207"); ln(a, 32, 66, 48, 66, color="#78350f", w=1.0)
    a.circle(40, 29, 24, color="#ef4444", fill=True, ry=26); a.circle(40, 29, 15, color="#fde047", fill=True, ry=26)
    a.circle(40, 29, 6.5, color="#ef4444", fill=True, ry=26); a.circle(40, 29, 24, color=OL, w=1.8, ry=26)
    arc(a, 40, 29, 15, -90, 90, color=OL, w=0.1, ry=26); shine(a, 28, 14, 3.4, 1.6)
    face(a, 40, 30, "dot", "smile", 6, 2.3, my=36.5, cheeks=False)


@st("semaforo", "Semáforo", "Traffic light")
def _(a):
    rr(a, 36, 60, 44, 76, 2, "#475569", w=1.6)
    rr(a, 24, 4, 56, 62, 7, "#334155"); shine(a, 30, 10, 2, 5)
    cc(a, 40, 17, 7.4, "#7f1d1d", w=1.4); cc(a, 40, 33, 7.4, "#713f12", w=1.4); cc(a, 40, 49, 7.4, "#22c55e", w=1.4)
    shine(a, 37.6, 46.6, 2.2, 1.2); tiny(a, 40, 49, "dot", "smile", 2.8, 1.1, my=52.4)
    for y in (17, 33): a.circle(40, y, 4, color="#451a1a" if y == 17 else "#422006", fill=True)


@st("alto", "Señal de alto", "Stop sign")
def _(a):
    rr(a, 37, 56, 43, 77, 2, "#94a3b8", w=1.6)
    pts = []
    for k in range(8): t = math.radians(22.5 + 45 * k); pts += [40 + 29 * math.cos(t), 32 + 29 * math.sin(t)]
    pg(a, *pts, fill="#ffffff", w=1.8)
    pts = []
    for k in range(8): t = math.radians(22.5 + 45 * k); pts += [40 + 25 * math.cos(t), 32 + 25 * math.sin(t)]
    a.poly(*pts, color="#ef4444", fill=True)
    face(a, 40, 24, "dot", "flat", 6.4, 2.4, my=31, cheeks=False, col="#ffffff"); a.text(27.5, 36.5, "ALTO", 10.5, "#ffffff")


@st("rascacielos", "Rascacielos", "Skyscraper")
def _(a):
    rr(a, 6, 38, 24, 76, 2, "#cbd5e1"); rr(a, 56, 44, 74, 76, 2, "#cbd5e1")
    for y in (44, 54, 64): rr(a, 10, y, 14, y + 5, 0.6, "#fde68a", w=1.0); rr(a, 16, y, 20, y + 5, 0.6, "#fde68a", w=1.0)
    for y in (50, 60, 70): rr(a, 60, y - 2, 64, y + 3, 0.6, "#fde68a", w=1.0); rr(a, 66, y - 2, 70, y + 3, 0.6, "#fde68a", w=1.0)
    ln(a, 40, 12, 40, 3, w=1.8); cc(a, 40, 3.4, 2, "#ef4444", w=1.0)
    rr(a, 22, 12, 58, 76, 3, "#94a3b8")
    for y in (17, 24): 
        for x in (27, 37, 47): rr(a, x, y, x + 7, y + 4.4, 0.8, "#fde68a", w=1.1)
    for y in (54, 61, 68):
        for x in (27, 37, 47): rr(a, x, y, x + 7, y + 4.4, 0.8, "#fde68a", w=1.1)
    face(a, 40, 37, "dot", "smile", 7, 2.4, my=43, cheeks=True); ln(a, 22, 31, 58, 31, color="#64748b", w=1.2); ln(a, 22, 49, 58, 49, color="#64748b", w=1.2)
    rr(a, 35, 72, 45, 76, 1, "#475569", w=1.2)


@st("casa", "Casa", "House")
def _(a):
    rr(a, 46, 14, 55, 32, 1.5, "#b45309", w=1.6); rr(a, 15, 36, 65, 72, 2, "#fde68a")
    pg(a, 8, 38, 40, 10, 72, 38, fill="#ef4444", w=1.9); ln(a, 14, 36, 66, 36, color=OL, w=1.2)
    for x in (28, 52): cc(a, x, 48, 6.4, "#ffffff", w=1.5); cc(a, x + 0.8, 48.6, 2.9, OL, w=0.4); a.circle(x - 0.2, 47.2, 0.9, color="#ffffff", fill=True)
    rr(a, 34, 57, 46, 72, 2.5, "#92400e", w=1.7); cc(a, 43, 65, 1.1, "#fbbf24", w=0.5); smile(a, 40, 55.6, 3.8, 1.5)
    cc(a, 40, 24, 4.4, "#fef9c3", w=1.4); ln(a, 40, 19.6, 40, 28.4, color=OL, w=1); ln(a, 35.6, 24, 44.4, 24, color=OL, w=1)


@st("tienda", "Tienda", "Shop")
def _(a):
    rr(a, 12, 32, 68, 72, 2, "#fef3c7")
    cols = ("#ef4444", "#ffffff")
    for i in range(6): cc(a, 12 + 4.67 + i * 9.33, 31, 4.67, cols[i % 2], ry=4.8, w=1.5)
    for i in range(6): a.poly(12 + i * 9.33, 17, 12 + (i + 1) * 9.33, 17, 12 + (i + 1) * 9.33, 31, 12 + i * 9.33, 31, color=cols[i % 2], fill=True)
    for i in range(7): ln(a, 12 + i * 9.33, 17, 12 + i * 9.33, 31, w=1.2)
    ln(a, 12, 17, 68, 17, w=1.8); rr(a, 8, 12, 72, 18, 2, "#b91c1c", w=1.5)
    rr(a, 17, 42, 42, 62, 2, "#bae6fd", w=1.6); shine(a, 24, 47, 4, 1.2)
    face(a, 29.5, 52, "dot", "smile", 5, 2, my=58, cheeks=False)
    rr(a, 48, 40, 62, 72, 2, "#92400e", w=1.7); cc(a, 59, 56, 1.1, "#fbbf24", w=0.5); cc(a, 55, 47, 3, "#fde68a", w=1.0)


@st("parque", "Parque", "Park")
def _(a):
    rr(a, 0, 66, 80, 78, 0, "#86efac", w=0.1); ln(a, 0, 66, 80, 66, color=OL, w=1.4)
    rr(a, 44, 44, 54, 68, 2, "#a16207", w=1.7)
    blob(a, circles=[(50, 27, 16), (35, 37, 12.5), (65, 37, 12.5)], fill="#4ade80", w=3.4)
    shine(a, 42, 17, 4, 1.8); face(a, 50, 32, "dot", "smile", 6.4, 2.4, my=38.5, cheeks=True)
    rr(a, 4, 46, 30, 50, 1.5, "#b45309", w=1.5); rr(a, 3, 56, 31, 60, 1.5, "#b45309", w=1.5)
    ln(a, 6, 60, 6, 68, w=1.8); ln(a, 28, 60, 28, 68, w=1.8); ln(a, 7, 50, 7, 56, w=1.6); ln(a, 27, 50, 27, 56, w=1.6)
    cc(a, 64, 62, 2.2, "#f472b6", w=1.0); cc(a, 71, 64, 2, "#fde047", w=1.0); ln(a, 64, 64, 64, 68, color="#16a34a", w=1.2); ln(a, 71, 66, 71, 68, color="#16a34a", w=1.2)


@st("puente", "Puente colgante", "Suspension bridge")
def _(a):
    rr(a, 0, 58, 80, 78, 0, "#7dd3fc", w=0.1)
    for k in range(7): arc(a, 6 + k * 12, 66, 6, 180, 360, color="#38bdf8", w=1.8, ry=3)
    left = [(2, 52), (8, 42), (14, 29), (21, 16)]; mid = [(21, 16), (28, 30), (40, 38), (52, 30), (59, 16)]; right = [(59, 16), (66, 29), (72, 42), (78, 52)]
    for c in (left, mid, right): a._add(c, "#ef4444", 2.2)
    for x in (28, 34, 40, 46, 52): ln(a, x, [30, 35, 38, 35, 30][(x - 28) // 6], x, 52, color="#fca5a5", w=0.9)
    for x in (8, 14): ln(a, x, [42, 29][(x - 8) // 6], x, 52, color="#fca5a5", w=0.9)
    for x in (66, 72): ln(a, x, [29, 42][(x - 66) // 6], x, 52, color="#fca5a5", w=0.9)
    rr(a, 0, 52, 80, 58, 1, "#94a3b8", w=1.4)
    for x in (21, 59): rr(a, x - 3.4, 12, x + 3.4, 62, 1.5, "#ef4444", w=1.7); ln(a, x - 3.4, 22, x + 3.4, 22, w=1.2); ln(a, x - 3.4, 38, x + 3.4, 38, w=1.2)
    cc(a, 70, 14, 5.6, "#fde047", w=1.4)


@st("tren-ligero", "Tren ligero", "Light rail")
def _(a):
    ln(a, 3, 7, 77, 7, color=OL, w=1.6); ln(a, 40, 7, 33, 19, 47, 19, 40, 7, color=OL, w=1.8); ln(a, 30, 19, 50, 19, color=OL, w=2.4)
    rr(a, 6, 22, 74, 60, 9, "#10b981")
    for x in (11, 25, 39, 53): rr(a, x, 27, x + 10, 39, 2.5, "#bae6fd", w=1.4)
    pg(a, 64, 27, 69, 27, 71, 39, 64, 39, fill="#bae6fd", w=1.4); ln(a, 7, 42, 73, 42, color="#047857", w=1.4)
    face(a, 40, 50, "dot", "smile", 7, 2.2, my=55.4, cheeks=True, col="#ffffff")
    wheel(a, 20, 62, 5, "#334155"); wheel(a, 60, 62, 5, "#334155"); ln(a, 2, 68, 78, 68, color="#64748b", w=2); cc(a, 72, 52, 2, "#fde047", w=1.0)


@st("gasolinera", "Gasolinera", "Gas pump")
def _(a):
    a._add([(50, 34), (60, 34), (62, 40), (62, 58)], OL, 5); a._add([(50, 34), (60, 34), (62, 40), (62, 58)], "#475569", 2.8)
    rr(a, 57, 56, 67, 66, 2, "#475569", w=1.6); ln(a, 52, 38, 52, 46, w=2)
    rr(a, 18, 66, 54, 74, 2, "#475569"); rr(a, 22, 8, 50, 68, 4, "#ef4444")
    rr(a, 27, 14, 45, 28, 2.5, "#bbf7d0", w=1.4); a.text(29.5, 17, "00.0", 8, "#166534")
    shine(a, 28, 34, 1.8, 5); face(a, 36, 43, "dot", "smile", 6, 2.3, my=49.4, cheeks=True, col="#ffffff")
    pg(a, 36, 53, 31, 60, 41, 60, fill="#fde68a", w=1.4); cc(a, 36, 60.4, 5, "#fde68a", w=1.4); a.circle(36, 60.4, 3.4, color="#ef4444", fill=True)
