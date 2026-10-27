"""Piezas compartidas por las plantillas y los stickers de varios paquetes."""
import math

M = 36.0          # margen de la hoja (pt)
W, H = 595.0, 842.0


def header(a, title, fields):
    a.title(M, M - 2, title)
    a.fields(M, M + 44, W - M, fields)
    return M + 58


def title_block(a, x0, y0, x1, y1, rows=("Proyecto", "Contenido", "Escala", "Fecha", "Lámina")):
    """Cuadro de datos de lámina (esquina inferior derecha)."""
    a.rect(x0, y0, x1, y1, w=1.2)
    rh = (y1 - y0) / len(rows)
    for i, r in enumerate(rows):
        if i: a.line(x0, y0 + i * rh, x1, y0 + i * rh, w=0.6)
        a.text(x0 + 4, y0 + i * rh + 3, r, 7.5)


def lab_report(a, title, table_headers, extra_sections=()):
    """Reporte de laboratorio: cabecera, objetivo, material, procedimiento, tabla de datos, gráfica y conclusiones."""
    y = header(a, title, ["Práctica", "Nombre", "Grupo", "Fecha"])
    a.section(M, y, W / 2 - 4, y + 110, "Objetivo"); a.section(W / 2 + 4, y, W - M, y + 110, "Material")
    y += 118
    a.section(M, y, W - M, y + 150, "Procedimiento"); y += 158
    for name, hgt in extra_sections:
        a.section(M, y, W - M, y + hgt, name); y += hgt + 8
    a.text(M, y, "Tabla de datos", 9.0); y += 14
    a.table(M, y, W / 2 + 40, y + 190, [1] * len(table_headers), 10, table_headers); 
    a.rect(W / 2 + 48, y, W - M, y + 190, w=0.7); a.text(W / 2 + 52, y + 4, "Gráfica", 9.0)
    a.grid(W / 2 + 56, y + 18, W - M - 8, y + 182, 14.17)
    y += 198
    a.section(M, y, W - M, H - M, "Resultados y conclusiones")


def badge(a, text, fill, fg="#ffffff", size=11.0):
    """Insignia redondeada con texto (sticker)."""
    a.round_rect(2, 2, a.w - 2, a.h - 2, (a.h - 4) / 2, color=fill, w=1.0, fill=True)
    a.text(a.w / 2 - len(text) * size * 0.29, a.h / 2 - size * 0.62, text, size, fg)


def diamond_sign(a, glyph, label=None, border="#dc2626"):
    """Pictograma en rombo rojo (estilo de seguridad de laboratorio)."""
    c = a.w / 2
    a.poly(c, 2, a.w - 2, c, c, a.w - 2, 2, c, color="#ffffff", w=0.5, fill=True)
    a.poly(c, 2, a.w - 2, c, c, a.w - 2, 2, c, color=border, w=3.2)
    a.text(c - 9, c - 13, glyph, 20.0, "#111111")
    if label: a.text(c - len(label) * 2.3, a.w + 1, label, 7.5, "#111111")   # debajo del rombo


def gear(a, cx, cy, r, color, teeth=10):
    pts = []
    for k in range(teeth * 4):
        t = 2 * math.pi * k / (teeth * 4); rr = r if (k // 2) % 2 == 0 else r * 0.8
        pts += [cx + rr * math.cos(t), cy + rr * math.sin(t)]
    a.poly(*pts, color=color, w=0.6, fill=True); a.circle(cx, cy, r * 0.3, color="#ffffff", w=0.5, fill=True)
