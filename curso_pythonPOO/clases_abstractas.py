from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.sexo} y trabajo como {self.trabajo}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    def hacer_actividad(self):
        print(f"Estudiando {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.trabajo = actividad
    
    def hacer_actividad(self):
        print(f"Trabajando como {self.trabajo}")

dalto = Estudiante("Dalto", 25, "Hombre", "Python")
dalto.hacer_actividad()
pedro = Trabajador("Pedro", 30, "Hombre", "Ingeniero")
pedro.hacer_actividad()