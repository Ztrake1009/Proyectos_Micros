import csv
import tkinter as tk
from tkinter import filedialog
import time

class Caja:
    # La clase madre, caracteriza cada objeto como debe ir en la zona de carga.
    # color: Es el tipo de caja (Rojo, Verde, Azul).
    def __init__(self,color):
        self.color = color

class Carga(Caja):
    # La subclase de una caja en la zona de carga deseada.
    # pos_x: Es la posición en x.
    # pos_y: Es la posición en y.
    def __init__(self,posx,posy,color,colocada):
        self.posx = posx
        self.posy = posy
        super().__init__(color)
        self.colocada = colocada  # Indica si tiene una caja.

class Suministro(Caja):
    # La subclase de una caja en la zona de suministro.
    # pos_x: Es la posición en x.
    # pos_y: Es la posición en y.
    def __init__(self,posx,posy,color,ocupada):
        self.posx = posx
        self.posy = posy
        super().__init__(color)
        self.ocupada = ocupada  # Indica si tiene una caja.

class Motor:
    # Clase del motor.
    def __init__(self,eje,estado):
        self.eje = eje  # Movimiento que realiza (x, y o z).
        self.estado = estado  # Si está en movimiento o no.

class Garra:
    # Clase de la garra.
    def __init__(self,agarra,posz):
        self.agarra = agarra # Si está agarrando (1) o no (0).
        self.posz = posz  # Si está arriba (0) o abajo (1).
        


# Clase a motor
