#una comprension de lista es para usar una nueva lista mas organizada

#Recorrer un lista ejemplo 1
#cuadrado=[]
#for i in range(1,11):
 #   cuadrado.append(i*i)
#print(cuadrado)

# recorrer una lista con comprension ejemplo 2
#cuadrado=[i*i  for i in range(1,11)]
#print(cuadrado)

#Comprension de listas con funcion lambda

estudiantes= [100,90,80,70,60,50,40,30,20,10,0] #filtraremos esta lista

#estudiantes_aprobados=list(filter(lambda x: x >= 60 , estudiantes)) # recupero todas notas mayor a 60 y se almacena en otra variables

estudiantes_aprobados= [i if i >=60 else "--" for i in estudiantes ]
print(estudiantes_aprobados)


