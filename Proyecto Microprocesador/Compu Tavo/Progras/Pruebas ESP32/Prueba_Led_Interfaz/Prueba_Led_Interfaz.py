import serial
from tkinter import Tk, Button
import tkinter.font as font

try:
    arduino = serial.Serial("COM3", 9600)
except:
    print("No se puede conectar al puerto.")

def onClosing():
    root.destroy()
    arduino.close()

def pressButton1():
    arduino.write(("1\n").encode())

def pressButton2():
    arduino.write(("0\n").encode())

# Iniaciliza la ventana.
root = Tk()
root.protocol("WM_DELETE_WINDOW", onClosing) # Protocolo para cerrar la ventana al presionar la X de la ventana.
root.title("Serial LED Control") # Título de la ventana.
root.configure(bg = "#FFFFFF")

myFont = font.Font(size=20)

button1 = Button(root, text="Encender", command=pressButton1, bg="#35B94B", fg="#FFFFFF", height=2, width=20)
button1["font"] = myFont
button1.pack(padx=20,pady=10)

button2 = Button(root, text="Apagar", command=pressButton2, bg="#EC2424", fg="#FFFFFF", height=2, width=20)
button2["font"] = myFont
button2.pack(padx=20,pady=10)

root.mainloop()