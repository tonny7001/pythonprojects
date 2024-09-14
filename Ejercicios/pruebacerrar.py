from tkinter import *
from tkinter import messagebox

def click():
    opcion = messagebox.askyesnocancel(title='Advertencia', message="¿Deseas salir?", icon="warning")

    def cerrar():
        if opcion == True:  # "Yes" fue seleccionado
            windows.destroy()
        elif opcion == False:  # "No" fue seleccionado
            print("No se cerrará la ventana.")
        else:  # "Cancel" fue seleccionado
            print("Cancelado, sin acción.")

    cerrar()

windows = Tk()
windows.geometry('250x300')
windows.title("MessageBox")
windows.iconbitmap('images/Logo-jorge.ico')

# ----------------------------------------------
Enviar = Button(windows, text="Enviar", command=click)
Enviar.pack()

windows.mainloop()
