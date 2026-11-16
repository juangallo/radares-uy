# Radares fijos de Uruguay

Listado de radares de fiscalización de velocidad de Uruguay con ubicación (latitud y longitud) y límite de velocidad cuando hay dato. Reúne fuentes oficiales y datos colaborativos.

Página para consultar: https://juangallo.github.io/radares-uy/ (requiere activar GitHub Pages en el repositorio)

Datos: [`radares-uruguay.json`](radares-uruguay.json)

URL directa del JSON para usar en otras herramientas:
`https://raw.githubusercontent.com/juangallo/radares-uy/main/radares-uruguay.json`

## Contenido

| Sección del JSON | Qué es | Coordenadas |
|---|---|---|
| `montevideo` | 50 puntos fijos de la Intendencia de Montevideo | Sí |
| `rutas_nacionales_mtop` | 127 puntos del MTOP, por ruta y kilómetro | 122 de 127 |
| `ministerio_interior` | 8 radares del Ministerio del Interior | Sí (interpoladas) |
| `intendencias_prensa_sin_coordenadas` | 9 esquinas de Canelones y Maldonado publicadas en prensa | No |
| `openstreetmap_adicionales` | 94 radares de OpenStreetMap que no figuran en los listados oficiales | Sí |

Cada registro incluye departamento, `lat`, `lon` y `limite` (km/h) cuando existe.

## Fuentes

- Intendencia de Montevideo, equipos de fiscalización fijos: https://montevideo.gub.uy/areas-tematicas/movilidad/fiscalizacion-de-infracciones/equipos-de-fiscalizacion-fijos
- Coordenadas y límites de Montevideo: https://www.jdavisonc.com/radares.html
- MTOP, ubicación de radares (listado del 17/12/2025): https://www.gub.uy/ministerio-transporte-obras-publicas/comunicacion/publicaciones/ubicacion-radares-0
- Geoportal del MTOP (capa `radares_rutas`, postes kilométricos y polígonos departamentales): https://geoportal.mtop.gub.uy/visualizador/
- Ministerio del Interior, ubicación de radares (16/01/2026): https://www.gub.uy/ministerio-interior/comunicacion/noticias/ubicacion-radares-del-ministerio-del-interior
- OpenStreetMap: límites de velocidad de rutas y de algunos puntos de Montevideo, y los radares adicionales.

## Cómo se obtuvo cada dato

- Coordenadas del MTOP: capa oficial del Geoportal. El departamento se asignó por ubicación sobre los polígonos departamentales del mismo servicio.
- Coordenadas del Ministerio del Interior: calculadas a partir de ruta y kilómetro con los postes kilométricos del MTOP (uno cada 1 km).
- Límites de velocidad de rutas: tomados de OpenStreetMap, no de una fuente oficial por punto.
- Radares adicionales: etiquetados por colaboradores de OpenStreetMap. No están verificados y pueden incluir equipos retirados, móviles o duplicados por sentido de circulación.

## Aviso

Los datos pueden estar desactualizados o contener errores. Los radares se agregan, se mueven y se retiran. No lo uses como única referencia: respetá siempre la señalización.

## Licencia y atribución

Este conjunto contiene datos derivados de OpenStreetMap, por lo que se distribuye bajo la licencia ODbL 1.0: https://opendatacommons.org/licenses/odbl/1-0/

Datos de OpenStreetMap © colaboradores de OpenStreetMap: https://www.openstreetmap.org/copyright

Los listados oficiales provienen de información pública publicada por el MTOP, el Ministerio del Interior y la Intendencia de Montevideo.
