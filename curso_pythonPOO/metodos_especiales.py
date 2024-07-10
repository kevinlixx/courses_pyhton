class Persona:
    def __init__(self, nombre, edad, sexo): #el __init__ es un metodo especial que contruye el objeto
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def __str__(self): #el __str__ es un metodo especial que retorna una representacion en string del objeto
        return f"Nombre:{self.nombre}, Edad: {self.edad}, Sexo:'{self.sexo}"
    
    def __repr__(self): # el __repr__ es un metodo especial que retorna una representacion en string del objeto
        return f"Persona('{self.nombre}', {self.edad}, '{self.sexo}')"
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor, self.sexo)
    
dalto = Persona("Dalto", 25, "Hombre")
pedro = Persona("Pedro", 30, "Hombre")

repre = repr(dalto)
resultado = eval(repre)
print(resultado.nombre)

nueva_persona = dalto + pedro
print(nueva_persona.nombre)

