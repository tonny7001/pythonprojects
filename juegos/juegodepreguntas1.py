import sqlite3


# Juego nuevo
def new_game():
    respuestas = []  # Variable para guardar todas las respuestas que da el jugador
    respuestas_correctas = 0  # Guarda las respuestas correctas

    # Conexión a la base de datos
    conn = sqlite3.connect('preguntas_respuestas.db')
    c = conn.cursor()

    # Obtener todas las preguntas de la base de datos
    c.execute("SELECT * FROM preguntas")
    preguntas = c.fetchall()

    for pregunta in preguntas:
        print('-------------------------------')
        print(pregunta[1])
        print(f"A. {pregunta[2]}")
        print(f"B. {pregunta[3]}")
        print(f"C. {pregunta[4]}")
        print(f"D. {pregunta[5]}")

        respuesta = input("Ingresa una respuesta (A,B,C,D): ").upper()
        respuestas.append(respuesta)

        # Llamar al método check_answer para pasarle la respuesta correcta desde la base de datos
        respuestas_correctas += check_answer(pregunta[6], respuesta)

    conn.close()

    display_score(respuestas_correctas, respuestas)


# Revisar las respuestas
def check_answer(respuesta_correcta, respuesta):
    if respuesta_correcta == respuesta:
        print("¡Correcto!")
        return 1
    else:
        print("Incorrecto.")
        return 0


# Calcular el puntaje
def display_score(respuestas_correctas, respuestas):
    print('-------------------------------')
    print("RESULTADOS")
    print(f"Respuestas correctas: {respuestas_correctas}")
    print("Tus respuestas: ", respuestas)


# Función para validar si se quiere jugar de nuevo
def play_again():
    respuesta = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    if respuesta == "si":
        new_game()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")


# Iniciar el juego
new_game()
