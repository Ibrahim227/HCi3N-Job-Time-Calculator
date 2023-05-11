import datetime
import tkinter as tk
from tkinter import ttk, messagebox, END


class JobTimeCalculator(object):
    def __init__(self):
        super().__init__()  # Allows to inherit from the tkinter object
        self.window = tk.Tk()
        self.window.title("HCi3N")
        self.window.geometry()
        self.window.iconbitmap('images\\logoHCi3N.ico')

        self.frame = ttk.Frame(self.window)
        self.frame.pack(anchor='center')

        # Saving user Information
        self.user_info_frame = ttk.Labelframe(self.frame, text='Information Employee', underline=0)
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky='news')

        # Create name and last name  labels
        self.first_name_label = ttk.Label(self.user_info_frame, text='Nom:', background="lightgrey", underline=0)
        self.first_name_label.grid(row=0, column=0)
        self.last_name_label = ttk.Label(self.user_info_frame, text='Prenom:', background="lightgrey", underline=0)
        self.last_name_label.grid(row=0, column=1)

        # create entry
        self.first_name_entry = ttk.Entry(self.user_info_frame)
        self.last_name_entry = ttk.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)

        # The post combobox
        self.post_label = ttk.Label(self.user_info_frame, text='Site', background='lightgrey', underline=0)
        self.post_label.grid(row=2, column=2)
        self.post_combobox = ttk.Combobox(self.user_info_frame, values=['SIEGE', 'ANNEXE 1', 'ANNEXE 2'], validate='focus')
        self.post_combobox.grid(row=3, column=2)

        # Create the title combo box
        self.title = ttk.Label(self.user_info_frame, text='Fonction:', background="lightgrey", underline=0)
        self.title_combox = ttk.Combobox(self.user_info_frame, values=["HAUT-COMMISSAIRE", "SECRETAIRE GENERAL", "SECRETAIRE GENERAL ADJOINT",
                                                                       "DIRECTRICE DAFC", "SECRETAIRE DE DIRECTION", "SECRETAIRE DE DIRECTION/BO", "CONSEILLER TECHNIQUE",
                                                                       "CHEF DE CABINET", "PROTOCOLE", "DIRECTEUR DPSFCI", "CHEF DIV INFORMATIQUE", "CHEF DIV FINANCE", "CHEF DIV. MARCHES PUBLIC/DSP",
                                                                       "GESTIONNAIRE DES CONVENTIONS", "CHEF DIV PATRIMOINE LOGISTIQUE", "APPELEE SERV CIVIQUE", "STAGIARE",
                                                                       "CHEF DIV RH", "DIRECTEUR DMRC", "CHEF DIV RENFORCEMENT CAPACITE", "CHEF DIV MOBILISATION SOCIAL",
                                                                       "DIRECTEUR DSEC", "CHEF DIV CAPITALISATION", "CHEF DIV SISAN", "CHEF DIV SUIVI-EVALUATION STATISTIQUE",
                                                                       "DIRECTEUR DPEP", "CHEF DIV PROGRAMMATION", "COORDINATEUR", "CHEF SERV CARTOGRAPHY", "CHEF SERV COM/CELLULE NUTRITION",
                                                                       "CHEF SERV BIO-STATISTIQUE", "ING STATISTICIEN ECONOMISTE P", "MEDECIN NUTRITIONISTE", "COORDINATRICE Proj NEXUS",
                                                                       "Resp ADMINISTRATIF FINANCE", "Resp SUIVI-EVALUATION", "SECRETAIRE COMPTABLE", "CR/TAHOUA", "AT CRi3N NIAMEY",
                                                                       "ASSISTANTE SG", "ASSISTANTE SGA", "Resp SECURITY", "AGENT SECURITY", "CHAUFFEUR", "PLANTON"])
        self.title.grid(row=0, column=2)
        self.title_combox.grid(row=1, column=2)

        self.department_label = ttk.Label(self.user_info_frame, text="Departement", background='lightgrey', underline=0)
        self.department_combobox = ttk.Combobox(self.user_info_frame, values=["CABINET", "SECRETARIAT GENERAL", "DAFC", "DEPARTMENT PARTENARIAT",
                                                                              "CELLULE NUTRITION", "NEXUS", "COORDINATION REGIONALE",
                                                                              "DMRC", "DSEC", "DPEP", "GARDES-SECURITY", "AUXILIARES"])
        self.department_label.grid(row=2, column=3)
        self.department_combobox.grid(row=3, column=3, sticky='news')

        self.time_start_label = ttk.Label(self.user_info_frame, text="Entree (HH:MM:SS AM/PM):", background="lightgreen", underline=0)
        self.time_end_label = ttk.Label(self.user_info_frame, text="Descente (HH:MM:SS AM/PM):", background="red", underline=0)
        self.time_start_label.grid(row=2, column=0)
        self.time_end_label.grid(row=2, column=1)

        # Create Entry widgets
        self.time_start_entry = ttk.Entry(self.user_info_frame)
        self.time_end_entry = ttk.Entry(self.user_info_frame)
        self.time_start_entry.grid(row=3, column=0)
        self.time_end_entry.grid(row=3, column=1)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=50, pady=20,)

        # Create the second LabelFrame: breakCheck and calculation
        self.reg_status_var = tk.StringVar(value='Pause Ok')
        self.registered_check = ttk.Checkbutton(self.frame, text="Pause", variable=self.reg_status_var, onvalue="Pause Ok", offvalue="Pause Non")
        self.registration_frame = ttk.LabelFrame(self.frame, text='Pause & Affichage', underline=0)
        self.registration_frame.grid(row=1, column=0, sticky='news', padx=20, pady=20)

        self.break_check_button_var = tk.BooleanVar(self.registration_frame, value=True)
        self.break_check_button = ttk.Checkbutton(self.registration_frame, text="Pause entre 13:00 PM et 15:00 PM", variable=self.break_check_button_var)
        self.break_check_button.grid(row=2, column=0)

        # create calculate button
        self.calculate_button = ttk.Button(self.registration_frame, text="Calculer", command=self.calculate)
        self.calculate_button.grid(row=2, column=1, sticky='news')

        # result view label
        self.result_label = ttk.Label(self.registration_frame, background='lightgreen')
        self.result_label.grid(row=2, column=3, sticky='news')

        for widget in self.registration_frame.winfo_children():
            widget.grid_configure(padx=10, pady=15, ipadx=7)

        # Create generate Button
        self.entry_button = ttk.Button(self.frame, text='Generer', command=self.generate)
        self.entry_button.grid(row=3, column=0, sticky='news', padx=20, pady=5)

        # add a clear button
        self.clear_button = ttk.Button(self.frame, text='Effacer', command=self.clear)
        self.clear_button.grid(row=2, column=0, sticky='nw', padx=20, pady=5)

    # Clear function
    def clear(self):
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.post_combobox.delete(0, END)
        self.title_combox.delete(0, END)
        self.time_start_entry.delete(0, END)
        self.time_end_entry.delete(0, END)
        self.department_combobox.delete(0, END)

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
