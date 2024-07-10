class Personaje:
    lista_personajes = []
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"Personaje('{self.nombre}', {self.fuerza}, {self.velocidad})"

    def __add__(self, otro_pj):
        self.nombre = self.nombre + "-" + otro_pj.nombre
        self.fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        self.velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(self.nombre, self.fuerza, self.velocidad)
    
    @classmethod #sirve para crear metodos de clase es decir que no necesitan una instancia para ser llamados
    def crear_personaje(cls): # se pone el cls como parametro para indicar que es un metodo de clase
        nombre = input("Dame el nombre del personaje: ")
        fuerza = float(input("¿Que fuerza tendra el personaje?: "))
        velocidad = float(input("¿ Que velodicad tendra el personaje?: "))
        personaje= Personaje(nombre,fuerza, velocidad)
        cls.lista_personajes.append(personaje)
    
    @classmethod
    def modificar_personaje(lista_personajes):
        name= str(int("dime el nombre del personaje que quieres modificar: "))
        for personaje in cls.lista_personaje:
            if personaje.nombre == nombre:
                new_fuerza = float(input("dime la nueva fuerza"))
                new_velocidad = float(input("dime la nueva velocidad"))
                personaje.fuerza = new_fuerza
                personaje.velocidad = new_velocidad
    @classmethod
    def consultar_personaje(cls):
        if not cls.lista_personajes: #verifica si la lista esta vacia
                print("no hay ningun personaje por favor crea uno \n")
        for personaje in cls.lista_personajes:
            print(personaje)
            option=int(input("¿que quieres hacer ahora? \n 1. regresar al menu principal \n 2. finalizar \n"))
            if option == 2:
                return "finalizar"

    @classmethod
    def eliminar_personaje(cls):
        nombre = input("Dame el nombre del personaje a eliminar: ")
        for i, personaje in enumerate(cls.lista_personajes):
            if personaje.nombre == nombre:
                del cls.lista_personajes[i]
                print("Personaje eliminado exitosamente.")
                return
        print("Personaje no encontrado.")
    
    @classmethod
    def fusionar(cls):
        primer_personaje= str(input("dime el primer personaje"))
        for personaje in cls.lista_personaje:
            if personaje.nombre == primer_personaje:
                segundo_personaje = str(input("dime el segundo personaje"))
                if personaje.nombre == segundo_personaje:
                    fusion = primer_personaje + segundo_personaje
                    return fusion
                else:
                    print("segundo personaje no existe")
            else:
                print("el primer personaje no existe")
    
def run_game():

    while True:
        option = int(input(f"Escoge una opción: \n 1. crear un personaje \n 2. modificar un personaje \n 3. consultar  personajes \n 4. Eliminar un personaje \n 5.fusionar personajes \n 6.finalizar \n  " Persona.lista_personajes))
        if option == 1:
            Personaje.crear_personaje()
        elif option == 2:
            Personaje.modificar_personaje()
        elif option == 3:
            resultado= Personaje.consultar_personaje()
            if resultado == "finalizar":
                break
        elif option == 4:
            Personaje.eliminar_personaje()
        elif option == 5:
            resultado= Personaje.fusionar()
            print(f"tu fusión quedaria asi: {resultado}")
        elif option == 6:
            print("gracias por jugar, ten buen día :3")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
        
run_game()