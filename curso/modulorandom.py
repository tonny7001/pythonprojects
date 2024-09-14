#metodo ramdom

# importar la biblioteca
import random

x=random.randint(1,6) # numeros enteros al azar
y=random.random()  # numeros decimales al azar


# Metodo choice sirve para mostrar elementos al azar de una lista

animales=["Perro","Gato","Pollo","Vaca", "Ardilla"] # nota la lista va dentro de corchetes
resultado=random.choice(animales)
print(resultado)


# metodo shuffle() mezcla aleatoriamente los elementos de una secuencia 

cartas=[ '1','2','3', '4', '5','6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]
random.shuffle(cartas)

print(cartas)

