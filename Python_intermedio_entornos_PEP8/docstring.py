"""
Docstrings en Python
====================
Un docstring es un string literal que aparece como PRIMERA línea
en un módulo, función, clase o método. Sirve como documentación
y se accede con `__doc__`.

La documentación oficial está en el PEP 257.
"""

# ============================================================
# 1. DIFERENCIA: COMENTARIO vs DOCSTRING
# ============================================================

# Esto es un COMENTARIO — se ignora completamente, no se puede acceder
# Python no lo ve como documentación

def ejemplo_sin_docstring():
    """Esto es un docstring — documentación real de la función."""
    return "HOLA, MUNDO"

# Accedés al docstring así:
print(ejemplo_sin_docstring.__doc__)
# Output: Esto es un docstring — documentación real de la función.

# ============================================================
# 2. DOCSTRINGS EN FUNCIONES
# ============================================================
# Estructura básica:
#   1. Línea resumen (qué hace)
#   2. Línea en blanco
#   3. Explicación detallada (si hace falta)
#   4. Args / Returns (documentar parámetros y retorno)

def calcular_area(largo: float, ancho: float) -> float:
    """
    Calcula el área de un rectángulo.

    Multiplica largo por ancho y devuelve el resultado.

    Args:
        largo: La dimensión mayor del rectángulo en unidades lineales.
        ancho: La dimensión menor del rectángulo en unidades lineales.

    Returns:
        El área calculada como largo * ancho.
    """
    return largo * ancho

print(calcular_area.__doc__)

# ============================================================
# 3. DOCSTRINGS EN CLASES
# ============================================================
# Documentás qué representa la clase y sus atributos principales

class Persona:
    """
    Representa una persona con nombre y edad.

    Esta clase se usa para modelar datos básicos de personas
    en el sistema.

    Attributes:
        nombre: Nombre completo de la persona.
        edad: Edad en años.
    """

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

print(Persona.__doc__)

# ============================================================
# 4. DOCSTRINGS EN MÓDULOS
# ============================================================
# El docstring del archivo va AL PRINCIPIO, antes de todo

# Ejemplo (ya lo tenemos arriba en este archivo):
# """
# Docstrings en Python
# ====================
# ...
# """

# ============================================================
# 5. DOCSTRINGS EN MÉTODOS
# ============================================================

class Calculadora:
    """Una calculadora simple con operaciones básicas."""

    def sumar(self, a: float, b: float) -> float:
        """
        Suma dos números.

        Args:
            a: Primer número.
            b: Segundo número.

        Returns:
            La suma de a + b.
        """
        return a + b

    def dividir(self, a: float, b: float) -> float:
        """
        Divide dos números.

        Args:
            a: Dividendo.
            b: Divisor. No puede ser cero.

        Returns:
            El resultado de a / b.

        Raises:
            ZeroDivisionError: Si b es igual a cero.
        """
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b

calc = Calculadora()
print(calc.sumar(10, 5))
print(calc.dividir(10, 2))

# ============================================================
# 6. FORMATOS DE DOCSTRING (PEP 257)
# ============================================================

# Formato GOOGLE (el más usado hoy en día):
def funcion_google(nombre: str) -> str:
    """
    Resumen corto de la función.

    Explicación más detallada si es necesaria.
    Se pueden agregar varios párrafos.

    Args:
        nombre: Descripción del parámetro.

    Returns:
        Descripción del valor que devuelve.

    Raises:
        ValueError: Cuándo se lanza esta excepción.
    """
    return f"Hola, {nombre}"

# Formato NUMPY (común en ciencia de datos):
def funcion_numpy(nombre: str) -> str:
    """
    Resumen de la función.

    Parámetros
    ----------
    nombre : str
        Descripción del parámetro.

    Returns
    -------
    str
        Descripción del retorno.
    """
    return f"Hola, {nombre}"

# Formato SPHINX (el más antiguo):
def funcion_sphinx(nombre: str) -> str:
    """
    Resumen de la función.

    :param nombre: Descripción del parámetro.
    :return: Descripción del retorno.
    :raises ValueError: Si hay un error.
    """
    return f"Hola, {nombre}"

# ============================================================
# 7. ACCEDER A DOCSTRINGS
# ============================================================

print("\n--- Accediendo a docstrings ---")
print(f"Función: {funcion_google.__doc__}")
print(f"Clase: {Persona.__doc__}")
print(f"Método: {Calculadora.sumar.__doc__}")

# Con help() — muestra el docstring formateado
# help(funcion_google)

# ============================================================
# 8. DOCSTRINGS Y TYPE HINTS SE COMPLEMENTAN
# ============================================================
# Los type hints dicen EL TIPO, los docstrings explican EL QUÉ y el POR QUÉ

def transferir(monto: float, cuenta_origen: str, cuenta_destino: str) -> dict[str, str | float]:
    """
    Transfiere dinero entre dos cuentas bancarias.

    Valida que el monto sea positivo y que las cuentas existan.
    Registra la transacción con timestamp.

    Args:
        monto: Cantidad a transferir. Debe ser mayor a 0.
        cuenta_origen: Número de cuenta de origen (10 dígitos).
        cuenta_destino: Número de cuenta de destino (10 dígitos).

    Returns:
        Dict con estado de la operación, fecha y monto.

    Raises:
        ValueError: Si el monto es negativo o las cuentas son iguales.
    """
    if monto <= 0:
        raise ValueError("El monto debe ser mayor a 0")
    if cuenta_origen == cuenta_destino:
        raise ValueError("Las cuentas no pueden ser iguales")
    return {"estado": "exitoso", "monto": monto, "origen": cuenta_origen, "destino": cuenta_destino}

# ============================================================
# RESUMEN
# ============================================================
# - Docstrings = documentación ACCESIBLE (no como comentarios)
# - Van entre triples comillas """
# - Se acceden con __doc__ o help()
# - Formatos: Google (recomendado), NumPy, Sphinx
# - SIEMPRE documentá: funciones públicas, clases y módulos
# - Los type hints dicen QUÉ TIPO, los docstrings dicen QUÉ HACE
