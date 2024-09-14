import time

#print(time.ctime(time.time())) # fecha y hora legible
#metodo localtime

#tiempo_actual= time.localtime()
#print(tiempo_actual)
#funcuion para hacer una hora legible


#Codigo para usar una hora y fecha Actual
#tiempo_actual= time.localtime()
#tiempo=time.strftime("%B %d %y %H:%M:S", fechaActual)
#print(tiempo)


#fechaActual=time.localtime()
#fechayHora=time.strftime("%B %d %y %H:%M:S", fechaActual)
#print(fechayHora)

# Hora universal

tiempoActual=time.gmtime()
tiempo=time.strftime("%H:%M:S %B %d %y ",tiempoActual)
print(tiempo)