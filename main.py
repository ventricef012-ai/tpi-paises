# =============================================================================
# main.py — Punto de entrada y menú principal
# Rama: main / develop
# =============================================================================

from datos import cargar_paises, guardar_paises, agregar_pais, actualizar_pais
from busqueda import (buscar_por_nombre, filtrar_por_continente,
                      filtrar_por_poblacion, filtrar_por_superficie)
from ordenamiento import ordenar_paises
from estadisticas import mostrar_estadisticas
from utils import separador, mostrar_lista_paises


def mostrar_menu():
    """Imprime el menú principal en consola."""
    separador()
    print("  GESTIÓN DE DATOS DE PAÍSES")
    separador()
    print("  1. Agregar país")
    print("  2. Actualizar país (población / superficie)")
    print("  3. Buscar país por nombre")
    print("  ── Filtros ──────────────────────")
    print("  4. Filtrar por continente")
    print("  5. Filtrar por rango de población")
    print("  6. Filtrar por rango de superficie")
    print("  ── Ordenamiento ─────────────────")
    print("  7. Ordenar países")
    print("  ── Estadísticas ─────────────────")
    print("  8. Mostrar estadísticas")
    print("  ── General ──────────────────────")
    print("  9. Mostrar todos los países")
    print("  0. Salir")
    separador()


def main():
    """Función principal: carga datos y gestiona el ciclo del menú."""
    print("\nCargando datos...")
    paises = cargar_paises()

    if paises is None:
        print("Error crítico al cargar el archivo. Verifique paises.csv.")
        return

    print(f"{len(paises)} países cargados correctamente.\n")

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            if agregar_pais(paises):
                guardar_paises(paises)

        elif opcion == "2":
            if actualizar_pais(paises):
                guardar_paises(paises)

        elif opcion == "3":
            buscar_por_nombre(paises)

        elif opcion == "4":
            resultado = filtrar_por_continente(paises)
            mostrar_lista_paises(resultado, "Países por continente")

        elif opcion == "5":
            resultado = filtrar_por_poblacion(paises)
            mostrar_lista_paises(resultado, "Países por rango de población")

        elif opcion == "6":
            resultado = filtrar_por_superficie(paises)
            mostrar_lista_paises(resultado, "Países por rango de superficie")

        elif opcion == "7":
            resultado = ordenar_paises(paises)
            mostrar_lista_paises(resultado, "Países ordenados")

        elif opcion == "8":
            mostrar_estadisticas(paises)

        elif opcion == "9":
            mostrar_lista_paises(paises, "Todos los países")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Ingrese un número del 0 al 9.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
