from tkinter import *
from tkinter import messagebox


#-----------------------------------------------------
#funciones
def hacer_algo(event): #recibe el evento
   messagebox.showinfo(title="saludo", message="Hola Jorge")

#--------------------------------------------
# interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Eventos del teclado.")
windows.iconbitmap('images/Logo-jorge.ico')
# ---------------------------------------------
windows.bind("<Return>", hacer_algo ) # lleva dos parametros un evento y una funcion




windows.mainloop()


#--------------------------------------------------
#eventos del teclado
#.bind("<>") # lleva dos parametros un evento y una funcion
#.bind("<Return>") # envento para cuando se le da enter