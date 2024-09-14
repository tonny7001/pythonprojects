bebidas=['cafe','soda','te']
cena= ['piza',"haburquesa", "hot dog"]
postres= ["pastel", 'helado']


comida=[bebidas,cena,postres]
print(comida[2]) # acede a la lista en la posicion 0
print(comida[0][2])#accede a una lista y a su respectivo elemento



columnas=3 
filas=4
lista_2d = [[0] * columnas for _ in range(filas)]
print(lista_2d)