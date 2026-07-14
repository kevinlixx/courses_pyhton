"""
Módulos en Python
=================
Un módulo es un archivo .py que contiene código reutilizable.
Un paquete es una carpeta con módulos + __init__.py.
"""

# ============================================================
# 1. IMPORTAR MÓDULOS DE LA LIBRERÍA ESTÁNDAR
# ============================================================

import math
import os
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# math — funciones matemáticas
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Redondeo hacia arriba: {math.ceil(4.2)}")
print(f"Redondeo hacia abajo: {math.floor(4.8)}")

# os — interactuar con el sistema
print(f"\nDirectorio actual: {os.getcwd()}")
print(f"Usuario: {os.getenv('USER', 'desconocido')}")

# json — trabajar con JSON
datos = {"nombre": "Kevin", "edad": 25, "activo": True}
json_str = json.dumps(datos, indent=2)
print(f"\nJSON serializado:\n{json_str}")

datos_parseados = json.loads(json_str)
print(f"Nombre: {datos_parseados['nombre']}")

# random — números aleatorios
print(f"\nNúmero aleatorio (0-100): {random.randint(0, 100)}")
print(f"Elegir de lista: {random.choice(['Python', 'JS', 'Go', 'Rust'])}")
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(f"Lista mezclada: {lista}")

# datetime — fechas y horas
ahora = datetime.now()
print(f"\nFecha actual: {ahora.strftime('%d/%m/%Y %H:%M')}")
en_una_semana = ahora + timedelta(days=7)
print(f"En una semana: {en_una_semana.strftime('%d/%m/%Y')}")

# pathlib — rutas de archivos
ruta = Path(".")
print(f"\nArchivos .py en este directorio:")
for archivo in ruta.glob("*.py"):
    print(f"  - {archivo.name}")

# ============================================================
# 2. FORMAS DE IMPORTAR
# ============================================================

# Forma 1: importar todo el módulo
import math as m
print(f"\nRaíz con alias: {m.sqrt(25)}")

# Forma 2: importar algo específico
from math import sqrt, pi, ceil
print(f"sqrt directo: {sqrt(36)}")
print(f"pi directo: {pi}")
print(f"ceil directo: {ceil(3.1)}")

# Forma 3: importar con alias
from datetime import datetime as dt
print(f"Fecha con alias: {dt.now().strftime('%Y-%m-%d')}")

# ============================================================
# 3. CREAR TU PROPIO MÓDULO
# ============================================================

# Este archivo ES un módulo. Si lo importás, podés usar sus funciones.
# Pero las funciones de abajo solo se ejecutan si corrés este archivo directamente.

def saludar(nombre: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}! Bienvenido a Python."

def despedir(nombre: str) -> str:
    """Devuelve una despedida personalizada."""
    return f"Chau, {nombre}! Vuelva pronto."

def sumar(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

def es_par(numero: int) -> bool:
    """Verifica si un número es par."""
    return numero % 2 == 0

def factorial(n: int) -> int:
    """Calcula el factorial de n."""
    if n < 0:
        raise ValueError("No existe factorial de números negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# ============================================================
# 4. __name__ y __main__
# ============================================================

# Este bloque solo se ejecuta si corrés: python modules.py
# NO se ejecuta si hacés: import modules
if __name__ == "__main__":
    print("\n--- Probando funciones del módulo ---")
    print(saludar("Kevin"))
    print(despedir("Kevin"))
    print(f"2 + 3 = {sumar(2, 3)}")
    print(f"¿7 es par? {es_par(7)}")
    print(f"5! = {factorial(5)}")
    print(f"0! = {factorial(0)}")

# ============================================================
# 5. ESTRUCTURA DE UN PAQUETE
# ============================================================

# mi_paquete/
# ├── __init__.py          → hace que sea un paquete
# ├── matematica.py        → funciones matemáticas
# ├── texto.py             → funciones de texto
# └── archivos.py          → funciones de archivos
#
# En __init__.py podés exportar:
# from .matematica import sumar, restar
# from .texto import saludar
#
# En main.py:
# from mi_paquete import sumar, saludar

# ============================================================
# 6. DIR() — VER QUÉ TIENE UN MÓDULO
# ============================================================

print("\n--- Atributos del módulo math ---")
print([attr for attr in dir(math) if not attr.startswith("_")])

# ============================================================
# RESUMEN
# ============================================================
# - Módulo = archivo .py con código reutilizable
# - Paquete = carpeta con __init__.py
# - import trae todo, from X import Y trae algo específico
# - __name__ == "__main__" para código que solo corre directamente
# - La librería estándar tiene módulos para todo
