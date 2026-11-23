#!/usr/bin/env python3
"""Genera prioridad.csv: los 100 radares con mayor prioridad para un limite de 100 recordatorios.

Lee radares-uruguay.csv (generado por exportar_csv.py). El orden por niveles es un criterio
editorial (zonas de mas circulacion y confiabilidad de la fuente), no un dato medido.

Niveles:
1 Montevideo (Intendencia)
2 MTOP/Interior en Montevideo
3 Interbalnearia
4 Ruta 8, 9 y 6 en Rocha, Maldonado, Canelones y Montevideo (se omiten Cerro Largo, Lavalleja y Treinta y Tres)
5 Esquinas de prensa de Maldonado (aproximadas)
6 Ruta 93 (Maldonado), oficial
7 Radares de OSM de Maldonado (no verificados) mas cercanos a Punta del Este (12), sin duplicados a menos de 110 m
8 Radares de OSM de Maldonado mas cercanos a Laguna del Sauce y el aeropuerto, hasta completar 100
Canelones queda afuera salvo lo que cruza la Interbalnearia y las Rutas 8 y 9.
"""
import csv, math, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
filas = list(csv.DictReader(open(RAIZ / "radares-uruguay.csv", encoding="utf-8")))
LIMITE = 100
PUNTA_DEL_ESTE = (-34.96, -54.95)
LAGUNA_DEL_SAUCE = (-34.862, -55.075)  # aproximado: localidad (Nominatim) y aeropuerto

def metros(a, b):
    lat = (float(a[0]) + float(b[0])) / 2
    return math.hypot((float(a[0]) - float(b[0])) * 110540,
                      (float(a[1]) - float(b[1])) * 111320 * math.cos(math.radians(lat)))

def nivel(x):
    p, ruta, dep = x["id"][:3], x["ruta"], x["departamento"]
    if p == "MVD": return 1
    if p in ("MTO", "INT") and dep == "Montevideo": return 2
    if ruta.startswith("Ruta Interbalnearia"): return 3
    if ruta in ("Ruta 8", "Ruta 9", "Ruta 6"):
        return 4 if dep in ("Rocha", "Maldonado", "Canelones", "Montevideo") else None
    if p == "PRE" and dep == "Maldonado": return 5
    if p == "MTO" and dep == "Maldonado" and ruta == "Ruta 93": return 6
    return None

sel = [dict(x, prioridad=nivel(x)) for x in filas if nivel(x)]
sel.sort(key=lambda x: x["prioridad"])  # estable: mantiene el orden del CSV dentro de cada nivel

osm = [x for x in filas if x["id"][:3] == "OSM" and x["departamento"] == "Maldonado"]
elegidos = []

def agregar_zona(centro, cupo, prioridad):
    """Suma hasta `cupo` radares de OSM mas cercanos a `centro`, sin duplicados a menos de 110 m."""
    n = 0
    for x in sorted(osm, key=lambda x: metros((x["lat"], x["lon"]), centro)):
        if n >= cupo or len(sel) + len(elegidos) >= LIMITE:
            break
        if all(y["id"] != x["id"] and metros((x["lat"], x["lon"]), (y["lat"], y["lon"])) >= 110 for y in elegidos):
            elegidos.append(dict(x, prioridad=prioridad))
            n += 1

# Nivel 7: Punta del Este. Nivel 8: Laguna del Sauce y aeropuerto (centro aproximado entre ambos).
agregar_zona(PUNTA_DEL_ESTE, 12, 7)
agregar_zona(LAGUNA_DEL_SAUCE, LIMITE, 8)  # completa los lugares que quedan
sel += elegidos
sel = sel[:LIMITE]

cols = ["orden", "prioridad"] + [c for c in filas[0].keys() if c not in ("fuente_coord", "fuente_limite")]
with open(RAIZ / "prioridad.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    for i, x in enumerate(sel, 1):
        w.writerow(dict(x, orden=i))
print(len(sel), "radares en prioridad.csv")
