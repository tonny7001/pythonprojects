from tkinter import *

def submit():
    temperatura = scale.get()
    print("La temperatura es: " + str(temperatura) + ' grados')
    actualizar_color(temperatura)

def actualizar_color(temperatura):
    if temperatura >= 75:
        color = '#FF4500'  # Rojo oscuro para temperaturas altas
    elif temperatura >= 50:
        color = '#FFA500'  # Naranja para temperaturas medias-altas
    elif temperatura >= 25:
        color = '#FFFF00'  # Amarillo para temperaturas medias
    else:
        color = '#00BFFF'  # Azul para temperaturas bajas
    scale.config(troughcolor=color)

# Crear una ventana
windows = Tk()
windows.geometry('500x500')  # Darle dimensiones a la ventana
windows.title('Termómetro')  # Título de la ventana

# Configurar el ícono de la ventana con un archivo .ico
#windows.iconbitmap('images/Logo-jorge.ico')
windows.config(background='#D8D9DA')

# Crear un widget Scale para simular un termómetro
scale = Scale(windows, from_=100, to=0, length=400, orient="vertical",
              tickinterval=10, font=("Arial", 10),
              troughcolor='#229799', bg='#424242', fg='#FFDA76')

# Establecer el valor inicial en el centro de la escala
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack(pady=20)  # Empaquetar el widget con un margen superior

# Crear un botón para enviar el valor de la temperatura
boton = Button(windows, text="Enviar", command=submit, font=("Arial", 12))
boton.pack(pady=20)

# Actualizar el color de la escala basado en la temperatura inicial
actualizar_color(scale.get())

windows.mainloop()  # Mostrar la ventana
