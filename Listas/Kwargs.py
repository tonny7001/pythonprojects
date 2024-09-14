# los Kwargs empqueta todos los elementos en un diccionario

def hola(**kwargs):
   # print('Hola ',kwargs['nombre']+ ' '+kwargs["apellido"],'',kwargs['Lenguaje'])
    print("Hola",end=" ")
    for clave,valor in kwargs.items():
        print(clave, end=' ')
    
    
hola(nombre="Jorge", apellido="Mosquera",Lenguaje="Python")   