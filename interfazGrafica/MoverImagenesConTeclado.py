from tkinter import *
import os

from interfazGrafica.prueba import imagen


#-----------------------------------------------------
# funciones
def click(event):
    print("Imagen clickeada")

def click2(event):
    print("Otro evento clickeado")

#--------------------------------------------
# interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Arrastrar widget")
windows.iconbitmap('images/Logo-jorge.ico')

# Imprimir ruta absoluta para depurar
import os
ruta_imagen = r'C:\Users\1\Desktop\curso python proyectos\interfazGrafica\images\python.png'
print(os.path.exists(ruta_imagen))  # Debería imprimir True si el archivo existe

# ---------------------------------------------


# Guardarla en una etiqueta
label = Label(windows, image=imagen)
label.pack()

#-------------------------------------------------
windows.mainloop()
