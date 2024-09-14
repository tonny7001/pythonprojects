import random

# Dimensiones de la lista
filas = 3
columnas = 4

# Crear y llenar la lista 2D con números aleatorios
lista_2d = [[random.randint(0, 100) for _ in range(columnas)] for _ in range(filas)]

# Mostrar la lista 2D
for fila in lista_2d:
    print(fila)




# Crear una lista 2D de 3x4 inicializada con ceros
filas = 3
columnas = 4
lista_2d = [[0] * columnas for _ in range(filas)]

print(lista_2d)

