import tkinter as tk

# Definir la lista de letras que determinan los colores
letras = ['R', 'B', 'G', 'R', 'B',
          'G', 'R', 'B', 'G', 'R',
          'B', 'G', 'R', 'B', 'G',
          'R', 'B', 'G', 'R', 'B',
          'G', 'R', 'B', 'G', 'R']

# Función para asignar colores según las letras
def asignar_color(letra):
    if letra == 'R':
        return 'red'
    elif letra == 'B':
        return 'blue'
    elif letra == 'G':
        return 'green'

# Crear la ventana y el lienzo
ventana = tk.Tk()
ventana.title("Matriz de Colores")

lienzo = tk.Canvas(ventana, width=300, height=300)
lienzo.pack()

# Crear la matriz de celdas coloreadas
tam_celda = 60
fila = 0
columna = 0

for letra in letras:
    color = asignar_color(letra)
    lienzo.create_rectangle(columna * tam_celda, fila * tam_celda, (columna + 1) * tam_celda, (fila + 1) * tam_celda, fill=color)
    columna += 1
    if columna == 5:
        columna = 0
        fila += 1

# Iniciar la interfaz gráfica
ventana.mainloop()
