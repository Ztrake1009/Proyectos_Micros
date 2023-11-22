import tkinter as tk
from tkinter import filedialog
import openpyxl

def leer_archivo_excel():
    archivo_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    if archivo_path:
        libro = openpyxl.load_workbook(archivo_path)
        hoja = libro.active

        letras = []
        for fila in hoja.iter_rows(min_row=1, max_row=5, min_col=1, max_col=5):
            for celda in fila:
                letras.append(celda.value)

        libro.close()

        lista_letras.config(text="Lista de letras: " + ", ".join(str(letra) for letra in letras))

# Configuración de la interfaz
ventana = tk.Tk()
ventana.title("Lector de Archivo Excel")

boton_cargar = tk.Button(ventana, text="Cargar Archivo Excel", command=leer_archivo_excel)
boton_cargar.pack(pady=20)

lista_letras = tk.Label(ventana, text="Lista de letras:")
lista_letras.pack()

ventana.mainloop()
