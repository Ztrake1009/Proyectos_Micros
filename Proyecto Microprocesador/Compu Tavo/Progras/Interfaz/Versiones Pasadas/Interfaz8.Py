import tkinter as tk
import random
import time

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matriz Interactiva")

        self.cell_size = 60
        self.rows = 5
        self.cols = 5

        self.canvas = tk.Canvas(root, width=self.cell_size*self.cols, height=self.cell_size*self.rows)
        self.canvas.pack()

        self.matrix = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.matrix[row][col] = self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")

        self.circle_radius = 20
        self.current_row = 0
        self.current_col = 0
        self.circle = self.canvas.create_oval(
            self.current_col * self.cell_size + self.cell_size // 2 - self.circle_radius,
            self.current_row * self.cell_size + self.cell_size // 2 - self.circle_radius,
            self.current_col * self.cell_size + self.cell_size // 2 + self.circle_radius,
            self.current_row * self.cell_size + self.cell_size // 2 + self.circle_radius,
            fill="black"
        )

        self.canvas.bind("<space>", self.color_cell)

        self.move_circle_randomly()

    def move_circle_randomly(self):
        while True:
            next_row = random.randint(0, self.rows - 1)
            next_col = random.randint(0, self.cols - 1)

            if (next_row, next_col) != (self.current_row, self.current_col):
                self.current_row = next_row
                self.current_col = next_col
                self.move_circle()
                self.root.update()  # Update the GUI to see the circle's new position
                time.sleep(2)
                self.color_cell(None)
                self.root.update()  # Update the GUI to see the red cell
                time.sleep(0.5)

    def move_circle(self):
        x0 = self.current_col * self.cell_size + self.cell_size // 2 - self.circle_radius
        y0 = self.current_row * self.cell_size + self.cell_size // 2 - self.circle_radius
        x1 = self.current_col * self.cell_size + self.cell_size // 2 + self.circle_radius
        y1 = self.current_row * self.cell_size + self.cell_size // 2 + self.circle_radius
        self.canvas.coords(self.circle, x0, y0, x1, y1)

    def color_cell(self, event):
        cell = self.matrix[self.current_row][self.current_col]
        self.canvas.itemconfig(cell, fill="red")

root = tk.Tk()
app = MatrixApp(root)
root.mainloop()
