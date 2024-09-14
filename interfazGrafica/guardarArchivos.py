from tkinter import *
from tkinter import filedialog, messagebox  # Se añade messagebox para las excepciones


# -----------------------------------------------------------------
# Funciones
# Guarda el documento
def guardarArchivos():
    try:
        # Abrir el cuadro de diálogo para seleccionar la ubicación de guardado
        documento = filedialog.asksaveasfile(
            initialdir='C:\\Users\\1\\Desktop\\curso python proyectos\\documentos',
            defaultextension='.txt',
            filetypes=[('Archivo de Texto', '.txt'),
                       ('HTML', '.html'),
                       ('Todos los Archivos', '.*')]
        )

        # Si el usuario cancela, `documento` será None
        if documento is None:
            return

        # Obtiene el contenido del área de texto
        documentoguardado = texto.get(1.0, END)

        # Escribe el contenido en el archivo seleccionado
        documento.write(documentoguardado)
        documento.close()

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Archivo guardado correctamente")

    except Exception as e:
        # En caso de cualquier error, mostrar un mensaje de error
        messagebox.showerror("Error", f"Se produjo un error al guardar el archivo: {str(e)}")


# ----------------------------
# Interfaz
windows = Tk()
windows.geometry('300x400')  # Ajuste de tamaño para acomodar el botón debajo del área de texto
windows.title("Guardar Archivos")
#windows.iconbitmap('images/Logo-jorge.ico')

# ----------------------------------------------
# Área de Texto
texto = Text(windows, bg='#ffffe0', font=('Ink Free', 15),
             height=8, width=20, padx=20, pady=20, fg="red")
texto.place(x=10, y=10)  # Posiciona el área de texto dentro de la ventana

# Botón
boton = Button(windows, text="Guardar", command=guardarArchivos)
boton.place(x=100, y=300)  # Posiciona el botón justo debajo del área de texto

# --------------------------------------------------------------------
windows.mainloop()
