from tkinter import *
from time import *

#----------------------------------------
# Funciones
def update():
    # Mostrar la hora
    hora = strftime("%I:%M:%S %p")  # Horario de doce horas
    time.config(text=hora)

    # Mostrar el día y la fecha
    dia = strftime("%A, %d %B %Y")  # Formato de día de la semana, día, mes y año
    day.config(text=dia)

    time.after(1000, update)  # Llamada a 'update' cada segundo

#--------------------------------------------
# Interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Reloj")
windows.iconbitmap('images/Logo-jorge.ico')
windows.config(background='#6A9C89')

# ---------------------------------------------
# Etiquetas
time = Label(windows, font=("Arial", 30), bg='#000', fg='#C4DAD2')  # Ajustar fuente para mejor visualización
time.pack(pady=20)  # Añadir margen para centrar mejor

day = Label(windows, font=("Ink Free", 25), bg='#6A9C89', fg='#000')  # Ajustar fuente y colores
day.pack(pady=20)  # Añadir margen para centrar mejor

# Llamar la función
update()

#----------------
# Cierre de la interfaz
windows.mainloop()
