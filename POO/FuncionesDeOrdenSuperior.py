
#funciones superior 

#Ejemplo 1 

def hablarAlto(texto):
    return texto.upper()

def hablarBajo(texto):
    return texto.lower()    

#Funcion Superior

def hola(func):  #Funcion por argumentos
    texto=func('Hola mundo')
    print(texto)

hola(hablarBajo)    


# Ejemplo 2 
    
def divisor(x):
    def dividendo(y):
        return y/x     
    return dividendo 

divide = divisor(2)
print(divide(10))