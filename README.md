# Radares fijos de Uruguay

Listado de radares de fiscalización de velocidad de Uruguay con ubicación (latitud y longitud) y límite de velocidad cuando hay dato. Reúne fuentes oficiales y datos colaborativos.

Datos: [`radares-uruguay.json`](radares-uruguay.json)

CSV plano (un radar por fila, solo los 278 con coordenadas): [`radares-uruguay.csv`](radares-uruguay.csv). Columna `calidad`: `oficial`, `oficial_via_tercero`, `oficial_interpolada`, `aproximada`, `estimada` u `osm_no_verificado`. Se regenera con `python3 scripts/exportar_csv.py`.
`https://raw.githubusercontent.com/juangallo/radares-uy/main/radares-uruguay.csv`

URL directa del JSON para usar en otras herramientas:
`https://raw.githubusercontent.com/juangallo/radares-uy/main/radares-uruguay.json`

## Contenido

| Sección del JSON | Qué es | Coordenadas |
|---|---|---|
| `montevideo` | 50 puntos fijos de la Intendencia de Montevideo | Sí |
| `rutas_nacionales_mtop` | 127 puntos del MTOP, por ruta y kilómetro | 125 de 127 (3 no vienen del Geoportal, ver abajo) |
| `ministerio_interior` | 8 radares del Ministerio del Interior | Sí (interpoladas) |
| `intendencias_prensa_sin_coordenadas` | 9 esquinas de Canelones y Maldonado publicadas en prensa | 6 de 9, aproximadas |
| `openstreetmap_adicionales` | 89 radares de OpenStreetMap que no figuran en los listados oficiales | Sí |

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
- Tres puntos del listado del MTOP no están en la capa del Geoportal y su campo `coord` indica el origen: Ruta 26 km 1,976 (interpolada con postes km y confirmada por 2 nodos de OSM), Ruta 21 km 255,710 (nodo de OSM `Carmelo O`) y Ruta 21 km 323,100 (**estimada**, extrapolada 100 m desde el poste km 323). Ruta 3 Young Sur y Young Norte (acceso) siguen sin coordenadas porque el listado no trae km.
- Esquinas de prensa: 4 tienen el centro de la intersección calculado con OpenStreetMap y 2 un radar de OSM candidato (ver `coord` de cada registro). No son ubicaciones verificadas. Sin coordenadas: Av. Francia entre Maipo y Urales, Wilson Ferreira Aldunate entre Puente Carrasco y Av. de la Playa, y Roosevelt y Agustín Hernández (Pando).
- Coordenadas del Ministerio del Interior: calculadas a partir de ruta y kilómetro con los postes kilométricos del MTOP (uno cada 1 km).
- Límites de velocidad de rutas: tomados de OpenStreetMap, no de una fuente oficial por punto.
- Radares adicionales: etiquetados por colaboradores de OpenStreetMap. No están verificados y pueden incluir equipos retirados, móviles o duplicados por sentido de circulación.

## Usar con Grok en un Tesla

No hay una forma documentada de importar radares al navegador del auto. El Tesla admite solo 100 recordatorios activos, por eso el prompt usa [`prioridad.csv`](prioridad.csv): 100 radares ordenados por prioridad (Montevideo, Interbalnearia, Rutas 8 y 9, Ruta 93 y Punta del Este). Se regenera con `python3 scripts/exportar_prioridad.py`; el criterio de prioridad es mío, no un dato medido. Este prompt es un intento con Grok y no está probado: puede que no pueda crear recordatorios por ubicación. Probalo estacionado, con un solo radar cercano primero, y comprobá lo que diga en el auto (no confíes en un "listo"). No lo pruebes manejando.

```text
Buscá en GitHub el archivo prioridad.csv del repositorio radares-uy del usuario juangallo. Tiene 100 radares ordenados por la columna orden, con nombre, lat, lon y limite_kmh.

Creá un recordatorio por ubicación para cada radar:
- Radio de 300 metros.
- Sin fecha de fin.
- Al pasar cerca, que diga solamente "acercándote a un radar" y, si limite_kmh tiene valor, el límite de velocidad. No digas el nombre.

Hacelo de a 5 radares en el orden del archivo. Al terminar cada tanda, confirmame que completaste todos los anteriores y pedime permiso antes de seguir con los 5 siguientes.

Si algo no se puede hacer, decímelo en vez de decir que ya está.
```

## Aviso

Los datos pueden estar desactualizados o contener errores. Los radares se agregan, se mueven y se retiran. No lo uses como única referencia: respetá siempre la señalización.

## Licencia y atribución

Este conjunto contiene datos derivados de OpenStreetMap, por lo que se distribuye bajo la licencia ODbL 1.0: https://opendatacommons.org/licenses/odbl/1-0/

Datos de OpenStreetMap © colaboradores de OpenStreetMap: https://www.openstreetmap.org/copyright

Los listados oficiales provienen de información pública publicada por el MTOP, el Ministerio del Interior y la Intendencia de Montevideo.
