from tkinter import *
from tkinter import messagebox

#------------------------------------
# Funciones
def enviar():
    caputartexto = texto.get("1.0", END)  # dos parámetros: donde empieza y donde termina
    messagebox.showinfo("Saludo", caputartexto)

# ----------------------------------------------
# 1. Interfaz
windows = Tk()
#windows.geometry('300x350')  # Ancho y largo
windows.title("block de notas")
windows.iconbitmap('images/Logo-jorge.ico')

# ----------------------------------------------
# 2. TextArea
texto = Text(windows, bg='#ffffe0',font=('Ink Free',25),
             height=8 ,width=20,padx=20,pady=20,fg="red")
texto.pack()

#----------------------------------------------------
# 3. Botones
Enviar = Button(windows, text="Enviar", command=enviar)  # Pasa la referencia de la función
Enviar.pack()

windows.mainloop()
