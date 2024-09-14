from tkinter import *
from tkinter import filedialog  # clase para importar los archivos

#-----------------------------------------------------------------
# funciones
def abrirArchivo():

  # capturando posibles errores
    try:
        filepath = filedialog.askopenfilename(initialdir='C:\\Users\\1\\Desktop\\curso python proyectos\\documentos',
                                              title='Abrir Archivos', filetypes=(('Archivos de Texto','*.txt'),
                                                                                 ("Todos los Archivos ","*.*")))  # Código para saber la ruta donde están los archivos
        if filepath:  # Verificar si se seleccionó un archivo
            with open(filepath, 'r') as archivo:  # Abrir el archivo en modo lectura
                print(archivo.read())  # Mostrar el contenido del archivo
        else:
            print("No se seleccionó ningún archivo.")
    except FileNotFoundError:
        print(f"Error: El archivo '{filepath}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

#----------------------------
# Interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Abrir Archivos")
windows.iconbitmap('images/Logo-jorge.ico')

# ----------------------------------------------
# Botones
boton = Button(windows, text="Abrir", command=abrirArchivo)
boton.pack()

windows.mainloop()
