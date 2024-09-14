
# como crear una clase abstracta
from abc import ABC, abstractmethod

# clase Abstracta
class Vehiculo(ABC):
    @abstractmethod
    def ir(self):
        pass
    
class Coche(Vehiculo):
    def ir(self):
        print("Conduces el Auto")
        
class Motocicleta(Vehiculo):
    def ir(self):
        print("Andas en la moto")  
        
#Objeto y Clase

vehiculo= Vehiculo()
carro= Coche()
moto= Motocicleta()

#llammar al objeto con el metodo que hereda
vehiculo.ir()
carro.ir()
moto.ir()             