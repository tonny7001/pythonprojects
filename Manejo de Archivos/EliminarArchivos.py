

import os
import shutil
#crear un variable con la direccion donde esta el archivo 
# nota no se pueden eliminar carpetas vacias
# para eliminar una carpeta con contenido  se importa el modulo shutil
archivo='C:\\Users\\USUARIO\\Documents\\curso python\\curso'

try:
    #os.remove(archivo) 
    #os.rmdir(archivo)  
    shutil.rmtree(archivo)
    
   # capturando excepciones     
except FileNotFoundError:
    print("El archivo no existe.")
except PermissionError:
    print("No tienes permiso para eliminar esta carpeta")    
except OSError:
    print(" La carpeta no esta vacia ")      
else:
    print("Carpeta eliminada..")



#usos 

#os.remove() Elimina un archivo 
#os.rmdir() elimina una carpeta
    




