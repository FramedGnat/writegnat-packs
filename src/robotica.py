import math
from wgpack import Pack

pack = Pack("robotica", "Robótica y mecatrónica", "Articulaciones, brazos editables, robots móviles, sensores, transmisiones y formulario de cinemática, dinámica y control.",
            "Ingenierías", "🤖", en={"Robótica y mecatrónica": "Robotics and mechatronics",
            "Articulaciones, brazos editables, robots móviles, sensores, transmisiones y formulario de cinemática, dinámica y control.":
            "Joints, editable arms, mobile robots, sensors, transmissions and formulas for kinematics, dynamics and control."})
P = pack
JNT, ARM, MOB, MEC = "Robótica: articulaciones", "Robótica: brazos y efectores", "Robótica: móviles y sensores", "Mecatrónica: transmisión"
P.en.update({JNT: "Robotics: joints", ARM: "Robotics: arms and end effectors", MOB: "Robotics: mobile and sensors", MEC: "Mechatronics: transmission"})

def deg(a): return math.radians(a)

# --- Articulaciones ----------------------------------------------------------------------------

@P.figure(JNT, "joint-revolute", "Articulación rotacional", "Revolute joint")
def _(g):
    g.line(0, 0, 0.35, 0); g.circle(0.5, 0, 0.15); g.circle(0.5, 0, 0.03, fill=True); g.line(0.65, 0, 1, 0)
    g.arc(0.5, 0, 0.24, 0.24, 40, 140)
    g.head(0.5 + 0.24 * math.cos(deg(130)), 0.24 * math.sin(deg(130)), 0.5 + 0.24 * math.cos(deg(140)), 0.24 * math.sin(deg(140)), 0.05)

@P.figure(JNT, "joint-revolute-3d", "Rotacional (3D)", "Revolute (3D)")
def _(g):
    g.line(0, 0, 0.35, 0); g.ellipse(0.5, 0.12, 0.15, 0.05); g.ellipse(0.5, -0.12, 0.15, 0.05)
    g.line(0.35, 0.12, 0.35, -0.12); g.line(0.65, 0.12, 0.65, -0.12); g.line(0.5, -0.12, 0.5, -0.3); g.line(0.5, -0.3, 1, -0.3)

@P.figure(JNT, "joint-prismatic", "Articulación prismática", "Prismatic joint")
def _(g): g.line(0, 0, 0.2, 0); g.rect(0.2, -0.12, 0.6, 0.12); g.rect(0.4, -0.05, 1, 0.05, fill=True); g.double_arrow(0.45, 0.22, 0.9, 0.22, 0.05)

@P.figure(JNT, "joint-spherical", "Articulación esférica", "Spherical joint")
def _(g):
    g.line(0, 0, 0.32, 0); g.arc(0.5, 0, 0.18, 0.18, 40, 320); g.circle(0.5, 0, 0.12)
    g.arc(0.5, 0, 0.12, 0.05, 180, 360, dashed=True); g.line(0.62, 0, 1, 0)

@P.figure(JNT, "joint-cylindrical", "Articulación cilíndrica", "Cylindrical joint")
def _(g):
    g.line(0, 0, 0.2, 0); g.rect(0.2, -0.12, 0.6, 0.12); g.rect(0.4, -0.05, 1, 0.05)
    g.double_arrow(0.45, 0.24, 0.9, 0.24, 0.05); g.arc(0.8, 0, 0.05, 0.15, 100, 260)
    g.head(0.8 + 0.05 * math.cos(deg(250)), 0.15 * math.sin(deg(250)), 0.8 + 0.05 * math.cos(deg(260)), 0.15 * math.sin(deg(260)), 0.04)

@P.figure(JNT, "joint-universal", "Junta universal", "Universal joint")
def _(g):
    g.line(0, 0, 0.3, 0); g.line(0.42, 0.15, 0.3, 0.15, 0.3, -0.15, 0.42, -0.15)
    g.circle(0.5, 0, 0.1); g.line(0.43, 0.07, 0.57, -0.07); g.line(0.43, -0.07, 0.57, 0.07)
    g.line(0.58, 0.15, 0.7, 0.15, 0.7, -0.15, 0.58, -0.15); g.line(0.7, 0, 1, 0)

@P.figure(JNT, "joint-helical", "Articulación helicoidal", "Helical joint")
def _(g):
    g.line(0, 0, 0.2, 0); g.rect(0.2, -0.1, 0.8, 0.1)
    for k in range(9): u = 0.24 + k * 0.065; g.line(u, -0.1, u + 0.04, 0.1)
    g.line(0.8, 0, 1, 0)

@P.figure(JNT, "joint-planar", "Articulación plana", "Planar joint")
def _(g): g.rect(0.1, -0.2, 0.9, -0.1); g.rect(0.3, -0.1, 0.7, 0.1); g.double_arrow(0.3, 0.2, 0.7, 0.2, 0.04); g.double_arrow(0.8, 0.15, 0.8, -0.05, 0.03)

@P.figure(JNT, "link", "Eslabón", "Link")
def _(g):
    g.arc(0.1, 0, 0.1, 0.1, 90, 270); g.line(0.1, -0.1, 0.9, -0.1); g.arc(0.9, 0, 0.1, 0.1, -90, 90); g.line(0.9, 0.1, 0.1, 0.1)
    g.circle(0.1, 0, 0.04); g.circle(0.9, 0, 0.04)

@P.figure(JNT, "link-ternary", "Eslabón ternario", "Ternary link")
def _(g):
    g.poly(0.1, -0.1, 0.9, -0.1, 0.5, 0.55); g.circle(0.18, -0.03, 0.04); g.circle(0.82, -0.03, 0.04); g.circle(0.5, 0.45, 0.04)

@P.figure(JNT, "base", "Base fija", "Fixed base")
def _(g): g.rect(0.3, 0, 0.7, 0.18); g.hatch(0.15, 0.85, 0, 6, 0.07); g.line(0.5, 0.18, 0.5, 0.45)

@P.figure(JNT, "four-bar", "Mecanismo de cuatro barras", "Four-bar linkage")
def _(g):
    g.hatch(-0.05, 0.15, -0.05, 3, 0.05); g.hatch(0.85, 1.05, -0.05, 3, 0.05)
    a, b, c, d = (0.05, 0), (0.25, 0.4), (0.8, 0.5), (0.95, 0)
    g.line(*a, *b); g.line(*b, *c); g.line(*c, *d)
    for p in (a, b, c, d): g.circle(p[0], p[1], 0.03)
    g.line(0.05, 0, 0.95, 0, dashed=True)

@P.figure(JNT, "slider-crank", "Biela-manivela", "Slider–crank")
def _(g):
    g.circle(0.15, 0, 0.03); g.hatch(0.05, 0.25, -0.05, 3, 0.05); g.line(0.15, 0, 0.3, 0.2); g.circle(0.3, 0.2, 0.025)
    g.line(0.3, 0.2, 0.75, 0); g.rect(0.7, -0.07, 0.85, 0.07); g.line(0.5, -0.07, 1, -0.07); g.line(0.5, 0.07, 1, 0.07, dashed=True)

# --- Brazos y efectores ----------------------------------------------------------------------------

P.robot(ARM, "arm-2r", "Brazo de 2 GDL", 2, "2-DOF arm")
P.robot(ARM, "arm-3r", "Brazo de 3 GDL", 3, "3-DOF arm")

@P.figure(ARM, "gripper", "Pinza (efector final)", "Gripper (end effector)")
def _(g): g.line(0, 0, 0.5, 0); g.line(0.5, -0.25, 0.5, 0.25); g.line(0.5, 0.25, 0.95, 0.25, 0.95, 0.15); g.line(0.5, -0.25, 0.95, -0.25, 0.95, -0.15)

@P.figure(ARM, "gripper-parallel", "Pinza paralela", "Parallel gripper")
def _(g):
    g.line(0, 0, 0.35, 0); g.rect(0.35, -0.3, 0.5, 0.3); g.rect(0.5, 0.15, 0.9, 0.25); g.rect(0.5, -0.25, 0.9, -0.15)
    g.double_arrow(0.7, 0.05, 0.7, -0.05, 0.03)

@P.figure(ARM, "suction", "Ventosa", "Suction cup")
def _(g): g.line(0, 0, 0.6, 0); g.line(0.6, -0.08, 0.6, 0.08); g.poly(0.6, 0.08, 0.85, 0.22, 0.85, -0.22, 0.6, -0.08)

@P.figure(ARM, "tool-weld", "Herramienta (soldadura)", "Tool (welding)")
def _(g): g.line(0, 0, 0.5, 0); g.rect(0.5, -0.08, 0.7, 0.08); g.line(0.7, 0, 0.95, -0.15); g.line(0.97, -0.2, 1.0, -0.26); g.line(0.94, -0.22, 0.92, -0.28)

@P.figure(ARM, "frame", "Marco de coordenadas", "Coordinate frame")
def _(g):
    g.circle(0, 0, 0.025, fill=True); g.arrow(0, 0, 0.7, 0); g.arrow(0, 0, 0, 0.7); g.arrow(0, 0, -0.4, -0.4)
    g.label(0.78, -0.06, "x"); g.label(-0.06, 0.78, "z"); g.label(-0.48, -0.36, "y")

@P.figure(ARM, "frame-2d", "Marco 2D", "2D frame")
def _(g): g.circle(0, 0, 0.025, fill=True); g.arrow(0, 0, 0.7, 0); g.arrow(0, 0, 0, 0.7); g.label(0.78, -0.06, "x"); g.label(-0.06, 0.78, "y")

@P.figure(ARM, "dh-frames", "Marcos de Denavit-Hartenberg", "Denavit–Hartenberg frames")
def _(g):
    g.circle(0, 0, 0.02, fill=True); g.arrow(0, 0, 0.35, 0, 0.04); g.arrow(0, 0, 0, 0.35, 0.04); g.label(0.38, -0.05, "x₀", 0.6); g.label(-0.06, 0.38, "z₀", 0.6)
    g.line(0, 0, 0.6, 0.3, dashed=True); g.label(0.3, 0.2, "a₁", 0.6)
    g.circle(0.6, 0.3, 0.02, fill=True); g.arrow(0.6, 0.3, 0.92, 0.46, 0.04); g.arrow(0.6, 0.3, 0.6, 0.65, 0.04)
    g.label(0.96, 0.44, "x₁", 0.6); g.label(0.54, 0.68, "z₁", 0.6)

@P.figure(ARM, "scara", "Robot SCARA", "SCARA robot")
def _(g):
    g.rect(0, -0.4, 0.15, 0.3); g.hatch(-0.05, 0.2, -0.4, 3, 0.05); g.rect(0.05, 0.3, 0.55, 0.4); g.circle(0.5, 0.35, 0.04)
    g.rect(0.5, 0.2, 0.9, 0.3); g.circle(0.85, 0.25, 0.04); g.line(0.85, 0.2, 0.85, -0.15); g.double_arrow(0.95, 0.1, 0.95, -0.1, 0.03)

@P.figure(ARM, "cartesian", "Robot cartesiano", "Cartesian robot")
def _(g):
    g.rect(0, 0.4, 1, 0.48); g.line(0.05, 0.4, 0.05, -0.3); g.line(0.95, 0.4, 0.95, -0.3); g.rect(0.45, 0.3, 0.6, 0.4)
    g.rect(0.5, -0.15, 0.55, 0.3); g.double_arrow(0.25, 0.55, 0.75, 0.55, 0.03); g.double_arrow(0.65, 0.2, 0.65, -0.05, 0.03)

# --- Móviles y sensores ------------------------------------------------------------------------------

@P.figure(MOB, "diff-drive", "Robot diferencial", "Differential-drive robot")
def _(g):
    g.circle(0.5, 0, 0.3); g.rect(0.42, 0.26, 0.58, 0.36, fill=True); g.rect(0.42, -0.36, 0.58, -0.26, fill=True)
    g.arrow(0.5, 0, 0.75, 0, 0.04); g.circle(0.5, 0, 0.015, fill=True); g.label(0.72, 0.08, "v", 0.6)
    g.double_arrow(0.3, 0.4, 0.3, -0.4, 0.03); g.label(0.24, 0.0, "L", 0.6)

@P.figure(MOB, "car-like", "Robot tipo auto", "Car-like robot")
def _(g):
    g.rect(0.1, -0.25, 0.9, 0.25); g.rect(0.18, 0.25, 0.32, 0.32, fill=True); g.rect(0.18, -0.32, 0.32, -0.25, fill=True)
    g.poly(0.7, 0.27, 0.82, 0.31, 0.8, 0.36, 0.68, 0.32, fill=True); g.poly(0.7, -0.33, 0.82, -0.29, 0.8, -0.24, 0.68, -0.28, fill=True)
    g.arrow(0.5, 0, 0.8, 0, 0.04)

@P.figure(MOB, "omni-wheel", "Rueda omnidireccional", "Omni wheel")
def _(g):
    g.circle(0.5, 0, 0.3); g.circle(0.5, 0, 0.05)
    for k in range(8): a = k * math.pi / 4; c, s = math.cos(a), math.sin(a); g.ellipse(0.5 + 0.3 * c, 0.3 * s, 0.05, 0.05)

@P.figure(MOB, "wheel", "Rueda", "Wheel")
def _(g):
    g.circle(0.5, 0, 0.35); g.circle(0.5, 0, 0.06)
    for k in range(6): a = k * math.pi / 3; g.line(0.5 + 0.06 * math.cos(a), 0.06 * math.sin(a), 0.5 + 0.33 * math.cos(a), 0.33 * math.sin(a))

@P.figure(MOB, "quadruped", "Robot cuadrúpedo", "Quadruped robot")
def _(g):
    g.rect(0.15, 0.1, 0.85, 0.3)
    for x in (0.22, 0.4, 0.62, 0.8):
        g.line(x, 0.1, x + 0.08, -0.12, x, -0.35); g.circle(x, 0.1, 0.02, fill=True); g.circle(x + 0.08, -0.12, 0.02, fill=True)
    g.rect(0.85, 0.2, 0.97, 0.32)

@P.figure(MOB, "biped-leg", "Pierna de robot", "Robot leg")
def _(g):
    g.circle(0.1, 0.4, 0.04); g.line(0.1, 0.4, 0.35, 0.05); g.circle(0.35, 0.05, 0.04); g.line(0.35, 0.05, 0.25, -0.35)
    g.circle(0.25, -0.35, 0.04); g.line(0.15, -0.42, 0.45, -0.42)

@P.figure(MOB, "ultrasonic", "Sensor ultrasónico", "Ultrasonic sensor")
def _(g):
    g.rect(0, -0.2, 0.3, 0.2); g.circle(0.15, 0.09, 0.06); g.circle(0.15, -0.09, 0.06)
    for r in (0.2, 0.32, 0.44): g.arc(0.3, 0, r, r, -25, 25)

@P.figure(MOB, "lidar", "LiDAR", "LiDAR")
def _(g):
    g.rect(0.35, -0.15, 0.55, 0.15); g.ellipse(0.45, 0.15, 0.1, 0.04)
    for a in (-30, -15, 0, 15, 30): r = deg(a); g.line(0.55, 0, 0.55 + 0.45 * math.cos(r), 0.45 * math.sin(r), dashed=True)

@P.figure(MOB, "camera", "Cámara", "Camera")
def _(g): g.rect(0.2, -0.2, 0.65, 0.2); g.poly(0.65, -0.1, 0.85, -0.2, 0.85, 0.2, 0.65, 0.1); g.circle(0.35, 0.28, 0.06)

@P.figure(MOB, "encoder", "Encoder", "Encoder")
def _(g):
    g.circle(0.5, 0, 0.3); g.circle(0.5, 0, 0.04, fill=True)
    for k in range(12): a = k * math.pi / 6; g.line(0.5 + 0.22 * math.cos(a), 0.22 * math.sin(a), 0.5 + 0.3 * math.cos(a), 0.3 * math.sin(a))

@P.figure(MOB, "imu", "IMU (acelerómetro y giroscopio)", "IMU (accelerometer and gyroscope)")
def _(g): g.rect(0.25, -0.25, 0.75, 0.25); g.arrow(0.5, 0, 0.7, 0, 0.03); g.arrow(0.5, 0, 0.5, 0.2, 0.03); g.label(0.5, -0.15, "IMU", 0.6)

# --- Transmisión -----------------------------------------------------------------------------------------

@P.figure(MEC, "motor", "Motor", "Motor")
def _(g): g.line(0, 0, 0.3, 0); g.circle(0.5, 0, 0.2); g.label(0.5, 0, "M"); g.line(0.7, 0, 1, 0)

@P.figure(MEC, "servo", "Servomotor", "Servo motor")
def _(g): g.rect(0.2, -0.2, 0.75, 0.2); g.circle(0.35, 0.2, 0.06); g.line(0.35, 0.26, 0.35, 0.45); g.line(0.2, 0.45, 0.5, 0.45); g.label(0.55, 0, "servo", 0.5)

@P.figure(MEC, "stepper", "Motor a pasos", "Stepper motor")
def _(g): g.line(0, 0, 0.3, 0); g.circle(0.5, 0, 0.2); g.label(0.5, 0.04, "M", 0.8); g.line(0.42, -0.1, 0.46, -0.1, 0.46, -0.06, 0.54, -0.06, 0.54, -0.1, 0.58, -0.1); g.line(0.7, 0, 1, 0)

@P.figure(MEC, "gear", "Engrane", "Gear")
def _(g):
    pts = []
    for k in range(48): a = 2 * math.pi * k / 48; r = 0.5 if (k // 2) % 2 == 0 else 0.4; pts += [0.5 + r * math.cos(a), r * math.sin(a)]
    g.poly(*pts); g.circle(0.5, 0, 0.1)

@P.figure(MEC, "gear-pair", "Par de engranes", "Gear pair")
def _(g):
    g.circle(0.3, 0, 0.28); g.circle(0.3, 0, 0.24, dashed=True); g.circle(0.3, 0, 0.03, fill=True)
    g.circle(0.72, 0, 0.18); g.circle(0.72, 0, 0.14, dashed=True); g.circle(0.72, 0, 0.03, fill=True)
    g.label(0.3, -0.35, "N₁", 0.6); g.label(0.72, -0.26, "N₂", 0.6)

@P.figure(MEC, "belt", "Banda y poleas", "Belt and pulleys")
def _(g):
    g.circle(0.2, 0, 0.18); g.circle(0.8, 0, 0.1); g.circle(0.2, 0, 0.02, fill=True); g.circle(0.8, 0, 0.02, fill=True)
    g.line(0.2, 0.18, 0.8, 0.1); g.line(0.2, -0.18, 0.8, -0.1)

@P.figure(MEC, "rack-pinion", "Piñón y cremallera", "Rack and pinion")
def _(g):
    g.circle(0.5, 0.25, 0.2); g.circle(0.5, 0.25, 0.03, fill=True)
    pts = [0, -0.05]
    for k in range(10): x = 0.05 + k * 0.1; pts += [x - 0.03, -0.05, x - 0.02, 0.02, x + 0.02, 0.02, x + 0.03, -0.05]
    pts += [1, -0.05]; g.line(*pts); g.line(0, -0.15, 1, -0.15); g.double_arrow(0.2, -0.25, 0.8, -0.25, 0.03)

@P.figure(MEC, "ball-screw", "Husillo de bolas", "Ball screw")
def _(g):
    g.line(0, 0, 0.1, 0); g.rect(0.1, -0.05, 0.95, 0.05)
    for k in range(14): u = 0.12 + k * 0.06; g.line(u, -0.05, u + 0.04, 0.05)
    g.rect(0.45, -0.15, 0.65, 0.15); g.double_arrow(0.4, 0.25, 0.7, 0.25, 0.03)

@P.figure(MEC, "bearing", "Rodamiento", "Bearing")
def _(g):
    g.circle(0.5, 0, 0.35); g.circle(0.5, 0, 0.15)
    for k in range(10): a = k * math.pi / 5; g.circle(0.5 + 0.25 * math.cos(a), 0.25 * math.sin(a), 0.055)

@P.figure(MEC, "piston-cyl", "Cilindro neumático", "Pneumatic cylinder")
def _(g):
    g.rect(0.05, -0.15, 0.6, 0.15); g.line(0.35, -0.15, 0.35, 0.15); g.rect(0.35, -0.03, 0.95, 0.03, fill=True)
    g.line(0.12, 0.15, 0.12, 0.3); g.line(0.52, 0.15, 0.52, 0.3)

@P.figure(MEC, "cam", "Leva y seguidor", "Cam and follower")
def _(g):
    g.polar(0.5, -0.1, lambda t: 0.2 + 0.14 * max(0.0, math.cos(t - math.pi / 2)) ** 2)
    g.circle(0.5, -0.1, 0.03, fill=True); g.line(0.5, 0.22, 0.5, 0.55); g.rect(0.45, 0.4, 0.55, 0.5)

# --- Fórmulas ------------------------------------------------------------------------------------------------

G = "Ingenierías"
P.formulas_in(G, "Robótica: cinemática", [
    ("Rotación en x", r"R_{x}(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}", "Rotation about x"),
    ("Rotación en y", r"R_{y}(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}", "Rotation about y"),
    ("Rotación en z", r"R_{z}(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}", "Rotation about z"),
    ("Transformación homogénea", r"T = \begin{pmatrix} R & \vec{p} \\ 0 & 1 \end{pmatrix}", "Homogeneous transformation"),
    ("Inversa de una transformación", r"T^{-1} = \begin{pmatrix} R^{T} & -R^{T} \vec{p} \\ 0 & 1 \end{pmatrix}", "Inverse transformation"),
    ("Denavit-Hartenberg", r"{}^{i-1}T_{i} = R_{z}(\theta_{i}) \, T_{z}(d_{i}) \, T_{x}(a_{i}) \, R_{x}(\alpha_{i})", "Denavit–Hartenberg"),
    ("Cadena cinemática", r"{}^{0}T_{n} = {}^{0}T_{1} \, {}^{1}T_{2} \cdots {}^{n-1}T_{n}", "Kinematic chain"),
    ("Directa 2R (x)", r"x = l_{1} \cos\theta_{1} + l_{2} \cos(\theta_{1} + \theta_{2})", "Forward 2R (x)"),
    ("Directa 2R (y)", r"y = l_{1} \sin\theta_{1} + l_{2} \sin(\theta_{1} + \theta_{2})", "Forward 2R (y)"),
    ("Inversa 2R (codo)", r"\cos\theta_{2} = \frac{x^{2} + y^{2} - l_{1}^{2} - l_{2}^{2}}{2 l_{1} l_{2}}", "Inverse 2R (elbow)"),
    ("Inversa 2R (hombro)", r"\theta_{1} = \operatorname{atan2}(y, x) - \operatorname{atan2}(l_{2} \sin\theta_{2}, \, l_{1} + l_{2} \cos\theta_{2})", "Inverse 2R (shoulder)"),
    ("Cinemática diferencial", r"\dot{\vec{x}} = J(\vec{q}) \, \dot{\vec{q}}", "Differential kinematics"),
    ("Jacobiano 2R", r"J = \begin{pmatrix} -l_{1} s_{1} - l_{2} s_{12} & -l_{2} s_{12} \\ l_{1} c_{1} + l_{2} c_{12} & l_{2} c_{12} \end{pmatrix}", "2R Jacobian"),
    ("Singularidad", r"\det J(\vec{q}) = 0", "Singularity"),
    ("Grados de libertad (Grübler)", r"M = 6(n - 1) - \sum_{i=1}^{j} (6 - f_{i})", "Degrees of freedom (Grübler)"),
    ("Grübler plano", r"M = 3(n - 1) - 2 j_{1} - j_{2}", "Planar Grübler"),
    ("Cuaternión de rotación", r"q = \cos\frac{\theta}{2} + \hat{u} \sin\frac{\theta}{2}", "Rotation quaternion"),
], "Robotics: kinematics")
P.formulas_in(G, "Robótica: dinámica y móviles", [
    ("Dinámica del manipulador", r"M(q)\ddot{q} + C(q, \dot{q})\dot{q} + g(q) = \tau", "Manipulator dynamics"),
    ("Lagrangiano", r"\frac{d}{dt} \frac{\partial L}{\partial \dot{q}_{i}} - \frac{\partial L}{\partial q_{i}} = \tau_{i}, \quad L = K - U", "Lagrangian"),
    ("Estática", r"\vec{\tau} = J^{T}(\vec{q}) \, \vec{F}", "Statics"),
    ("Energía cinética de un eslabón", r"K = \frac{1}{2} m v_{c}^{T} v_{c} + \frac{1}{2} \omega^{T} I \omega", "Link kinetic energy"),
    ("Robot diferencial (v)", r"v = \frac{r (\omega_{R} + \omega_{L})}{2}", "Differential robot (v)"),
    ("Robot diferencial (ω)", r"\omega = \frac{r (\omega_{R} - \omega_{L})}{L}", "Differential robot (ω)"),
    ("Modelo uniciclo", r"\dot{x} = v \cos\theta, \; \dot{y} = v \sin\theta, \; \dot{\theta} = \omega", "Unicycle model"),
    ("Odometría", r"\theta_{k+1} = \theta_{k} + \omega \, \Delta t", "Odometry"),
    ("Relación de engranes", r"\frac{\omega_{1}}{\omega_{2}} = \frac{N_{2}}{N_{1}} = \frac{\tau_{2}}{\tau_{1}}", "Gear ratio"),
    ("Par de un motor DC", r"\tau = K_{t} \, i, \quad e = K_{e} \, \omega", "DC motor torque"),
    ("Resolución de un encoder", r"\Delta\theta = \frac{360^{\circ}}{4 N}", "Encoder resolution"),
], "Robotics: dynamics and mobile")
P.formulas_in(G, "Control y señales", [
    ("Función de transferencia", r"G(s) = \frac{Y(s)}{U(s)}", "Transfer function"),
    ("Lazo cerrado", r"T(s) = \frac{G(s)}{1 + G(s) H(s)}", "Closed loop"),
    ("Segundo orden", r"G(s) = \frac{\omega_{n}^{2}}{s^{2} + 2 \zeta \omega_{n} s + \omega_{n}^{2}}", "Second order"),
    ("Sobreimpulso", r"M_{p} = e^{-\pi \zeta / \sqrt{1 - \zeta^{2}}}", "Overshoot"),
    ("Tiempo de establecimiento", r"t_{s} \approx \frac{4}{\zeta \omega_{n}}", "Settling time"),
    ("Error en estado estable", r"e_{ss} = \lim_{s \to 0} \frac{s R(s)}{1 + G(s) H(s)}", "Steady-state error"),
    ("Control PID", r"u(t) = K_{p} e(t) + K_{i} \int_{0}^{t} e(\tau) d\tau + K_{d} \frac{de}{dt}", "PID control"),
    ("PID en Laplace", r"C(s) = K_{p} + \frac{K_{i}}{s} + K_{d} s", "PID in Laplace"),
    ("PID discreto", r"u_{k} = K_{p} e_{k} + K_{i} T \sum_{j=0}^{k} e_{j} + \frac{K_{d}}{T} (e_{k} - e_{k-1})", "Discrete PID"),
    ("Espacio de estados", r"\dot{x} = A x + B u, \quad y = C x + D u", "State space"),
    ("Controlabilidad", r"\mathcal{C} = \begin{pmatrix} B & AB & \cdots & A^{n-1}B \end{pmatrix}", "Controllability"),
    ("Transformada de Fourier", r"X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j \omega t} dt", "Fourier transform"),
    ("Transformada Z", r"X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}", "Z-transform"),
    ("Convolución", r"(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) d\tau", "Convolution"),
    ("Nyquist", r"f_{s} \ge 2 f_{max}", "Nyquist"),
    ("Filtro de Kalman (ganancia)", r"K_{k} = P_{k}^{-} H^{T} (H P_{k}^{-} H^{T} + R)^{-1}", "Kalman filter (gain)"),
], "Control and signals")

P.labels = [["Eslabón", "#2563eb"], ["Articulación", "#7c3aed"], ["Efector final", "#16a34a"], ["Base", "#334155"],
            ["Sensor", "#0891b2"], ["Actuador", "#dc2626"], ["Controlador", "#ea580c"], ["GDL", "#be185d"]]
P.en.update({"Eslabón": "Link", "Articulación": "Joint", "Efector final": "End effector", "Actuador": "Actuator", "Controlador": "Controller", "GDL": "DOF"})
P.emoji = {"Robótica": "🤖 🦾 🦿 ⚙️ 🔩 🔧 🛠️ 🔋 📡 🎮 🕹️ 🛞 🚗 🛸 🧠 💻"}
