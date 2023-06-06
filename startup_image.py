from PIL import Image, ImageTk
import tkinter
import tkinter as tk
from tkinter import PhotoImage, Canvas, YES

root = tk.Tk()
root.title("HC3N")
root.geometry("990x500")
root.iconbitmap("images\\logoHCi3N.ico")
root.config(background="lightblue")


width = 300
height = 300
image = PhotoImage(file='images\\zero.png')
canvas = Canvas(root, width=width, height=height)
canvas.create_image(width=width/2, height=height/2, image=image)

canvas.pack(expand=YES)

root.mainloop()
