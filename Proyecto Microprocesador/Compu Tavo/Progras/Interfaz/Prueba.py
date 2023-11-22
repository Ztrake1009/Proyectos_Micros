import threading
import time

listo = 0

# Define dos funciones que deseas ejecutar
def funcion1(cont):
    global listo
    for i in range(cont):
        print("Funcion 1 - Iteracion", i)
        time.sleep(0.5)
        listo = 1


def funcion2(cont):
    for i in range(cont):
        print("Funcion 2 - Iteracion", i)
        time.sleep(0.5)


cont = 5

# Crea dos hilos para ejecutar las funciones
hilo1 = threading.Thread(target=funcion1(cont))
hilo2 = threading.Thread(target=funcion2(cont))

# Inicia el primer hilo
hilo1.start()

# Espera a que el primer hilo termine antes de iniciar el segundo hilo
hilo1.join()

print(listo)

# Inicia el segundo hilo
hilo2.start()

# Espera a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Ambas funciones han terminado.")
print("------------------------------")

"""
cont = 10

# Crea dos hilos para ejecutar las funciones
hilo1 = threading.Thread(target=funcion1(cont))
hilo2 = threading.Thread(target=funcion2(cont))

# Inicia el primer hilo
hilo1.start()

# Espera a que el primer hilo termine antes de iniciar el segundo hilo
hilo1.join()

# Inicia el segundo hilo
hilo2.start()

# Espera a que ambos hilos terminen
hilo1.join()
hilo2.join()
"""
print("Ambas funciones han terminado.")