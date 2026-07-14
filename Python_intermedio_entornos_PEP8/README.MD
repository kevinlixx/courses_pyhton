# Python intermedio: entornos virtales y PEP8

## PEP8

- EL PEP8 es una guía de estilo para escribir código en Python. Su objetivo es mejorar la legibilidad y consistencia del código, facilitando su mantenimiento y colaboración entre desarrolladores.
- Algunas de las recomendaciones más importantes del PEP8 incluyen:
    - Usar nombres de variables y funciones descriptivos y en minúsculas, separados por guiones bajos (snake_case).
    - Usar 4 espacios para la indentación.
    - Limitar la longitud de las líneas a 79 caracteres.
- una extension en visual studio code que nos ayuda a seguir el formato es `ruff` esta extension nos ayuda a seguir el formato de PEP8 y nos da sugerencias para mejorar nuestro código.

## List comprehensions
- Las list comprehensions son una forma concisa y eficiente de crear listas en Python. Permiten generar nuevas listas aplicando una expresión a cada elemento de una secuencia o iterable, opcionalmente filtrando elementos según una condición.
- La sintaxis básica de una list comprehension es la siguiente:

```python
#list comprehension
[expresion for elemento in iterable if condicion]

# es como si en un bucle for normal hiciéramos lo siguiente:
nueva_lista = []
for elemento in iterable:
    if condicion:
        nueva_lista.append(expresion)
    
```

### donde usar list comprehensions
- Las list comprehensions son útiles cuando se desea crear una nueva lista a partir de una existente, aplicando una transformación o filtrando elementos. Son especialmente útiles en situaciones donde se necesita generar listas de manera concisa y legible, evitando la necesidad de escribir bucles for explícitos. Algunos ejemplos de uso incluyen:
- Filtrar elementos de una lista según una condición.
- Aplicar una función a cada elemento de una lista.

## f - strings
- Las f-strings, introducidas en Python 3.6, son una forma de formatear cadenas de texto de manera más legible y concisa. Permiten incrustar expresiones dentro de cadenas utilizando llaves `{}` y el prefijo `f` antes de la cadena. Esto facilita la creación de cadenas dinámicas y mejora la legibilidad del código.

``` python 
# Usando métodos de cadena
autor = "gabriel garcia"
print(f"Libro escrito por {autor.title()}.")
# Salida: Libro escrito por Gabriel Garcia.


# Usando expresiones matemáticas
precio_unitario = 10.5
cantidad = 3
total = precio_unitario * cantidad
print(f"El total es: {total}")
# Salida: El total es: 31.5


# Accediendo a diccionarios
persona = {"nombre": "Juan", "edad": 25}
print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")
# Salida: Nombre: Juan, Edad: 25


# Formato de números (ej. solo un decimal)
puntuacion = 95.12345
print(f"Tu puntuación es {puntuacion:.1f}")
# Salida: Tu puntuación es 95.1

# Depuración (Python 3.8+)
valor = 100
print(f"{valor=}")  # Muestra la variable y su valor
# Salida: valor=100
```

### Specifers in python
- Los especificadores de formato en Python se utilizan para controlar cómo se representan los valores al formatear cadenas.
- Algunos de los especificadores más comunes incluyen:
- `d`: Entero decimal.
- `f`: Número de punto flotante.
- `s`: Cadena de texto.
- `x`: Entero hexadecimal (minúsculas).

ejemplo:

```python
# Formateo de enteros
numero = 42
print(f"El número es: {numero:d}")  # Salida: El número es: 42

# Formateo de flotantes
pi = 3.14159
print(f"El valor de pi es: {pi:.2f}")  # Salida: El valor de pi es: 3.14

# Formateo de cadenas
nombre = "Alice"
print(f"Hola, {nombre:>12}")  # Alineación a la derecha con un ancho de 12 caracteres
# Salida: Hola,        Alice

#date
fecha = datetime.now()
print(f"La fecha actual es: {fecha:%Y-%m-%d}")  # Salida: La fecha actual es: 2023-10-01

#porcentaje
porcentaje = 0.85
print(f"El porcentaje es: {porcentaje:.2%}")  # Salida: El porcentaje s: 85.00%
```

## 
