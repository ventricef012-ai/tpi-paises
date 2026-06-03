# =============================================================================
# ordenamiento.py — Ordenamiento del dataset de países
# Rama: feature/busqueda-y-ordenamiento
# =============================================================================


def ordenar_paises(paises):
    """
    Presenta un submenú al usuario para elegir criterio y dirección
    de ordenamiento, y muestra el resultado en consola.

    Criterios disponibles:
      1. Nombre (alfabético)
      2. Población
      3. Superficie

    Dirección:
      A. Ascendente
      D. Descendente

    No modifica la lista original (trabaja sobre una copia).

    Parámetros:
        paises (list[dict]): lista de países.

    Retorna:
        list[dict]: nueva lista ordenada según la elección del usuario.
    """
    # TODO: implementar
    pass


def _ordenar_por_campo(paises, campo, ascendente=True):
    """
    Función auxiliar privada.
    Ordena la lista de países por el campo indicado.
    Implementar SIN usar sorted() con key lambda directamente en el menú
    — la lógica de ordenamiento va acá adentro.

    Parámetros:
        paises (list[dict]): lista de países.
        campo (str): 'nombre', 'poblacion' o 'superficie'.
        ascendente (bool): True para ascendente, False para descendente.

    Retorna:
        list[dict]: nueva lista ordenada.
    """
    # TODO: implementar
    pass
