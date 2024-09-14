

# clase padre 
class Animal:
    def comer(self):
        print("Este animal esta comiendo")
    
   # clase hija  
class Conejo (Animal):
    def comer(self):
        print("Este conejo esta comiedo una zanahoria  ")




conejo = Conejo()
conejo.comer()
   




    
    # como Anular un  metodo 
    # crear un metodo dentro de la clase que esta heredando con el mismo nombre y valor pero con diferente comportamiento
    