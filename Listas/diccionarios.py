# los diccionarios es un conjunto de informacion que se puede modificar y no es ordenada 
# y llevan clave y valores unicos


capitales={'EEUU':'Washington DC', 'Colombia': 'Bogota',
           'Chile': ' Santiago de Chile', 'Perú':'Lima',
           'Ecuador':'Quito'}

# para acceder al valor primero hay que darle el nombre de la clave o normbre de variable

print(f"la calpital de Chile es:",capitales['Chile']) # con [] se imprime el valor que tiene la clave

print("La capital de  EEUU es:",capitales.get("EEUU"))
print("Los paises de este diccionario son: ",capitales.keys())

print("Las capitales de estos paises son: ",capitales.values())
print("Todos los datos que hay en el diccionario con claves y valores son:", capitales.items())
capitales.update({"Alemania":"Berlin"})
#capitales.clear()

#Recorrer un diccionario con un bucle for se crean dos valores uno para las claves y otro para los valores con el metodo items

for clave,valores in capitales.items():
    print(clave,":", valores)



# metodos 
# 1. get() muestra un valor falso o verdadero en caso que la clave este o no 
# 2. Keys() nos muestra solo las claves o variables de un diccionario
# 3. values() nos muestra los valores que tienen todas las claves
# 4. items() muestra todos los valores de un diccionario 
# 5. uptdate() Agrega un valor nuevo al diccionario
# 6.pop() eleimina una clave y su valor 
# 7.Clear()Limpia todo el diccionario

#Nota :  dentro de un dicccionario podemos crear otro diccionario o una list