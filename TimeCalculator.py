import datetime
import tkinter as tk
import webbrowser
from tkinter import Menu, ttk, messagebox, X, Y, RIGHT, BOTTOM, NO, filedialog
import os
import shutil


class TimeCalculatorGUI:
    """
    Design of : Buttons, Entry, Label, main window
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HCi3N Job Time Calculator")
        self.root.geometry("1000x600")
        self.root.iconbitmap('images\\logoHCi3N.ico')
        # self.root.config(background="#40826d", width=12, relief='flat', highlightthickness=0)

        self.input_frame0 = ttk.Frame(self.root)
        self.input_frame0.pack()

        self.start_labelnom = ttk.Label(self.input_frame0, text="Entrer Nom & Prenom:", underline=0)
        self.start_labelnom.grid(row=0, column=0, padx=5, pady=5)

        self.start_labelnom_entry = ttk.Entry(self.input_frame0)
        self.start_labelnom_entry.grid(row=0, column=1, padx=5, pady=5)

        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack()

        self.start_label = ttk.Label(self.input_frame, text="Heure de Debut (HH:MM:SS AM/PM):", underline=0, foreground="green")
        self.start_label.grid(row=0, column=0, padx=5, pady=5)

        self.start_entry = ttk.Entry(self.input_frame)
        self.start_entry.grid(row=0, column=1, padx=5, pady=5)

        self.end_label = ttk.Label(self.input_frame, text="Heure de Fin (HH:MM:SS AM/PM):", underline=0,
                                   foreground='red')
        self.end_label.grid(row=1, column=0, padx=5, pady=5)

        self.end_entry = ttk.Entry(self.input_frame)
        self.end_entry.grid(row=1, column=1, padx=5, pady=5)

        self.break_checkbutton_var = tk.BooleanVar(value=True)
        self.break_checkbutton = ttk.Checkbutton(self.input_frame, text="Pause entre 13:00 PM et 15:00 PM",
                                                 variable=self.break_checkbutton_var)
        self.break_checkbutton.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.calculate_button = ttk.Button(self.root, text="Calculer", command=self.calculate)
        self.calculate_button.pack(padx=5, pady=5)

        self.result_label = ttk.Label(self.root)
        self.result_label.pack(padx=5, pady=5, expand=False, side='bottom')

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

        # Exit function
        def exit_01():
            if messagebox.askokcancel(title='Quitter', message='Voulez-vous quitter ?'):
                self.root.destroy()

        # add a web link to http://www.initiative3n.ne/ to display by clicking on the on_click function
        def on_click():
            url = "http://www.initiative3n.ne/"
            webbrowser.open_new_tab(url)

        # function to open folder
        def open_folder():
            folder_to_open = filedialog.askdirectory(title='Select Folder to open')
            os.startfile(folder_to_open)

        # function to open a file
        def open_file():
            # selecting the file using the askopenfilename() method of filedialog
            file_to_open = filedialog.askopenfilename(title='Select file', filetypes=[("All files", "*.*"), ("Excel file", "*.xlsx")])
            os.startfile(os.path.abspath(file_to_open))

        # delete file function
        def delete_file():
            file_to_delete = filedialog.askopenfilename(title="Select file to delete", filetypes=[("All files", "*.*")])
            os.remove(os.path.abspath(file_to_delete))
            # display success message
            messagebox.showinfo(title="File deleted !", message="The file has been deleted successfully")

        # Fichier Menu configuration.
        menubar = tk.Menu(self.root)
        menu01 = Menu(menubar, tearoff=0)
        menu01.add_command(label='Nouveau', compound='right', command=open_folder, underline=0)
        menu01.add_command(label='Ouvrir', compound='right', command=open_file, underline=0, accelerator='Ctrl+O')
        menu01.add_command(label='Enregistrer', compound='right', command='', underline=0, accelerator='Ctrl+S')
        menu01.add_command(label='Enregistrer Sous', compound='right', command=on_click)
        menu01.add_separator(background='')
        menu01.add_command(label='A propos HCi3N', hidemargin=True, compound='left', command='', underline=0)
        menu01.add_separator()
        menu01.add_command(label='Quitter', command=exit_01, compound='left', accelerator='Alt+F4', underline=1)

        # Modifier MEnu configuration
        menu02 = Menu(menu01, tearoff=0)
        menu02.add_command(label='Annuler', compound='right', command='', underline=0, accelerator=' Alt+Z')
        menu02.add_separator()
        menu02.add_command(label='Copier', compound='right', command='', underline=0, accelerator='Ctrl+C')
        menu02.add_command(label='Couper', compound='right', command='', underline=0, accelerator='Ctrl+X')
        menu02.add_command(label='Coller', compound='right', command='', underline=0, accelerator='Ctrl+V')
        menu02.add_command(label='Supprimer', compound='right', command=delete_file, underline=0, accelerator=' Supp')

        # Create Menu Bar
        menubar.add_cascade(label='Fichier', menu=menu01)
        menubar.add_cascade(label='Modifier', menu=menu02)
        self.root.config(menu=menubar)

    def calculate(self):
        start_time_str = self.start_entry.get()
        end_time_str = self.end_entry.get()
        name_str = self.start_labelnom_entry.get()

        start_time = datetime.datetime.strptime(start_time_str, "%I:%M:%S %p").time()
        end_time = datetime.datetime.strptime(end_time_str, "%I:%M:%S %p").time()

        # total_time = datetime.timedelta()

        if end_time < start_time:
            end_time += datetime.timedelta(days=1)

        if self.break_checkbutton_var.get():
            break_start_time = datetime.time(hour=13)
            break_end_time = datetime.time(hour=15)

            if start_time < break_start_time and end_time >= break_end_time:
                total_time = datetime.timedelta(hours=8, minutes=30) - datetime.timedelta(hours=2)
            elif start_time >= break_end_time:
                total_time = datetime.timedelta(hours=8, minutes=30)
            elif end_time <= break_start_time:
                total_time = datetime.timedelta(hours=8, minutes=30) - datetime.timedelta(hours=2)
            else:
                time_before_break = datetime.datetime.combine(datetime.date.today(),
                                                              break_start_time) - datetime.datetime.combine(
                    datetime.date.today(), start_time)
                time_after_break = datetime.datetime.combine(datetime.date.today(),
                                                             end_time) - datetime.datetime.combine(
                    datetime.date.today(), break_end_time)
                total_time = time_before_break + time_after_break - datetime.timedelta(hours=2)
        else:
            total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
                datetime.date.today(), start_time)

        total_time_str = str(total_time)
        self.result_label.config(text=f"Le Temps de travail de : '{f'{name_str}'}' est de: '{total_time_str}'", background='lightgreen', underline=0)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = TimeCalculatorGUI()
    gui.run()
