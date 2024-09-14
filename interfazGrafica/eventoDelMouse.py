from tkinter import *
from tkinter import messagebox


#-----------------------------------------------------
#funciones
def click(event): #recibe el evento
   messagebox.showinfo(title="saludo", message="Hola Jorge")

#--------------------------------------------
# interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Eventos del mouse.")
windows.iconbitmap('images/Logo-jorge.ico')
# ---------------------------------------------
windows.bind("<Button-1>", click ) # lleva dos parametros un evento y una funcion
windows.bind("<Button-2>", click ) # lleva dos parametros un evento y una funcion
windows.bind("<Button-3>", click ) # lleva dos parametros un evento y una funcion
windows.bind("<ButtonRelease>", click ) # lleva dos parametros un evento y una funcion




windows.mainloop()


#--------------------------------------------------
#eventos del teclado
#.bind("<>") # lleva dos parametros un evento y una funcion
#.bind("<Return>") # envento para cuando se le da enter