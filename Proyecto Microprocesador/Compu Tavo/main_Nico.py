# Librerías
import tkinter as tk
from tkinter import filedialog
import csv
import time
from Clases import *

#########################################################################################################
# Variables Globales.

lista_Suministro1 = []
lista_Suministro2 = []
lista_Carga = []

letras_Suministro1 = []
letras_Suministro2 = []
letras_Carga = []

contador_R = 0
contador_G = 0
contador_B = 0

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

Modo_Seleccionado = 0

#########################################################################################################
# Funciones.
def Interfaz(ventana):
    global boton_Cargar

    ventana.title("Grúa Pórtico")
    ventana.geometry("600x600")

    boton_Cargar = tk.Button(ventana, text="Cargar Archivo CSV", command=abrir_Excel)
    boton_Cargar.pack(side="top")

# Función: Abrir los archivos de excel en formato cvs.
def abrir_Excel():
    global letras_Carga
    global contador_R
    global contador_G
    global contador_B

    letras_Carga = []

    archivo_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

    if archivo_path:
        with open(archivo_path, 'r', newline='') as file:
            lector_csv = csv.reader(file, delimiter=';')
            for fila in lector_csv:
                for color in fila:
                    letras_Carga.append(color)

    letra = 0
    contador_R = 0
    contador_G = 0
    contador_B = 0

    while letra < len(letras_Carga):
        if letras_Carga[letra] == "R":  # Caja Roja.
            contador_R += 1

        elif letras_Carga[letra] == "G":  # Caja Verde.
            contador_G += 1

        elif letras_Carga[letra] == "B":  # Caja Azul.
            contador_B += 1
        letra += 1
    
    print(contador_R)
    print(contador_G)
    print(contador_B)

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
    global Mensaje
    global boton_Volver
    global boton_Iniciar
    global lienzo

    global grua
    global X_Actual
    global Y_Actual

    boton_Cargar.destroy()
    boton_Modo1.destroy()
    boton_Modo2.destroy()

    lienzo = tk.Canvas(ventana, width=ancho, height=alto, background="black")
    lienzo.place(x=(600/2)-(ancho/2), y=(600/2)-(alto/2))

    matriz1 = [[None for _ in range(tamX_Matriz1)] for _ in range(tamY_Matriz1)]  # Cantidad en X, Cantidad en Y.
    matriz1.append([None]) # Crea un nuevo espacio en la matriz para que sean 25
    matriz2 = [[None for _ in range(tamX_Matriz2)] for _ in range(tamY_Matriz2)]
    matriz3 = [[None for _ in range(tam_Matriz3)] for _ in range(tam_Matriz3)]

    # Crea un espacio libre en gris.
    # Las medidas son las escogidas según las especificaciones.
    x0 = tam_Bases
    y0 = tam_Bases
    x1 = 416  # (60*8)-(8*8)
    y1 = 416
    Esp_Libre = lienzo.create_rectangle(x0, y0, x1, y1, fill="#B2B2B2")

    """
    If (Modo_Seleccionado == 1):
        Lectura del Espacio de Trabajo (Modo_Seleccionado)
    """

    
    # Crea el objeto representativo de la grúa.
    X_Actual = tam_Bases
    Y_Actual = tam_Bases
    X_Final = X_Actual + tam_Celdas
    Y_Final = Y_Actual + tam_Celdas
    

    Mensaje = tk.Label(ventana, text="En espera", font=("Arial", 16))
    Mensaje.pack(side="bottom")

    boton_Volver = tk.Button(ventana, text="Volver a pantalla principal", command=volver_Inicio)
    boton_Volver.pack(side="top")

    if (Modo_Seleccionado == 1):
        crear_Matriz_S1(lienzo, matriz1)
        crear_Matriz_S2(lienzo, matriz2)
        crear_Matriz_C(lienzo, matriz3)
        grua = lienzo.create_oval(X_Actual, Y_Actual, X_Final, Y_Final, width=1, fill="orange")
        boton_Iniciar = tk.Button(ventana, text="Iniciar Acomodo", command=acomodo_Cajas_1)
        boton_Iniciar.pack(side="top")

    if (Modo_Seleccionado == 2):
        crear_Matriz_S1_vacio(lienzo, matriz1)
        crear_Matriz_S2_M2(lienzo, matriz2)
        crear_Matriz_C(lienzo, matriz3)
        grua = lienzo.create_oval(X_Actual, Y_Actual, X_Final, Y_Final, width=1, fill="orange")
        boton_Iniciar = tk.Button(ventana, text="Iniciar Acomodo", command=acomodo_Cajas_2)
        boton_Iniciar.pack(side="top")

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
def iniciar_suministros():
    global letras_Suministro1
    global letras_Suministro2
    
    letras_Suministro1 = []
    letras_Suministro2 = []
    j=0
    while(j<25):
        color = ""
        letras_Suministro1.append(color)
        j += 1

    i = 0
    while (i < 16):
        color = ""
        letras_Suministro2.append(color)
        i += 1



# Crea la Matriz de Suministro 1.
def crear_Matriz_S1(lienzo, matriz1):
    global lista_Suministro1
    lista_Suministro1 = []

    leer_Excel_Prueba()
    letra_actual = 0

    for fila_Matriz1 in range(tamY_Matriz1):
        for col_Matriz1 in range(tamX_Matriz1):
            x0 = tam_Bases + tam_Esp_Libre + (col_Matriz1 * tam_Celdas)
            y0 = tam_Bases + tam_Esp_Libre + (fila_Matriz1 * tam_Celdas)
            x1 = x0 + tam_Celdas
            y1 = y0 + tam_Celdas
            color = ident_Color(letra_actual, letras_Suministro1)
            matriz1[fila_Matriz1][col_Matriz1] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)
                        
            posx = x0
            posy = y0
            color = letras_Suministro1[letra_actual]

            letra_actual += 1

            espacio = Suministro(posx,posy,color,False)
            lista_Suministro1.append(espacio)

            # Crea el ultimo espacio de la matriz de manera que se "sale" de los 8x3 espacios originales, esto para que sean 25 espacios en total.
            if (fila_Matriz1 == 2) and (col_Matriz1 == 7):
                col_Matriz1 = 0
                fila_Matriz1 = 3
                x0 = tam_Bases + tam_Esp_Libre + (col_Matriz1 * tam_Celdas)
                y0 = tam_Bases + tam_Esp_Libre + (fila_Matriz1 * tam_Celdas)
                x1 = x0 + tam_Celdas
                y1 = y0 + tam_Celdas                    
                color = ident_Color(letra_actual, letras_Suministro1)
                matriz1[fila_Matriz1][col_Matriz1] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)
                
                posx = x0
                posy = y0
                color = letras_Suministro1[letra_actual]

                espacio = Suministro(posx,posy,color,True)
                lista_Suministro1.append(espacio)

def crear_Matriz_S1_vacio(lienzo, matriz1):
    global lista_Suministro1
    iniciar_suministros()
    letra_actual = 0

    for fila_Matriz1 in range(tamY_Matriz1):
        for col_Matriz1 in range(tamX_Matriz1):
            x0 = tam_Bases + tam_Esp_Libre + (col_Matriz1 * tam_Celdas)
            y0 = tam_Bases + tam_Esp_Libre + (fila_Matriz1 * tam_Celdas)
            x1 = x0 + tam_Celdas
            y1 = y0 + tam_Celdas
            color = ident_Color(letra_actual, letras_Suministro1)
            matriz1[fila_Matriz1][col_Matriz1] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)
                        
            posx = x0
            posy = y0

   
            espacio = Suministro(posx,posy,color,False)
            lista_Suministro1.append(espacio)

            # Crea el ultimo espacio de la matriz de manera que se "sale" de los 8x3 espacios originales, esto para que sean 25 espacios en total.
            if (fila_Matriz1 == 2) and (col_Matriz1 == 7):
                col_Matriz1 = 0
                fila_Matriz1 = 3
                x0 = tam_Bases + tam_Esp_Libre + (col_Matriz1 * tam_Celdas)
                y0 = tam_Bases + tam_Esp_Libre + (fila_Matriz1 * tam_Celdas)
                x1 = x0 + tam_Celdas
                y1 = y0 + tam_Celdas                    
                color = ident_Color(letra_actual, letras_Suministro1)
                matriz1[fila_Matriz1][col_Matriz1] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)
                
                posx = x0
                posy = y0
                color = letras_Suministro1[letra_actual]

                espacio = Suministro(posx,posy,color,False)
                lista_Suministro1.append(espacio)



# Crea la Matriz 2.
def crear_Matriz_S2(lienzo, matriz2):
    global lista_Suministro2
    lista_Suministro2 = []

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
            color = ident_Color(letra_actual, letras_Suministro2)
            matriz2[fila_Matriz2][col_Matriz2] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)

            posx = x0
            posy = y0
            color = letras_Suministro2[letra_actual]

            espacio = Suministro(posx,posy,color,False)
            lista_Suministro2.append(espacio)

            letra_actual += 1

def crear_Matriz_S2_M2(lienzo, matriz2):
    global lista_Suministro2
    lista_Suministro2 = list(range(16))

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
            color = ident_Color(letra_actual, letras_Suministro2)
            matriz2[fila_Matriz2][col_Matriz2] = lienzo.create_rectangle(x0, y0, x1, y1, fill=color)

            posx = x0
            posy = y0
            color = letras_Suministro2[letra_actual]

            espacio = Suministro(posx,posy,color,False)
            lista_Suministro2.append(espacio)

            letra_actual += 1

# Crea la Matriz 3.
def crear_Matriz_C(lienzo, matriz3):
    letra_actual = 0
    for fila_Matriz3 in range(tam_Matriz3):
        for col_Matriz3 in range(tam_Matriz3):
            x0 = tam_Bases + tam_Esp_Libre + (tam_Celdas * tamX_Matriz2) + (col_Matriz3 * tam_Celdas)
            y0 = tam_Bases + tam_Esp_Libre + (tam_Celdas * tamY_Matriz1) + (fila_Matriz3 * tam_Celdas)
            x1 = x0 + tam_Celdas
            y1 = y0 + tam_Celdas
            color = ident_Color(letra_actual, letras_Carga)
            matriz3[fila_Matriz3][col_Matriz3] = lienzo.create_rectangle(x0, y0, x1, y1, width=3, fill=color)

            posx = x0
            posy = y0
            color = letras_Carga[letra_actual]

            espacio = Carga(posx,posy,color,False)
            if (color == ""):
                espacio.colocada = True
            lista_Carga.append(espacio)
            letra_actual += 1

def pintar_Matriz_CargaActual(lienzo, carga_actual):
    letra_actual = 0
    matriz3 = [[None for _ in range(tam_Matriz3)] for _ in range(tam_Matriz3)]
    for fila_Matriz3 in range(tam_Matriz3):
        for col_Matriz3 in range(tam_Matriz3):
            x0 = tam_Bases + tam_Esp_Libre + (tam_Celdas * tamX_Matriz2) + (col_Matriz3 * tam_Celdas)
            y0 = tam_Bases + tam_Esp_Libre + (tam_Celdas * tamY_Matriz1) + (fila_Matriz3 * tam_Celdas)
            x1 = x0 + tam_Celdas
            y1 = y0 + tam_Celdas
            color = ident_Color(letra_actual, carga_actual)
            matriz3[fila_Matriz3][col_Matriz3] = lienzo.create_rectangle(x0, y0, x1, y1, width=3, fill=color)

            posx = x0
            posy = y0
            color = letras_Carga[letra_actual]

            letra_actual += 1

# Define el color del espacio de la matriz dependiendo de la lista que reciba.
def ident_Color(letra_actual, letras):
    while letra_actual < len(letras):
        if letras[letra_actual] == "R":  # Rojo Claro.
            return "#FFAAAA"

        elif letras[letra_actual] == "G":  # Verde Claro.
            return "#AAFFAA"

        elif letras[letra_actual] == "B":  # Azul Claro.
            return "#AAAAFF"
        
        else:
            return "white"

def ident_Color_2(letra):
        if letra == "R":  # Rojo Claro.
            return "#FFAAAA"

        elif letra == "G":  # Verde Claro.
            return "#AAFFAA"

        elif letra == "B":  # Azul Claro.
            return "#AAAAFF"
        
        else:
            return "white"


def acomodo_Cajas_1():
    global boton_Iniciar
    global Mensaje

    global lista_Suministro1
    global lista_Suministro1

    boton_Iniciar.destroy()

    #for pos_Carga_I, elem_Carga_I in enumerate(letras_Carga_Inicial):
    for pos_Sum1, elem_Sum1 in enumerate(lista_Suministro1):
        for pos_Carga, elem_Carga in enumerate(lista_Carga):
            if (elem_Sum1.color == elem_Carga.color) and (elem_Carga.colocada == False):
                X_Destino = elem_Sum1.posx
                Y_Destino = elem_Sum1.posy


                # Ejecuta el movimiento, primero en X y luego en Y.
                # Primero se mueve hacia la caja que debe recoger.
                Mensaje.config(text="Moviendo Grua hacia la caja por recoger.")
                mover_Grua_X(X_Destino)

                mover_Grua_Y(Y_Destino)
                Mensaje.config(text="Recogiendo caja.")
                ventana.update()

                actualizar_Suministro1(X_Destino, Y_Destino)
                agarre_grua(elem_Sum1.color,X_Actual,Y_Actual)


                X_Destino = elem_Carga.posx
                Y_Destino = elem_Carga.posy
                
                # Ahora se mueve hacia el espacio donde debe dejar la caja.
                Mensaje.config(text="Moviendo Grua hacia el espacio designado.")
                mover_Grua_X(X_Destino)
                ventana.update()

                mover_Grua_Y(Y_Destino)
                Mensaje.config(text="Dejando caja.")
                ventana.update()
    
                actualizar_Carga(elem_Carga.color, X_Destino, Y_Destino)
                agarre_grua("naranja",X_Destino,Y_Destino)
                
                letras_Carga[pos_Carga] = 0

                lista_Suministro1[pos_Sum1].color = ""
                lista_Suministro1[pos_Sum1].ocupada = False
                lista_Carga[pos_Carga].colocada = True

                break

    # Se mueve a la posición inicial.
    Mensaje.config(text="Volviendo a la posición inicial.")
    X_Destino = tam_Bases
    Y_Destino = tam_Bases
    mover_Grua_X(X_Destino)
    time.sleep(2)
    ventana.update()

    mover_Grua_Y(Y_Destino)
    time.sleep(2)
    Mensaje.config(text="Ha finalizado el acomodo.")
    ventana.update()

# Mover la grúa horizontalmente.
def mover_Grua_X(X_Destino):
    global grua
    global X_Actual

    # Movimiento horizontal.
    movimiento_X = X_Destino - X_Actual
    sum = movimiento_X/4
    #mov = 2 #movimiento_X/10
    if movimiento_X>0:
        mov = 4
    elif movimiento_X<0:
        mov = -4

    # Si ya está en la misma posición en X que el destino.
    if (X_Actual == X_Destino):
        movimiento_X = 0


    while X_Actual != X_Destino:
        lienzo.move(grua, mov, 0)
        X_Actual = X_Actual + mov
        time.sleep(0.1)
        ventana.update()
        if (movimiento_X > 0 and X_Actual >= X_Destino):
            movimiento_X = X_Destino - X_Actual
            lienzo.move(grua, movimiento_X, 0)
            X_Actual = X_Destino
            time.sleep(0.1)
            ventana.update()
            break
        elif (movimiento_X < 0 and X_Actual <= X_Destino):
            movimiento_X = X_Destino - X_Actual
            lienzo.move(grua, movimiento_X, 0)
            X_Actual = X_Destino
            
            time.sleep(0.1)
            ventana.update()
            break

    #lienzo.move(grua, movimiento_X, 0)
    X_Actual = X_Destino
    return

# Mover la grúa verticalmente.
def mover_Grua_Y(Y_Destino):
    global grua
    global Y_Actual

    # Movimiento vertical.
    movimiento_Y = Y_Destino - Y_Actual
    if movimiento_Y>0:
        mov = 4
    elif movimiento_Y<0:
        mov = -4

    # Si ya está en la misma posición en Y que el destino.
    if (Y_Actual == Y_Destino):
        movimiento_Y = 0


    while Y_Actual != Y_Destino:
        lienzo.move(grua, 0, mov)
        Y_Actual = Y_Actual + mov
        time.sleep(0.1)
        ventana.update()
        if (movimiento_Y > 0 and Y_Actual >= Y_Destino):
            movimiento_Y = Y_Destino - Y_Actual
            lienzo.move(grua, 0, movimiento_Y)
            Y_Actual = Y_Destino
            time.sleep(0.1)
            ventana.update()
            break
        elif (movimiento_Y < 0 and Y_Actual <= Y_Destino):
            movimiento_Y = Y_Destino - Y_Actual
            lienzo.move(grua, 0, movimiento_Y)
            Y_Actual = Y_Destino
            time.sleep(0.1)
            ventana.update()
            break
    # Si ya está en la misma posición en Y que el destino.

    lienzo.move(grua, 0, movimiento_Y)

    Y_Actual = Y_Destino        
    return

def actualizar_Suministro1(X_Destino, Y_Destino):
    global lienzo
    global grua
    # Actualiza la matriz de la zona de Suministro 1.
    lienzo.create_rectangle(X_Destino, Y_Destino, X_Destino + 40, Y_Destino + 40, fill="white")
    
    #grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill="orange")
    return


def agarre_grua(letra,X_Actual,Y_Actual):
    global lienzo
    global grua
    if letra == "R":  # Rojo Claro.
        color = "#FF0000"

    elif letra == "G":  # Verde Claro.
        color = "#00FF00"

    elif letra == "B":  # Azul Claro.
        color = "#0000FF"
    elif letra == "":
        color = "white"
    else:
        color = "orange"
    # Actualiza la matriz de la zona de Suministro 1.
    grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill=color)
    time.sleep(1.5)
    ventana.update()
    return
 

def colocar_Suministro1(color,X_Destino, Y_Destino):
    global lienzo
    global grua
    if color == "R":  # Rojo Claro.
        color = "#FF0000"

    elif color == "G":  # Verde Claro.
        color = "#00FF00"

    elif color == "B":  # Azul Claro.
        color = "#0000FF"
    elif color == "":
        color = "white"
    
    # Actualiza la matriz de la zona de Suministro 1 con una caja nueva.
    lienzo.create_rectangle(X_Destino, Y_Destino, X_Destino + 40, Y_Destino + 40, fill=color)
    
    #grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill="orange")
    
    return


def actualizar_Carga(letra, X_Destino, Y_Destino):
    global lienzo
    global grua

    if letra == "R":  # Rojo Claro.
        color = "#FF0000"

    elif letra == "G":  # Verde Claro.
        color = "#00FF00"

    elif letra == "B":  # Azul Claro.
        color = "#0000FF"
    else:
        color = "white"

    # Actualiza la matriz de la zona de Carga.
    lienzo.create_rectangle(X_Destino, Y_Destino, X_Destino + 40, Y_Destino + 40, width=3, fill=color)
    time.sleep(1)
    ventana.update

    #grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill="orange")

    return

def Carga_actual():
    letras_Carga = []

    archivo_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

    if archivo_path:
        with open(archivo_path, 'r', newline='') as file:
            lector_csv = csv.reader(file, delimiter=';')
            for fila in lector_csv:
                for color in fila:
                    letras_Carga.append(color)
    return letras_Carga
    
def buscar_espacio():
    pos_Sum1 = 0
    while pos_Sum1<25:
        if lista_Suministro1[pos_Sum1].ocupada == False:
            return pos_Sum1
        pos_Sum1 += 1 
    
    # Si no hay cajas en suministro se debe de colocar en 0


def acomodo_Cajas_2():
    """
    Algoritmo de acomodo 2
    """
    global lista_Suministro1  # Ya está inicializada en crear_Matriz_S1_vacio
    global lista_Carga 
    global lienzo     

    boton_Iniciar.destroy()
    # Se sube la carga actual
    lista_act = Carga_actual()

    Pos_act = 0 
    pintar_Matriz_CargaActual(lienzo,lista_act)  

    while Pos_act <25:
        
        # Mover a posición en X y Y para la pos_act
        
        X_destino = lista_Carga[Pos_act].posx
        Y_destino =  lista_Carga[Pos_act].posy
        mover_Grua_X(X_destino)
        mover_Grua_Y(Y_destino)
    
        # Escanea
        Escaneo = lista_act[Pos_act] # Función de escanear QR
        color_act = Escaneo  # Es el color escaneado en la posición actual
        agarre_grua(color_act,X_Actual,Y_Actual)  #Simula que lo agarra
        color_des = lista_Carga[Pos_act].color


        if (color_des == color_act):
            # Se deja ahí, no agarra la caja
            lista_Carga[Pos_act].colocada = True
        
            # print("No se mueve, la caja para la posición ",Pos_act," ya está colocada")
            actualizar_Carga(color_act,X_destino, Y_destino)  # Se actualiza la interfaz

            agarre_grua("n",X_Actual,Y_Actual)
            
            
        else:
            colocada_ant = False  # Para validar si se colocó en pos ant en carga 
            if Pos_act!=0:
                colocada_ant = False  # Para validar si se colocó en pos ant en carga   
                for i in list(range(Pos_act)):
                    if (lista_Carga[i].color == color_act and colocada_ant == False and lista_Carga[i].colocada == False):
                        # Se busca dejar la caja escaneada en una posición anterior
                        # Microprocesador
                        # Agarra la caja (Bajar_garra= ON -> imán = ON  -> Subir_garra=ON) y moverse a la posición i
                        # Bajar_garra(True)
                        # Prender_iman(True)
                        # Subir_garra (True)
                        # Mov_x(lista_carga[i].posx)) # Para moverse en X
                        # Mov_y(lista_carga[i].posy)) # Para moverse en Y 
                        # Bajar_garra(True)
                        # Prender_iman(False)**
                        # Subir_garra (True)
                        actualizar_Carga("w",X_destino, Y_destino)  # Se coloca cuadro blanco
                        ventana.update()

                        agarre_grua(color_act,X_Actual,Y_Actual)
                        X_destino = lista_Carga[i].posx
                        Y_destino =  lista_Carga[i].posy
                        mover_Grua_X(X_destino)
                        mover_Grua_Y(Y_destino)


                        colocada_ant = True
                        lista_Carga[i].colocada = True

                        actualizar_Carga(color_act,X_destino, Y_destino)  # Se coloca el cuadrado, grua naranja
                        agarre_grua("naranja",X_destino,Y_destino) # Se coloca la grúa naranja
                        time.sleep(1)
                        ventana.update()


                        lista_act[i] = lista_Carga[i].color
                        lista_act[Pos_act] = "" # Se vacía
                        lista_act[i] = lista_Carga[i].color
                        # print("Se mueve la caja de la posición", Pos_act, " a ", i)
                        
                        
             # No hay espacios anteriores, se debe dejar la caja en suministro
            if (colocada_ant == False):
                # Crea el objeto suministro y lo registra en la lista de suministro
                #j = len(lista_Suministro1) # Para saber cual posición física de suministro debe ir
                #sum_x = posxf_sum[j]
                #sum_y = posyf_sum[j]
                #new_sum = Suministro(0,0,color_act, True) 
                #lista_Suministro1.append(new_sum)

                # Se busca el primer espacio en suministro vacío
                espacio = buscar_espacio()
                actualizar_Carga("w",X_destino,Y_destino)  # Se pone en blanco
                agarre_grua(color_act,X_Actual,Y_Actual)
                time.sleep(1)
                ventana.update()
                


                #agarre_grua(color_act,X_Actual,Y_Actual) # Se pone la grua del color de la caja q agarró
                lista_act[Pos_act] = "-" # Se vacía

                X_destino = lista_Suministro1[espacio].posx
                Y_destino =  lista_Suministro1[espacio].posy

                mover_Grua_X(X_destino)
                time.sleep(1)
                ventana.update()

                mover_Grua_Y(Y_destino)
                time.sleep(1)
                ventana.update()

                colocar_Suministro1(color_act,X_destino, Y_destino)  # Se coloca la caja
                agarre_grua("n",X_Actual,Y_Actual)
                time.sleep(1)
                ventana.update()

                #actualizar_Suministro1(X_destino,Y_destino)
                lista_Suministro1[espacio].color = color_act
                lista_Suministro1[espacio].ocupada = True

                """
                # Se mueve físicamente al lugar sum_x y sum_y
                # Agarra la caja (Bajar_garra= ON -> imán = ON  -> Subir_garra=ON) y moverse a la posición i
                # Bajar_garra(True)
                # Prender_iman(True)
                # Subir_garra (True)
                # Mov_x(lista_sumin[i].posx)) # Para moverse en X
                # Mov_y(lista_sumin[i].posy)) # Para moverse en Y 
                # Bajar_garra(True)
                # Prender_iman(False)
                # Subir_garra (True)
                """


            # Busca si en SUMINISTRO hay cajas con el color deseado para la Pos_act
            if (len(lista_Suministro1) != 0):
                for c in list(range((len(lista_Suministro1)))):
                    if (lista_Suministro1[c].color == color_des and lista_Carga[Pos_act].colocada == False and lista_Suministro1[c].ocupada == True):
                        # Sí hay cajas con el color deseado para la posción actual en carga
                        # Debe ir por la caja en suministro y colocarla en Pos_act
                        """
                        # Yendo por la caja a suministro
                        # Agarra la caja (Bajar_garra= ON -> imán = ON  -> Subir_garra=ON) y moverse a la posición i
                        # Bajar_garra(False)
                        # Prender_iman(False)
                        # Subir_garra (False)
                        # Mov_x(lista_sumin[c].posx)) # Para moverse en X
                        # Mov_y(lista_sumin[c].posy)) # Para moverse en Y 
                        # Bajar_garra(False)
                        # Prender_iman(False)
                        # Subir_garra (False)

                        #Yendo otra vez a la Pos_act en carga
                        # Agarra la caja (Bajar_garra= ON -> imán = ON  -> Subir_garra=ON) y moverse a la posición i
                        # Bajar_garra(True)
                        # Prender_iman(True)
                        # Subir_garra (True)
                        # Mov_x(lista_carga[Pos_act].posx)) # Para moverse en X
                        # Mov_y(lista_carga[Pos_act].posy)) # Para moverse en Y 
                        # Bajar_garra(True)
                        # Prender_iman(False)
                        # Subir_garra (True)
                        """
                        # C es la posicion de suministro que debe ir
                        X_destino = lista_Suministro1[c].posx
                        Y_destino =  lista_Suministro1[c].posy

                        mover_Grua_X(X_destino)
                        time.sleep(1)
                        ventana.update()

                        mover_Grua_Y(Y_destino)
                        time.sleep(1)
                        ventana.update()

                        colocar_Suministro1("",X_destino, Y_destino)  # Se quita la caja
                        agarre_grua(color_des,X_Actual,Y_Actual)
                        time.sleep(1)
                        ventana.update()

                        
                        lista_act[Pos_act] = lista_Carga[Pos_act].color
                        lista_Suministro1[c].ocupada = False
                        lista_Suministro1[c].color = " "
                        # Se deja en carga

                        X_destino = lista_Carga[Pos_act].posx
                        Y_destino =  lista_Carga[Pos_act].posy

                        mover_Grua_X(X_destino)
                        time.sleep(1)
                        ventana.update()

                        mover_Grua_Y(Y_destino)
                        time.sleep(1)
                        ventana.update()
                                                

                        lista_Carga[Pos_act].colocada = True
                        lista_act[Pos_act] = lista_Carga[Pos_act].color
                        actualizar_Carga(color_des,X_destino,Y_destino)
                        agarre_grua("n",X_Actual,Y_Actual)
                        time.sleep(1)
                        ventana.update()
                        break  # Se sale del ciclo For


        Pos_act += 1

    # Ya acabó de revisar toda la carga, debe revisar si quedan espacios en carga sin colocar

    faltan = 0
    for i in list(range(25)):
        if lista_Carga[i].colocada == False:
            faltan += 1

    if faltan == 0:
        print("¡Ya terminó el acomodo!")

        return
    else:
        for j in list(range(25)):
            if lista_Carga[j].colocada == False:  # Condición que no está colocada
                color_des = lista_Carga[j].color
                listo = False  # Verifica cuando ya se colocó

                for k in list(range((len(lista_Suministro1)))): 
                    # Revisa si hay cajas con el color en suministro

                    if (lista_Suministro1[k].color == color_des and lista_Suministro1[k].ocupada == True and listo == False):
                        # Sí hay cajas con el color deseado en sum para la posción actual (j) en carga
                        # Debe ir por la caja en suministro y colocarla en Pos_act (j) en carga

                        # Yendo por la caja a suministro
                        # Bajar_garra(False)
                        # Prender_iman(False)
                        # Subir_garra (False)
                        # Mov_x(lista_sumin[k].posx)) # Para moverse en X
                        # Mov_y(lista_sumin[k].posy)) # Para moverse en Y 
                        # Bajar_garra(False)
                        # Prender_iman(False)
                        # Subir_garra (False)
                        lista_Suministro1[k].ocupada = False

                        #Yendo otra vez a la Pos_act en carga
                        # Agarra la caja (Bajar_garra= ON -> imán = ON  -> Subir_garra=ON) y moverse a la posición i
                        # Bajar_garra(True)
                        # Prender_iman(True)
                        # Subir_garra (True)
                        # Mov_x(lista_carga[j].posx)) # Para moverse en X
                        # Mov_y(lista_carga[j].posy)) # Para moverse en Y 
                        # Bajar_garra(True)
                        # Prender_iman(False)
                        # Subir_garra (True)
                        lista_Carga[j].colocada = True
                        listo = True
                        lista_act[j] = lista_Carga[j].color
                                            
                if listo == False:
                    # No hay cajas en suministro para colocar en carga
                    # Caso: Ni modo
                    #lista_carga[j].colocada = True
                    print("Para la posición ",j," para el color ",lista_Carga[j].color," no hay cajas disponibles")           
        Mensaje.config(text="Volviendo a la posición inicial.")
        X_Destino = tam_Bases
        Y_Destino = tam_Bases
        mover_Grua_X(X_Destino)
        time.sleep(0.1)
        ventana.update()

        mover_Grua_Y(Y_Destino)
        time.sleep(0.1)
        Mensaje.config(text="Ha finalizado el acomodo.")
        ventana.update()
        return


# Vuelve al menu principal.
def volver_Inicio():
    global boton_Cargar
    global Mensaje
    global boton_Volver
    global boton_Iniciar
    global lienzo

    global lista_Carga
    global lista_Suministro1
    global lista_Suministro2
    global Modo_Seleccionado

    global X_Actual
    global Y_Actual

    lienzo.destroy()
    boton_Volver.destroy()
    boton_Iniciar.destroy()
    Mensaje.destroy()

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