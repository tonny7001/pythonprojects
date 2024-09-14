#Metodos para cadenas de texto
nombre="Jorge Mosquera"

print("el nombre inicial es ",nombre)
print("")

#Mostra la longitud de una cadena
print("Mostrar la longitud de una cadena")

print("El nombre jorge tiene: ", len(nombre)," Caracteres") 
print("")

#Mostrar la posicion de un caracter
print("Mostra la posicion de un caracter")
print("la poscicion de la letra J es: ",nombre.find("e")) 
print("")

# colocar la primera letra en Mayuscula
print("Mostra la primera letra en mayuscula")

print("El nombre con la funcion ", nombre.capitalize())
print("")

#cambiar todas las letras de un texto a Mayusculas 
print(f"El nombre original es {nombre} y con el metodo upper queda: ", nombre.upper())
print("")
#cambiar todas las letras de un texto a minusculas 
print(f"El nombre original es {nombre} y con el metodo lower queda: ", nombre.lower())
print("")

#metodo para saber si una cadena es un digito o no 
print(f"El nombre oginal es{nombre} entonces  tiene numeros?",nombre.isdigit())
print("")

#saber si un texto tiene caracteres especiales
print(f"El nombre oginal es{nombre} entonces  tiene caracteres especiales ?",nombre.isalpha())
print("")

# metodo para saber cuantos caracteres hay repetidos en una cadena 
print(f"El nombre oginal es {nombre} cuantas letras hay repetidas", nombre.count("e"))
print("")

#Metodo para remplzar un caracter  texto 
print(f"El nombre oginal es{nombre} entonces  se cambio por: ",nombre.replace("Jorge", "carlos"))
print("")


