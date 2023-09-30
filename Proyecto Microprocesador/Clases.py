import csv
import tkinter as tk
from tkinter import filedialog
import time
from Interfaz import *
class Carga:
    # La clase Carga se trata de poder caracterizar los espacios en la matriz de carga
    # pos_x: Es la posición en x 
    # pos_y: Es la posición en y
    # color: Es el tipo de caja (Rojo, Verde, Azul)
    # colocada: Indica si ya está la c

    def __init__(self,pos_x,pos_y,color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.colocada = False

    def colocar(self):
        self.colocada = True

    def get_color(self):
         return self.color
    
# Selecciona el archivo de excel para saber que cajas deben ir en la matriz de carga.    
def abrir_Excel(letras_Carga=list):
    archivo_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    
    if archivo_path:
        with open(archivo_path, 'r', newline='') as file:
            lector_csv = csv.reader(file, delimiter=';')
            for fila in lector_csv:
                for elemento in fila:
                    i = Carga(pos_x,pos_y,elemento)
                    pos_x=0
                    pos_y=0
                    letras_Carga.append(elemento)
        ventana.Sel_Modo()

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


""" def abrir_Excel():
        lista_carga=[]
        #i=1
        pos_x=1
        pos_y=1
        with open('Carga.csv', newline='') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            for fila in lector_csv:
                for elemento in fila:
                    i = Carga(pos_x,pos_y,elemento)
                    lista_carga.append(i)
                    pos_x=pos_x+1
                    pos_y+=1
                

        return lista_carga
 """



""" 
# Prueba
i=0
lista_carga=abrir_Excel()
#print(len(lista_carga))
print("Objetos de carga")
while i <(len(lista_carga)):
     print(lista_carga[i].color,lista_carga[i].pos_x,lista_carga[i].pos_y)
     i+=1 """