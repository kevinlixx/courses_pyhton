from fastapi import FastAPI # Importamos la clase FastAPI

app = FastAPI() # Instanciamos la clase FastAPI
app.title = "My API" # Definimos el título de la API
app.version = "0.0.1" # Definimos la versión de la API

@app.get('/', tags= ["home"]) # Definimos una ruta para el método GET se coloca el @ debido ya que es un decorador y un decorador es una función que recibe otra función como argumento, es decir, es una función que modifica a otra función.
def message():
    return  "Hello World"