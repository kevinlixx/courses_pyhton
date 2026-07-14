# Virtual Environments en Python

Un **virtual environment** es una CARPETA AISLADA que tiene su propia instalación de Python y sus propios paquetes. Cada proyecto puede tener el SUYO sin que se pisen entre sí.

Sin virtual environments, todos los proyectos comparten los mismos paquetes instalados globalmente → conflictos de versiones → caos.

> Los virtual environments se crean y gestionan desde la **TERMINAL**, no desde Python.

---

## El problema sin virtual environments

Imaginá esto:
- Proyecto A necesita: `requests==2.28.0`
- Proyecto B necesita: `requests==2.31.0`

Sin virtual environment: ¿cuál instalás? Si instalás la 2.31.0, el Proyecto A se rompe. Si instalás la 2.28.0, el Proyecto B se rompe. Es un desastre.

---

## 1. Crear un virtual environment

Desde la terminal:

```bash
python -m venv mi_entorno
```

Esto crea una carpeta `mi_entorno` con:
- `bin/` o `Scripts/` → ejecutables (python, pip)
- `lib/` → paquetes instalados
- `pyvenv.cfg` → configuración

---

## 2. Activar el virtual environment

**Linux/Mac:**
```bash
source mi_entorno/bin/activate
```

**Windows:**
```bash
mi_entorno\Scripts\activate
```

**Windows (PowerShell):**
```powershell
mi_entorno\Scripts\Activate.ps1
```

Cuando lo activás:
- El prompt cambia: `(mi_entorno) tu_usuario@tu_pc$`
- Python y pip apuntan al entorno, NO al global
- Cualquier paquete que instales va a ESTE entorno

---

## 3. Verificar que está activo

Comandos útiles:

```bash
python --version    # debería mostrar la versión del entorno
which python        # muestra la ruta del Python activo
echo $VIRTUAL_ENV   # muestra la ruta del entorno activo
```

---

## 4. Instalar paquetes dentro del entorno

Una vez activado:

```bash
pip install requests
pip install flask==2.3.0
pip install numpy pandas matplotlib
```

Estos paquetes se instalan SOLO en tu entorno, no globalmente.

---

## 5. Listar paquetes instalados

```bash
pip list              # todos los paquetes
pip freeze            # formato requirements.txt
pip show requests     # info de un paquete específico
```

---

## 6. Exportar dependencias (requirements.txt)

```bash
pip freeze > requirements.txt
```

Esto genera un archivo con todas las dependencias y versiones:
```
flask==2.3.0
requests==2.31.0
numpy==1.24.0
```

Otro dev puede replicar tu entorno con:
```bash
pip install -r requirements.txt
```

---

## 7. Desactivar el entorno

```bash
deactivate
```

Esto te vuelve al Python del sistema.

---

## 8. Eliminar un entorno

Simplemente borrás la carpeta:

```bash
rm -rf mi_entorno        # Linux/Mac
rmdir /s /q mi_entorno   # Windows
```

---

## 9. .gitignore — NUNCA subas el entorno a GIT

Agregá esto a tu `.gitignore`:

```
mi_entorno/
venv/
.venv/
env/
```

El entorno es LOCAL. Solo se sube `requirements.txt`.

---

## Estructura de un virtual environment

```
mi_entorno/
├── bin/                  (Linux/Mac) o Scripts/ (Windows)
│   ├── python            → intérprete Python del entorno
│   ├── pip               → gestor de paquetes del entorno
│   ├── activate          → script para activar
│   └── python3           → symlink a python
├── lib/
│   └── python3.10/
│       └── site-packages/
│           ├── requests/
│           ├── flask/
│           └── ...
├── include/
├── pyvenv.cfg            → configuración del entorno
└── .gitignore            → ignorar archivos del entorno
```

---

## Flujo completo (lo que vas a hacer SIEMPRE)

```bash
# 1. Crear entorno:
python -m venv .venv

# 2. Activar:
source .venv/bin/activate

# 3. Instalar paquetes:
pip install flask requests numpy

# 4. Guardar dependencias:
pip freeze > requirements.txt

# 5. Trabajar en tu proyecto...

# 6. Desactivar cuando terminás:
deactivate
```

---

## Ventajas

- **Aislamiento**: cada proyecto tiene SUS paquetes
- **Reproducibilidad**: requirements.txt replica el entorno
- **Sin conflictos**: Proyecto A puede usar requests 2.28 y B 2.31
- **Limpieza**: si algo se rompe, borras el entorno y creás otro
- **Portabilidad**: cualquier persona puede replicar tu entorno
