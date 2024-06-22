class Celular:  # pascal case (la primera letra de cada palabra en mayúscula)
    def __init__(self, marca, modelo, camara):  # el self es una referencia a la instancia actual de la clase
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo un llamado desde un celular {self.marca}") #el f es para concatenar variables con texto
        
Celular1 = Celular("samsung", "s23", "48MP")  # este objeto es una instancia de la clase Celular
Celular2 = Celular("iphone", "12", "12MP")

Celular1.llamar()  # Corregido para llamar al método correctamente
Celular2.llamar()  # Corregido para llamar al método correctamente
