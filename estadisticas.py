# =============================================================================
# estadisticas.py — Estadísticas sobre el dataset de países
# Rama: feature/datos-y-estadisticas
# =============================================================================


def mostrar_estadisticas(paises):
    """
    Muestra en consola un resumen estadístico completo:
      - País con mayor población y su valor
      - País con menor población y su valor
      - Promedio de población (redondeado a entero)
      - País con mayor superficie y su valor
      - País con menor superficie y su valor
      - Promedio de superficie (redondeado a entero)
      - Cantidad de países por continente

    Parámetros:
        paises (list[dict]): lista de países.
    """
    # TODO: implementar
    pass


def _pais_mayor(paises, campo):
    """
    Función auxiliar privada.
    Retorna el diccionario del país con el valor máximo en 'campo'.

    Parámetros:
        paises (list[dict]): lista de países.
        campo (str): 'poblacion' o 'superficie'.

    Retorna:
        dict: país con el valor máximo, o None si la lista está vacía.
    """
    # TODO: implementar
    pass


def _pais_menor(paises, campo):
    """
    Función auxiliar privada.
    Retorna el diccionario del país con el valor mínimo en 'campo'.

    Parámetros:
        paises (list[dict]): lista de países.
        campo (str): 'poblacion' o 'superficie'.

    Retorna:
        dict: país con el valor mínimo, o None si la lista está vacía.
    """
    # TODO: implementar
    pass


def _promedio(paises, campo):
    """
    Función auxiliar privada.
    Calcula el promedio del campo numérico indicado.

    Parámetros:
        paises (list[dict]): lista de países.
        campo (str): 'poblacion' o 'superficie'.

    Retorna:
        float: promedio, o 0 si la lista está vacía.
    """
    # TODO: implementar
    pass


def _cantidad_por_continente(paises):
    """
    Función auxiliar privada.
    Cuenta cuántos países hay por continente.

    Parámetros:
        paises (list[dict]): lista de países.

    Retorna:
        dict: {continente: cantidad}, ordenado alfabéticamente por continente.
    """
    # TODO: implementar
    pass
