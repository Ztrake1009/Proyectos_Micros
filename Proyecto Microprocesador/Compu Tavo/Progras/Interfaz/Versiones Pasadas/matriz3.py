#matriz3

import tkinter as tk

class ColorMatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Matrix")

        self.colors = ["red", "green", "blue"]
        self.matrix = [["red" for _ in range(5)] for _ in range(5)]

        self.square_buttons = []

        for row in range(5):
            row_buttons = []
            for col in range(5):
                color = self.matrix[row][col]
                button = tk.Button(root, width=10, height=3, bg=color,
                                   command=lambda r=row, c=col: self.change_color(r, c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.square_buttons.append(row_buttons)

    def change_color(self, row, col):
        current_color_index = self.colors.index(self.matrix[row][col])
        new_color_index = (current_color_index + 1) % len(self.colors)
        new_color = self.colors[new_color_index]
        self.matrix[row][col] = new_color
        self.square_buttons[row][col].config(bg=new_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorMatrixApp(root)
    root.mainloop()

