# Complementos de WriteGnat

Paquetes de contenido por área (figuras, fórmulas LaTeX, etiquetas y emojis) que la app
[WriteGnat](https://github.com/FramedGnat) descarga desde **Ajustes › Complementos**.

| Paquete | Área |
|---|---|
| Física | Ciencias |
| Química | Ciencias |
| Biología y salud | Ciencias |
| Electrónica y eléctrica | Ingenierías |
| Robótica y mecatrónica | Ingenierías |
| Ingeniería civil | Ingenierías |
| Industrial y computación | Ingenierías |
| Economía, finanzas y administración | Licenciaturas |
| Arquitectura y dibujo técnico | Licenciaturas |
| Psicología y ciencias sociales | Licenciaturas |

## Formato `.wgpack`

Zip **sólo de datos** (la app no ejecuta nada de un paquete):

- `manifest.json`: `format`, `id`, `name`, `description`, `area`, `icon`, `version`, `counts`.
- `content.json`:
  - `figures`: categorías con figuras. Cada figura son trazos en el marco local de la app
    (`u` a lo largo del arrastre de 0 a 1 y `v` perpendicular), así que giran y escalan al colocarlas.
    `robot: n` crea un brazo editable de n articulaciones.
  - `formulas`: categorías con `[nombre, latex]` y el grupo (`Ciencias`, `Ingenierías`, `Licenciaturas`).
  - `labels`: `[texto, "#rrggbb"]`; `emoji`: categorías con emojis.
  - `templates`: plantillas de página (trazos y textos en pt de la hoja; la app las escala).
  - `stickers`: stickers vectoriales de color (`{p, c, w, f, d}` en pt).
  - `symbols`: símbolos LaTeX de la carrera para el editor de fórmulas.
  - Una categoría de figuras con `"snap": true` es de circuitos: se pega a la rejilla y a las terminales.
- `strings_en.json`: traducciones al inglés de los textos del paquete.

`catalog.json` lista los paquetes con su tamaño y SHA-256; la app verifica la huella al descargar.

## Agregar o cambiar contenido

1. Edita o crea `src/<área>.py` (API `Fig`: `line`, `poly`, `rect`, `arc`, `circle`, `arrow`,
   `hatch`, `curve`, `label`…; ver `wgpack.py`). Sube `version` del paquete si cambias uno publicado.
2. `./build.py` regenera `packs/*.wgpack` y `catalog.json`.
3. Confirma y sube a `main`: la app lo verá en Complementos (y ofrecerá actualizar si subió la versión).
