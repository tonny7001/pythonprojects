# modulo os para el uso de archivos

# os nos sirve para saber si un archivo existe o no 

import os
# al guardar la ruta se tiene que poner doble \\ para que no se tome como una cadena
path = 'C:\\Users\\USUARIO\\Desktop\python.txt'  

# verificar que el archivo si exista y que tipo de archivo es 

if os.path.exists(path):
    print("El archivo existe")
    if os.path.isfile(path):
        print("Es una carpeta")
    elif os.path.isdir(path):
        print("es una carpeta")
else:  
    print("El Archivo no existe")      