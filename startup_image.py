import tkinter as tk
from tkinter import BOTH


def mainwindow():
    """
    :return: Display startup image
    """
    root = tk.Tk()
    root.title("HC3N")
    root.geometry("980x250")
    root.iconbitmap("images\\logoHCi3N.ico")
    root.config(background="lightblue")
    root.resizable(height=False, width=False)
    root.wait_visibility(window=root)
    root.overrideredirect(False)
    root.wm_state(newstate='normal')

    width = 400
    height = 400

    canvas_1 = tk.Canvas(root, width=width, height=height)
    canvas_1.pack(expand=True, fill=BOTH)
    canvas_1.image_1 = tk.PhotoImage(file='images\\hci3n.png')
    canvas_1.create_image(0, 0, image=canvas_1.image_1, anchor='nw')
    # root.after(5000, mainwindow)
    root.mainloop()

mainwindow()
