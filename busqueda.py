# =============================================================================
# busqueda.py — Búsqueda y filtros sobre el dataset de países
# Rama: feature/busqueda-y-ordenamiento
# =============================================================================


def buscar_por_nombre(paises):
    """
    Solicita un nombre o fragmento al usuario y muestra todos los países
    cuyo nombre lo contenga (sin distinguir mayúsculas/minúsculas).
    Muestra un mensaje claro si no hay resultados.

    Parámetros:
        paises (list[dict]): lista de países.

    Retorna:
        list[dict]: lista de países que coinciden (puede estar vacía).
    """
    # TODO: implementar
    pass


def filtrar_por_continente(paises):
    """
    Muestra los continentes disponibles y solicita al usuario que elija uno.
    Retorna los países de ese continente.
    Valida que la entrada no esté vacía y que el continente exista.

    Parámetros:
        paises (list[dict]): lista de países.

    Retorna:
        list[dict]: países del continente elegido.
    """
    # TODO: implementar
    pass


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
