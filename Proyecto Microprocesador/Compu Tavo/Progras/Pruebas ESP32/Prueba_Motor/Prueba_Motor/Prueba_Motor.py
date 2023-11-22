import tkinter as tk
import threading
import serial

microProces = serial.Serial("COM3", 9600)

mensaje = ""

def crear_Hilos():
    pasos = int(entrada_numero.get())

    hilo1 = threading.Thread(target=mover_Motor("X", pasos))
    hilo2 = threading.Thread(target=mover_Motor("Y", pasos))

    print("Moviendo el Motor X")
    # Inicia el primer hilo, mueve el Motor de X.
    hilo1.start()
    # Espera a que el primer hilo termine antes de iniciar el segundo hilo.
    hilo1.join()
    """
    if (mensaje == "Motor_Listo"):
        # Inicia el segundo hilo, mueve el Motor de Y.
        print("Moviendo el Motor Y")
        hilo2.start()
    """
    print("Moviendo el Motor Y")
    hilo2.start()

    # Espera a que ambos hilos terminen.
    hilo1.join()
    hilo2.join()

def mover_Motor(motor):
#def mover_Motor(motor):
    global mensaje

    pasos = int(entrada_numero.get())

    #Se envía el motor a utilizar y el número de pasos a dar.
    comando = f"{motor}{pasos}\n"
    microProces.write(comando.encode())
    print(comando)

    mensaje = microProces.readline().decode()
    print(f"Arduino: {mensaje}")

def onClosing():
    ventana.destroy()
    microProces.close()

# Crear la ventana principal
ventana = tk.Tk()
ventana.protocol("WM_DELETE_WINDOW", onClosing) # Protocolo para cerrar la ventana al presionar la X de la ventana.
ventana.title("Motores")




# Etiqueta y entrada para ingresar el número
etiqueta_numero = tk.Label(ventana, text="Ingrese un número:")
etiqueta_numero.pack()

entrada_numero = tk.Entry(ventana)
entrada_numero.pack()


# Boton para seleccionar cual motor mover.
button_Motor_X = tk.Button(ventana, text="Mover Motor X", command=lambda: mover_Motor('X'))
button_Motor_X.pack()

button_Motor_Y = tk.Button(ventana, text="Mover Motor Y", command=lambda: mover_Motor('Y'))
button_Motor_Y.pack()

"""
# Boton para mover ambos motores, uno tras otro.
button_Mover_Motores = tk.Button(ventana, text="Mover Motores", command=lambda: mover_Motor())
button_Mover_Motores.pack()
"""

# Etiqueta para mostrar el estado del motor
label_estado = tk.Label(ventana, text="")
label_estado.pack()

# Iniciar la aplicación
ventana.mainloop()
