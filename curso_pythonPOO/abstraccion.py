class Auto():
    def __init__(self):
        self._estado = "apagado" #el _ indica que es un atributo protegido
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo")

mi_auto = Auto()
mi_auto.conducir()