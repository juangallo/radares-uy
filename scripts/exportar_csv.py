#!/usr/bin/env python3
"""Genera radares-uruguay.csv (un radar por fila, solo con coordenadas) desde radares-uruguay.json."""
import csv, json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((RAIZ / "radares-uruguay.json").read_text(encoding="utf-8"))

COLS = ["id", "nombre", "organismo", "departamento", "ruta", "km", "limite_kmh",
        "lat", "lon", "calidad", "fuente_coord", "fuente_limite"]
filas = []

def agregar(prefijo, x, nombre, calidad, fuente_coord, **extra):
    if x.get("lat") is None or x.get("lon") is None:
        return
    n = sum(1 for f in filas if f["id"].startswith(prefijo)) + 1
    filas.append({
        "id": f"{prefijo}{n:03d}", "nombre": nombre,
        "organismo": x.get("organismo", ""), "departamento": x.get("departamento") or "",
        "ruta": extra.get("ruta", ""), "km": extra.get("km", ""),
        "limite_kmh": x.get("limite") or "", "lat": x["lat"], "lon": x["lon"],
        "calidad": calidad, "fuente_coord": fuente_coord,
        "fuente_limite": x.get("lim_fuente") or ("" if not x.get("limite") else "ver README"),
    })

for x in d["montevideo"]:
    agregar("MVD", x, x["ubicacion"], "oficial_via_tercero",
            "jdavisonc.com (dice tomarlas del mapa oficial de la Intendencia)")

for x in d["rutas_nacionales_mtop"]:
    c = x.get("coord") or ""
    if c == "MTOP Geoportal":
        calidad = "oficial"
    elif c.startswith("ESTIMADA"):
        calidad = "estimada"
    else:
        calidad = "aproximada"
    nombre = f'{x["ruta"]} km {x["km"]}' + (f' ({x["referencia"]})' if x.get("referencia") else "")
    agregar("MTOP", x, nombre, calidad, c, ruta=x["ruta"], km=x["km"])

for x in d["ministerio_interior"]:
    agregar("INT", x, f'{x["ruta"]} km {x["km"]}', "oficial_interpolada", x.get("coord") or "",
            ruta=x["ruta"], km=x["km"])

for x in d["intendencias_prensa_sin_coordenadas"]:
    x = dict(x, organismo="Intendencia (prensa)")
    agregar("PRE", x, x["ubicacion"], "aproximada", x.get("coord") or "")

for x in d["openstreetmap_adicionales"]:
    agregar("OSM", x, f'Radar OSM ({x["departamento"]})', "osm_no_verificado", "OpenStreetMap")

with open(RAIZ / "radares-uruguay.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    w.writerows(filas)
print(len(filas), "radares escritos")
