class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_dato(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)#si usamos la función super, no es necesario self
        self.grado = grado

    def mostrar_grado(self):
        return f'Grado: {self.grado}'
    
estudiante = Estudiante('Juan', 20, '10mo')

print(estudiante.mostrar_dato())
print(estudiante.mostrar_curso())


    