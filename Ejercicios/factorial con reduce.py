
# serie Fibinacci con reduce
# 1. importar la libreria
import  functools
#2. Crear la lista
serie=[5,4,3,2,1]
# 3. crear la variable que toma el resultado llmar la libreria y la funcion que toma el nuevo valor
resultado = functools.reduce(lambda x,y: x*y, serie)
#4. mostrar el resultado
print(f"El resultado de la serie {serie}, es: ",resultado)




