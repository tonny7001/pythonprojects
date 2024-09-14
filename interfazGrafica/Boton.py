from tkinter import *
def click(): # funcion para crear el evento al boton
    print("Le diste enter")

#interfaz
windows =Tk()
windows.geometry('250x300')
windows.title("botones")
windows.iconbitmap('images/Logo-jorge.ico')
#fin de la configurarion de la interfaz

# Creacion el boton y darle formato
boton=Button(windows, text="Enter",command=click,
             font=('Arial', 20, 'bold'), bg='#3C3D37' ,activebackground= '#5B99C2' ,
             activeforeground='#7FA1C3')
#mostrar el boton
boton.pack()




windows.mainloop()