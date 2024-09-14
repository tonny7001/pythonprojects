from tkinter import *




def submit():
    print("La temperatura es:  "+ str(scale.get())+' grados')

# Crear una ventana
windows = Tk()
windows.geometry('500x500')  # Darle dimensiones a la ventana
windows.title('Barra de desplazamiento')  # Darle un título a la ventana

# Configurar el ícono de la ventana con un archivo .ico
windows.iconbitmap('/images/Logo-jorge.ico')
windows.config(background='#D8D9DA')
#----------------------------------------------------------------

scale=Scale(windows, from_=100, to=0, length=400, orient="vertical",
            tickinterval= 10, font=("Arial", 10),
            troughcolor='#229799', bg='#424242', fg='#FFDA76')
scale.set(((scale['from']- scale['to'])/2)+ scale['to'])
scale.pack()
boton=Button(windows, text="Enviar", command=submit)
boton.pack()






windows.mainloop()  # Mostrar la ventana


# from  to: (desde y hasta )
# length: largo de la barra
# orient=orientacion de la barra " vertical" , "horizontal"
# tickinterval= coloca mustra las marcas o numeros en la escala
# .set es para decirle desde que marcador queremos que este el medidor
# scale.set(((scale['from']- scale['to'])/2)+ scale['to'] codigo para que la escala quede siempre
# en medio sea cual sea el intervalo
# troughcolor= colocar color al medidor de la escala



#uso del tkinter
