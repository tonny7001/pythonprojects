from tkinter import *

#--------------------------------------------
# interfaz
windows = Tk()
#windows.geometry('250x300')
windows.title("Canvas")
windows.iconbitmap('images/Logo-jorge.ico')
# ---------------------------------------------
# canvas
canvas=Canvas(windows, height=500, width=500)
#x1,y1=50,50
#x2,y2=350, 350
canvas.create_line(0,0,500,500,fill='red')
canvas.create_rectangle(50,50,250,250,fill="yellow",width=1.5)
canvas.create_polygon(250,0,500,500,0,500)
canvas.pack()




windows.mainloop()


#----------------------------------------------------
#CREAR UNA LINEA
#create_line() posicion inicial y posicion final
#fill= color de la linea
#width= grosor de la linea

#CREAR UN RECTANGULO
#create_rectangle(0,250,10,250) coordenadas x1-y1  x2-y2   izquierda abajo , largo ,derecha abajo
#(x1=izquierda,  y1= abajo izquierda, x2= largo de objeto, y2= derecha abajo)

#CREAR UN POLIGONO
#este lleva tres coordenadas