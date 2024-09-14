#Las excepciones en programación son eventos que ocurren durante la ejecución de un programa 
# y que interrumpen el flujo normal de instrucciones.


try:
    numero1= int(input("Ingresa el primer numero: "))
    numero2= int(input("Ingresa el segundo numero:"))
    resultado= numero1/numero2
except  ZeroDivisionError as e:
    print("no se puede divir por cero!!")  
except ValueError as e:
    print("Solo se deben ingresar numeros")      
    
except Exception as e:
   print("Algo salio mal!!!")
else:
    print(resultado)   