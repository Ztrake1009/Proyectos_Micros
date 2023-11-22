import tkinter as tk
from tkinter import filedialog
import openpyxl

class Grua:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Grúa Pórtico")
        self.ventana.geometry("1000x800")

        self.boton_cargar = tk.Button(ventana, text="Cargar Archivo Excel", command=self.abrir_Excel)
        self.boton_cargar.pack(side="top")

        self.letras = []
        self.matriz_A_Colores = None
        self.matrices_Frame = None
        self.boton_volver = None

    def abrir_Excel(self):
        archivo_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
        if archivo_path:
            libro = openpyxl.load_workbook(archivo_path)
            hoja = libro.active
            self.letras = [cell.value for row in hoja.iter_rows() for cell in row]
            libro.close()
            self.Matrices()
        #print (letras)

    def Matrices(self):
        self.boton_cargar.destroy()

        self.boton_volver = tk.Button(ventana, text="Volver a pantalla principal", command=self.volver_inicio)
        self.boton_volver.pack(side="top")

        self.matriz_A_Colores = []

        tam_Matriz1 = 2  # Tamaño de la zona de suministro 1.

        tamX_Matriz2 = 6  # Cantidad columnas de la zona de suministro 2.
        tamY_Matriz2 = 2  # Cantidad filas de la zona de suministro 2.

        tamX_Matriz3 = 2  # Cantidad columnas de la zona de suministro 3.
        tamY_Matriz3 = 6  # Cantidad filas de la zona de suministro 3.

        tam_Matriz4 = 5  # Tamaño de la zona de carga.

        self.matriz1 = [[None for _ in range(tam_Matriz1)] for _ in range(tam_Matriz1)]  # Cantidad en X, Cantidad en Y.
        self.matriz2 = [[None for _ in range(tamX_Matriz2)] for _ in range(tamY_Matriz2)]
        self.matriz3 = [[None for _ in range(tamX_Matriz3)] for _ in range(tamY_Matriz3)]
        self.matriz4 = [[None for _ in range(tam_Matriz4)] for _ in range(tam_Matriz4)]


        #self.matrices_Frame = tk.Frame(ventana)
        #self.matrices_Frame.place(x=0, y=0)

        tam_Celdas_Suministro = 35
        tam_Celdas_Carga = 40

        #tam_MatrizA = 5  # Tamaño de la zona de carga.

        ancho = 300
        alto = 300
        self.lienzo = tk.Canvas(ventana, width=ancho, height=alto, background="black")
        self.lienzo.place(x=1000-ancho, y=800-alto)

        tam_MatrizA = 5  # Tamaño de la zona de carga.

        tam_celda = 60
        fila = 0
        columna = 0

        letra_actual = 0

        while letra_actual < len(self.letras):
            if self.letras[letra_actual] == "R":  # Rojo Claro.
                color = "#FFAAAA"

            elif self.letras[letra_actual] == "G":  # Verde Claro.
                color = "#AAFFAA"

            elif self.letras[letra_actual] == "B":  # Azul Claro.
                color = "#AAAAFF"
            
            else:
                color = "white"

            self.lienzo.create_rectangle(columna * tam_celda, fila * tam_celda, (columna + 1) * tam_celda, (fila + 1) * tam_celda, fill=color)
            columna += 1
            letra_actual += 1
            if columna == tam_MatrizA:
                columna = 0
                fila += 1
        
        letra_actual = 0

    def volver_inicio(self):
        self.lienzo.destroy()
        self.boton_volver.destroy()

        self.boton_cargar = tk.Button(ventana, text="Cargar Archivo Excel", command=self.abrir_Excel)
        self.boton_cargar.pack(side="top")

        self.matriz_A_Colores = None

    def ident_Color(self, color):
        if color == "R":
            return "#FFAAAA"
        elif color == "G":
            return "#AAFFAA"
        elif color == "B":
            return "#AAAAFF"
        else:
            return "white"

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Grua(ventana)
    ventana.mainloop()