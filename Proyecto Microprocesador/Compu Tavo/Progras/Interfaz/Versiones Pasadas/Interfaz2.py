import tkinter as tk
from tkinter import messagebox

class MatrixGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Grúa Pórtico")

        self.main_frame = tk.Frame(ventana)
        self.main_frame.pack()

        self.matrix_frame_1 = tk.Frame(self.main_frame, borderwidth=2, relief="solid")
        self.matrix_frame_2 = tk.Frame(self.main_frame, borderwidth=2, relief="solid")
        self.matrix_frame_3 = tk.Frame(self.main_frame, borderwidth=2, relief="solid")
        self.matrix_frame_4 = tk.Frame(self.main_frame, borderwidth=2, relief="solid")

        self.matrix_frame_1.grid(row=0, column=0)
        self.matrix_frame_2.grid(row=0, column=1)
        self.matrix_frame_3.grid(row=1, column=0)
        self.matrix_frame_4.grid(row=1, column=1)

        self.create_matrices()

    def create_matrices(self):
        matrix_1_cells = [1, 2, 3, 4]
        matrix_2_cells = [2, 3, 4, 5, 6, 4, 5, 6, 2, 9]
        matrix_3_cells = [15, 16, 22, 23, 29, 30, 36, 37, 43, 44]
        matrix_4_cells = [1, 2, 3, 4, 5, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 38, 39, 40, 41, 42, 45, 46, 47, 48, 49]

        self.fill_matrix(self.matrix_frame_1, matrix_1_cells)
        self.fill_matrix(self.matrix_frame_2, matrix_2_cells)
        self.fill_matrix(self.matrix_frame_3, matrix_3_cells)
        self.fill_matrix(self.matrix_frame_4, matrix_4_cells)

    def fill_matrix(self, frame, cell_list):
        for i in cell_list:
            row = (i - 1) // 7
            col = (i - 1) % 7
            cell = tk.Label(frame, text=i, width=5, height=2, borderwidth=1, relief="solid")
            cell.grid(row=row, column=col)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = MatrixGUI(ventana)
    ventana.mainloop()