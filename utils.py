# =============================================================================
# utils.py — Funciones de visualización compartidas
# Responsable: ambos integrantes (acordar formato antes de implementar)
# =============================================================================

# Función para mostrar los datos del país con formato legible
# Parámetro: pais(dict) es un diccionario con claves de nombre, población, superficie y continente. 
def mostrar_pais(pais):
    print(f"  Nombre:      {pais['nombre']}")
    print(f"  Continente:  {pais['continente']}")
    print(f"  Población:   {pais['poblacion']}".replace(",", "."))       # Función replace para reemplazar las comas por puntos al ejecutar
    print(f"  Superficie:  {pais['superficie']} km²".replace(",", "."))
    print("  " + "-" * 24)



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
