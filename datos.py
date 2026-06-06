# =============================================================================
# datos.py — Carga de CSV, agregar y actualizar países
# Rama: feature/datos-y-estadisticas
# =============================================================================

import csv
import os

ARCHIVO_CSV = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises(ruta=ARCHIVO_CSV):
    """Lee el CSV y devuelve una lista de diccionarios (un país por dict).
    Devuelve lista vacía si el archivo no existe o tiene datos mal formados."""
    datos_paises=[]
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            # DictReader usa la primera fila (encabezado) como claves del dict
            lector = csv.DictReader(archivo)
            for fila in lector:
                # El CSV trae todo como texto: convertimos los números a int
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
    except ValueError as e:
        print(f"El CSV tiene valores numéricos mal cargados. Detalle: {e}")
        return []
    return datos_paises


def guardar_paises(paises, ruta=ARCHIVO_CSV):
    """Escribe la lista de países en el archivo CSV. Sobreescribe el contenido."""
    # newline="" evita filas vacías entre registros (importante en Windows)
    try:
        with open(ruta,"w",newline="",encoding="utf-8") as archivo:
            escritor_dict = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor_dict.writeheader()
            escritor_dict.writerows(paises)
    except PermissionError as e:
        print(f"No se pudo guardar el archivo. Detalle: {e}")


def agregar_pais(paises):
    try:
        nombre_pais = input("Ingrese el nombre del pais: ").strip()
        if not nombre_pais:
            raise ValueError("El nombre no puede estar vacío")
        for pais_existente in paises:
            if nombre_pais.lower() == pais_existente["nombre"].lower():
                raise ValueError(f"El país '{nombre_pais}' ya existe en la lista")
            
        poblacion_pais = int(input("Ingrese la poblacion del pais: ").strip())
        if poblacion_pais <= 0:
            raise ValueError("No se puede ingresar datos negativos o iguales a 0")
        
        superficie_pais = int(input("Ingrese la superficie del pais: ").strip())
        if superficie_pais <= 0:
            raise ValueError("No se puede ingresar datos negativos o iguales a 0")

        continente_pais = input("Ingrese el continente donde se encuentra ubicado el pais: ").strip()
        if not continente_pais:
            raise ValueError("El continente no puede estar vacío")
        
        pais = {
                    "nombre": nombre_pais,
                    "poblacion": poblacion_pais,
                    "superficie": superficie_pais,
                    "continente": continente_pais
                    }
        paises.append(pais)
        return True
    
    except ValueError as e:
        print(f"Error:{e}")
        return False

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
