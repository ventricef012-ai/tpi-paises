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
    return resultados


# Función para filtrar países por población dentro de un rango indicado por el usuario
def filtrar_por_poblacion(paises):
    print("  Ingresá el rango de población a filtrar: ")

    try:
        minimo = int(input("  Población mínima: ").strip())
        maximo = int(input("  Población máxima: ").strip())
    except ValueError:                                                       # Valida que se ingrese un entero positivo
        print("  Solo es posible ingresar números enteros.")
        return

    if minimo < 0 or maximo < 0:                                             # Valida que ninguno de los valores ingresados por usuario sea negativo
        print("  Solo es posible ingresar números positivos.")
        return

    if minimo > maximo:                                                      # Valida que la población mínima no supere la población máxima ingresada
        print("  El mínimo no puede ser mayor que el máximo.")

    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:                            # Compara los límites ingresados por usuario con la población actual, agrega a resultados[] si cumple la condición
            resultados.append(pais)

    if not resultados:
        print(f"  No se encontraron países con rango poblacional entre {minimo:,} y {maximo:,}.".replace(",", "."))
    return resultados


# Función para filtrar países por superficie dentro de un rango indicado por el usuario (mismo trabajo que función filtrar_por_poblacion)
def filtrar_por_superficie(paises):
    print("  Ingresá el rango de superficie a filtrar (en km²).")

    try:
        minimo = int(input("  Superficie mínima (km²): ").strip())
        maximo = int(input("  Superficie máxima (km²): ").strip())
    except ValueError:                                                       # Valida que se ingrese un entero positivo
        print("  Solo es posible ingresar números enteros.")
        return

    if minimo < 0 or maximo < 0:                                             # Valida que ninguno de los valores ingresados por usuario sea negativo
        print("  Solo es posible ingresar números positivos.")
        return

    if minimo > maximo:                                                      # Valida que la población mínima no supere la población máxima ingresada
        print("  El mínimo no puede ser mayor que el máximo.")
        return

    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:                           # Compara la superficie ingresada por usuario con la superficie de cada país, agrega a resultados[] si cumple la condición
            resultados.append(pais)

    if not resultados:
        print(f"  No se encontraron países con superficie entre {minimo:,} y {maximo:,}km².".replace(",", "."))
    return resultados