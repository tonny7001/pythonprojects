from tkinter import *

# Funciones
# ------------------------------------------------
def click():
    # new_window = Toplevel()
    new_window = Tk()  # Crear nueva ventana independiente
    # Cerrar la ventana principal si se abre la secundaria
    windows.destroy()

# --------------------------------------------------------------
# Interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Abrir Archivos")
windows.iconbitmap('images/Logo-jorge.ico')

# -------------------------------------------------------
# Creación del botón y mostrarlo en una sola línea
Button(windows, text="Crear nueva ventana", command=click).pack()

# ----------------------------------------------------
windows.mainloop()

# new_window = Toplevel() crea una nueva ventana pero no cierra la anterior.
# Si cierro la ventana principal, se cierran las dos.

# new_window = Tk() crea una ventana independiente totalmente.
# Si cierro la ventana principal, la secundaria no se cierra.
