
from tkinter import *


#--------------------------------------------
#interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Grid")
windows.iconbitmap('images/Logo-jorge.ico')
# ---------------------------------------------
#tiquetas
label_nombre=Label(windows, text='Nombre:').grid(row=0, column=0) # fila columna
# campos de texto
campo_nombre=Entry(windows).grid(row=0, column=1)

label_apellido=Label(windows, text='Apellido:').grid(row=1, column=0) # fila columna
# campos de texto
campo_apellido=Entry(windows).grid(row=1, column=1)
# campos de texto
label_email=Label(windows, text='Email:').grid(row=2, column=0) # fila columna
# campos de texto
campo_email=Entry(windows).grid(row=2, column=1)
# boton
boton_enviar=Button(windows, text="Enviar").grid(row=3,column=1,columnspan=2)




windows.mainloop() # muestra la ventana
#---------------------------------------------
#  las formas de mostrar los elementos de una interfaz son:
#.pack()  mustras los elementos por defecto
#.place(x=, y=) muestra los elementos con coordenadas
#.grid(row= ,column=) es para dale lugar a los elementos en modo filas y columnas