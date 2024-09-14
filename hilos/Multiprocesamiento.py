from multiprocessing import Process
import time
from os import cpu_count


def contador(num):
    cont = 0
    while cont < num:
        cont += 1

def main():
    iniciar = time.perf_counter()
    a = Process(target=contador, args=(250000000,))
    b = Process(target=contador, args=(250000000,))
    c = Process(target=contador, args=(250000000,))
    d = Process(target=contador, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    b.join()
    # Espera a que el proceso termine

    final = time.perf_counter()
    tiempo = final - iniciar
    print(f"Finalizó en {tiempo:.2f} segundos")

    print(f"su PC tiene ", cpu_count(), "Nucleos")

if __name__ == '__main__':
    main()
