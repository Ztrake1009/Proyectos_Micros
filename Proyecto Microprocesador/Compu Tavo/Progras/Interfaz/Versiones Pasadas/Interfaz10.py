import tkinter as tk
import time

class MatrixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Circle Matrices")

        self.matrix_1 = [[None for _ in range(5)] for _ in range(5)]
        self.matrix_2 = [[None for _ in range(2)] for _ in range(7)]
        self.current_row_1 = 0
        self.current_col_1 = 0
        self.current_row_2 = 0

        self.canvas = tk.Canvas(self.root, width=700, height=700)
        self.canvas.pack()

        self.create_matrix_1()
        self.create_matrix_2()

        self.circle = self.canvas.create_oval(10, 10, 40, 40, fill="black")
        self.move_circle()

    def move_circle(self):
        if self.current_row_2 < 7:
            cell_x, cell_y = 100 * self.current_col_1, 100 * self.current_row_1
            self.canvas.coords(self.circle, cell_x + 10, cell_y + 10, cell_x + 40, cell_y + 40)
            self.root.update()

            time.sleep(1)

            cell_1 = self.matrix_1[self.current_row_1][self.current_col_1]
            self.canvas.itemconfig(cell_1, fill="red")
            self.root.update()

            time.sleep(1)

            self.canvas.itemconfig(cell_1, fill="white")
            self.current_col_1 += 1

            if self.current_col_1 >= 5:
                self.current_col_1 = 0
                self.current_row_1 += 1

            if self.current_row_1 >= 5:
                self.current_row_1 = 0
                self.current_row_2 += 1

            if self.current_row_2 < 7:
                self.root.after(1000, self.move_circle)

    def create_matrix_1(self):
        for i in range(5):
            for j in range(5):
                x1, y1 = 100 * j, 100 * i
                x2, y2 = x1 + 100, y1 + 100
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                self.matrix_1[i][j] = cell

    def create_matrix_2(self):
        for i in range(7):
            for j in range(2):
                x1, y1 = 100 * j + 600, 100 * i
                x2, y2 = x1 + 100, y1 + 100
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                self.matrix_2[i][j] = cell

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixGUI(root)
    root.mainloop()
