from pydoc import text
from tkinter import *

windows1 = Tk()
windows1.geometry('500x500')  # Darle dimensiones a la ventana
windows1.title('Etiquetas')  # Darle un título a la ventana
windows1.iconbitmap('images/Logo-jorge.ico')
windows1.config(background='#D8D9DA')
etiqueta=Label(windows1,
               text='Hola mundo, como estas',
               font= ('Arial', 20, 'bold'),
               fg="#E8B86D",
               bg='#295F98',
               relief="raised",
               bd=10,
               padx=20,
               pady=20)
etiqueta.pack() # Mostrar la etiqueta y lo muestra y el el comienzo de la interfaz
#etiqueta.place(x=20, y=30) # darle coordenadas a la etiqueta


windows1.mainloop()



# font= ('Arial', 20, 'bold'), tipo de fuente
#fg="#E8B86D", Color de la fuente
# #bg='#295F98', color del fondo
#relief="ridge" bordes
#bd=tamaño del borde





