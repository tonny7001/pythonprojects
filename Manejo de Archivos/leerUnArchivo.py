
#ruta y variable donde se va a guardar el contenido del archivo
try: 
    with open('C:\\Users\\USUARIO\\Desktop\\python.txt' ) as file:   
       print(file.read())
except FileNotFoundError:
     print("Archivo no encontrado!!!")    
