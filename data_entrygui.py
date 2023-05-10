import datetime
from tkinter import ttk, messagebox
import tkinter as tk


class JobTimeCalculator(object):
    def __init__(self):
        super().__init__()
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
        self.reg_status_var = tk.StringVar(value='Pause Ok')
        self.registered_check = ttk.Checkbutton(self.frame, text="Pause", variable=self.reg_status_var, onvalue="Pause Ok", offvalue="Pause No")
        self.registration_frame = ttk.LabelFrame(self.frame, text='Pause & Calcule', underline=0)
        self.registration_frame.grid(row=1, column=0, sticky='news', padx=20, pady=20)

        self.break_check_button_var = tk.BooleanVar(self.registration_frame, value=True)
        self.break_check_button = ttk.Checkbutton(self.registration_frame, text="Pause entre 13:00 PM et 15:00 PM", variable=self.break_check_button_var)
        self.break_check_button.grid(row=2, column=0)

        self.calculate_button = ttk.Button(self.registration_frame, text="Calculer", command=self.calculate)
        self.calculate_button.grid(row=2, column=1, sticky='news')

        self.result_label = ttk.Label(self.registration_frame, background='lightgreen')
        self.result_label.grid(row=2, column=2, sticky='news')

        for widget in self.registration_frame.winfo_children():
            widget.grid_configure(padx=10, pady=15, ipadx=10)

        # Create generate Button
        self.entry_button = ttk.Button(self.frame, text='Generer', command=self.generate)
        self.entry_button.grid(row=3, column=0, sticky='news', padx=20, pady=5)

        # Calculate function
    def calculate(self):
        # pause = self.reg_status_var.get()
        start_time_str = self.time_start_entry.get()
        end_time_str = self.time_end_entry.get()
        # name_str = self.first_name_entry.get()
        # last_name_str = self.last_name_entry.get()

        start_time = datetime.datetime.strptime(start_time_str, "%I:%M:%S %p").time()
        end_time = datetime.datetime.strptime(end_time_str, "%I:%M:%S %p").time()

        # totaltime = datetime.timedelta()
        if end_time < start_time:
            end_time += datetime.timedelta(days=1)

        if self.break_check_button_var.get():
            break_start_time = datetime.time(hour=13)
            break_end_time = datetime.time(hour=15)

            if start_time < break_start_time and end_time >= break_end_time:
                total_time = datetime.timedelta(hours=8, minutes=30) - datetime.timedelta(hours=2)
            elif start_time >= break_end_time:
                total_time = datetime.timedelta(hours=8, minutes=30)
            elif end_time <= break_end_time:
                total_time = datetime.timedelta(hours=8, minutes=30) - datetime.timedelta(hours=2)
            else:
                time_before_break = datetime.datetime.combine(datetime.datetime.today(), break_start_time) - datetime.datetime.combine(datetime.datetime.today(), start_time)
                time_after_break = datetime.datetime.combine(datetime.datetime.today(), end_time) - datetime.datetime.combine(datetime.datetime.today(), break_end_time)

                total_time = time_before_break + time_after_break - datetime.timedelta(hours=2)
        else:
            total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(datetime.date.today(), start_time)

        total_time_str = str(total_time)
        self.result_label.config(text=f"Temps Total: %s" % total_time_str, background='lightgreen')

    # Excel file generator
    def generate(self):
        accepted = self.reg_status_var.get()

        if accepted == "Pause Ok":
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()
            title = self.title_combox.get()

            print("titre:", title, "firstname: ", firstname, "lastname: ", lastname, "pause:", accepted)

        else:
            tk.messagebox.showwarning(title='Warning', message='Warning')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = JobTimeCalculator()
    gui.run()
