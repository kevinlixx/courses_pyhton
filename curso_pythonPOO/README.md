# Python en POO

## ¿Que pasa si no uso POO?
- se vuelve tedioso el codigo
- no es reutilizable el codigo
- no es optimo 

## Clases y objetos
### Clases
- Las clases en Python nos permiten estructurar nuestro software de una manera que modela más de cerca el mundo real, agrupando datos y funcionalidades relacionadas. Usar clases nos ayuda a crear código más reutilizable y fácil de entender.

- Para definir una clase en Python, utilizamos la palabra clave `class`, seguida del nombre de la clase y dos puntos. Dentro de la clase, podemos definir funciones (llamadas métodos) y variables (llamadas atributos) que pertenecen a la clase.

- paa escibir el nombre de la clase se usa pascal case de la siguiente manera `NombreDeLaClase`
>[!NOTE]
> **Pascal case** es una convención de escritura en la que cada palabra en una frase o nombre de una variable comienza con una letra mayúscula. Por ejemplo, `MiVariable`, `MiClase`, `MiMetodo`, etc.


### Objetos
- Un objeto es una instancia de una clase. Cuando creamos un objeto, decimos que estamos instanciando la clase. Podemos crear múltiples objetos a partir de una misma clase, y cada objeto puede tener sus propios valores para los atributos de la clase.


>[!NOTE]
> INSTANCIAR: Crear un objeto a partir de una clase.

## Atributos y métodos

### Atributos
- Los atributos son variables que pertenecen a una clase. Cada objeto que creamos a partir de una clase puede tener sus propios valores para los atributos de la clase.
- Los atributos pueden ser de dos tipos: de instancia y de clase. Los atributos de instancia son propios de cada objeto, mientras que los atributos de clase son compartidos por todos los objetos de una clase.
#### Atributos de instancia
- Los atributos de instancia son propios de cada objeto. Cada objeto puede tener sus propios valores para los atributos de instancia.
- Para acceder a los atributos de instancia de un objeto, utilizamos la notación de punto seguida del nombre del atributo.
- Para definir un atributo de instancia, lo hacemos dentro de un método especial llamado `__init__`. Este método se llama automáticamente cuando creamos un objeto a partir de una clase.
- El método `__init__` recibe como primer parámetro la palabra clave `self`, que hace referencia al objeto que se está creando. Luego, podemos definir los atributos de instancia del objeto utilizando `self.nombre_del_atributo = valor`.

##### ejemplo:
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
persona = Persona("Juan", 30)
```
#### Atributos de clase
- Los atributos de clase son compartidos por todos los objetos de una clase. Si modificamos un atributo de clase, todos los objetos de la clase verán el cambio.
- Para definir un atributo de clase, lo hacemos fuera de cualquier método de la clase, pero dentro de la definición de la clase. Utilizamos la notación de punto seguida del nombre de la clase para acceder a los atributos de clase.
- Los atributos de clase se suelen utilizar para almacenar valores que son comunes a todos los objetos de una clase, como por ejemplo, constantes.

### Métodos
- Los métodos son funciones que pertenecen a una clase. Cada objeto que creamos a partir de una clase puede llamar a los métodos de la clase.

## Herencia
- La herencia es un concepto fundamental en la programación orientada a objetos que nos permite crear nuevas clases a partir de clases existentes. La clase existente se llama clase base o clase padre, y la nueva clase se llama clase derivada o clase hija.
- La herencia nos permite reutilizar el código de la clase base en la clase derivada, evitando la duplicación de código y facilitando la creación de nuevas clases con funcionalidades similares.
- Para definir una clase derivada, utilizamos la siguiente sintaxis: `class NombreDeLaClaseDerivada(NombreDeLaClaseBase):`. Esto indica que la clase derivada hereda de la clase base.
- La clase derivada hereda todos los atributos y métodos de la clase base, y puede añadir nuevos atributos y métodos, o modificar los existentes.
- hay diferentes tipos de herencia:
    - `Herencia simple`: una clase derivada hereda de una sola clase base.
        - ejemplo:
        ```python
        class Animal:
            def __init__(self, nombre):
                self.nombre = nombre
            def hablar(self):
                pass
        class Perro(Animal):
            def hablar(self):
                return "¡Guau!"
        ```
    - `Herencia múltiple`: una clase derivada hereda de múltiples clases base.
        - ejemplo:
        ```python
        class Vehiculo:
            def __init__(self, marca):
                self.marca = marca
        class MotorElectrico:
            def __init__(self, potencia):
                self.potencia = potencia
        class Coche(Vehiculo, MotorElectrico):
            def __init__(self, marca, potencia):
                Vehiculo.__init__(self, marca) # Llamamos al constructor de la clase base Vehiculo
                MotorElectrico.__init__(self, potencia)
        ```

        >[!NOTE]
        > no se usa super() en herencia multiple por que no se sabe de que clase se va a heredar
>[!IMPORTANT]
> el super() se usa para llamar al constructor de la clase padre, es decir a la clase principal
>el self se usa para llamar a los metodos de la misma clase

## MRO (Method Resolution Order)
- orden en el que python busca los metodos en la herencia multiple
- se puede ver con el metodo `mro()` de la clase
- ejemplo:
```python
class A:
    def hablar(self):
        print('Hola desde A')

class B(A):
    def hablar(self):
        print('Hola desde B')

class C(A):
    def hablar(self):
        print('Hola desde C')

class D(B, C):
    pass

d = D()
d.hablar()
```
- en este caso el metodo hablar de la clase B se ejecutara por que es la primera clase que se hereda
- para ver el orden de ejecucion se usa el metodo `mro()` de la clase
```python
print(D.mro())
```
- el resultado sera:
``` sh
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

## Polimorfismo
- El polimorfismo es un concepto fundamental en la programación orientada a objetos que nos permite tratar objetos de diferentes clases de manera uniforme. En otras palabras, el polimorfismo nos permite utilizar un objeto de una clase derivada como si fuera un objeto de la clase base.
- tipos de polimorfismo:
    - `Polimorfismo de herecia`: se puede hacer polimorfismo de herecia cuando se hereda de una clase y se sobreescribe un metodo de la clase padre

    - `Polimorfismo de sobrecarga`: se puede hacer polimorfismo de sobrecarga cuando se sobreescribe un metodo de la clase padre
    - `Polimorfismo de coersión`: se puede hacer polimorfismo de coersión cuando se cambia el tipo de dato de una variable

>[!NOTE]
> en los lenguajes de tipado dinamico no es necesario hacer un polimorfismo de herecia, ya que se puede hacer polimorfismo de sobrecarga

### enlace dinamico
- el enlace dinamico es cuando se llama a un metodo de una clase y se ejecuta el metodo de la clase hija


### enlace estatico
- el enlace estatico es cuando se llama a un metodo de una clase y se ejecuta el metodo de la clase padre

## Encapsulamiento
- El encapsulamiento es un concepto fundamental en la programación orientada a objetos que nos permite ocultar los detalles internos de una clase y proteger los datos de la clase de accesos no autorizados.

- En Python, el encapsulamiento se logra utilizando métodos y atributos privados. Los métodos y atributos privados se definen con dos guiones bajos al principio del nombre, como `__nombre_del_atributo` o `__nombre_del_metodo`.

- cuando solo tiene un guion bajo al principio del nombre del atributo o metodo se le llama protegido

- Los métodos y atributos privados solo pueden ser accedidos desde dentro de la clase en la que se definen. Si intentamos acceder a un método o atributo privado desde fuera de la clase, obtendremos un error.

- Para acceder a los métodos y atributos privados desde fuera de la clase, podemos definir métodos públicos que actúen como interfaz para acceder a los métodos y atributos privados.

```python
class Miclase:
    def __init__(self):
        self._protegido = "Soy protegido"
        self.__muy_privado = "Soy muy privado"
        self.publico = "Soy publico"
```

## Getters y Setters
- Los getters y setters son métodos que nos permiten acceder y modificar los atributos privados de una clase desde fuera de la clase.
### Getters
- Los getters son métodos que nos permiten acceder a los atributos privados de una clase desde fuera de la clase.
- Para definir un getter, creamos un método público que devuelva el valor del atributo privado.

- El nombre del getter suele ser `get_nombre_del_atributo`, donde `nombre_del_atributo` es el nombre del atributo privado al que queremos acceder.

### Setters

- Los setters son métodos que nos permiten modificar los atributos privados de una clase desde fuera de la clase.

- Para definir un setter, creamos un método público que reciba un parámetro y modifique el valor del atributo privado.

- El nombre del setter suele ser `set_nombre_del_atributo`, donde `nombre_del_atributo` es el nombre del atributo privado que queremos modificar.

### Ejemplo
```python
    class Persona:
        def __init__(self, nombre, edad):
            self.__nombre = nombre
            self.__edad = edad
        
        def get_nombre(self):#muestra el nombre
            return self.__nombre
        
        def set_nombre(self, nombre):#permite cambiar el nombre 
            self.__nombre = nombre  

    dato = Persona("Juan", 30) #Crea un objeto de la clase Persona
    print(dato.get_nombre())# Muestra el nombre
    dato.set_nombre("Pedro") #Cambia el nombre
    print(dato.get_nombre()) # Muestra el nombre cambiado
```

## Decoradores
- Los decoradores son una característica avanzada de Python que nos permiten modificar o extender el comportamiento de una función o método.
- Los decoradores se utilizan para añadir funcionalidades a una función o método sin modificar su código.
- Los decoradores se definen utilizando la sintaxis `@nombre_del_decorador` encima de la definición de la función o método que queremos decorar.
- Los decoradores pueden recibir argumentos, lo que nos permite personalizar su comportamiento.
- Los decoradores se utilizan en la programación orientada a objetos para añadir funcionalidades a los métodos de una clase, como por ejemplo, la validación de datos o la medición del tiempo de ejecución de un método.

### Ejemplo
    ```python
        def decorador(funcion):
            def nueva_funcion():
                print("Antes de llamar a la función")
                funcion()
                print("Después de llamar a la función")
            return nueva_funcion

        @decorador
        def saludo():
            print("Hola, mundo!")

        Saludo()
    ```
### propiedades de los decoradores
- el @property se usa para definir un metodo como un atributo
- mos permite acceder a un metodo como si fuera un atributo
- se usa para no tener que llamar a un metodo con parentesis
```python
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
```
#### ventajas
- se puede acceder,modificar y eliminar a un metodo como si fuera un atributo
- se puede acceder a un metodo sin parentesis

## Abstracción
- La abstracción es un concepto fundamental en la programación orientada a objetos que nos permite modelar objetos del mundo real en nuestro software.
- La abstracción nos permite centrarnos en los aspectos más importantes de un objeto y ocultar los detalles menos relevantes.
### clases abstractas
- Las clases abstractas son clases que no pueden ser instanciadas directamente, sino que sirven como plantilla para definir otras clases.
#### ventajas
- Las clases abstractas nos permiten definir métodos que deben ser implementados por las clases derivadas.
- Las clases abstractas nos permiten definir métodos que deben ser implementados por las clases derivadas.

## Metodos especiales
- Los métodos especiales son métodos predefinidos en Python que nos permiten añadir funcionalidades especiales a nuestras clases.
- Los métodos especiales se definen utilizando doble guion bajo al principio y al final del nombre, como `__nombre_del_metodo__`.
### Ejemplos
- `__init__` : se llama automáticamente cuando se crea un objeto a partir de una clase.
- `__str__` : se llama automáticamente cuando se convierte un objeto a una cadena de texto.
- `__repr__` : se llama automáticamente cuando se representa un objeto se diferencia del __str__ por que .
- `__len__` : se llama automáticamente cuando se llama a la función `len()` sobre un objeto.
- `__add__` : se llama automáticamente cuando se suman dos objetos.
- `__sub__` : se llama automáticamente cuando se restan dos objetos.

