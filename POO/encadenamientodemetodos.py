# el encadenamiento de metodos es delcarar varios metodos en una funcion y mandarlos a llamar al tiempo 
class Coche():
    def encender(self):
        print("has arancado el motor")
        return self
    def conducir(self):
        print("estas conduciendo el coche")
        return self
    def frenar(self):
        print("has arancado el motor")
        return self
    def apagando(self):
        print("has apagado el motor")
        return self
    
    
# creando el objeto y llamando los metodos 

coche= Coche()
#coche.encender()
#coche.conducir()
#coche.frenar() 
#coche.apagando()   


# Como llamarlos secuencialmente

coche.encender().conducir().frenar().apagando()
    