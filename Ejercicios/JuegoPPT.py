# juego Piedra papel o tijera

# importar el modulo random
import random

# Crear la lista de opciones
lista = ["piedra", "papel", "tijera"]

while True:
    # dejar que la computadora elija al azar con el metodo choice de la libreria random
    computadora = random.choice(lista)
    jugador = None

    while jugador not in lista:
        jugador = input('Piedra, Papel ó Tijera: ').lower()
    
    # validar que el jugador haya seleccionado lo mismo de la computadora
    if jugador == computadora:
        print('Computadora: ', computadora)
        print('Jugador: ', jugador)
        print('Empate!')
    elif jugador == 'piedra':
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste!')
        if computadora == 'tijera':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste!')
    elif jugador == 'papel':
        if computadora == 'tijera':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste!')
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste!')
    elif jugador == 'tijera':
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste!')
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste!')
    
    jugar_de_nuevo = input("¿Quieres seguir jugando? (si/no): ")

    if jugar_de_nuevo != 'si':
        break

print("¡Adiós!")


