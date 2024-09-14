
class Animal:
    vivo= True
    
    def comer(self):
        print("esta comiendo")
    def dormir(self):
        print("esta despierto")
    
class Conejo(Animal): #hereda de la clase Animal
    
    def orejas(self):
        print("El conejo tiene dos orejas y una cola ")
class pez(Animal):
     pass
 
class Halcon(Animal):
    pass 
 
 
 #crear  Los Objetos
 
Conejo = Conejo()
pez= pez()
Halcon= Halcon()


print(Conejo.dormir(), Conejo.orejas())

# nota con la herencia no solo se pueden heredar la clase sino tambien los metodos
