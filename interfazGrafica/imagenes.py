from tkinter import *
#---------------------------
#Funciones
def arriba(event):
    #label.place(x=label.winfo_x(),y=label.winfo_y()-10)
    canvas.move(miImagen,0,-10)
def abajo(event):
     #label.place(x=label.winfo_x(),y=label.winfo_y()+10)
     canvas.move(miImagen,0,10)

def izquierda(event):
     #label.place(x=label.winfo_x()-10,y=label.winfo_y()-10)
    canvas.move(miImagen,-10,0)
def derecha(event):
    #label.place(x=label.winfo_x()+10,y=label.winfo_y()-10)
    canvas.move(miImagen,10,0)
#---------------------------------e
# Crear la ventana principal
windows = Tk()
windows.geometry('250x300')
windows.title("Imagenes")
#windows.iconbitmap('imagenes/Logo-jorge.ico')


#---------------------------------------------------------
#teclas para mover la imagen por letres
windows.bind("<w>",arriba)
windows.bind("<s>",abajo)
windows.bind("<a>",izquierda)
windows.bind("<d>",derecha)
#teclas para mover la imagen por flechas
windows.bind("<Up>",arriba)
windows.bind("<Down>",abajo)
windows.bind("<Left>",izquierda)
windows.bind("<Right>",derecha)
#--------------------------------------------
#Mover la imagen con canvas
canvas=Canvas(windows,width=500,height=500)
canvas.pack()
# crear la imagen con canvas
imagenes = PhotoImage(file='imagenes/python.png')
miImagen=canvas.create_image(0,0,image=imagenes,anchor=NW)




# Cargar y mostrar la imagen con tkinter
#imagenes = PhotoImage(file='imagenes/python.png')
# #label = Label(windows, image=imagenes)
#label.place(x=0,y=0)



# Ejecutar el bucle principal
windows.mainloop()
