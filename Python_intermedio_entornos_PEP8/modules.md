# Módulos en Python

Un **módulo** es un archivo `.py` que contiene código (funciones, clases, variables) que podés **reusar** en otros archivos. Un **paquete** es una carpeta con módulos.

---

## El problema que resuelven

Sin módulos, tendrías TODO en un solo archivo gigante:

```python
# archivo.py con 5000 líneas... IMPOSIBLE de mantener
```

Con módulos, separás el código por responsabilidades:

```
proyecto/
├── main.py          → usa todo
├── funciones.py     → funciones auxiliares
├── clases.py        → clases del sistema
└── constants.py     → constantes
```

---

## Crear un módulo

Es simplemente crear un archivo `.py`:

```python
# saludos.py
def saludar(nombre):
    return f"Hola, {nombre}"

def despedir(nombre):
    return f"Chau, {nombre}"
```

---

## Importar un módulo

### Forma 1: Importar todo el módulo

```python
import saludos

print(saludos.saludar("Kevin"))   # "Hola, Kevin"
print(saludos.despedir("Kevin"))  # "Chau, Kevin"
```

### Forma 2: Importar algo específico

```python
from saludos import saludar

print(saludar("Kevin"))  # "Hola, Kevin"
# despedir() no está disponible porque no se importó
```

### Forma 3: Importar con alias

```python
import saludos as s

print(s.saludar("Kevin"))  # "Hola, Kevin"
```

### Forma 4: Importar todo (NO recomendado)

```python
from saludos import *

print(saludar("Kevin"))  # funciona, pero no sabés de dónde viene
```

---

## Módulos de la librería estándar

Python ya trae módulos listos para usar:

| Módulo | Para qué sirve |
|--------|----------------|
| `os` | Interactuar con el sistema operativo |
| `sys` | Configuración del sistema |
| `json` | Trabajar con JSON |
| `datetime` | Fechas y horas |
| `random` | Números aleatorios |
| `math` | Funciones matemáticas |
| `re` | Expresiones regulares |
| `pathlib` | Rutas de archivos |
| `collections` | Estructuras de datos especiales |
| `itertools` | Iteradores |
| `functools` | Funciones de orden superior |

### Ejemplos comunes

```python
import math
math.sqrt(16)      # 4.0
math.pi            # 3.14159...
math.ceil(4.2)     # 5
math.floor(4.8)    # 4

import os
os.getcwd()        # directorio actual
os.getenv("USER")  # usuario del sistema

import json
datos = {"nombre": "Kevin"}
json_str = json.dumps(datos)      # dict → string JSON
datos = json.loads(json_str)      # string JSON → dict

from datetime import datetime, timedelta
ahora = datetime.now()
en_una_semana = ahora + timedelta(days=7)

import random
random.randint(0, 100)            # número aleatorio
random.choice(["a", "b", "c"])    # elegir de lista
```

---

## `__name__` y `__main__`

```python
# calculadora.py
def sumar(a, b):
    return a + b

# Este código solo se ejecuta si corro ESTE archivo directamente
# No se ejecuta si lo importo desde otro archivo
if __name__ == "__main__":
    print("Probando la calculadora...")
    print(sumar(2, 3))
```

**¿Por qué?** Cuando importás un módulo, Python ejecuta todo el código del archivo. `__name__` es una variable especial que:
- Vale `"__main__"` si corrés el archivo directamente
- Vale el nombre del módulo si lo importás

---

## Crear un paquete

Cuando tenés MUCHOS módulos, los organizás en carpetas:

```
mi_paquete/
├── __init__.py      → hace que la carpeta sea un paquete
├── matematica.py
├── texto.py
└── archivos.py
```

### `__init__.py`

Puede estar vacío o exportar cosas:

```python
# mi_paquete/__init__.py
from .matematica import sumar, restar
from .texto import saludar
```

### Usar el paquete

```python
# main.py
from mi_paquete import sumar, saludar

print(sumar(2, 3))      # 5
print(saludar("Kevin"))  # "Hola, Kevin"
```

---

## `dir()` — ver qué tiene un módulo

```python
import math

# Ver todos los atributos del módulo
print(dir(math))

# Filtrar solo los públicos
print([attr for attr in dir(math) if not attr.startswith("_")])
```

---

## Resumen

| Concepto | Qué es |
|----------|--------|
| Módulo | Archivo `.py` con código reutilizable |
| Paquete | Carpeta con módulos + `__init__.py` |
| `import` | Trae el módulo completo |
| `from X import Y` | Trae algo específico |
| `as` | Le pone un alias |
| `if __name__ == "__main__"` | Código que solo corre si ejecutás el archivo |
| `dir()` | Lista los atributos de un módulo |
| Librería estándar | Módulos que vienen con Python |
