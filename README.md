# Radares fijos de Uruguay

Listado de radares de fiscalización de velocidad de Uruguay con ubicación (latitud y longitud) y límite de velocidad cuando hay dato. Reúne fuentes oficiales y datos colaborativos.

Página para consultar: https://juangallo.github.io/radares-uy/ (requiere activar GitHub Pages en el repositorio)

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

No hay una forma documentada de importar radares al navegador del auto. Este prompt es un intento con Grok y no está probado: puede que no pueda crear alertas por ubicación ni mostrar iconos en el mapa. Probalo estacionado, con un solo radar cercano primero, y comprobá en el mapa lo que diga (no confíes en un "listo"). No lo pruebes manejando.

```text
Quiero que me avises por voz cuando me acerque a un radar de velocidad en Uruguay, 200 metros antes de pasar por él.

Datos: usá este CSV, una fila por radar (278 en total), con las columnas nombre, lat, lon, limite_kmh y calidad:
https://raw.githubusercontent.com/juangallo/radares-uy/main/radares-uruguay.csv

Lo que necesito:
1. Alerta por ubicación a 200 m de cada radar. Si podés, que diga el límite de velocidad cuando exista.
2. Un icono de radar o de faro en el mapa para cada punto. Si no se puede, decímelo.
3. Cargá todos los radares del archivo.

Antes de empezar, respondeme en pocas líneas:
- Qué de esto podés hacer realmente en este auto y qué no.
- Cómo lo vas a hacer (por ejemplo, cómo vas a detectar la cercanía sin que yo te pregunte).
- Si encontrás un problema, proponé una alternativa en vez de decir que ya está hecho.

Después de cargar, decime exactamente cuántos radares cargaste. Tienen que ser 278. Probemos primero con un radar cercano antes de seguir.

Nota: la columna calidad indica qué tan confiable es cada punto. Los marcados osm_no_verificado pueden no ser radares vigentes.
```

## Aviso

Los datos pueden estar desactualizados o contener errores. Los radares se agregan, se mueven y se retiran. No lo uses como única referencia: respetá siempre la señalización.

## Licencia y atribución

Este conjunto contiene datos derivados de OpenStreetMap, por lo que se distribuye bajo la licencia ODbL 1.0: https://opendatacommons.org/licenses/odbl/1-0/

Datos de OpenStreetMap © colaboradores de OpenStreetMap: https://www.openstreetmap.org/copyright

Los listados oficiales provienen de información pública publicada por el MTOP, el Ministerio del Interior y la Intendencia de Montevideo.
