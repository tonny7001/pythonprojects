# las tuplas no se pueden modificar 
estudiantes= ("jorge", 45)
print(estudiantes.count("jorge"))# cuenta cuantas veces esta repetido un elemento 
print(estudiantes.index(45)) # muestra en que posicion esta un elemento
for i in estudiantes:
    print(i)
    
    if "jorge" in estudiantes:
        print("Hola Jorge")
    else:
        print("nombre no valido")    