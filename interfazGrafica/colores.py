# Selector de colores

from tkinter import *
from tkinter import  colorchooser # submetodo para los colores

#---------------------------------------------------
#Funcion de los botones
def click():
   # color=colorchooser.askcolor() # muestra la paleta de colores
    # podemos saber los valores RGB y Exadecimal de los colores
    #colorHexadecimal=color[1]
    #colorprimario=color[0]
   # print(f"El rgb de este color es:{colorprimario} y el exadecimal es:{colorHexadecimal}")
    #cambiar la interfaz con el color escogido
    windows.config(bg=colorchooser.askcolor()[1] )# nota: solo se cambia al decimal







#---------------------------------------------------
# Interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("tabla de colores")
windows.iconbitmap('images/Logo-jorge.ico')
#---------------------------------------------------
#Botones
Enviar = Button(windows, text="Cambiar color", command=click)
Enviar.pack()





windows.mainloop()