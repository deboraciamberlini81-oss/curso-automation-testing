
import csv
import json
from pathlib import Path


# Ruta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


def leer_csv(nombre_archivo):
    """Lee un archivo CSV y devuelve una lista de diccionarios."""
    ruta = BASE_DIR / "datos" / nombre_archivo

    with open(ruta, mode="r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def leer_json(nombre_archivo):
    """Lee un archivo JSON y devuelve su contenido."""
    ruta = BASE_DIR / "datos" / nombre_archivo

    with open(ruta, mode="r", encoding="utf-8") as archivo:
        return json.load(archivo)
