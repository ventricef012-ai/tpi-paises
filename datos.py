# =============================================================================
# datos.py — Carga de CSV, agregar y actualizar países
# Rama: feature/datos-y-ordenamiento
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

    """Pide los datos de un país por consola, lo valida y lo agrega a la lista.
    Devuelve True si lo agregó, False si hubo algún error."""

    try:
        nombre_pais = input("Ingrese el nombre del pais: ").strip()
        if not nombre_pais:
            raise ValueError("El nombre no puede estar vacío")
        # Evita duplicados: compara en minúsculas para que "Argentina" y "argentina" cuenten igual
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
        paises.append(pais) # lo agrega a la lista en memoria; main se encarga de guardar
        return True
    
    except ValueError as e:
        print(f"Error:{e}")
        return False


def actualizar_pais(paises):

    """Busca un país por nombre y actualiza su población y superficie.
    Devuelve True si lo actualizó, False si no lo encontró o hubo error."""

    try:
        buscar_pais = input("Ingrese el nombre del pais que quiere actualizar: ").strip()
        for datos_pais in paises:
            # Búsqueda en minúsculas para no depender de mayúsculas/minúsculas
            if buscar_pais.lower() == datos_pais["nombre"].lower():
                print(f"Encontrado! los datos actuales son: \n"
                f"Poblacion: {datos_pais['poblacion']}\n"
                f"Superficie: {datos_pais['superficie']}")

                # Validamos los dos valores ANTES de asignar, para no dejar una actualización a medias
                poblacion_actualizada = int(input("Cual es el nuevo valor de poblacion: ").strip())
                if poblacion_actualizada <= 0:
                    raise ValueError("La poblacion no puede ser negativa o igual a 0")
                superficie_actualizada = int(input("Cual es el nuevo valor de superficie: ").strip())
                if superficie_actualizada <= 0:
                    raise ValueError("La superficie no puede ser negativa o igual a 0")

                datos_pais["poblacion"] = poblacion_actualizada
                datos_pais["superficie"] = superficie_actualizada
                return True
        # Si el for terminó sin encontrar el país, avisa que no existe
        raise ValueError(f"No se encontró el país '{buscar_pais}'")
    except ValueError as e:
        print(f"Error:{e}")
        return False
