import tkinter as tk
from tkinter import PhotoImage, Canvas, BOTH


def mainwindow():

    root = tk.Tk()
    root.title("HC3N")
    root.geometry("980x250+110+100")
    root.iconbitmap("images\\logoHCi3N.ico")
    root.config(background="lightblue")
    root.resizable(height=False, width=False)
    root.wait_visibility(window=root)
    root.overrideredirect(False)

    width = 400
    height = 400

    image_1 = PhotoImage(file='hci3n.png')
    canvas_1 = Canvas(root, width=width, height=height)
    canvas_1.create_image(0, 0, image=image_1, anchor='nw')
    canvas_1.pack(expand=True, fill=BOTH, side='top')
    # root.after(5000)

    root.mainloop()


mainwindow()
