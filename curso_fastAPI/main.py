from fastapi import FastAPI, Body #Importamos la clase FastAPI, Body
from fastapi.responses import HTMLResponse #Importamos la clase HTMLResponse

app = FastAPI() #Instanciamos la clase FastAPI
app.title = "My API" #Definimos el título de la API
app.version = "0.0.1" #Definimos la versión de la API

movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "year": 1994,
        "duration": 142,
        "category": "drama"
    }
]

@app.get('/', tags= ["home"]) #Definimos una ruta para el método GET se coloca el @ debido ya que es un decorador y un decorador es una función que recibe otra función como argumento, es decir, es una función que modifica a otra función.
def message():
    return  HTMLResponse(content="<h1>Welcome to my API</h1>", status_code=200) # Retornamos un mensaje en HTML


@app.get('/movies', tags=['movies']) #Definimos una ruta para el método GET
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

#Parametros Query

@app.get("/movies", tags=["movies"]) # cuando no se especifica en la ruta lo tomara como un parametro Query

def get_movies_by_Categories(category: str, year: int):
    return [ item for item in movies if item["category"] == category]

# Metodo POST

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

# Metodo PUT

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

# Metodo DELETE
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for index, item in enumerate(movies):
        if item["id"] == id:
            movie = movies.pop(index)
            return movie
    return []
 
