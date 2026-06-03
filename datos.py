# =============================================================================
# datos.py — Carga de CSV, agregar y actualizar países
# Rama: feature/datos-y-estadisticas
# =============================================================================

import csv
import os

ARCHIVO_CSV = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises(ruta=ARCHIVO_CSV):
    datos_paises=[]
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                    }
                datos_paises.append(pais)
    except FileNotFoundError:
        print("El archivo que intenta abrir no existe")
        return []
    except ValueError:
        print("El csv tiene valores erroneos")
        return []
    return datos_paises


def guardar_paises(paises, ruta=ARCHIVO_CSV):
    """
    Escribe la lista de países en el archivo CSV.
    Sobreescribe el contenido existente.

    Parámetros:
        paises (list[dict]): lista de países a guardar.
        ruta (str): ruta del archivo CSV.
    """
    # TODO: implementar
    pass


def agregar_pais(paises):
    """
    Solicita al usuario los datos de un nuevo país por consola
    y lo agrega a la lista. No se permiten campos vacíos.
    Valida que la población y superficie sean números enteros positivos.
    Valida que el país no exista ya (por nombre, sin distinguir mayúsculas).

    Parámetros:
        paises (list[dict]): lista actual de países (se modifica en lugar).

    Retorna:
        bool: True si se agregó correctamente, False si se canceló o hubo error.
    """
    # TODO: implementar
    pass


def actualizar_pais(paises):
    """
    Solicita el nombre de un país y permite actualizar
    su población y/o superficie.
    Muestra los valores actuales antes de pedir los nuevos.
    Valida que los nuevos valores sean enteros positivos.

    Parámetros:
        paises (list[dict]): lista actual de países (se modifica en lugar).

    Retorna:
        bool: True si se actualizó, False si no se encontró el país.
    """
    # TODO: implementar
    pass
