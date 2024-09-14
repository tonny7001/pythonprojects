nombre=""

while True:
    nombre=input("Ingresa tu nombre: ")
    if nombre != "":
        break
print(f"El nombre ingresado es: {nombre}")    
print("Fin del programa.")
print()    
telefono= "123-456-789"

for i in telefono:
    if i=="-":
        continue
    print( i,end="")
print(f" la cadena original es: {telefono}")  
print()

for i in range(1, 21):
    if i==13:
        pass 
    else:
        print(i,end=",") 
   