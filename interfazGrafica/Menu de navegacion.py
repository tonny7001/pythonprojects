from tkinter import *
from tkinter import filedialog, messagebox  # Se añade messagebox para las excepciones

# --------------------------------------
# funciones
# --------------------------------------
# Funciones para abrir, guardar y salir
def abrirArchivo():
    try:
        filepath = filedialog.askopenfilename(
            initialdir='C:\\Users\\1\\Desktop\\curso python proyectos\\documentos',
            title='Abrir Archivos',
            filetypes=(('Archivos de Texto', '*.txt'), ("Todos los Archivos", "*.*"))
        )  # Código para saber la ruta donde están los archivos
        if filepath:  # Verificar si se seleccionó un archivo
            with open(filepath, 'r') as archivo:  # Abrir el archivo en modo lectura
                print(archivo.read())  # Mostrar el contenido del archivo
        else:
            print("No se seleccionó ningún archivo.")
    except FileNotFoundError:
        print(f"Error: El archivo '{filepath}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def guardarArchivos():
    try:
        # Abrir el cuadro de diálogo para seleccionar la ubicación de guardado
        documento = filedialog.asksaveasfile(
            initialdir='C:\\Users\\1\\Desktop\\curso python proyectos\\documentos',
            defaultextension='.txt',
            filetypes=[('Archivo de Texto', '.txt'), ('HTML', '.html'), ('Todos los Archivos', '.*')]
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

# -----------------------------------------------------------------------------------------------------------
# Funciones para cortar, copiar y pegar
def cortar():
    pass
    #texto.event_generate("<<Cut>>")


def copiar():
    pass
    #texto.event_generate("<<Copy>>")

def pegar():
    pass
    #texto.event_generate("<<Paste>>")

# ----------------------------
# Interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Abrir Archivos")
windows.iconbitmap('images/Logo-jorge.ico')

# ----------------------------------------------
# Menú
menubar = Menu(windows)
windows.config(menu=menubar)

# Elementos del menú y subelementos
fileMenu = Menu(menubar, tearoff=0)  # aquí van todas las opciones que vamos a escoger
menubar.add_cascade(label='Archivos', menu=fileMenu)  # agregar la barra de menú para las opciones

# Submenú
fileMenu.add_command(label="Abrir", command=abrirArchivo)
fileMenu.add_command(label="Guardar", command=guardarArchivos)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=quit)

# Nuevo menú en la misma barra
editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editar", menu=editMenu)

# Elementos del menú de edición
editMenu.add_command(label="Cortar", command=cortar)
editMenu.add_command(label="Copiar", command=copiar)
editMenu.add_command(label="Pegar", command=pegar)

# ----------------------------------------------
# Área de texto para interactuar con cortar/copiar/pegar
texto = Text(windows)
texto.pack(expand=True, fill=BOTH)

# ----------------------------------------------
windows.mainloop()
