import tkinter as tk
from tkinter import messagebox

class Matrices:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Grúa Pórtico")
        self.ventana.geometry("800x600")

        #self.main_frame = tk.Frame(ventana)
        #self.main_frame.pack()

        self.letras = ['R', 'B', 'G', 'R', 'G',
                       'G', 'G', 'R', 'B', 'G',
                       'G', 'B', 'R', 'B', 'G',
                       'R', 'B', 'G', 'G', 'R',
                       'B', 'R', 'R', 'B', 'B']

        self.letra_actual = 0

        self.matrix_frame_1 = tk.Frame(self.ventana)
        self.matrix_frame_2 = tk.Frame(self.ventana)
        self.matrix_frame_3 = tk.Frame(self.ventana)
        self.matrix_frame_4 = tk.Frame(self.ventana)
        #self.matrix_frame_1.place(x=82, y=138)

        self.matrix_frame_1.grid(row=0, column=0)
        self.matrix_frame_2.grid(row=0, column=1)
        self.matrix_frame_3.grid(row=1, column=0)
        self.matrix_frame_4.grid(row=1, column=1)

        self.tam_Matriz1 = 2  # Tamaño de la zona de suministro 1.

        self.tamX_Matriz2 = 6  # Cantidad columnas de la zona de suministro 2.
        self.tamY_Matriz2 = 2  # Cantidad filas de la zona de suministro 2.

        self.tamX_Matriz3 = 2  # Cantidad columnas de la zona de suministro 3.
        self.tamY_Matriz3 = 6  # Cantidad filas de la zona de suministro 3.

        self.tam_Matriz4 = 5  # Tamaño de la zona de carga.

        self.matriz1 = [[None for _ in range(self.tam_Matriz1)] for _ in range(self.tam_Matriz1)]  # Cantidad en X, Cantidad en Y.
        self.matriz2 = [[None for _ in range(self.tamX_Matriz2)] for _ in range(self.tamY_Matriz2)]
        self.matriz3 = [[None for _ in range(self.tamX_Matriz3)] for _ in range(self.tamY_Matriz3)]
        self.matriz4 = [[None for _ in range(self.tam_Matriz4)] for _ in range(self.tam_Matriz4)]

        """
        background="#FF0000" (Rojo)
        background="#FFAAAA" (Rojo claro)
        background="#00FF00" (Verde)
        background="#AAFFAA" (Verde claro)
        background="#0000FF" (Azul)
        background="#AAAAFF" (Azul claro)

        background="#B2B2B2" (Gris)
        """

        for i in range(self.tam_Matriz1):
            for j in range(self.tam_Matriz1):
                self.matriz1[i][j] = tk.Canvas(self.matrix_frame_1, width=35, height=35, background="#B2B2B2", borderwidth=2, relief="solid")
                self.matriz1[i][j].grid(row=i, column=j, padx=5, pady=5)

        for i in range(self.tamY_Matriz2):  # Cantidad en Y.
            for j in range(self.tamX_Matriz2):  # Cantidad en X.
                self.matriz2[i][j] = tk.Canvas(self.matrix_frame_2, width=35, height=35, background="#B2B2B2", borderwidth=2, relief="solid")
                self.matriz2[i][j].grid(row=i, column=j, padx=5, pady=5)

        for i in range(self.tamY_Matriz3):  # Cantidad en Y.
            for j in range(self.tamX_Matriz3):  # Cantidad en X.
                self.matriz3[i][j] = tk.Canvas(self.matrix_frame_3, width=35, height=35, background="#B2B2B2", borderwidth=2, relief="solid")
                self.matriz3[i][j].grid(row=i, column=j, padx=5, pady=5)

        for i in range(self.tam_Matriz4):
            for j in range(self.tam_Matriz4):
                self.matriz4[i][j] = tk.Canvas(self.matrix_frame_4, width=40, height=40, background="white", borderwidth=2, relief="solid")
                self.matriz4[i][j].grid(row=i, column=j, padx=5, pady=5)

                if self.letra_actual < len(self.letras):
                    self.matriz4[i][j].create_text(23, 23, text=self.letras[self.letra_actual], font=("Helvetica", 12))
                    self.letra_actual += 1

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Matrices(ventana)
    ventana.mainloop()