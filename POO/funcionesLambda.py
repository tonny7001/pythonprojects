# Sintaxis de las funciones lambda (lambda parametro: expresion)
# Funcion lamba con un parametro
doble = lambda x:x*2
print(doble(10))
#funcion lambda con dos parametros 

# Definir la función lambda
multiplicar = lambda x, y: x * y

# Ingresar los parámetros y llamar a la función lambda
resultado = multiplicar(10, 20)  # Llamar a la función lambda con los argumentos 10 y 20

# Imprimir el resultado
print(resultado)  # Esto imprimirá 200, que es el resultado de multiplicar 10 y 20


# funcion con tres o mas parametros 

suma= lambda x,y,z: x+y+z
resultado1=suma(10,20,30)
print(resultado1)


# funcion  con cadenas de texto

nombre_completo= lambda nombre, apellido: nombre+ " "+ apellido

nombre= nombre_completo("Jorge", "Mosquera")
print(nombre)

# funcion lambda para validar datos 

verificar_Edad= lambda edad:True if edad>18 else False

print(verificar_Edad(5))

# Solicitar entrada de datos al usuario y convertir a enteros
x = int(input("Introduce el primer número: "))
y = int(input("Introduce el segundo número: "))

# Llamar a la función lambda con los datos ingresados
resultado = multiplicar(x, y)

# Imprimir el resultado
print(f"El resultado de multiplicar {x} y {y} es {resultado}")