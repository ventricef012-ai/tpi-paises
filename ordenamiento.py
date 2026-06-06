# =============================================================================
# ordenamiento.py — Ordenamiento del dataset de países
# Rama: feature/datos-y-ordenamiento
# =============================================================================


def ordenar_paises(paises):

    """Presenta un submenú para elegir criterio y dirección de ordenamiento.
    Devuelve una nueva lista ordenada sin modificar la original."""

    try:
        opcion = int(input("Indique el criterio de ordenamiento: \n" \
        "1. Por Nombre \n" \
        "2. Por Poblacion \n" \
        "3. Por Superficie \n").strip())
        if opcion == 1:
            campo = "nombre"
        elif opcion == 2:
            campo = "poblacion"
        elif opcion == 3:
            campo = "superficie"
        else:
            print("La opcion ingresada no existe")
            return []
        
        # .upper() para aceptar 'a' o 'A' indiferentemente
        direccion= input("Ingrese direccion: \n" \
        "A. Ascendente \n" \
        "D. Descendente \n").strip().upper()
        if direccion == "A":
            ascendente = True
        elif direccion == "D":
            ascendente = False
        else:
            print("La opcion ingresada es incorrecta")
            return []
        return _ordenar_por_campo(paises, campo, ascendente)
    except ValueError as e:
        print(f"Error: {e}")
        return []


def _ordenar_por_campo(paises, campo, ascendente=True):

    """Ordena una copia de la lista por el campo indicado usando Bubble Sort mejorado.
    Devuelve la nueva lista; la original no se modifica."""

    copia = list(paises)  # trabajamos sobre una copia para no alterar la original
    n = len(copia)
    for i in range(n):           
        intercambio = False
        # n-1-i: los últimos i elementos ya están en su lugar, no hace falta compararlos      
        for j in range(0, n-1-i):
            if ascendente:
                if copia[j][campo] > copia[j+1][campo]:
                    copia[j], copia[j+1] = copia[j+1], copia[j]
                    intercambio = True
            else:
                if copia[j][campo] < copia[j+1][campo]:
                    copia[j], copia[j+1] = copia[j+1], copia[j]
                    intercambio = True
        if not intercambio:      # optimización: si no hubo intercambios, la lista ya está ordenada
            break
    return copia
