# para crear un objeto primero hay que crear una clase 

# Del archivo Auto importe la clase carro
from Auto import Carro
# Creacion de los objetos
auto_1= Carro("Renault","Megane",2022,"Negro")
auto_2= Carro("Toyota","Prado",1990,"Blanca")

# Acceder a los atributos de los objetos


# llamar los metodo y los estados 

auto_1.encendido()
auto_1.apagado()

print(f"El Auto es un: {auto_1.marca}, es un modelo: {auto_1.modelo}  del año: {auto_1.ano} es de color: {auto_1.color}")