

#importar el modulo os

import os

origen='C:\\Users\\USUARIO\\Desktop\\curso'
destino= 'C:\\Users\\USUARIO\\Documents\\curso python\\curso'

#Encerrar todo el codigo try except

try:
    #validar que el archivo no exista
    if os.path.exists(destino):
        print("El Archivo ya existe")
    else:
        os.replace(origen,destino)
        print(origen+" El archivo fue movido")    

except FileNotFoundError:    #Error que detecta que el archivo no existe
    print(origen + "Archivo no encontrado")





