# manejo de hilos

# 1. descargar las librerias
import threading
import time



def desyunar():
    print("Iniciando hilo 1....")
    time.sleep(3) # funcion sleep de libreria time para programar el tiempo de los hilos
    print("Finalizando  hilo 1....")

def tomarcafe():
    print("Iniciando hilo 2....")
    time.sleep(4)# funcion sleep de libreria time para programar el tiempo de los hilos
    print("Finalizando  hilo 2....")

def estudiar():
    print("Iniciando hilo 3....")
    time.sleep(5) # funcion sleep de libreria time para programar el tiempo de los hilos
    print("Finalizando  hilo 3....")
#creamos una variable para crear un cronometo
inicio=time.perf_counter()

# vamos a llamar las tres funciones
#desyunar()
#tomarcafe()
#estudiar()

# Crear un hilo
x=threading.Thread(target= desyunar , args=())
x.start() # iniciar el hilo

y=threading.Thread(target= tomarcafe , args=())
y.start() # iniciar el hilo

z=threading.Thread(target= estudiar , args=())
z.start() # iniciar el hilo

x.join()
y.join()
z.join()

print(threading.active_count())
print(f"se esta ejecutando el hilo principal==",threading.enumerate())

fin=time.perf_counter()
tiempo= fin- inicio
print(f"El tiempo en que se tomo la persona para hacer fue de: ", round(tiempo) , "Segundos")




#Funciones
# active_count() cuenta el numero de hilos que se estan ejecutando
# enumere() cuenta una lista de todos los hilos que se esten ejecutando
# perf_counter() del modulo time para crear un cromnomtro de tiempo
# threadding.Thread crea el hilo
# .star() inicia el hilo
#.join()Sincloniza el hilo
