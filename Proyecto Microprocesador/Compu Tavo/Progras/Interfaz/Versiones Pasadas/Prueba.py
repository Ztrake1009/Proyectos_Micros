import tkinter as tk

class CircleMoverApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        
        self.circle_radius = 20
        self.circle_x = self.circle_radius + 10
        self.circle_y = 200
        self.x_velocity = 3
        
        self.circle = self.canvas.create_oval(
            self.circle_x - self.circle_radius, self.circle_y - self.circle_radius,
            self.circle_x + self.circle_radius, self.circle_y + self.circle_radius,
            fill="blue"
        )
        
        self.move_circle()
    
    def move_circle(self):
        
        self.canvas.move(self.circle, self.x_velocity, 0)
        self.circle_x += self.x_velocity
        
        if self.circle_x + self.circle_radius >= self.canvas.winfo_width() or self.circle_x - self.circle_radius <= 0:
            self.x_velocity = -self.x_velocity
        
        self.root.after(20, self.move_circle)

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleMoverApp(root)
    root.mainloop()
