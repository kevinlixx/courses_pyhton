"""
Type Hints en Python
====================
Los type hints son ANOTACIONES (no restricciones) que le indican al lector
y al IDE qué tipo de datos espera cada variable, parámetro o retorno.

NO validan en tiempo de ejecución — Python no tira error si pasás algo distinto.
Para que realmente validen, usá herramientas como `mypy` o `pyright`.
"""

# ============================================================
# 1. TIPOS BÁSICOS
# ============================================================
# Se declara con `variable: tipo = valor`

variable: int = 42
nombre: str = "Kevin"
altura: float = 1.75
activo: bool = True

print(f"variable: {variable}, del tipo {type(variable)}")
print(f"nombre: {nombre}, del tipo {type(nombre)}")

# OJO: los type hints NO validan en runtime
# Esto NO tira error, a pesar del type hint:
# variable: int = "soy un string"  ← Python lo permite igual

# ============================================================
# 2. OPTIONAL — Puede ser un tipo o None
# ============================================================
# Equivale a: tipo | None

user_id: int | None = None  # Python 3.10+
# forma anterior: Optional[int] = None

# ============================================================
# 3. LISTAS, DICCIONARIOS, TUPLES
# ============================================================
# Python 3.9+ usa minúsculas: list, dict, tuple
# Python anterior necesita importar: List, Dict, Tuple

notas: list[int] = [10, 8, 9]
edades: dict[str, int] = {"Ana": 25, "Juan": 30}
coordenadas: tuple[float, float] = (1.5, 2.3)

# ============================================================
# 4. UNION — Puede ser uno de varios tipos
# ============================================================

def procesar(valor: str | int) -> str:
    """Recibe str o int, devuelve str siempre."""
    return str(valor)

print(procesar(42))       # "42"
print(procesar("hola"))   # "hola"

# ============================================================
# 5. TYPE HINTS EN FUNCIONES
# ============================================================
# Se usa `-> tipo` para indicar qué devuelve

def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

def sumar_numeros(numeros: list[int]) -> int:
    return sum(numeros)

def buscar_usuario(user_id: int) -> dict[str, str | int] | None:
    """Simula buscar un usuario. Devuelve dict o None."""
    usuarios = {1: {"nombre": "Ana", "edad": 25}}
    return usuarios.get(user_id)

print(saludar("Kevin"))
print(sumar_numeros([1, 2, 3, 4]))

# ============================================================
# 6. TIPO PERSONALIZADO CON TYPE ALIAS
# ============================================================

UserDict = dict[str, str | int]

def crear_usuario(nombre: str, edad: int) -> UserDict:
    return {"nombre": nombre, "edad": edad}

# ============================================================
# 7. CLASES COMO TYPE HINTS
# ============================================================

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

def presentar(persona: Persona) -> str:
    return f"Soy {persona.nombre}, tengo {persona.edad} años"

kevin = Persona("Kevin", 25)
print(presentar(kevin))

# ============================================================
# 8. NIL — Valor especial para "no retornado"
# ============================================================

def imprimir_mensaje(msg: str) -> None:
    """Solo imprime, no devuelve nada有意义."""
    print(msg)

# ============================================================
# RESUMEN
# ============================================================
# - Los type hints son DOCUMENTACIÓN, no reglas de ejecución
# - Sirven para: autocompletado del IDE, detección con mypy, legibilidad
# - No obligan: Python permite ignorarlos en runtime
# - Para validar estáticamente: pip install mypy && mypy archivo.py
