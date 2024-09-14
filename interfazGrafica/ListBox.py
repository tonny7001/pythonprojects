from tkinter import *

# Función para mostrar la selección
def submit():
    # Crear una lista para almacenar los elementos seleccionados
    food = []
    # Recorrer los elementos seleccionados y agregarlos a la lista 'food'
    for index in listbox.curselection():
        food.append(listbox.get(index))

    print("Su orden es:")
    # Mostrar los elementos seleccionados
    for item in food:
        print(item)

# Función para agregar un elemento
def agregar():
    listbox.insert(listbox.size(), texto.get())
    texto.delete(0, END)
    listbox.config(height=listbox.size())

# Función para borrar un elemento
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
#--------------------------------------------
#interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("List Box")
#windows.iconbitmap('images/Logo-jorge.ico')

# ---------------------------------------------

listbox = Listbox(windows, font=("Arial", 25), width=20, selectmode="multiple")
listbox.pack()

# Insertar los datos a la lista
listbox.insert(1, "Pizza hawaiana")
listbox.insert(2, "Pizza napolitana")
listbox.insert(3, "Pizza peperonni")
listbox.insert(4, "Pizza campiñones")
listbox.insert(5, "Pizza ranchera")
listbox.config(height=listbox.size())

texto = Entry(windows,bg='#ffffe0')
texto.pack()

# Botón para agregar
agregarButton = Button(windows, text="Agregar", command=agregar)
agregarButton.pack()

# Botón para enviar
enviarButton = Button(windows, text="Enviar", command=submit)
enviarButton.pack()

# Botón para borrar
deleteButton = Button(windows, text="Borrar", command=delete)
deleteButton.pack()

windows.mainloop()
