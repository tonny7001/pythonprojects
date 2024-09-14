from tkinter import *
from tkinter import messagebox


def click():
    # Puedes descomentar una de estas líneas para probar diferentes mensajes.
    # messagebox.showinfo(title="Hola mundo", message="Hola Jorge")
    # messagebox.showwarning(title="Peligro", message="Puede ser un virus")
    # messagebox.showerror(title="ERROR!!", message="Tienes un error!!!")
    # messagebox.askokcancel() # Mensaje para decidir si salir o no
    # messagebox.askretrycancel() # Mensaje para preguntar si se desea cancelar o cerrar
    # messagebox.askyesno() # Sirve para preguntar si afirmativo o negativo
    # pregunta = messagebox.askquestion(title="Pregunta", message="¿Quieres un helado?")
    # if pregunta == "yes":
    #     respuesta = messagebox.showinfo(title='Respuesta', message="¿De qué sabor?")
    # else:
    #     respuesta = messagebox.showinfo(title='Respuesta', message="No te gusta el helado.")

    opcion = messagebox.askyesnocancel(
        title='Advertencia', message="¿Deseas salir?", icon="warning"
    )  # Se usa para las opciones sí, no o cancelar
    return opcion


def cerrar():
    opcion = click()
    if opcion is None:  # Si se selecciona 'Cancelar'
        print("Cancelar")
    elif opcion:  # Si se selecciona 'Sí'
        windows.destroy()
    else:  # Si se selecciona 'No'
        print("No se cerrará la ventana")


windows = Tk()
windows.geometry('250x300')
windows.title("MessageBox")
# Asegúrate de tener el archivo de ícono en la ubicación correcta.
windows.iconbitmap('images/Logo-jorge.ico')

# ----------------------------------------------
Enviar = Button(windows, text="Enviar", command=click)
Enviar.pack()

Cerrar = Button(windows, text="Cerrar", command=cerrar)
Cerrar.pack()

windows.mainloop()
