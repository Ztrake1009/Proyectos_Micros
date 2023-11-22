import tkinter as tk
import threading
import serial
import time

microProces = serial.Serial("COM3", 9600)

mensaje = ""

def iniciar():

    pasos = 1600

    # Movimiento hacia la derecha.
    X_Destino = 400 - radio
    hilo1 = threading.Thread(target=mover_Motores("X", pasos))
    hilo3 = threading.Thread(target=mover_X_Interfaz(X_Destino))

    print("Moviendo el Motor X y la interfaz en X")
    # creamos la barrera para 2 hilos
    barrera = threading.Barrier(2)
    # Inicia los hilos, mueve el Motor de X y la interfaz.
    hilo1.start()
    hilo3.start()

    # Espera a que ambos hilos terminen.
    hilo1.join()
    hilo3.join()

    # Movimiento hacia abajo.
    Y_Destino = 400 - radio
    hilo2 = threading.Thread(target=mover_Motores("Y", pasos))
    hilo4 = threading.Thread(target=mover_Y_Interfaz(Y_Destino))

    print("Moviendo el Motor Y y la interfaz en Y")

    # Inicia los hilos, mueve el Motor de Y y la interfaz.
    hilo2.start()
    hilo4.start()

    # Espera a que ambos hilos terminen.
    hilo2.join()
    hilo4.join()


    pasos = -1600
    
    # Movimiento hacia la izquierda.
    X_Destino = 0
    hilo1 = threading.Thread(target=mover_Motores("X", pasos))
    hilo3 = threading.Thread(target=mover_X_Interfaz(X_Destino))

    print("Moviendo el Motor X y la interfaz en X")
    # creamos la barrera para 2 hilos
    barrera = threading.Barrier(2)
    # Inicia los hilos, mueve el Motor de X y la interfaz.
    hilo1.start()
    hilo3.start()

    # Espera a que ambos hilos terminen.
    hilo1.join()
    hilo3.join()

    # Movimiento hacia arriba.
    Y_Destino = 0
    hilo2 = threading.Thread(target=mover_Motores("Y", pasos))
    hilo4 = threading.Thread(target=mover_Y_Interfaz(Y_Destino))

    print("Moviendo el Motor Y y la interfaz en Y")
    # creamos la barrera para 2 hilos
    barrera = threading.Barrier(2)
    # Inicia los hilos, mueve el Motor de Y y la interfaz.
    hilo2.start()
    hilo4.start()

    # Espera a que ambos hilos terminen.
    hilo2.join()
    hilo4.join()

# Mover la grúa horizontalmente en la interfaz.
def mover_X_Interfaz(X_Destino):
    global circulo
    global X_Actual

    # Movimiento horizontal.
    movimiento_X = X_Destino - X_Actual

    if movimiento_X > 0:
        mov = 10
    elif movimiento_X < 0:
        mov = -10

    # Si ya está en la misma posición en X que el destino.
    if (X_Actual == X_Destino):
        movimiento_X = 0

    while X_Actual != X_Destino:

        canvas.move(circulo, mov, 0)
        X_Actual = X_Actual + mov

        time.sleep(0.1)
        ventana.update()

        if (movimiento_X > 0 and X_Actual >= X_Destino):
            movimiento_X = X_Destino - X_Actual
            canvas.move(circulo, movimiento_X, 0)
            X_Actual = X_Destino

            time.sleep(0.1)
            ventana.update()
            break

        elif (movimiento_X < 0 and X_Actual <= X_Destino):
            movimiento_X = X_Destino - X_Actual
            canvas.move(circulo, movimiento_X, 0)
            X_Actual = X_Destino

            time.sleep(0.1)
            ventana.update()
            break

    X_Actual = X_Destino

    return

# Mover la grúa verticalmente en la interfaz.
def mover_Y_Interfaz(Y_Destino):
    global circulo
    global Y_Actual

    # Movimiento vertical.
    movimiento_Y = Y_Destino - Y_Actual
    
    if movimiento_Y > 0:
        mov = 10
    elif movimiento_Y < 0:
        mov = -10
    
    # Si ya está en la misma posición en Y que el destino.
    if (Y_Actual == Y_Destino):
        movimiento_Y = 0

    while Y_Actual != Y_Destino:

        canvas.move(circulo, 0, mov)
        Y_Actual = Y_Actual + mov

        time.sleep(0.1)
        ventana.update()

        if (movimiento_Y > 0 and Y_Actual >= Y_Destino):
            movimiento_Y = Y_Destino - Y_Actual
            canvas.move(circulo, 0, movimiento_Y)
            Y_Actual = Y_Destino

            time.sleep(0.1)
            ventana.update()
            break
        
        elif (movimiento_Y < 0 and Y_Actual <= Y_Destino):
            movimiento_Y = Y_Destino - Y_Actual
            canvas.move(circulo, 0, movimiento_Y)
            Y_Actual = Y_Destino

            time.sleep(0.1)
            ventana.update()
            break

    Y_Actual = Y_Destino
    ventana.update()
    return

def mover_Motores(motor, pasos):
    global mensaje

    #Se envía el motor a utilizar y el número de pasos a dar.
    comando = f"{motor}{pasos}\n"
    microProces.write(comando.encode())
    print(comando)

    mensaje = microProces.readline().decode()
    print(f"ESP32: {mensaje}")

def mover_Motor_Z():
    motor = "Z"
    comando = f"{motor}{0}\n"
    microProces.write(comando.encode())
    print(comando)

def onClosing():
    ventana.destroy()
    #microProces.close()

# Crear la ventana principal
ventana = tk.Tk()
ventana.protocol("WM_DELETE_WINDOW", onClosing) # Protocolo para cerrar la ventana al presionar la X_Actual de la ventana.
ventana.title("Guardar Número")

# Ventana para mover el círculo.
canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
canvas.pack()

# Iniciar el movimiento del círculo
X_Actual = 0
Y_Actual = 0
radio = 40
velocidad_x = 2
velocidad_y = 2
direccion = "derecha"
circulo = canvas.create_oval(X_Actual, Y_Actual, X_Actual + radio, Y_Actual + radio, fill="black")

# Botón para mover ambos motores, uno tras otro.
button_Mover_Motores = tk.Button(ventana, text="Iniciar", command=lambda: iniciar())
button_Mover_Motores.pack()

# Botón para activar el mover ambos motores, uno tras otro.
button_Mover_Motor_Z = tk.Button(ventana, text="Mover Z", command=lambda: mover_Motor_Z())
button_Mover_Motor_Z.pack()

"""
def actualizar(self):
    circulo.mover()
    after(10, self.actualizar)
"""
    
# Etiqueta para mostrar el estado del motor
label_estado = tk.Label(ventana, text="")
label_estado.pack()

# Iniciar la aplicación
ventana.mainloop()