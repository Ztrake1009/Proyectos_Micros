# Librerías
import tkinter as tk
from tkinter import filedialog
import csv
import time
from Clases import *




def abrir_Excel(list_posx,list_posy):
        """
        Función: Abrir los archivos de excel en formato cvs
        Entrada: Lista de las posiciones de X y Y
        Salida: Lista con las cajas de carga
        """

        lista = []
        archivo_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        i=0
        j=0

        if archivo_path:
            with open(archivo_path, 'r', newline='') as file:
                lector_csv = csv.reader(file, delimiter=';')
                for fila in lector_csv:
                    for elemento in fila:
                        posx = list_posx[i]
                        posy = list_posy[i]

                        a = Carga(posx, posy,elemento)
                        lista.append(a)
                        i+=1


        letra = 0
        contador_R = 0
        contador_G = 0
        contador_B = 0

        while letra < len(lista):
            if lista[letra].color == "R":  # Caja Roja.
                contador_R += 1

            elif lista[letra].color == "G":  # Caja Verde.
                contador_G += 1

            elif lista[letra].color == "B":  # Caja Azul.
                contador_B += 1
            letra += 1
        print(contador_R)
        print(contador_G)
        print(contador_B)

        return lista


posx = [0,1,2,3,4,
        0,1,2,3,4,
        0,1,2,3,4,
        0,1,2,3,4,
        0,1,2,3,4]
posy = [0,0,0,0,0,
        1,1,1,1,1,
        2,2,2,2,2,
        3,3,3,3,3,
        4,4,4,4,4,]
lista_carga = abrir_Excel(posx,posy)
i=0
print("Objetos de carga")
print("N°","    ","Color","    ","Pos X","    ","Pos Y")
while i <(len(lista_carga)):
     print(i,"    ",lista_carga[i].color,"    ",lista_carga[i].pos_x,"    ",lista_carga[i].pos_y)
     i+=1 