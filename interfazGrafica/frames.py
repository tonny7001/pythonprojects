
from tkinter import *



# Interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Frame")
windows.iconbitmap('images/Logo-jorge.ico')

#-------------------------------------------------
#el Marco o frame
marco=Frame(windows,bg='blue',bd=20, relief="flat")
marco.place(x=0, y=10)
#--------------------------------
# botones
#Los botones estan dentro de un marco
Button(marco, text="W", font=('Consolas, 25'),width=3).pack(side=TOP)
Button(marco, text="A", font=('Consolas, 25'),width=3).pack(side=LEFT)
Button(marco, text="S", font=('Consolas, 25'),width=3).pack(side=LEFT)
Button(marco, text="D", font=('Consolas, 25'),width=3).pack(side=LEFT)



windows.mainloop(),


#bg= colo de fondo , bd=borde,relief="grosor del borde"