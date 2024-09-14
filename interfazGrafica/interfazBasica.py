from tkinter import *

# Crear una ventana
windows = Tk()
windows.geometry('500x500')  # Darle dimensiones a la ventana
windows.title('primer interfaz')  # Darle un título a la ventana

# Configurar el ícono de la ventana con un archivo .ico
windows.iconbitmap('images/Logo-jorge.ico')
windows.config(background='#D8D9DA')

windows.mainloop()  # Mostrar la ventana

