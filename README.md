# TPI — Gestión de Datos de Países en Python
**Programación 1 | Tecnicatura Universitaria en Programación | UTN**

Aplicación de consola desarrollada en Python que permite gestionar un dataset de países, aplicando listas, diccionarios, funciones, ordenamientos y estadísticas.

---

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1 | Agregar un nuevo país (con validación de campos y duplicados) |
| 2 | Actualizar población y superficie de un país existente |
| 3 | Buscar país por nombre (coincidencia parcial o exacta) |
| 4 | Filtrar países por continente |
| 5 | Filtrar países por rango de población |
| 6 | Filtrar países por rango de superficie |
| 7 | Ordenar países por nombre, población o superficie (asc/desc) |
| 8 | Mostrar estadísticas del dataset |
| 9 | Mostrar todos los países |
| 0 | Salir |

---

## Requisitos

- Python 3.x
- No requiere librerías externas (solo el módulo `csv` de la biblioteca estándar)

---

## Cómo ejecutar

1. Clonar el repositorio:
```bash
git clone https://github.com/ventricef012-ai/tpi-paises.git
cd tpi-paises
```

2. Ejecutar el programa:
```bash
python main.py
```

El archivo `paises.csv` debe estar en la misma carpeta que `main.py` (ya está incluido en el repositorio).

---

## Ejemplos de uso

**Agregar un país:**
```
Ingrese el nombre del pais: Francia
Ingrese la poblacion del pais: 67000000
Ingrese la superficie del pais: 551695
Ingrese el continente donde se encuentra ubicado el pais: Europa
País agregado correctamente.
```

**Ordenar por población descendente:**
```
Indique el criterio de ordenamiento:
1. Por Nombre
2. Por Poblacion
3. Por Superficie
2
Ingrese dirección:
A. Ascendente
D. Descendente
D

==================================================
Países ordenados
==================================================
  Nombre:      China
  Continente:  Asia
  Población:   1.412.600.000
  Superficie:  9.596.960 km²
  ------------------------
  Nombre:      India
  ...
```

**Buscar un país:**
```
Ingrese el nombre del país a buscar: arg
  Nombre:      Argentina
  Continente:  América
  Población:   45.376.763
  Superficie:  2.780.400 km²
```

---

## Estructura del proyecto

```
tpi-paises/
├── main.py           → Menú principal y flujo del programa
├── datos.py          → Carga, guardado, alta y actualización de países
├── busqueda.py       → Búsqueda y filtros por continente, población y superficie
├── ordenamiento.py   → Ordenamiento con Bubble Sort mejorado
├── estadisticas.py   → Estadísticas del dataset (máximos, mínimos, promedios)
├── utils.py          → Funciones de visualización compartidas
├── paises.csv        → Dataset base (21 países)
└── README.md         → Este archivo
```

---

## Integrantes y participación

| Integrante | GitHub | Módulos a cargo |
|------------|--------|-----------------|
| Franco Ezequiel Ventrice | [@ventricef012-ai](https://github.com/ventricef012-ai) | `datos.py`, `ordenamiento.py`, `utils.py` |
| Geronimo Jose Cardoso | [@geroc-py](https://github.com/geroc-py) | `busqueda.py`, `estadisticas.py`, `utils.py` |

---

## Links

- 📹 **Video demostrativo:** https://youtu.be/V4lHhQ9NKlU
- 📄 **Documentación PDF:** [Ver documento](https://docs.google.com/document/d/1WmU190k_7FWe5UHriI9qNp_Xp7j8HZ-M4s4sZcBMTyA/edit?usp=sharing)

