# una funcion en un bloque de codigo que solo funciona cuando se la llama
# la funcion se define con la palabra def

#declarar la funcion 
def operaciones():    
    numero1=int (input("Ingresa un numero: "))
    numero2= int(input("Ingresa el segundo numero: "))
    Resultado= numero1+numero2
    print(f"La suma entre {numero1} y {numero2} es: ",Resultado)
operaciones() # Llamar la funcion 


# funcion con parametros
def numeros(numero1, numero2):
    multiplicacion= numero1*numero2
    print(f"La multiplicacion  entre {numero1} y {numero2} es: ",multiplicacion)
#Llamar la funcion y pasarle los argumentos
numeros(50,30)
    