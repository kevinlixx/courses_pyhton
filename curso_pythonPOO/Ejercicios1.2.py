class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando")

nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad del estudiante: ")
grado = input("Ingrese el grado del estudiante: ")

Estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE \n
        Nombre: {Estudiante.nombre}
        Edad: {Estudiante.edad}
        Grado: {Estudiante.grado}
    """)
while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        Estudiante.estudiar()
