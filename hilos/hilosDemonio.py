# Los hilos demonio son hilos que se ejecutan en segundo plano y se ejecutan hasta que cumplan la funcion no se pueden matar

import  threading
import time
def tiempo():
    print()
    print()
    contador=0
    while True:
        time.sleep(1)
        contador +=1
        print(contador, "segundos")
x=threading.Thread(target=tiempo, daemon=True) # crear el hilo
x.start() #iniciar el hilo


entrada= input("Desea salir?")