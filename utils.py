# =============================================================================
# utils.py — Funciones de visualización compartidas
# Responsable: ambos integrantes (acordar formato antes de implementar)
# =============================================================================


def mostrar_pais(pais):

    #Muestra los datos de un país (un diccionario) en formato legible.
    # ':<10' alinea las etiquetas a 10 caracteres para que los ':' queden parejos
    # ':,' agrega el separador de miles a los números

    print(f"{'Nombre':<10}: {pais['nombre']}")
    print(f"{'Población':<10}: {pais['poblacion']:,}")
    print(f"{'Superficie':<10}: {pais['superficie']:,} km²")
    print(f"{'Continente':<10}: {pais['continente']}")


def mostrar_lista_paises(paises, titulo="Resultados"):

    #Muestra una lista de países con un encabezado. Avisa si está vacía.

    if len(paises) == 0:
        print("No hay países para mostrar")
    else:
        separador()
        print(titulo)
        separador()
        for datos in paises:
            mostrar_pais(datos)


def separador(caracter="=", largo=50):

    #Imprime una línea separadora en consola.
    
    print(caracter * largo)
