from tkinter import *

# Lista de opciones de comida
comida = ['Pizza', 'Hamburguesa', 'Hot Dog']

# Función para manejar la orden seleccionada
def orden():
    if x.get() == 0:
        resultado_orden.config(text="¡Has ordenado una Pizza!")
    elif x.get() == 1:
        resultado_orden.config(text="¡Has ordenado una Hamburguesa!")
    else:
        resultado_orden.config(text="¡Has ordenado un Hot Dog!")

# Configuración de la ventana principal
windows = Tk()
windows.geometry('250x300')
windows.title("RadioButton")
windows.iconbitmap('images/Logo-jorge.ico')
windows.config(background='#AAB396')

# Variable para almacenar la selección del usuario
x = IntVar()
x.set(-1)  # Sin selección por defecto

# Creación de los Radiobuttons
for index in range(len(comida)):
    radiobutton = Radiobutton(
        windows,
        text=comida[index],
        variable=x,
        value=index,
        padx=25,
        command=orden,
    background='#AAB396')
    radiobutton.pack(anchor='w')

# Label para mostrar el resultado
resultado_orden = Label(windows, text="", font=("Arial", 12),background='#AAB396')
resultado_orden.pack(pady=20)

# Ejecución del bucle principal de la aplicación
windows.mainloop()



radiobutton.pack(anchor='w')

windows.mainloop()
