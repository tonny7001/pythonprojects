# 1 crar una lista
from audioop import reverse

estudiantes = ['Jorge', 'Juan', 'Pedro', 'Leidy', 'Jose', 'Andres']
estudiantes.sort()  # funcion para ordenar 

# Recorrer la lista 
for i in estudiantes:
    print(i)


# en las tuplas el metodo sort() no sirve porque las tuplas son inmutables
estudiantes1 =('Jorge', 'Juan', 'Pedro', 'Leidy', 'Jose', 'Andres')
sorted(estudiantes1, reverse=True) # esta funcion convertimos las tuplas a listas

# guardar la conversion en una variable nueva 
print()
estudiantes2= sorted(estudiantes1)
for i in estudiantes2:
    print(i)
estudiantes3=[('Juan', 'F', 60),
              ("Alex", "A", 23),
              ('Jorge', 'D', 34),
              ('Roberto', 'B', 20),
              ('pedro','C', 45)]

#funcion Lambda
 # crear la variale que va a recibir los datos
 # crear en la funcion lambda los valores que recibe y de donde ordenarlos

calificacion= lambda tupla:tupla[2]
estudiantes3.sort(key=calificacion)
for i in estudiantes3:
    print(i)
