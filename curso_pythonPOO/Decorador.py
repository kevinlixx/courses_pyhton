def decorador(funcion):
    def nueva_funcion():
        print("Podemos agregar código antes")
        funcion()
        print("Podemos agregar código después")
    return nueva_funcion
# forma de usar el decorador
# def saludo():
#     print("Hola!")

# saludo = decorador(saludo)
# saludo()

#forma optima de usar el decorador
@decorador
def saludo():
    print("Hola!")

saludo()
