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

#para poder llamar solo la clase B
B.hablar(d) #Hola desde B
