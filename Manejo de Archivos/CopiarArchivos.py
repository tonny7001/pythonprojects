# Metodos:

#copyfile(): copia solo el contenido
#copy(): copia el contenidoy los permisos 
#copy(): copia todo el contenido y los metadatos metadatos: son datos que describen otros datos 

import shutil
# para copiar un archivo hay que seleccionar la ruta de origen y la ruta de destino 
shutil.copyfile('C:\\Users\\USUARIO\\Desktop\\python.txt','C:\\Users\\USUARIO\\Desktop\\ArchivoNuevo.txt')