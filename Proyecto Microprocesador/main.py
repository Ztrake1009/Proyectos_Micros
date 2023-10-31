# Librerías
import tkinter as tk
from tkinter import filedialog
import csv
import time
import serial
import cv2
from pyzbar.pyzbar import decode
import threading
from Clases import *

#########################################################################################################
# Variables Globales.

lista_Suministro1 = []
lista_Suministro2 = []
lista_Carga = []

letras_Suministro1 = []
letras_Suministro2 = []
letras_Carga = []

contador_R_Carga = 0
contador_G_Carga = 0
contador_B_Carga = 0

tamX_Matriz1 = 8  # Cantidad columnas de la zona de suministro 1.
tamY_Matriz1 = 3  # Cantidad filas de la zona de suministro 1.
tamX_Matriz2 = 3  # Cantidad columnas de la zona de suministro 2.
tamY_Matriz2 = 5  # Cantidad filas de la zona de suministro 2.
tam_Matriz3 = 5  # Tamaño de la zona de carga.

# Realmente cada espacio de las matrices mide 5 cm, en interfaz las medidas se multiplican por 8.
tam_Celdas = 40
# Realmente el espacio libre es de 4 cm, en interfaz las medidas se multiplican por 8.
tam_Esp_Libre = 32
# Las bases de la grúa miden 8 cm cuadrados, en interfaz las medidas se multiplican por 8.
tam_Bases = 64

# Simula el tamaño de los 60x60 cm, igualmente cada lado se multiplica por 8.
ancho = 480  # 60*8
alto = 480  # 60*8

# Sirve para seleccionar entre ambos modos (1 y 2).
Modo_Seleccionado = 0

# Mensaje que retorna el ESP cuando se terminó de mover algún motor.
mensaje_Motores = ""

#########################################################################################################
# Funciones.
def Interfaz(ventana):
    global boton_Cargar
    global microProces

    ventana.title("Grúa Pórtico")
    ventana.geometry("600x600")

    microProces = serial.Serial("COM3", 9600)

    boton_Cargar = tk.Button(ventana, text="Cargar Archivo CSV", command=abrir_Excel)
    boton_Cargar.pack(side="top")

# Función: Abrir los archivos de excel en formato cvs.
def abrir_Excel():
    global letras_Carga
    global contador_R_Carga
    global contador_G_Carga
    global contador_B_Carga

    letras_Carga = []

    archivo_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

    if archivo_path:
        with open(archivo_path, 'r', newline='') as file:
            lector_csv = csv.reader(file, delimiter=';')
            for fila in lector_csv:
                for color in fila:
                    letras_Carga.append(color)

    letra = 0
    contador_R_Carga = 0
    contador_G_Carga = 0
    contador_B_Carga = 0

    while letra < len(letras_Carga):
        if letras_Carga[letra] == "R":  # Caja Roja.
            contador_R_Carga += 1

        elif letras_Carga[letra] == "G":  # Caja Verde.
            contador_G_Carga += 1

        elif letras_Carga[letra] == "B":  # Caja Azul.
            contador_B_Carga += 1
        letra += 1
    
    print(contador_R_Carga)
    print(contador_G_Carga)
    print(contador_B_Carga)

    Sel_Modo()

def Sel_Modo():
    global boton_Modo1
    global boton_Modo2

    boton_Modo1 = tk.Button(ventana, text="Ejecutar Modo de Acomodo 1", command=Modo1)
    boton_Modo1.pack(side="top")
    boton_Modo2 = tk.Button(ventana, text="Ejecutar Modo de Acomodo 2", command=Modo2)
    boton_Modo2.pack(side="top")

def Modo1():
    global Modo_Seleccionado
    Modo_Seleccionado = 1
    Dibujar(Modo_Seleccionado)

def Modo2():
    global Modo_Seleccionado
    Modo_Seleccionado = 2
    Dibujar(Modo_Seleccionado)

def Dibujar(Modo_Seleccionado):
    global boton_Cargar
    global boton_Modo1
    global boton_Modo2
    global mensaje_Interfaz
    global boton_Volver
    global boton_Iniciar
    global lienzo

    global grua
    global X_Actual
    global Y_Actual
    global lista_Suministro1
    global lista_Suministro2
    
    boton_Cargar.destroy()
    boton_Modo1.destroy()
    boton_Modo2.destroy()

    lienzo = tk.Canvas(ventana, width=ancho, height=alto, background="black")
    lienzo.place(x=(600/2)-(ancho/2), y=(600/2)-(alto/2))

    matriz1 = [[None for _ in range(tamX_Matriz1)] for _ in range(tamY_Matriz1)]  # Cantidad en X, Cantidad en Y.
    matriz1.append([None]) # Crea un nuevo espacio en la matriz para que sean 25.
    matriz2 = [[None for _ in range(tamX_Matriz2)] for _ in range(tamY_Matriz2)]
    matriz3 = [[None for _ in range(tam_Matriz3)] for _ in range(tam_Matriz3)]

    # Crea un espacio libre en gris.
    # Las medidas son las escogidas según las especificaciones.
    x0 = tam_Bases
    y0 = tam_Bases
    x1 = 416  # (60*8)-(8*8)
    y1 = 416
    Esp_Libre = lienzo.create_rectangle(x0, y0, x1, y1, fill="#B2B2B2")
    
    # Define las coordenadas iniciales donde ubicar la grúa.
    X_Actual = tam_Bases
    Y_Actual = tam_Bases
    X_Final = X_Actual + tam_Celdas
    Y_Final = Y_Actual + tam_Celdas

    # Mensaje para mostrar lo que realiza la grúa en ese momento.
    mensaje_Interfaz = tk.Label(ventana, text="En espera.", font=("Arial", 16))
    mensaje_Interfaz.pack(side="bottom")

    # Botón de volver a la pantalla principal.
    boton_Volver = tk.Button(ventana, text="Volver a pantalla principal", command=volver_Inicio)
    boton_Volver.pack(side="top")

    # Si se selecciona el modo 1.
    if (Modo_Seleccionado == 1):
        # Inicializa las listas de suministros con espacios vacios.
        iniciar_Suministros()

        # Crea las matrices.
        crear_Matriz_S1(lienzo, matriz1)
        crear_Matriz_S2(lienzo, matriz2)
        crear_Matriz_C(lienzo, matriz3)

        # Crea el objeto representativo de la grúa.
        grua = lienzo.create_oval(X_Actual, Y_Actual, X_Final, Y_Final, width=1, fill="orange")
        
        # Botón para iniciar el acomodo 1.
        boton_Iniciar = tk.Button(ventana, text="Iniciar Acomodo", command=acomodo_Cajas_1)
        boton_Iniciar.pack(side="top")

    # Si se selecciona el modo 2.
    if (Modo_Seleccionado == 2):
        # Inicializa las listas de suministros con espacios vacios.
        iniciar_Suministros()

        # Crea las matrices.
        crear_Matriz_S1(lienzo, matriz1)
        crear_Matriz_S2(lienzo, matriz2)
        crear_Matriz_C(lienzo, matriz3)

        # Crea el objeto representativo de la grúa.
        grua = lienzo.create_oval(X_Actual, Y_Actual, X_Final, Y_Final, width=1, fill="orange")
        
        # Botón para iniciar el acomodo 2.
        boton_Iniciar = tk.Button(ventana, text="Iniciar Acomodo", command="""acomodo_Cajas_2""")
        boton_Iniciar.pack(side="top")

# Inicializa las listas de suministros con espacios vacios.
def iniciar_Suministros():
    global lista_Suministro1
    global lista_Suministro2

    lista_Suministro1 = []
    lista_Suministro2 = []

    i = 0
    while (i < 25):
        color = ""
        espacio = Suministro(0,0,color,False)
        lista_Suministro1.append(espacio)
        i += 1

    j = 0
    while (j < 14):
        color = ""
        espacio = Suministro(0,0,color,False)
        lista_Suministro2.append(espacio)
        j += 1

# Carga el archivo de excel de prueba para la matriz de suministro.
def leer_Excel_Prueba():
    global letras_Suministro1
    global letras_Suministro2
    
    letras_Suministro1 = []
    letras_Suministro2 = []

    archivo_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    
    if archivo_path:
        with open(archivo_path, 'r', newline='') as file:
            lector_csv = csv.reader(file, delimiter=';')
            for fila in lector_csv:
                for color in fila:
                    letras_Suministro1.append(color)

    i = 0
    while (i < 16):
        color = ""
        letras_Suministro2.append(color)
        i += 1

# Define el color del espacio de la matriz dependiendo de la lista que reciba.
def ident_Color(letra):
    if letra == "R":  # Rojo Claro.
        return "#FFAAAA"

    elif letra == "G":  # Verde Claro.
        return "#AAFFAA"

    elif letra == "B":  # Azul Claro.
        return "#AAAAFF"
    
    else:
        return "white"

# Crea la Matriz de Suministro 1.
def crear_Matriz_S1(lienzo, matriz1):
    global lista_Suministro1

    espacio_actual = 0
    for fila_Matriz1 in range(tamY_Matriz1):
        for col_Matriz1 in range(tamX_Matriz1):
            x0 = tam_Bases + tam_Esp_Libre + (col_Matriz1 * tam_Celdas)
            y0 = tam_Bases + tam_Esp_Libre + (fila_Matriz1 * tam_Celdas)
            x1 = x0 + tam_Celdas
            y1 = y0 + tam_Celdas
            color = ident_Color(lista_Suministro1[espacio_actual].color)
            matriz1[fila_Matriz1][col_Matriz1] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)
                        
            posx = x0
            posy = y0

            # Para el modo 1.
            lista_Suministro1[espacio_actual].posx = x0
            lista_Suministro1[espacio_actual].posy = y0

            espacio_actual += 1

            # Crea el último espacio de la matriz de manera que se "sale" de los 8x3 espacios originales, esto para que sean 25 espacios en total.
            if (fila_Matriz1 == 2) and (col_Matriz1 == 7):
                col_Matriz1 = 0
                fila_Matriz1 = 3
                x0 = tam_Bases + tam_Esp_Libre + (col_Matriz1 * tam_Celdas)
                y0 = tam_Bases + tam_Esp_Libre + (fila_Matriz1 * tam_Celdas)
                x1 = x0 + tam_Celdas
                y1 = y0 + tam_Celdas                    
                color = ident_Color(lista_Suministro1[espacio_actual].color)
                matriz1[fila_Matriz1][col_Matriz1] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)
                
                posx = x0
                posy = y0

                # Para el modo 1.
                lista_Suministro1[espacio_actual].posx = x0
                lista_Suministro1[espacio_actual].posy = y0

# Crea la Matriz de Suministro 2.
def crear_Matriz_S2(lienzo, matriz2):
    global lista_Suministro2

    letra_actual = 0
    for fila_Matriz2 in range(tamY_Matriz2):
        for col_Matriz2 in range(tamX_Matriz2):
            # Se salta de crear el primer espacio, esto para que sea el ultimo espacio de la Matriz 1.
            if (fila_Matriz2 == 0) and (col_Matriz2 == 0):
                col_Matriz2 = 1
            
            x0 = tam_Bases + tam_Esp_Libre + (col_Matriz2 * tam_Celdas)
            y0 = tam_Bases + tam_Esp_Libre + (tam_Celdas * tamY_Matriz1) + (fila_Matriz2 * tam_Celdas)
            x1 = x0 + tam_Celdas
            y1 = y0 + tam_Celdas
            color = ident_Color(lista_Suministro2[letra_actual].color)
            matriz2[fila_Matriz2][col_Matriz2] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)

            posx = x0
            posy = y0

            lista_Suministro2[letra_actual].posx = x0
            lista_Suministro2[letra_actual].posy = y0

            letra_actual += 1

# Crea la Matriz de Carga.
def crear_Matriz_C(lienzo, matriz3):
    global lista_Carga

    lista_Carga = []

    letra_actual = 0
    for fila_Matriz3 in range(tam_Matriz3):
        for col_Matriz3 in range(tam_Matriz3):
            x0 = tam_Bases + tam_Esp_Libre + (tam_Celdas * tamX_Matriz2) + (col_Matriz3 * tam_Celdas)
            y0 = tam_Bases + tam_Esp_Libre + (tam_Celdas * tamY_Matriz1) + (fila_Matriz3 * tam_Celdas)
            x1 = x0 + tam_Celdas
            y1 = y0 + tam_Celdas
            color = ident_Color(letras_Carga[letra_actual])
            matriz3[fila_Matriz3][col_Matriz3] = lienzo.create_rectangle(x0, y0, x1, y1, width=3, fill=color)

            posx = x0
            posy = y0
            color = letras_Carga[letra_actual]

            espacio = Carga(posx,posy,color,False)

            if (color == ""):
                espacio.colocada = True
            lista_Carga.append(espacio)

            letra_actual += 1

def acomodo_Cajas_1():
    global boton_Iniciar
    global mensaje_Interfaz

    global lista_Suministro1
    global lista_Suministro2

    boton_Iniciar.destroy()

    lectura_Inicial_Modo1()

    tiempo = 1
    #for pos_Carga_I, elem_Carga_I in enumerate(letras_Carga_Inicial):
    for pos_Sum1, elem_Sum1 in enumerate(lista_Suministro1):
        for pos_Carga, elem_Carga in enumerate(lista_Carga):
            if (elem_Sum1.color == elem_Carga.color) and (elem_Carga.colocada == False):
                X_Destino = elem_Sum1.posx
                Y_Destino = elem_Sum1.posy
                
                # Se mueve primero hacia el espacio en suministro.
                # Dentro de la función de mover_Motores se envía 0 para mover en X y 1 para mover en Y.
                # Crea los hilos para mover los motores y tambien la interfaz.
                hilo1 = threading.Thread(target=mover_Motores("X", X_Actual, X_Destino))
                hilo2 = threading.Thread(target=mover_Motores("Y", Y_Actual, Y_Destino))
                hilo3 = threading.Thread(target=mover_X_Interfaz(X_Destino))
                hilo4 = threading.Thread(target=mover_Y_Interfaz(Y_Destino))

                # Ejecuta el movimiento en X.
                mensaje_Interfaz.config(text="Moviendo Grúa hacia la caja por recoger.")
                # Inicia el primer hilo, mueve el motor de X.
                hilo1.start()
                # Espera a que el primer hilo termine antes de iniciar el tercer hilo.
                hilo1.join()
                # Inicia el tercer hilo, mueve la interfaz en X.
                hilo3.start()
                # Espera a que ambos hilos terminen.
                hilo1.join()
                hilo3.join()
                
                # Ejecuta el movimiento en Y
                # Inicia el segundo hilo, mueve el motor de Y.
                hilo2.start()
                # Espera a que el segundo hilo termine antes de iniciar el cuarto hilo.
                hilo2.join()
                # Inicia el cuarto hilo, mueve la interfaz en Y.
                hilo4.start()
                # Espera a que ambos hilos terminen.
                hilo2.join()
                hilo4.join()

                # Recoge la caja.
                mensaje_Interfaz.config(text="Recogiendo caja.")
                ventana.update()
                # Llamar la función de activar el motor CD y activar el imán.
                # Crear nuevo hilo que suba y baje el motor CD.

                limpiar_Suministro1(X_Destino, Y_Destino, elem_Sum1)
                ventana.update()

                # Se definen los nuevos espacio donde se debe dejar la caja.
                X_Destino = elem_Carga.posx
                Y_Destino = elem_Carga.posy
                
                # Ahora se mueve hacia el espacio donde debe dejar la caja.
                # Crea los hilos para mover los motores y tambien la interfaz.
                hilo1 = threading.Thread(target=mover_Motores("X", X_Actual, X_Destino))
                hilo2 = threading.Thread(target=mover_Motores("Y", Y_Actual, Y_Destino))
                hilo3 = threading.Thread(target=mover_X_Interfaz(X_Destino))
                hilo4 = threading.Thread(target=mover_Y_Interfaz(Y_Destino))
                
                # Ejecuta el movimiento en X.
                mensaje_Interfaz.config(text="Moviendo Grúa hacia el espacio designado.")
                # Inicia el primer hilo, mueve el motor de X.
                hilo1.start()
                # Espera a que el primer hilo termine antes de iniciar el tercer hilo.
                hilo1.join()
                # Inicia el tercer hilo, mueve la interfaz en X.
                hilo3.start()
                # Espera a que ambos hilos terminen.
                hilo1.join()
                hilo3.join()

                # Ejecuta el movimiento en Y
                # Inicia el segundo hilo, mueve el motor de Y.
                hilo2.start()
                # Espera a que el segundo hilo termine antes de iniciar el cuarto hilo.
                hilo2.join()
                # Inicia el cuarto hilo, mueve la interfaz en Y.
                hilo4.start()
                # Espera a que ambos hilos terminen.
                hilo2.join()
                hilo4.join()

                # Suelta la caja.
                mensaje_Interfaz.config(text="Dejando caja.")
                ventana.update()
                # Llamar la función de activar el motor CD y desactivar el imán.

                actualizar_Carga(X_Destino, Y_Destino, elem_Carga.color)
                ventana.update()
                letras_Carga[pos_Carga] = 0

                lista_Suministro1[pos_Sum1].color = ""
                lista_Suministro1[pos_Sum1].ocupada = False
                lista_Carga[pos_Carga].colocada = True

                break

    # Se mueve a la posición inicial.
    mensaje_Interfaz.config(text="Volviendo a la posición inicial.")
    ventana.update()

    X_Destino = tam_Bases
    Y_Destino = tam_Bases

    # Crea los hilos para mover los motores y tambien la interfaz.
    hilo1 = threading.Thread(target=mover_Motores("X", X_Actual, X_Destino))
    hilo2 = threading.Thread(target=mover_Motores("Y", Y_Actual, Y_Destino))
    hilo3 = threading.Thread(target=mover_X_Interfaz(X_Destino))
    hilo4 = threading.Thread(target=mover_Y_Interfaz(Y_Destino))

    # Ejecuta el movimiento en X.
    # Inicia el primer hilo, mueve el motor de X.
    hilo1.start()
    # Espera a que el primer hilo termine antes de iniciar el tercer hilo.
    hilo1.join()
    # Inicia el tercer hilo, mueve la interfaz en X.
    hilo3.start()
    # Espera a que ambos hilos terminen.
    hilo1.join()
    hilo3.join()

    # Ejecuta el movimiento en Y
    # Inicia el segundo hilo, mueve el motor de Y.
    hilo2.start()
    # Espera a que el segundo hilo termine antes de iniciar el cuarto hilo.
    hilo2.join()
    # Inicia el cuarto hilo, mueve la interfaz en Y.
    hilo4.start()
    # Espera a que ambos hilos terminen.
    hilo2.join()
    hilo4.join()
    
    mensaje_Interfaz.config(text="Ha finalizado el acomodo.")
    ventana.update()

# Función para realizar la lectura de la zona de Suministro.
def lectura_Inicial_Modo1():
    global lista_Suministro1
    global lista_Carga
    global mensaje_Interfaz

    mensaje_Interfaz.config(text="Leyendo zona de suministro.")

    contador_R_Suministro = 0
    contador_G_Suministro = 0
    contador_B_Suministro = 0
    
    # Ciclo para recorrer la zona de suministro.
    for pos_Sum1, elem_Sum1 in enumerate(lista_Suministro1):
        X_Destino = elem_Sum1.posx
        Y_Destino = elem_Sum1.posy
        
        # Se mueve primero hacia el espacio en suministro para leer el color de la caja en ese espacio.
        # Dentro de la función de mover_Motores se envía 0 para mover en X y 1 para mover en Y.
        # Crea los hilos para mover los motores y tambien la interfaz.
        hilo1 = threading.Thread(target=mover_Motores("X", X_Actual, X_Destino))
        hilo2 = threading.Thread(target=mover_Motores("Y", Y_Actual, Y_Destino))
        hilo3 = threading.Thread(target=mover_X_Interfaz(X_Destino))
        hilo4 = threading.Thread(target=mover_Y_Interfaz(Y_Destino))

        # Ejecuta el movimiento en X.
        # Inicia el primer hilo, mueve el motor de X.
        hilo1.start()
        # Espera a que el primer hilo termine antes de iniciar el tercer hilo.
        hilo1.join()
        # Inicia el tercer hilo, mueve la interfaz en X.
        hilo3.start()
        # Espera a que ambos hilos terminen.
        hilo1.join()
        hilo3.join()
        
        # Ejecuta el movimiento en Y
        # Inicia el segundo hilo, mueve el motor de Y.
        hilo2.start()
        # Espera a que el segundo hilo termine antes de iniciar el cuarto hilo.
        hilo2.join()
        # Inicia el cuarto hilo, mueve la interfaz en Y.
        hilo4.start()
        # Espera a que ambos hilos terminen.
        hilo2.join()
        hilo4.join()

        color = leer_QR()

        if (color == "V"):
            color = "white"
            lista_Suministro1[pos_Sum1].ocupada = False
        
        elif (color == "R"):
            lista_Suministro1[pos_Sum1].color = color
            color = "#FFAAAA" # Rojo Claro.
            contador_R_Suministro += 1
            lista_Suministro1[pos_Sum1].ocupada = True
        
        elif (color == "G"):
            lista_Suministro1[pos_Sum1].color = color
            color = "#AAFFAA" # Verde Claro.
            contador_G_Suministro += 1
            lista_Suministro1[pos_Sum1].ocupada = True

        elif (color == "B"):
            lista_Suministro1[pos_Sum1].color = color
            color = "#AAAAFF" # Azul Claro.
            contador_B_Suministro += 1
            lista_Suministro1[pos_Sum1].ocupada = True

        # Pinta el espacio del suministro del color de la caja que leyó.
        lienzo.create_rectangle(X_Destino, Y_Destino, X_Destino + 40, Y_Destino + 40, width=3, fill=color)
        grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill="orange")
        break

    """
    # Activación de las alarmas.
    # Alarma 1.
    if (contador_R_Suministro < contador_R_Carga):
        # Llama a la función de la alarma 1
    if (contador_G_Suministro < contador_G_Carga):
        # Llama a la función de la alarma 1
    if (contador_B_Suministro < contador_B_Carga):
        # Llama a la función de la alarma 1
    
    # Alarma 2.
    if (contador_R_Suministro > contador_R_Carga):
        # Llama a la función de la alarma 2
    if (contador_G_Suministro > contador_G_Carga):
        # Llama a la función de la alarma 2
    if (contador_B_Suministro > contador_B_Carga):
        # Llama a la función de la alarma 2
    """

    print("SUMINISTRO")
    b= []
    for pos,elem in enumerate(lista_Suministro1):
        a = elem.color
        if elem.ocupada == False:
            a = "-"
        print(pos, "      ",a)

    # Ciclo para recorrer la zona de carga y revisar la alarma 3.
    obstaculos = 0
    """
    for pos_Carga, elem_Carga in enumerate(lista_Carga):
        X_Destino = elem_Carga.posx
        Y_Destino = elem_Carga.posy
        
        # Se mueve primero hacia el espacio en suministro para leer el color de la caja en ese espacio.
        # Dentro de la función de mover_Motores se envía 0 para mover en X y 1 para mover en Y.
        # Crea los hilos para mover los motores y tambien la interfaz.
        hilo1 = threading.Thread(target=mover_Motores("X", X_Actual, X_Destino))
        hilo2 = threading.Thread(target=mover_Motores("Y", Y_Actual, Y_Destino))
        hilo3 = threading.Thread(target=mover_X_Interfaz(X_Destino))
        hilo4 = threading.Thread(target=mover_Y_Interfaz(Y_Destino))

        # Ejecuta el movimiento en X.
        # Inicia el primer hilo, mueve el motor de X.
        hilo1.start()
        # Espera a que el primer hilo termine antes de iniciar el tercer hilo.
        hilo1.join()
        # Inicia el tercer hilo, mueve la interfaz en X.
        hilo3.start()
        # Espera a que ambos hilos terminen.
        hilo1.join()
        hilo3.join()
        
        # Ejecuta el movimiento en Y
        # Inicia el segundo hilo, mueve el motor de Y.
        hilo2.start()
        # Espera a que el segundo hilo termine antes de iniciar el cuarto hilo.
        hilo2.join()
        # Inicia el cuarto hilo, mueve la interfaz en Y.
        hilo4.start()
        # Espera a que ambos hilos terminen.
        hilo2.join()
        hilo4.join()

        color = leer_QR()

        if (color != "V") or (color != ""):
            obstaculos += 1
        break
    
    if (obstaculos > 0)
        # Llama a la función de la alarma 3.
    """

    # Se mueve a la posición inicial después de verificar las alarmas.
    mensaje_Interfaz.config(text="Volviendo a la posición inicial.")
    ventana.update()

    X_Destino = tam_Bases
    Y_Destino = tam_Bases

    # Crea los hilos para mover los motores y tambien la interfaz.
    hilo1 = threading.Thread(target=mover_Motores("X", X_Actual, X_Destino))
    hilo2 = threading.Thread(target=mover_Motores("Y", Y_Actual, Y_Destino))
    hilo3 = threading.Thread(target=mover_X_Interfaz(X_Destino))
    hilo4 = threading.Thread(target=mover_Y_Interfaz(Y_Destino))

    # Ejecuta el movimiento en X.
    # Inicia el primer hilo, mueve el motor de X.
    hilo1.start()
    # Espera a que el primer hilo termine antes de iniciar el tercer hilo.
    hilo1.join()
    # Inicia el tercer hilo, mueve la interfaz en X.
    hilo3.start()
    # Espera a que ambos hilos terminen.
    hilo1.join()
    hilo3.join()
    
    # Ejecuta el movimiento en Y
    # Inicia el segundo hilo, mueve el motor de Y.
    hilo2.start()
    # Espera a que el segundo hilo termine antes de iniciar el cuarto hilo.
    hilo2.join()
    # Inicia el cuarto hilo, mueve la interfaz en Y.
    hilo4.start()
    # Espera a que ambos hilos terminen.
    hilo2.join()
    hilo4.join()

    mensaje_Interfaz.config(text="En espera.")
    ventana.update()

def leer_QR():
    # Creamos la videocaptura
    cap = cv2.VideoCapture(0)
    leyo = False
    # Empezamos
    while True:
        # Leemos los frames
        ret, frame = cap.read()

        # Leemos los codigos QR
        for codes in decode(frame):

            # Decodidficamos
            info = codes.data.decode("utf-8") # En código ASCII

            # Tipo de caja, LETRA en ASCII
            tipo = info[0:2]
            tipo = int(tipo)

            #Formato para los códigos:
            #Caja Roja: 82
            if tipo == 82:  # R->82, RED
                color = "R"
                leyo = True
                break

            #Formato para los códigos:
            #Caja Verde: 71
            if tipo == 71:  # G->71, GREEN
                color = "G"
                leyo = True
                break
            
            #Formato para los códigos:
            #Caja Azul: 66
            if tipo == 66:  # B->66, BLUE
                color = "B"
                leyo = True
                break

            #Formato para los códigos:
            #Espacio Vacio: 86
            if tipo == 86:  # V->86, Espacio Vacio
                color = "V"
                leyo = True
                break

        if (leyo == True):
            break
        
    cv2.destroyAllWindows()
    cap.release()

    return (color)

# Mover la grúa horizontalmente en la interfaz.
def mover_X_Interfaz(X_Destino):
    global grua
    global X_Actual

    # Movimiento horizontal.
    movimiento_X = X_Destino - X_Actual

    # Si ya está en la misma posición en X que el destino.
    if (X_Actual == X_Destino):
        movimiento_X = 0

    lienzo.move(grua, movimiento_X, 0)
    X_Actual = X_Destino
    ventana.update()

    return

# Mover la grúa verticalmente en la interfaz.
def mover_Y_Interfaz(Y_Destino):
    global grua
    global Y_Actual

    # Movimiento vertical.
    movimiento_Y = Y_Destino - Y_Actual
    
    # Si ya está en la misma posición en Y que el destino.
    if (Y_Actual == Y_Destino):
        movimiento_Y = 0

    lienzo.move(grua, 0, movimiento_Y)
    Y_Actual = Y_Destino
    ventana.update()
    return

# Ejecuta la comunicación con el ESP32 y le indica cual motor mover, en qué dirección y cuantos pasos.
def mover_Motores(motor, X_Actual, X_Destino):
    global microProces
    global mensaje_Motores
    
    pasos = X_Destino - X_Actual

    # Se envía al ESP32 el Motor a utilizar y el número de pasos a dar.
    comando = f"{motor}{pasos}\n"
    microProces.write(comando.encode())

    # Lo que retorna el ESP32 cuando se terminó de mover un motor.
    mensaje_Motores = microProces.readline().decode()

# Actualiza el color de cada espacio del suministro 1 según va posicionando cada caja.
def limpiar_Suministro1(X_Destino, Y_Destino, elemento):
    global lienzo
    global grua

    color = elemento.color

    # Pinta el espacio de suministro de color blanco debido a que la grua recoge la caja.
    # En caso de que recoja una caja, la grúa también se pinta del color de la caja.
    color = ident_Color(elemento.color)
    lienzo.create_rectangle(X_Destino, Y_Destino, X_Destino + 40, Y_Destino + 40, fill="white")

    grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill=color)

    return
    
# Actualiza el color de cada espacio de la carga según va posicionando cada caja.
def actualizar_Carga(X_Destino, Y_Destino, color):
    global lienzo
    global grua

    if color == "R":  # Rojo Oscuro.
        color = "#FF0000"

    elif color == "G":  # Verde Oscuro.
        color = "#00FF00"

    elif color == "B":  # Azul Oscuro.
        color = "#0000FF"

    # Actualiza la matriz de la zona de Carga.
    lienzo.create_rectangle(X_Destino, Y_Destino, X_Destino + 40, Y_Destino + 40, width=3, fill=color)

    grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill="orange")

    return

# Vuelve al menu principal.
def volver_Inicio():
    global boton_Cargar
    global mensaje_Interfaz
    global boton_Volver
    global boton_Iniciar
    global lienzo

    global lista_Carga
    global lista_Suministro1
    global lista_Suministro2
    global Modo_Seleccionado

    global X_Actual
    global Y_Actual

    global microProces

    lienzo.destroy()
    boton_Volver.destroy()
    boton_Iniciar.destroy()
    mensaje_Interfaz.destroy()

    microProces.close()

    lista_Carga = []
    lista_Suministro1 = []
    lista_Suministro2 = []

    Modo_Seleccionado = 0

    X_Actual = 0
    Y_Actual = 0

    boton_Cargar = tk.Button(ventana, text="Cargar Archivo CSV", command=abrir_Excel)
    boton_Cargar.pack(side="top")

#########################################################################################################
# Main.
if __name__ == "__main__":
    ventana = tk.Tk()
    app = Interfaz(ventana)
    ventana.mainloop()
