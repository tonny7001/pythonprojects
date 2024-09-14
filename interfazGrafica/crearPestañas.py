from tkinter import *
from tkinter import ttk   #importar diferentes widget para la creacion de pestañas


def click():
    pass

# --------------------------------------------------------------
# Interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Crear pestaña")
windows.iconbitmap('images/Logo-jorge.ico')

# -------------------------------------------------------
#pestañas
notebook=ttk.Notebook(windows)
notebook.pack(expand=True,fill="both") #propiedades para la pestaña
pestana1=Frame(notebook)
pestana2=Frame(notebook)
pestana3=Frame(notebook)
notebook.add(pestana1,text="pestaña 1")
notebook.add(pestana2,text="pestaña 2")
notebook.add(pestana3,text="pestana 3")
#--------------------------------------------------------
#agregar elementos a las pestañas
Label(pestana1,text="Pestaña 1", width=50,height=25).pack()
Label(pestana2,text="Pestaña 2", width=50,height=25).pack()
Label(pestana3,text="Pestaña 3", width=50,height=25).pack()





#--------------------------------------------------------
# Creación del botón y mostrarlo en una sola línea
#Button(windows, text="Crear nueva ventana", command=click).pack()

# ----------------------------------------------------
windows.mainloop()