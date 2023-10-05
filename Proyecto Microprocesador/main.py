# Librerías
import tkinter as tk
from tkinter import filedialog
import csv
import time
import serial
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
    global microProces
    
    global letras_Carga
    global contador_R
    global contador_G
    global contador_B

    microProces = serial.Serial("COM3", 9600)

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
    boton_Modo2 = tk.Button(ventana, text="Ejecutar Modo de Acomodo 2", command="""__init__""")
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

    crear_Matriz_S1(lienzo, matriz1)
    crear_Matriz_S2(lienzo, matriz2)
    crear_Matriz_C(lienzo, matriz3)
    
    # Crea el objeto representativo de la grúa.
    X_Actual = tam_Bases
    Y_Actual = tam_Bases
    X_Final = X_Actual + tam_Celdas
    Y_Final = Y_Actual + tam_Celdas
    grua = lienzo.create_oval(X_Actual, Y_Actual, X_Final, Y_Final, width=1, fill="orange")

    Mensaje = tk.Label(ventana, text="En espera", font=("Arial", 16))
    Mensaje.pack(side="bottom")

    boton_Volver = tk.Button(ventana, text="Volver a pantalla principal", command=volver_Inicio)
    boton_Volver.pack(side="top")

    if (Modo_Seleccionado == 1):
        boton_Iniciar = tk.Button(ventana, text="Iniciar Acomodo", command=acomodo_Cajas_1)
        boton_Iniciar.pack(side="top")

    """if (Modo_Seleccionado == 2):
        boton_Iniciar = tk.Button(ventana, text="Iniciar Acomodo", command=acomodo_Cajas_2)
        boton_Iniciar.pack(side="top")"""

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

def acomodo_Cajas_1():
    global boton_Iniciar
    global Mensaje

    global lista_Suministro1
    global lista_Suministro1

    boton_Iniciar.destroy()

    tiempo = 2
    #for pos_Carga_I, elem_Carga_I in enumerate(letras_Carga_Inicial):
    for pos_Sum1, elem_Sum1 in enumerate(lista_Suministro1):
        for pos_Carga, elem_Carga in enumerate(lista_Carga):
            if (elem_Sum1.color == elem_Carga.color) and (elem_Carga.colocada == False):
                X_Destino = elem_Sum1.posx
                Y_Destino = elem_Sum1.posy

                # Ejecuta el movimiento, primero en X y luego en Y.
                # Primero se mueve hacia la caja que debe recoger.
                Mensaje.config(text="Moviendo Grua hacia la caja por recoger.")
                motor = 0 # Este es el número para activar el motor que mueve en X
                mover_Motor_X(motor, X_Actual, X_Destino)
                mover_X_Interfaz(X_Destino)
                #time.sleep(tiempo)

                mover_Y_Interfaz(Y_Destino)
                time.sleep(tiempo)
                Mensaje.config(text="Recogiendo caja.")
                ventana.update()

                actualizar_Suministro1(X_Destino, Y_Destino)
                time.sleep(tiempo)
                ventana.update()

                X_Destino = elem_Carga.posx
                Y_Destino = elem_Carga.posy
                
                # Ahora se mueve hacia el espacio donde debe dejar la caja.
                Mensaje.config(text="Moviendo Grua hacia el espacio designado.")

                motor = 0 # Este es el número para activar el motor que mueve en X
                mover_Motor_X(motor, X_Actual, X_Destino)
                mover_X_Interfaz(X_Destino)
                #time.sleep(tiempo)

                mover_Y_Interfaz(Y_Destino)
                time.sleep(tiempo)
                Mensaje.config(text="Dejando caja.")
                ventana.update()

                actualizar_Carga(elem_Carga.color, X_Destino, Y_Destino)
                time.sleep(tiempo)
                ventana.update()
                letras_Carga[pos_Carga] = 0

                lista_Suministro1[pos_Sum1].color = ""
                lista_Suministro1[pos_Sum1].ocupada = False
                lista_Carga[pos_Carga].colocada = True

                break

    # Se mueve a la posición inicial.
    Mensaje.config(text="Volviendo a la posición inicial.")
    X_Destino = tam_Bases
    Y_Destino = tam_Bases

    motor = 0 # Este es el número para activar el motor que mueve en X
    mover_Motor_X(motor, X_Actual, X_Destino)
    mover_X_Interfaz(X_Destino)
    #time.sleep(tiempo)

    mover_Y_Interfaz(Y_Destino)
    time.sleep(tiempo)
    Mensaje.config(text="Ha finalizado el acomodo.")
    ventana.update()

# Mover la grúa horizontalmente.
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

# Mover la grúa verticalmente.
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
    return

def actualizar_Suministro1(X_Destino, Y_Destino):
    global lienzo
    global grua
    # Actualiza la matriz de la zona de Suministro 1.
    lienzo.create_rectangle(X_Destino, Y_Destino, X_Destino + 40, Y_Destino + 40, fill="white")
    
    grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill="orange")
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

    # Actualiza la matriz de la zona de Carga.
    lienzo.create_rectangle(X_Destino, Y_Destino, X_Destino + 40, Y_Destino + 40, width=3, fill=color)

    grua = lienzo.create_oval(X_Actual, Y_Actual, X_Actual + 40, Y_Actual + 40, width=1, fill="orange")

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

    global microProces

    lienzo.destroy()
    boton_Volver.destroy()
    boton_Iniciar.destroy()
    Mensaje.destroy()

    microProces.close()

    lista_Carga = []
    lista_Suministro1 = []
    lista_Suministro2 = []

    Modo_Seleccionado = 0

    X_Actual = 0
    Y_Actual = 0

    boton_Cargar = tk.Button(ventana, text="Cargar Archivo CSV", command=abrir_Excel)
    boton_Cargar.pack(side="top")

def mover_Motor_X(motor, X_Actual, X_Destino):
    global microProces

    pasos = X_Destino - X_Actual

    #Se envían los pasos que debe dar el motor y el motor a utilizar
    microProces.write(str(pasos).encode())

    time.sleep(2)


#########################################################################################################
# Main.
if __name__ == "__main__":
    ventana = tk.Tk()
    app = Interfaz(ventana)
    ventana.mainloop()
