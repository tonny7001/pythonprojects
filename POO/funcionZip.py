# La funcion Zip agrega dos o mas elementos de dos o mas iterables sean listas o tuplas etc crearndo una nueva tupla

nombre_usuario=["Jorge", "Mosquera", "Hijo"]
contrasena=('123','abc','contra')
# Funcion Zip

usuario=zip(nombre_usuario, contrasena)

# convertir una funcion zip en lista
#print(type(usuario))

usuario= list(zip(nombre_usuario, contrasena))
print(usuario)
print(type(usuario))
for i in usuario:
   print(i)

