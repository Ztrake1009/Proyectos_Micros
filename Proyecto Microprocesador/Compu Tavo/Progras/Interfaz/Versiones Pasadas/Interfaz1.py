import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Matriz 5x5")

frame1 = tk.Frame(ventana)
frame1.pack(padx=00, pady=00)
#frame_1.place(x=00, y=00)
frame2 = tk.Frame(ventana)
frame2.pack(padx=00, pady=00)
#frame_2.place(x=00, y=00)

ventana.geometry("800x600")
#frame2.grid_columnconfigure(0, minsize=100)


#tam_Matriz1 = 7 # Tamaño de la zona de suministro.
#tam_Matriz2 = 5 # Tamaño de la zona de carga.

matriz1 = [[None for _ in range(6)] for _ in range(5)] # Cantidad en X, Cantidad en Y.
#matriz2 = [[None for _ in range(tam_Matriz2)] for _ in range(tam_Matriz2)]


"""
background="#FF0000" (Rojo)
background="#FFAAAA" (Rojo claro)
background="#00FF00" (Verde)
background="#AAFFAA" (Verde claro)
background="#0000FF" (Azul)
background="#AAAAFF" (Azul claro)

background="#B2B2B2" (Gris)
"""
for i in range(5): # Cantidad en Y.
    for j in range(6): # Cantidad en X.
        matriz1[i][j] = tk.Canvas(frame1, width=35, height=35, background="#AAFFAA", highlightbackground="red", borderwidth=2, relief="solid")
        matriz1[i][j].grid(row=i, column=j, padx=5, pady=5)

#for i in range(tam_Matriz2):
#    for j in range(tam_Matriz2):
#        matriz2[i][j] = tk.Canvas(frame2, width=40, height=40, background="#FFAAAA", highlightbackground="red", borderwidth=2, relief="solid")
#        matriz2[i][j].grid(row=i, column=j, padx=5, pady=5)



ventana.mainloop()
