class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad



class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas, universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad
    #pass  la palabra clave pass se usa para evitar errores de sintaxis

class Artista:
    def __init__(self,habilidad):
        self.habilidad= habilidad
    def mostrar_habilidad(self):
        return f"mi hablidad es {self.habilidad}"
    
class Empleado(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad, empresa,salario):
        super().__init__(nombre,edad,nacionalidad) # super() es una referencia a la clase padre
        self.empresa = empresa
        self.salario = salario

    def presentarse(self):
        return f"Hola soy {self.nombre} y trabajo en {self.empresa} y mi salario es {self.salario}"

roberto = Empleado("roberto",25,"mexicana","pintar","google",1000)

print(roberto.presentarse())