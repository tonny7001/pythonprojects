from tkinter import *
import time
#-----------------------------------------------------------------
#funciones
#-------------------------------------------------------------------
#variables para ancho y largo
ancho=500
alto=500
# variables para la velocidad de la imagen
velX=3
velY=2
#-------------------------------------------------------------------
#interfaz
windows = Tk()
#windows.geometry('500x500')  # Darle dimensiones a la ventana
windows.title('Animacion ')  # Darle un título a la ventana
# Configurar el ícono de la ventana con un archivo .ico
windows.iconbitmap('images/Logo-jorge.ico')
windows.config(background='#D8D9DA')
#----------------------------------------------------------------
#canvas
canvas=Canvas(windows,width=ancho, height=alto,bg='#000')
canvas.pack()
#importar la imagen
imagen=PhotoImage(file='images/nave.png')
miImagen= canvas.create_image(0,0,image=imagen,anchor=NW)
#------------------------------------------------------------------------
# crear las dimensiones a la imagen
#-----------------------------------------------------------------------
ancho_imagen = imagen.width()  # Método correcto para obtener ancho
alto_imagen = imagen.height()  # Método correcto para obtener alto
#-------------------------------------
# Crear la animacion
while True:
#variables para las coordenadas
    coordenadas=canvas.coords(miImagen)
    #print(coordenadas)
# restringir el movimiento de la nave el la coordenada X
    if(coordenadas[0]>=ancho-ancho_imagen or coordenadas[0]<0):
        velX= -velX
    # restringir el movimiento de la nave el la coordenada Y
    if(coordenadas[1]>=alto-alto_imagen or coordenadas[1]<0):
        velY= - velY
#mover la imagen
    canvas.move(miImagen, velX,velY)
#mostrar la ventana
    windows.update()
#darle la velocidad a la imagen con el modulo time
    time.sleep(0.01)
#--------------------------------------------------------------
#mostrar la ventana
windows.mainloop()