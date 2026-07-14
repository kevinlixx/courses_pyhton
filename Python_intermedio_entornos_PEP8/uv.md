# UV — Gestor de dependencias y proyectos Python

**UV** es un gestor de dependencias y proyectos Python escrito en **Rust**. Es 10-100x más rápido que pip y reemplaza muchas herramientas que antes necesitabas por separado.

---

## ¿Qué reemplaza?

| Herramienta | UV la reemplaza con |
|-------------|---------------------|
| `pip` | `uv pip install` |
| `virtualenv` / `venv` | `uv venv` |
| `pip-tools` | `uv pip compile` |
| `pipx` | `uv tool install` |
| `pyenv` | `uv python install` |
| `poetry` | `uv init` + `uv add` |

---

## Instalación

```bash
# Linux/Mac
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Con pip (si ya tenés Python)
pip install uv
```

---

## Crear un proyecto nuevo

```bash
# Crear proyecto con estructura básica
uv init mi-proyecto
cd mi-proyecto

# Esto genera:
# - pyproject.toml    → configuración del proyecto
# - uv.lock           → lockfile de dependencias
# - .python-version   → versión de Python a usar
# - hello.py          → archivo de ejemplo
```

---

## Gestionar dependencias

```bash
# Agregar dependencia
uv add requests

# Agregar dependencia de desarrollo
uv add pytest --dev

# Agregar varias a la vez
uv add flask sqlalchemy redis

# Remover dependencia
uv remove requests

# Ver dependencias instaladas
uv pip list
```

---

## Entornos virtuales

```bash
# Crear venv (automático con uv init)
uv venv

# Activar venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows

# Sincronizar entorno con dependencias
uv sync

# Desactivar
deactivate
```

---

## Instalar versiones de Python

```bash
# Ver versiones disponibles
uv python list

# Instalar una versión específica
uv python install 3.12
uv python install 3.11 3.12 3.13

# Usar una versión específica en un proyecto
uv python pin 3.12
```

---

## Lockfile (uv.lock)

UV genera un `uv.lock` que garantiza que TODOS usen las mismas versiones:

```bash
# Generar/actualizar lockfile
uv lock

# Instalar desde lockfile (reproduce el entorno exacto)
uv sync
```

**Ventaja sobre requirements.txt:** el lockfile es cross-platform y determinístico.

---

## Interfaz compatible con pip

Si ya usás pip, UV funciona igual pero más rápido:

```bash
# Reemplaza: pip install flask
uv pip install flask

# Reemplaza: pip install -r requirements.txt
uv pip install -r requirements.txt

# Reemplaza: pip freeze > requirements.txt
uv pip freeze > requirements.txt

# Reemplaza: pip list
uv pip list
```

---

## Scripts con dependencias inline

UV puede ejecutar scripts Python con dependencias definidas en el mismo archivo:

```python
# script.py
# /// script
# dependencies = [
#   "requests",
#   "rich",
# ]
# ///

import requests
from rich import print

response = requests.get("https://httpbin.org/json")
print(response.json())
```

```bash
# Ejecutar el script
uv run script.py
```

---

## Workspaces (proyectos múltiples)

```bash
# Inicializar workspace
uv init --workspace mi-workspace

# Agregar paquetes al workspace
uv init --package paquete-uno
uv init --package paquete-dos
```

Estructura:
```
mi-workspace/
├── pyproject.toml        → config del workspace
├── uv.lock               → lockfile compartido
├── paquete-uno/
│   ├── pyproject.toml
│   └── ...
└── paquete-dos/
    ├── pyproject.toml
    └── ...
```

---

## Instalar herramientas CLI

```bash
# Instalar herramienta globalmente (como pipx)
uv tool install ruff
uv tool install black

# Ejecutar herramienta sin instalar
uvx ruff check .
uvx black .

# Listar herramientas instaladas
uv tool list
```

---

## Ejemplo completo: proyecto nuevo

```bash
# 1. Crear proyecto
uv init mi-api
cd mi-api

# 2. Agregar dependencias
uv add fastapi uvicorn sqlalchemy

# 3. Agregar dependencias de desarrollo
uv add pytest ruff --dev

# 4. Verificar entorno
uv sync

# 5. Ejecutar proyecto
uv run python main.py

# 6. Lockear para deploy
uv lock
```

---

## Comparación: pip + venv vs UV

| Aspecto | pip + venv | UV |
|---------|------------|-----|
| Velocidad | Lento | 10-100x más rápido |
| Lockfile | No (necesitás requirements.txt) | Sí (`uv.lock`) |
| Gestión de Python | Necesitás pyenv | UV instala Python |
| Workspaces | No | Sí |
| Scripts | No | Sí (inline metadata) |
| Herramientas CLI | Necesitás pipx | UV las instala |
| Cross-platform | Parcial | Sí |

---

## Comandos rápidos de referencia

```bash
uv init                    # Crear proyecto
uv add <paquete>           # Agregar dependencia
uv remove <paquete>        # Remover dependencia
uv sync                    # Sincronizar entorno
uv lock                    # Generar lockfile
uv run <script>            # Ejecutar script
uv venv                    # Crear venv
uv python install <ver>    # Instalar Python
uvx <herramienta>          # Ejecutar herramienta
uv pip install <paquete>   # Instalar con interfaz pip
```

---

## Ventajas

- **Velocidad**: escrito en Rust, cache global agresivo
- **Unificado**: una herramienta para todo
- **Determinístico**: lockfile cross-platform
- **Sin dependencias**: se instala sin necesitar Python previo
- **Compatible**: funciona con pyproject.toml existente
- **Workspaces**: soporte nativo para proyectos múltiples
