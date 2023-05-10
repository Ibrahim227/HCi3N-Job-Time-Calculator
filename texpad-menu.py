'''from tkinter import *
import tkinter as tk


# Create Texpad
texpad = tk.Text(self.root)
scroll = tk.Scrollbar(texpad)
texpad.configure(yscrollcommand=scroll.set)
scroll.config(command=texpad.xview)
scroll.pack(side=RIGHT, fill=Y)
texpad.pack(fill=X, ipadx=250, ipady=100, padx=10, side=BOTTOM, pady=15)

# Create Information Bar
inforbar = ttk.Label(texpad, text='Line: 1 | Column: 0')
inforbar.pack(expand=NO, anchor='s', side=RIGHT)
curline, curcolumn = texpad.index("insert").split('.')
inforbar.config(text='Line: %s | Column: %s' % (curline, curcolumn))


# function to open folder
def open_folder():
    folder_to_open = filedialog.askdirectory(title='Select Folder to open')
    os.startfile(folder_to_open)


# function to open a file
def open_file():
    # selecting the file using the askopenfilename() method of filedialog
    file_to_open = filedialog.askopenfilename(title='Select file',
                                              filetypes=[("All files", "*.*"), ("Excel file", "*.xlsx")])
    os.startfile(os.path.abspath(file_to_open))


# delete file function
def delete_file():
    file_to_delete = filedialog.askopenfilename(title="Select file to delete", filetypes=[("All files", "*.*")])
    os.remove(os.path.abspath(file_to_delete))
    # display success message
    messagebox.showinfo(title="File deleted !", message="The file has been deleted successfully")


   # Modifier MEnu configuration
        menu02 = Menu(menu01, tearoff=0)
        menu02.add_command(label='Annuler', compound='right', command='', underline=0, accelerator=' Alt+Z')
        menu02.add_separator()
        menu02.add_command(label='Copier', compound='right', command='', underline=0, accelerator='Ctrl+C')
        menu02.add_command(label='Couper', compound='right', command='', underline=0, accelerator='Ctrl+X')
        menu02.add_command(label='Coller', compound='right', command='', underline=0, accelerator='Ctrl+V')
        menu02.add_command(label='Supprimer', compound='right', command=delete_file, underline=0, accelerator=' Supp')


menu01.add_command(label='Nouveau', compound='right', command=open_folder, underline=0)
menu01.add_command(label='Ouvrir', compound='right', command=open_file, underline=0, accelerator='Ctrl+O')
menu01.add_command(label='Enregistrer', compound='right', command='', underline=0, accelerator='Ctrl+S')
menu01.add_command(label='Enregistrer Sous', compound='right', command=on_click)'''