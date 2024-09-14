# librerias y modulos
from tkinter import *
from tkinter.ttk import * # módulo para la barra de progreso
import time # módulo de tiempo

#----------------------------------------------------------
# funciones
def descargar():
    # variables
    GB = 10  # cuanto por descargar
    dowload = 0  # cuanto se ha descargado
    velocidad=1# velocidad de descarga
    # recorrer la barra
    while dowload < GB:
        time.sleep(0.05)# simula el progreso de la barra
        barra['value'] += (velocidad/GB)*100
        dowload += velocidad
        porcentaje.set(str(int((dowload/GB)*100))+"%") # mostrar el porcentaje de la descarga
        faltante.set(str(dowload)+"/"+str(GB)+" Completando!!! ")
        # Actualizar la pantalla para que se vaya mostrando el progreso de la barra
        windows.update_idletasks()


#--------------------------------------------
# interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("ProgressBar")
windows.iconbitmap('images/Logo-jorge.ico')
# ---------------------------------------------
porcentaje=StringVar() # Variable para mostrar el progreso de la barra
faltante=StringVar() # variable para mostrar el restante de la descarga
# barra
barra = Progressbar(windows, orient="horizontal", length=300)
barra.pack(pady=10)
# etiqueta para mostra el porcentaje
texto_progreso=Label(windows, textvariable=porcentaje).pack()
#etiqueta para mostrar el faltante de la descarga
texto_faltante=Label(windows, textvariable=faltante).pack()
# botones
boton = Button(windows, text='Descargar', command=descargar)
boton.pack()
#---------------------------------------------------------------

windows.mainloop()
#-----------------------------------------------

# GB = cuanto falta por descargar
