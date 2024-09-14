# Diccionario = {Key: expresión for (key , value ) in iterable}
# Diccionario = {Key: expresion for (key , value ) in iterable if condicion}
# Diccionario = {Key: (if/else) for (key , value ) in iterable}
# Diccionario = {Key: function(value) for (key , value ) in iterable}



#------------------------------------------------------------------#
# Ejemplo 1.
ciudades_F= {'New York': 32, 'Bosto': 75, 'Los Angeles': 100, 'Chicago':50 }
#2. crear el nuevo diccionario para mostrar los valores
ciudades_C={key:round((values-32)*(5/9)) for (key , values) in ciudades_F.items()}
print(f"el cambio grados fahrenheit  {ciudades_F} a grados Centigrados {ciudades_C} °")

#------------------------------------------------------------------#
# Ejemplo 2.
clima={'New York':'Nieve', 'Boston':'Soleado','Los Angeles ':'Soleado','Chicago':'Nublado'}
clima_soleado={clave:valor for (clave, valor) in clima.items() if valor=='Soleado'}
print(f"Los dias soleados son", clima_soleado)

#------------------------------------------------------------------#
# Ejemplo 3.

ciudades_F= {'New York': 32, 'Bosto': 75, 'Los Angeles': 100, 'Chicago':50 }
clima_2={key:("Calor" if value >=40 else "Frio")for (key, value) in ciudades_F.items()}
print(f"En estas ciudadedes calor{clima_2}")

#Ejercicio 3. cambia los valores por una funcion

def check_temp(value):
    if value>=70:
        return  "Calor"
    elif 60 >= value  >=40:
        return "Normal"
    else:
        return "Frio"

ciudades_F= {'New York': 32, 'Bosto': 75, 'Los Angeles': 100, 'Chicago':50 }
clima_3={key: check_temp(value)  for(key, value) in ciudades_F.items()}
print(clima_3)