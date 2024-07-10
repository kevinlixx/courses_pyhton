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

## Documentación automática con FastAPI
- FastAPI proporciona una documentación automática e interactiva para las APIs creadas, lo que facilita la comprensión y el uso de las mismas. La documentación se genera automáticamente a partir de los tipos de datos y anotaciones de Python utilizados en la definición de las rutas y parámetros de la API.
- Para acceder a la documentación de tu API, simplemente abre un navegador web y navega a la dirección `http://localhost:8000/docs` (o la dirección correspondiente a tu servidor). Verás una interfaz interactiva que muestra todas las rutas disponibles, los parámetros esperados y las respuestas posibles para cada una de ellas. Puedes probar las rutas directamente desde la interfaz, lo que te permite verificar su funcionamiento y comprender mejor cómo interactuar con la API.

<center><img src="https://static.platzi.com/media/user_upload/Captura%20desde%202024-06-15%2018-15-56-b5146310-c086-4336-aa40-4538d74fc91e.jpg"> </center>

### Ejemplo
    ``` python
    from fastapi import FastAPI # Importamos la clase FastAPI

    app = FastAPI() # Instanciamos la clase FastAPI
    app.title = "My API" # Definimos el título de la API
    app.version = "0.0.1" # Definimos la versión de la API

    @app.get('/', tags= ["home"]) # Definimos una ruta para el método GET se coloca el @ debido ya que es un decorador y un decorador es una función que recibe otra función como argumento, es decir, es una función que modifica a otra función.
    def message():
        return  "Hello World"
    ```
## CRUD con FastAPI
### Crear un registro (Método POST)
- Para crear un registro, se utiliza el método POST y se define una ruta que recibe los datos del nuevo registro a crear. El controlador asociado a esta ruta recibe los datos, los valida y los almacena en la base de datos. Luego, devuelve el registro creado como respuesta.
    ``` python
   @app.post('/movies', tags=['movies'])
    def create_movie(id: int = Body(), title: str = Body(), year: int = Body(), duration: int = Body(), category: str = Body()): # l body permite recibir los datos de la petición
        movie = ({
            "id": id,
            "title": title,
            "year": year,
            "duration": duration,
            "category": category
        })
        movies.append(movie)
        return movie
    ```

### Leer un registro (Método GET)
- Para leer un registro, se utiliza el método GET y se define una ruta que recibe un parámetro identificador (ID) para buscar el registro correspondiente en la base de datos. El controlador asociado a esta ruta realiza la búsqueda del registro y lo devuelve como respuesta.
    ``` python
    from fastapi import FastAPI #Importamos la clase FastAPI
    from fastapi.responses import HTMLResponse #Importamos la clase HTMLResponse

    movies = [
        {
            "id": 1,
            "title": "The Shawshank Redemption",
            "release_year": 1994,
            "duration": 142
        }
    ]
    @app.get('/movies/', tags=['movies']) #Definimos una ruta para el método GET
    def get_movies():
        return movies
    
    ```
### Actualizar un registro (Método PUT)
```python    
    @app.put('/movies/{id}', tags=['movies'])
    def update_movie(id: int, title: str = Body(), year: int = Body(), duration: int = Body(), category: str = Body()):
        for item in movies:
            if item["id"] == id:
                item["title"] = title
                item["year"] = year
                item["duration"] = duration
                item["category"] = category
                return item
        return []
```
### Eliminar un registro (Método DELETE)
```python
    @app.delete('/movies/{id}', tags=['movies'])
    def delete_movie(id: int):
        for index, item in enumerate(movies): #enumerate() devuelve un objeto enumerado. Este objeto es una lista de tuplas que contienen el índice y el valor de cada elemento en la lista original.
            if item["id"] == id: 
                movies.pop(index)#pop() elimina el elemento en la posición especificada de una lista y devuelve el elemento eliminado.
                return item
        return []
```

