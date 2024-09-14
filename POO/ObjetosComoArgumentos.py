
# Como pasar objetos como argumentos

# 1. Crear las clases
class Coche:
    # 2 crar variables de clase
    color=None
    
    
class Motocicleta:
    color=None    
 
 # 3. Crear un funcion que reciba un objeto como parametro y debe ser fuera de la clase
def cambiar_color(coche, color):   #4.  crear el objeto y los argumentos[]
    coche.color=color
    
# 5. Crear los objetos de la clase Coche 
coche1 = Coche() 
coche2 = Coche()
coche3 = Coche() 
moto= Motocicleta() 

# 6.llamar la funicio del objeto y darle el atributo
cambiar_color(coche1, "Rojo")
cambiar_color(coche2, "Azul")
cambiar_color(coche3, "Verde")
cambiar_color(moto,"Rosada")

print(coche1.color)
print(coche2.color)
print(coche3.color)
print(moto.color)
    
    
    
    