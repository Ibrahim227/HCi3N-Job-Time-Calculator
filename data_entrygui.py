from tkinter import ttk, messagebox
import tkinter as tk


class JobTimeCalculator(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("HCi3N")
        self.window.geometry()
        self.window.iconbitmap('images\\logoHCi3N.ico')

        self.frame = ttk.Frame(self.window)
        self.frame.pack()

        # Saving user Information
        self.user_info_frame = ttk.Labelframe(self.frame, text='Information Employee', underline=0)
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=20)

        self.first_name_label = ttk.Label(self.user_info_frame, text='Nom:', background="lightgrey", underline=0)
        self.first_name_label.grid(row=0, column=0)
        self.last_name_label = ttk.Label(self.user_info_frame, text='Prenom:', background="lightgrey", underline=0)
        self.last_name_label.grid(row=0, column=1)

        self.first_name_entry = ttk.Entry(self.user_info_frame)
        self.last_name_entry = ttk.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)

        self.title = ttk.Label(self.user_info_frame, text='Titre:', background="lightgrey", underline=0)
        self.title_combox = ttk.Combobox(self.user_info_frame, values=["", "Mme.", "M.", "Dr.", "Phd"])
        self.title.grid(row=0, column=2)
        self.title_combox.grid(row=1, column=2)

        self.time_start_label = ttk.Label(self.user_info_frame, text="Heure Arrivee (HH:MM:SS AM/PM):", background="lightgreen", underline=0)
        self.time_end_label = ttk.Label(self.user_info_frame, text="Heure De Fin (HH:MM:SS AM/PM):", background="red", underline=0)
        self.time_start_label.grid(row=2, column=0)
        self.time_end_label.grid(row=2, column=1)

        self.time_start_entry = ttk.Entry(self.user_info_frame)
        self.time_end_entry = ttk.Entry(self.user_info_frame)
        self.time_start_entry.grid(row=3, column=0)
        self.time_end_entry.grid(row=3, column=1)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=15, ipadx=10)

        # Create the second LabelFrame: breakCheck and calculation
        self.reg_status_var = tk.StringVar()
        self.registered_check = ttk.Checkbutton(self.frame, text="Pause", variable=self.reg_status_var, onvalue="Pause Ok", offvalue="Pause No")
        self.registration_frame = ttk.LabelFrame(self.frame, text='Pause & Calcule')
        self.registration_frame.grid(row=1, column=0, sticky='news', padx=20, pady=20)

        self.break_check_button_var = tk.BooleanVar(self.registration_frame, value=True)
        self.break_check_button = ttk.Checkbutton(self.registration_frame, text="Pause entre 13:00 PM et 15:00 PM", variable=self.break_check_button_var)
        self.break_check_button.grid(row=2, column=0)

        self.calculate_button = ttk.Button(self.registration_frame, text="Calculer", command=self.calculate)
        self.calculate_button.grid(row=2, column=1, sticky='news')

        self.result_label = ttk.Label(self.registration_frame, background='lightgreen')
        self.result_label.grid(row=2, column=2, sticky='news')

        # Create generate Button
        self.entry_button = ttk.Button(self.frame, text='Generer', command=self.generate)
        self.entry_button.grid(row=3, column=0, sticky='news', padx=20, pady=5)

        # Calculate function
    def calculate(self):
        pass
        # pause = self.reg_status_var.get(value='Pause Ok')

    # Excel file generator
    def generate(self):
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        title = self.title_combox.get()
        pause = self.reg_status_var.get()

        print("titre:", title,"firstname: ", firstname,"lastname: ", lastname, "pause:", pause)
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = JobTimeCalculator()
    gui.run()
