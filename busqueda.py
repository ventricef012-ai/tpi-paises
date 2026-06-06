# =============================================================================
# busqueda.py — Búsqueda y filtros sobre el dataset de países
# Rama: feature/busqueda-y-ordenamiento
# =============================================================================


from utils import mostrar_lista_paises                                       # Importa función creada en utils.py

# Función para buscar países por coincidencia parcial o total
# Parámetro: paises(list) es una lista de diccionarios de países
def buscar_por_nombre(paises):
    termino = input("  Ingresá el nombre del país a buscar (coincidencia parcial o total): ").strip()

    if not termino:                                                          # Valida que el usuario no deje el campo en blanco 
        print("  El campo no puede estar vacío.")
        return
    
    termino_lower = termino.lower()                                          # .lower() para convertir el string ingresado a minúsculas
    resultados = []                                                          # Guarda las coincidencias en una lista y las pasa a la función mostrar_lista_paises()
    
    for pais in paises:
        if termino_lower in pais["nombre"].lower():
            resultados.append(pais)                                          # Agrega el resultado al final de la lista

    if not resultados:                                                       # Si no encuentra coincidencias imprime mensaje de error
        print(f'  No se encontraron países que coincidan con "{termino}"')
    else:                                                                    # Si encuentra coincidencias las muestra por pantalla con llamado a funcion mostrar_lista_paises()
        mostrar_lista_paises(resultados)



# Función para mostrar los países pertenecientes al continente ingresado
# Parámetro: paises(list) es una lista de diccionarios de países
def filtrar_por_continente(paises):
    continentes = []

    for pais in paises:
        if pais["continente"] not in continentes:
            continentes.append(pais["continente"])                           # Agrega a la lista el país ingresado por el usuario si no existía anteriormente
    continentes.sort()                                                       # sort() ordena los continentes alfabéticamente
    print("  Continentes disponibles: " + ", ".join(continentes))            # join() convierte la lista en un string separado por comas
    continente = input("  Ingresá el continente: ").strip()

    if not continente:                                                       # Valida que no se deje el campo en blanco
        print("  El campo no puede estar vacío.")
        return
    
    resultados = []
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            resultados.append(pais)                                          # Si coincide, agrega el país al final de la lista

    if not resultados:
        print(f'  No se encontraron países en "{continente}".')              # Si no coincide, imprime mensaje de error
    else:
        mostrar_lista_paises(resultados)                                     # Muestra los países del continente consultado 




def filtrar_por_poblacion(paises):
    """
    Solicita un rango mínimo y máximo de población.
    Retorna los países cuya población esté dentro del rango (inclusive).
    Valida que los valores sean enteros positivos y que mínimo <= máximo.

    Parámetros:
        paises (list[dict]): lista de países.

    Retorna:
        list[dict]: países dentro del rango de población.
    """
    # TODO: implementar
    pass


def filtrar_por_superficie(paises):
    """
    Solicita un rango mínimo y máximo de superficie en km².
    Retorna los países cuya superficie esté dentro del rango (inclusive).
    Valida que los valores sean enteros positivos y que mínimo <= máximo.

    Parámetros:
        paises (list[dict]): lista de países.

    Retorna:
        list[dict]: países dentro del rango de superficie.
    """
    # TODO: implementar
    pass
