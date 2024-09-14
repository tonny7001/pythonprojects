import tkinter as tk
import random

# Crear la lista de opciones
lista = ["piedra", "papel", "tijera"]

# Función para manejar la elección del jugador y el resultado del juego
def jugar(eleccion_jugador):
    computadora = random.choice(lista)

    if eleccion_jugador == computadora:
        resultado = 'Empate!'
    elif eleccion_jugador == 'piedra':
        if computadora == 'papel':
            resultado = 'Perdiste!'
        else:
            resultado = 'Ganaste!'
    elif eleccion_jugador == 'papel':
        if computadora == 'tijera':
            resultado = 'Perdiste!'
        else:
            resultado = 'Ganaste!'
    elif eleccion_jugador == 'tijera':
        if computadora == 'piedra':
            resultado = 'Perdiste!'
        else:
            resultado = 'Ganaste!'

    label_computadora.config(text=f"Computadora eligió: {computadora}")
    label_resultado.config(text=f"Resultado: {resultado}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")

# Crear etiquetas para mostrar la elección de la computadora y el resultado
label_computadora = tk.Label(ventana, text="Computadora eligió: ", font=('Arial', 14))
label_computadora.pack(pady=10)

label_resultado = tk.Label(ventana, text="Resultado: ", font=('Arial', 14))
label_resultado.pack(pady=10)

# Crear botones para las opciones
btn_piedra = tk.Button(ventana, text="Piedra", command=lambda: jugar('piedra'), font=('Arial', 14))
btn_piedra.pack(pady=10)

btn_papel = tk.Button(ventana, text="Papel", command=lambda: jugar('papel'), font=('Arial', 14))
btn_papel.pack(pady=10)

btn_tijera = tk.Button(ventana, text="Tijera", command=lambda: jugar('tijera'), font=('Arial', 14))
btn_tijera.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
