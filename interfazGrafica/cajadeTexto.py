from tkinter import *


# funciones para los comportamientos de los botones
def enviar():
    nombre_usuario = texto.get()
    contrasena_usuario = text2.get()
    print(nombre_usuario)
    print(contrasena_usuario)

def resetear_campos():
    texto.delete(0, END)  # Borrar el texto desde el primer caracter hasta el último
    text2.delete(0, END)

def eliminar_caracter():
    texto.delete(len(texto.get())-1, END)

# Inicio de la interfaz principal
windows = Tk()
windows.geometry('350x200')
windows.title("Cuadro de texto")
windows.iconbitmap('images/Logo-jorge.ico')

# Campos de texto
texto = Entry(windows, font=("Arial", 10))
texto.pack(side=LEFT)

text2 = Entry(windows, font=("Arial", 10), show="*")  # show="*" oculta el texto con asteriscos
text2.place(x=0, y=20)

# Botones
resetear_btn = Button(windows, text="Resetear", command=resetear_campos, font=("Monotype Corsiva", 10))
resetear_btn.pack(side=RIGHT)

eliminar_btn = Button(windows, text="Eliminar", command=eliminar_caracter, font=("Monotype Corsiva", 10))
eliminar_btn.pack(side=RIGHT)

enter_btn = Button(windows, text="Enter", command=enviar, font=("Monotype Corsiva", 10))
enter_btn.pack(side=RIGHT)

windows.mainloop()
