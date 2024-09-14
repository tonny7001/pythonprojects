from tkinter import *






def enviar():
    nombre_usuario=user.get()
    contrasena_usuario= password.get()
    print(nombre_usuario)
    print(contrasena_usuario)

# crear la interfaz
windows = Tk()
windows.geometry('500x500')
windows.title("Pagina de prueba")
windows.config(background='#D8D9DA')

etiqueta_titulo=Label(windows, text="Suma de números")
etiqueta_titulo.pack()

#-------------------------------------------------------
label_User=Label(windows, text="Usuario: ")
label_User.place(x=10 ,y=40)

user=Entry(windows, font=("Arial",10))
user.place(x=70, y= 40)
#-------------------------------------------------------
label_Contrasena=Label(windows, text="Contraseña: ", )
label_Contrasena.place(x=10 ,y= 80)

password=Entry(windows, font=("Arial",10) ,show='*')
password.place(x=90, y= 80)

# Formatear el botón
Boton1=Button(windows, text="Enter", command=enviar, font=("Arial", 15), bg="#4CAF50", fg="white", bd=3, relief="raised")
Boton1.place(x=300, y=50)

windows.mainloop()
