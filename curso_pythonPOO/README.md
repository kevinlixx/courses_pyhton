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