# Juego de Preguntas y respuestas

# 1. Crear las funciones

# Juego nuevo
def new_game():
    respuestas = []  # Variable para guardar todas las respuestas que da el jugador
    respuestas_correctas = 0  # Guarda las respuestas correctas
    preguntas_num = 0

    # Recorrer las preguntas del diccionario y mostrarlas
    for key in preguntas:
        print('-------------------------------')
        print(key)
        # For para recorrer las opciones de respuestas
        for i in opciones[preguntas_num]:
            print(i)

        respuesta = input("Ingresa una respuesta (A,B,C,D): ").upper()
        respuestas.append(respuesta)

        # Llamar al método check_answer para pasarle las claves
        respuestas_correctas += check_answer(preguntas.get(key), respuesta)
        preguntas_num += 1

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
    print(f"Respuestas correctas: {respuestas_correctas} de {len(preguntas)}")
    print("Tus respuestas: ", respuestas)

# Función para validar si se quiere jugar de nuevo
def play_again():
    respuesta = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    if respuesta == "si":
        new_game()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

# 2. Crear un diccionario con las preguntas y las respuestas correctas
preguntas = {
    '¿Qué idioma se habla en Brasil?': 'A',
    '¿Cuál es el océano más grande del mundo?': 'B',
    '¿Cuál es la estrella más cercana a la Tierra?': 'C',
    '¿Cuál es el segundo país más grande del mundo?': 'A'
}

# 3. Crear un arreglo para guardar todas las opciones de respuestasa
opciones = [
    ['A. Portugués', 'B. Español', 'C. Brasileño', 'D. Inglés'],
    ['A. Atlántico', 'B. Pacífico', 'C. Ártico', 'D. Índico'],
    ['A. La Luna', 'B. Alfa Centauri', 'C. El Sol', 'D. Ninguna'],
    ['A. Canadá', 'B. Rusia', 'C. EE.UU.', 'D. China']
]

# 4. Llamar las funciones 
new_game()
