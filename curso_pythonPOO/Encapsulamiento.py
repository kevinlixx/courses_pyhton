class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):#muestra el nombre
        return self.__nombre
    
    def set_nombre(self, nombre):#permite cambiar el nombre 
        self.__nombre = nombre  

dato = Persona("Juan", 30)
print(dato.get_nombre())# Muestra el nombre

dato.set_nombre("Pedro") #Cambia el nombre

print(dato.get_nombre()) # Muestra el nombre cambiado

