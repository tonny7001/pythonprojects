# los sets no pueden haber elementos repetidos
#no mantienen el orden en el que se declaran 
# su elementos no pueden ser modificados despues de declarado

cubiertos={ 'tenedor', 'cuchara','cuchillo'}
print("la lista original es", cubiertos)    
print("")
cubiertos.add('pocillo')

for i in cubiertos:
   
   print(i , end=",")
print("la lista con el nuevo elemento")

    
#metodos     
# 1. add(), agrega un elemento al conjunto pero no pueden ser repetidos
# 2 remove() remueve un elemento de los set
# 3 pop()remueve un elemento al azar
# 4 clear() limpia la lista completa
# 5.update() une varias listas 
# 6. difference() muestra la diferencia de los elemenentos  o elementos comunes
# 7.  intersection()muestra el o los elementos los cuales estan repetidos en la listas