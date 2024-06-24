class Animal:
    def comer(self):
        print("Comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando")

class Ave(Animal):
    def volar(self):
        print("Volando")

class Murcielago(Mamifero, Ave):
    pass 

m = Murcielago()
m.comer()
m.amamantar()
m.volar()
print(Murcielago.mro())
    