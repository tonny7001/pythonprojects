import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('preguntas_respuestas.db')
c = conn.cursor()

# Crear tabla de preguntas
c.execute('''CREATE TABLE IF NOT EXISTS preguntas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pregunta TEXT NOT NULL,
                opcion_a TEXT NOT NULL,
                opcion_b TEXT NOT NULL,
                opcion_c TEXT NOT NULL,
                opcion_d TEXT NOT NULL,
                respuesta_correcta TEXT NOT NULL)''')

# Agregar algunas preguntas iniciales
c.execute("INSERT INTO preguntas (pregunta, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta) VALUES (?, ?, ?, ?, ?, ?)",
          ('¿Qué idioma se habla en Brasil?', 'Portugués', 'Español', 'Brasileño', 'Inglés', 'A'))
c.execute("INSERT INTO preguntas (pregunta, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta) VALUES (?, ?, ?, ?, ?, ?)",
          ('¿Cuál es el océano más grande del mundo?', 'Atlántico', 'Pacífico', 'Ártico', 'Índico', 'B'))
c.execute("INSERT INTO preguntas (pregunta, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta) VALUES (?, ?, ?, ?, ?, ?)",
          ('¿Cuál es la estrella más cercana a la Tierra?', 'La Luna', 'Alfa Centauri', 'El Sol', 'Ninguna', 'C'))
c.execute("INSERT INTO preguntas (pregunta, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta) VALUES (?, ?, ?, ?, ?, ?)",
          ('¿Cuál es el segundo país más grande del mundo?', 'Canadá', 'Rusia', 'EE.UU.', 'China', 'A'))

conn.commit()
conn.close()
