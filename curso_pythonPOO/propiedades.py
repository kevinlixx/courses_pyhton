class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property #indica que es una propiedad
    def nombre(self):#muestra el nombre
        return self.__nombre
    
    @nombre.setter #permite modificar el nombre
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter #permite eliminar el nombre
    def nombre(self):
        del self.__nombre


# nos permite encapsular los atributos de la clase
dato = Persona("Juan", 30)
print(dato.nombre)
#cambiar el nombre
dato.nombre = "Carlos"
print(dato.nombre)
#eliminar el atributo

del dato.nombre

