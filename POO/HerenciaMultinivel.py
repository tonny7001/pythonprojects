
#clase padre
class Organismo:
    vivo=True
# Clase hija que hereda de la clase organismo
class Animal(Organismo): 
#metodos o atributos propios de la clase hija   
    def comer(self):
        print("este animal esta comiendo ")
# clase que hereda de la clase hija con su metodosy atributos propios         
class Perro(Animal):
    def ladrar(self):
        print("El perro esta ladrando ")
# Creacion de los objetos

perro=Perro()
perro.comer()
perro.vivo
perro.ladrar()
