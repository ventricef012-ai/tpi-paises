# =============================================================================
# estadisticas.py — Estadísticas sobre el dataset de países
# Rama: feature/datos-y-estadisticas
# =============================================================================


def mostrar_estadisticas(paises):

# Muestra en consola un resumen estadístico completo:
# - País con mayor población y su valor
# - País con menor población y su valor
# - Promedio de población (redondeado a entero)
# - País con mayor superficie y su valor
# - País con menor superficie y su valor
# - Promedio de superficie (redondeado a entero)
# - Cantidad de países por continente

    if not paises:
        print("  No existen países cargados.")                                  # Valida que existan países cargados antes de llamar a helpers
        return

# Llamado de funciones (helpers)
    mayor_poblacion = _pais_mayor(paises, "poblacion")
    menor_poblacion = _pais_menor(paises, "poblacion")
    promedio_poblacion = _promedio(paises, "poblacion")
    mayor_superficie = _pais_mayor(paises, "superficie")
    menor_superficie = _pais_menor(paises, "superficie")
    promedio_superficie = _promedio(paises, "superficie")
    cant_por_cont = _cantidad_por_continente(paises)

# Mostrar resultados formateados
    print("\n  " + "=" * 40)
    print("\n  ESTADÍSTICAS")
    print("  " + "=" * 40)

    print(f"\nTotal de países cargados: {len(paises)}")
    print(f"\n  - Mayor población:    {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']:,})".replace(",","."))
    print(f"  - Menor población:    {menor_poblacion['nombre']} ({menor_poblacion['poblacion']:,})".replace(",","."))
    print(f"  - Promedio de población: {round(promedio_poblacion):,}".replace(",", "."))           # round() redondea el número indicado entre paréntesis

    print(f"\n  - Mayor superficie:    {mayor_superficie['nombre']} ({mayor_superficie['superficie']:,})".replace(",","."))
    print(f"  - Menor superficie:    {menor_superficie['nombre']} ({menor_superficie['superficie']:,})".replace(",","."))
    print(f"  - Promedio de superficie: {round(promedio_superficie):,}".replace(",", "."))

    print("\nPaíses por continente:")
    for continente, cantidad in cant_por_cont.items():                                             # items() convierte en pares clave-valor
        print(f"    {continente}: {cantidad}")

    print("\n  " + "=" * 40)


# Función auxiliar: retorna diccionario del país con el valor máximo en el parámetro "campo"
def _pais_mayor(paises, campo):
    if not paises:
        return None                                                                # Valida que existan países en la lista

    mayor = paises[0]
    for pais in paises:
        if pais[campo] > mayor[campo]:
            mayor = pais
    return mayor

# Función auxiliar: retorna diccionario del país con el valor mínimo en el parámetro "campo"
def _pais_menor(paises, campo):
    if not paises:
        return None

    menor = paises[0]
    for pais in paises:
        if pais[campo] < menor[campo]:
            menor = pais
    return menor

# Función auxiliar: calcula promedio de superficie de países
def _promedio(paises, campo):
    if not paises:
        return 0

    promedio_sup = 0
    for pais in paises:
        promedio_sup+=pais[campo]
    return promedio_sup / len(paises)

# Función auxiliar: calcula cuántos países hay por continente
def _cantidad_por_continente(paises):
    conteo = {}
    for pais in paises:
        continente = pais["continente"]
        if continente not in conteo:
            conteo[continente] = 0
        conteo[continente]+=1

    conteo_ordenado = {}                                                           # Diccionario con los nombres de continentes ordenados
    for clave in sorted(conteo):                                                   # sorted() para ordenar los continentes alfabéticamente
        conteo_ordenado[clave] = conteo[clave]
    return conteo_ordenado