# FastAPI
FastAPI es un framework de desarrollo web de alto rendimiento para Python. Permite crear aplicaciones web de manera rápida y eficiente, aprovechando las características modernas de Python, como la tipificación estática y la asincronía. Con FastAPI, puedes construir APIs robustas y escalables de forma sencilla, gracias a su enfoque en la simplicidad y la productividad del desarrollador. Además, FastAPI ofrece una documentación automática y interactiva, lo que facilita la comprensión y el uso de las APIs creadas. En resumen, FastAPI es una excelente opción para desarrolladores que buscan construir aplicaciones web rápidas, seguras y fáciles de mantener en Python.

## Configuración de un servidor con FastAPI
priemra mente instalaremos fastAPI

``` SH
pip install fastapi
```

ahora Crearemos n entorno virtual (venv): Se creó un entorno virtual utilizando venv. 
- Un entorno virtual es un ambiente aislado que permite instalar y gestionar paquetes de Python específicos para un proyecto, sin afectar al sistema global.

``` sh
python -m venv nombre_del_entorno
```

Activación del entorno virtual: Se activó el entorno virtual para asegurar que las dependencias se instalen y se ejecuten dentro de este entorno aislado.
``` sh
source nombre_del_entorno/bin/activate  # En sistemas basados en Unix
```

### Instalación de Uvicorn: 

Uvicorn es un servidor ASGI (Asynchronous Server Gateway Interface) que se utiliza para ejecutar aplicaciones FastAPI de manera asincrónica. Se instaló Uvicorn dentro del entorno virtual.
``` sh
pip install uvicorn
```
Desarrollo de una aplicación FastAPI simple: Se creó un archivo Python con un código mínimo de FastAPI. El código define una instancia de la clase FastAPI y una ruta (/) que responde con un mensaje "Hello world!" cuando se realiza una solicitud GET.


### inicalizar el servicio uvicorn

para iniciar esto se usa el comando 


```sh
uvicorn nombre_del_archivo:app --reload --host 0.0.0.0 --port 8000`
```

- -`reload`: Esta opción indica a Uvicorn que recargue automáticamente la aplicación cuando se realicen cambios en el código fuente. Esto es útil durante el desarrollo, ya que no tienes que reiniciar manualmente el servidor cada vez que realices cambios en tu código.
- `--host` 0.0.0.0: Esta opción especifica la dirección IP en la que el servidor escuchará las solicitudes entrantes. En este caso, "0.0.0.0" significa que el servidor estará disponible en todas las interfaces de red.
- `--port 8000:` Esta opción especifica el número de puerto en el que el servidor escuchará las solicitudes entrantes. En este caso, el servidor estará disponible en el puerto 8000.
[!NOTE]
>
> este comando ejecutará tu aplicación web utilizando el servidor Uvicorn, permitiéndote acceder a ella en la dirección IP y puerto especificados. Además, Uvicorn se encargará de recargar automáticamente la aplicación cuando realices cambios en el código fuente.