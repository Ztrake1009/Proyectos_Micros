import csv
import tkinter as tk
from tkinter import filedialog
import time
from Interfaz import *
class Caja:
    # La clase madre, caracteriza cada objeto como debe ir en la zona de carga
    # pos_x: Es la posición en x 
    # pos_y: Es la posición en y
    # color: Es el tipo de caja (Rojo, Verde, Azul)

    def __init__(self,posx,posy,color):
        self.posx = posx
        self.posy = posy
        self.color = color

class Carga(Caja):
    # La subclase de una caja en la zona de carga deseada

    def __init__(self,posx,posy,color,colocada):
        super().__init__(posx,posy,color)
        self.colocada = colocada  # Indica si ya se colocó en la carga

class Suministro(Caja):
     # La clase de una caja en la zona de suministro

    def __init__(self,posx,posy,color,clear):
        super().__init__(posx,posy,color)
        self.clear = clear  # Indica si ya se colocó en la carga

class Motor:
    # Clase del motor 
    def __init__(self,eje,estado):
        self.eje = eje  # Movimiento que realiza (x, y o z)
        self.estado = estado  # Si está en movimiento o no

class Garra:
    # Clase de la garra
    def __init__(self,agarra, posz):
        self.agarra = agarra # Si está agarrando (1) o no (0)
        self.posz = posz  # Si está arriba (0) o abajo (1)


# Clase a motor
