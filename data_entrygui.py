import datetime
import os
import tkinter as tk
# import unittest
import webbrowser
from tkinter import ttk, messagebox, END

import openpyxl


# redirect to HCi3N website
def on_click():
    url = "http://www.initiative3n.ne/"
    webbrowser.open_new_tab(url)


### Class Definition

class JobTimeCalculator:
    # Initialize the class
    def __init__(self):
        super().__init__()  # Allows to inherit from the tkinter class object
        # Main window
        self.window = tk.Tk()
        self.window.title("HCi3N")
        self.window.geometry()
        self.window.iconbitmap('images\\logoHCi3N.ico')
        self.window.config(background="#87E990")

        self.frame = ttk.Frame(self.window)
        self.frame.pack(anchor='center')

        ################################# Configure First LabelFrame ############################
        # Saving user Information
        self.user_info_frame = ttk.Labelframe(self.frame, text='Information Employee', underline=0)
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky='news')

        # Create name and last name  labels
        self.first_name_label = ttk.Label(self.user_info_frame, text='Nom:', background="lightgrey", underline=0)
        self.first_name_label.grid(row=0, column=0)
        self.last_name_label = ttk.Label(self.user_info_frame, text='Prenom:', background="lightgrey", underline=0)
        self.last_name_label.grid(row=0, column=1)

        # create  first name and last name entry widgets
        self.first_name_entry = ttk.Entry(self.user_info_frame, )
        self.last_name_entry = ttk.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0, ipadx=10)
        self.last_name_entry.grid(row=1, column=1, ipadx=10)

        # Create the title combo box
        self.title = ttk.Label(self.user_info_frame, text='Fonction:', background="lightgrey", underline=0)
        self.title_combox = ttk.Combobox(self.user_info_frame,
                                         values=["HAUT-COMMISSAIRE", "SECRETAIRE GENERAL", "SECRETAIRE GENERAL ADJOINT",
                                                 "DIRECTRICE DAFC", "SECRETAIRE DE DIRECTION",
                                                 "SECRETAIRE DE DIRECTION/BO", "CONSEILLER TECHNIQUE",
                                                 "CHEF DE CABINET", "PROTOCOLE", "DIRECTEUR DPSFCI",
                                                 "CHEF DIV INFORMATIQUE", "CHEF DIV FINANCE",
                                                 "CHEF DIV. MARCHES PUBLIC/DSP",
                                                 "GESTIONNAIRE DES CONVENTIONS", "CHEF DIV PATRIMOINE LOGISTIQUE",
                                                 "APPELEE SERV CIVIQUE", "STAGIARE",
                                                 "CHEF DIV RH", "DIRECTEUR DMRC", "CHEF DIV RENFORCEMENT CAPACITE",
                                                 "CHEF DIV MOBILISATION SOCIAL",
                                                 "DIRECTEUR DSEC", "CHEF DIV CAPITALISATION", "CHEF DIV SISAN",
                                                 "CHEF DIV SUIVI-EVALUATION STATISTIQUE",
                                                 "DIRECTEUR DPEP", "CHEF DIV PROGRAMMATION", "COORDINATEUR",
                                                 "CHEF SERV CARTOGRAPHY", "CHEF SERV COM/CELLULE NUTRITION",
                                                 "CHEF SERV BIO-STATISTIQUE", "ING STATISTICIEN ECONOMISTE P",
                                                 "MEDECIN NUTRITIONISTE", "COORDINATRICE Proj NEXUS",
                                                 "Resp ADMINISTRATIF FINANCE", "Resp SUIVI-EVALUATION",
                                                 "SECRETAIRE COMPTABLE", "CR/TAHOUA", "AT CRi3N NIAMEY",
                                                 "ASSISTANTE SG", "ASSISTANTE SGA", "Resp SECURITY", "AGENT SECURITY",
                                                 "CHAUFFEUR", "PLANTON"])
        self.title.grid(row=0, column=2)
        self.title_combox.grid(row=1, column=2, ipadx=50)

        # Create department label and combobox
        self.department_label = ttk.Label(self.user_info_frame, text="Departement:", background='lightgrey',
                                          underline=0)
        self.department_combobox = ttk.Combobox(self.user_info_frame, values=["CABINET", "SECRETARIAT GENERAL", "DAFC",
                                                                              "DEPARTMENT PARTENARIAT",
                                                                              "CELLULE NUTRITION", "NEXUS",
                                                                              "COORDINATION REGIONALE",
                                                                              "DMRC", "DSEC", "DPEP", "GNN-SECURITY",
                                                                              "AUXILIAIRES"])
        self.department_label.grid(row=0, column=3)
        self.department_combobox.grid(row=1, column=3, ipadx=20)

        # The place/site combobox
        self.place_label = ttk.Label(self.user_info_frame, text='Site:', background='lightgrey', underline=0)
        self.place_label.grid(row=0, column=4)
        self.place_combobox = ttk.Combobox(self.user_info_frame, values=['SIEGE', 'ANNEXE 1', 'ANNEXE 2'],
                                           validate='focus')
        self.place_combobox.grid(row=1, column=4)

        # Create break time start and end labels
        self.break_start_label = ttk.Label(self.user_info_frame, text="Debut Pause (HH:MM AM/PM):", background="orange",
                                           underline=0)
        self.break_end_label = ttk.Label(self.user_info_frame, text="Retour Pause (HH:MM AM/PM):", background="orange",
                                         underline=0)
        self.break_start_label.grid(row=2, column=1)
        self.break_end_label.grid(row=2, column=2)

        # Create  start and end time labels
        self.time_start_label = ttk.Label(self.user_info_frame, text="Entree (HH:MM AM/PM):", background="lightgreen",
                                          underline=0)
        self.time_end_label = ttk.Label(self.user_info_frame, text="Descente (HH:MM AM/PM):", background="red",
                                        underline=0)
        self.time_start_label.grid(row=2, column=0)
        self.time_end_label.grid(row=2, column=3)

        # Create Entry widgets for arrival and departure time entries
        self.time_start_entry = ttk.Entry(self.user_info_frame)
        self.time_end_entry = ttk.Entry(self.user_info_frame)
        self.time_start_entry.grid(row=3, column=0)
        self.time_end_entry.grid(row=3, column=3)

        # Create entry widget for break starts and break ends time entries
        self.break_start_entry = ttk.Entry(self.user_info_frame)
        self.break_end_entry = ttk.Entry(self.user_info_frame)
        self.break_start_entry.grid(row=3, column=1)
        self.break_end_entry.grid(row=3, column=2)

        # Week days combobox entry
        self.week_label = ttk.Label(self.user_info_frame, text="Jour de Semaine:", underline=0, background="lightgrey")
        self.week_combobox = ttk.Combobox(self.user_info_frame,
                                          values=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi",
                                                  "Dimanche"])
        self.week_label.grid(row=2, column=4)
        self.week_combobox.grid(row=3, column=4)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=30, pady=10, sticky="news")

        ############################################### Second LabelFrame ###################################################

        # Create the exit/entry label and Buttons from HQ to annexe1-2
        self.exit_entry_frame = ttk.LabelFrame(self.frame, text="Equipe Site vers (ANNEXE1-ANNEXE2)", underline=0)
        self.exit_entry_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

        self.exit_entry_status_var_1 = tk.BooleanVar(self.exit_entry_frame, value=True)
        self.exit_entry_status_check_1 = ttk.Checkbutton(self.exit_entry_frame, text="Verify Presence Annexe-1",
                                                         variable=self.exit_entry_status_var_1, onvalue=False,
                                                         offvalue=True)
        self.exit_entry_status_check_1.grid(row=0, column=0)

        # Create Entry widgets for exit/entry from Site
        self.exit_entry_label_entry = ttk.Label(self.exit_entry_frame, text="Entree (HH:MM AM/PM):",
                                                background="lightgreen", underline=0)
        self.exit_entry_label_exit = ttk.Label(self.exit_entry_frame, text="Sortie (HH:MM AM/PM):",
                                               background="red", underline=0)
        self.exit_entry_label_entry.grid(row=1, column=0)
        self.exit_entry_label_exit.grid(row=1, column=1)

        self.site_entry = ttk.Entry(self.exit_entry_frame)
        self.site_exit = ttk.Entry(self.exit_entry_frame)
        self.site_entry.grid(row=2, column=0)
        self.site_exit.grid(row=2, column=1)

        ############# second entry/exit Entry widget

        self.exit_entry_status_var_2 = tk.BooleanVar(self.exit_entry_frame, value=True)
        self.exit_entry_status_check_2 = ttk.Checkbutton(self.exit_entry_frame, text="Verify Presence vers Annexe-2",
                                                         variable=self.exit_entry_status_var_2, onvalue=False,
                                                         offvalue=True)
        self.exit_entry_status_check_2.grid(row=0, column=3)

        # Create Entry Exit Status from HQ to annexe1-2
        self.exit_entry_label_entry_01 = ttk.Label(self.exit_entry_frame, text="Entree (HH:MM AM/PM):",
                                                   background="lightgreen", underline=0)
        self.exit_entry_label_exit_01 = ttk.Label(self.exit_entry_frame, text="Sortie (HH:MM AM/PM):",
                                                  background="red", underline=0)
        self.exit_entry_label_entry_01.grid(row=1, column=3)
        self.exit_entry_label_exit_01.grid(row=1, column=4)

        self.site_entry_01 = ttk.Entry(self.exit_entry_frame)
        self.site_exit_01 = ttk.Entry(self.exit_entry_frame)
        self.site_entry_01.grid(row=2, column=3)
        self.site_exit_01.grid(row=2, column=4)

        for widget in self.exit_entry_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10, sticky="news")

        ################################################### Configure Third LabelFrame ################################

        # Create the labelFrame
        ################# first check, entries and labels
        self.verify_frame = ttk.LabelFrame(self.frame, text="Equipe Annexe vers (Site-Annexe)", underline=0)
        self.verify_frame.grid(row=2, column=0, padx=20, pady=20, sticky="news")
        self.presence_check_var = tk.BooleanVar(self.verify_frame, value=True)
        self.presence_check = ttk.Checkbutton(self.verify_frame, text="Verify Presence Siege",
                                              variable=self.presence_check_var,
                                              onvalue=False, offvalue=True)
        self.presence_check.grid(row=0, column=0)

        # Verify presence Entry and Exit / label and entry widgets
        self.annexe_entry_label = ttk.Label(self.verify_frame, text="Entree (HH:MM AM/PM):", background="lightgreen",
                                            underline=0)
        self.annexe_exit_label = ttk.Label(self.verify_frame, text="Sortie (HH:MM AM/PM):", background="red",
                                           underline=0)
        self.annexe_entry_label.grid(row=1, column=0)
        self.annexe_exit_label.grid(row=1, column=1)

        self.annexe_entry = ttk.Entry(self.verify_frame)
        self.annexe_exit = ttk.Entry(self.verify_frame)
        self.annexe_entry.grid(row=2, column=0)
        self.annexe_exit.grid(row=2, column=1)

        ####################
        # second check variable, labels and Entries widgets
        self.annexe_to_annexe_var = tk.BooleanVar(self.verify_frame, value=True)
        self.annexe_to_annexe = ttk.Checkbutton(self.verify_frame, text="Verify Presence Annexe",
                                                variable=self.annexe_to_annexe_var, onvalue=False, offvalue=True)
        self.annexe_to_annexe.grid(row=0, column=3)

        self.check_annexe_entry_label = ttk.Label(self.verify_frame, text="Entree (HH:MM AM/PM):",
                                                  background="lightgreen", underline=0)
        self.check_annexe_exit_label = ttk.Label(self.verify_frame, text="Sortie (HH:MM AM/PM):", background="red",
                                                 underline=0)

        self.check_annexe_entry_label.grid(row=1, column=3)
        self.check_annexe_exit_label.grid(row=1, column=4)

        # Create entry widget
        self.annexe_entry_01 = ttk.Entry(self.verify_frame)
        self.annexe_exit_01 = ttk.Entry(self.verify_frame)
        self.annexe_entry_01.grid(row=2, column=3)
        self.annexe_exit_01.grid(row=2, column=4)

        for widget in self.verify_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10, sticky="news")

        ############################################ Configure Fourth LabelFrame ################################

        # Create the second LabelFrame: breakCheck and calculation
        # self.reg_status_var = tk.StringVar(value='Ok')
        # self.registered_check = ttk.Checkbutton(self.frame, text="Pause", variable=self.reg_status_var,
        #                                         onvalue=True, offvalue=False)
        self.registration_frame = ttk.LabelFrame(self.frame, text='Pause & Affichage', underline=0)
        self.registration_frame.grid(row=3, column=0, sticky='news', padx=20, pady=20)

        self.break_check_button_var = tk.BooleanVar(self.registration_frame, value=True)
        self.break_check_button = ttk.Checkbutton(self.registration_frame, text="Pause entre 13:30 PM et 14:15 PM",
                                                  variable=self.break_check_button_var, onvalue=False, offvalue=True)
        self.break_check_button.grid(row=2, column=0)

        # create calculate button
        self.calculate_button = ttk.Button(self.registration_frame, text="Calculer", command=self.calculate_total_time)
        self.calculate_button.grid(row=3, column=2, sticky='news')

        # result view label
        self.result_view = ttk.Label(self.registration_frame, text="Le Temps total est:", underline=0,
                                     background="lightgrey")
        self.result_view.grid(row=2, column=1, sticky='news')
        self.result_label = ttk.Label(self.registration_frame, background='lightgreen')
        self.result_label.grid(row=2, column=2, sticky='news')

        for widget in self.registration_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10, sticky="news")

        ################################################################

        """
            # Create Buttons
        """

        ############ Create save_to_excel Button
        self.entry_button = ttk.Button(self.registration_frame, text='Sauvegarder', command=self.save_to_excel)
        self.entry_button.grid(row=3, column=0, sticky='news', padx=20, pady=7)

        ################ add a clear button
        self.clear_button = ttk.Button(self.registration_frame, text='Effacer Champs', command=self.clear)
        self.clear_button.grid(row=3, column=1)

        #################################### Configure the Menu #################################
        # Create Menu menubar
        self.menu_ = tk.Menu(self.frame, tearoff=0)
        self.menu_bar = tk.Menu(self.menu_, tearoff=0)
        self.menu_bar.add_command(label="A propos HCi3N", command=on_click)
        self.menu_bar.add_separator()
        self.menu_bar.add_command(label="Quitter", accelerator='Alt+F4', command=self.exit_01)

        self.menu_.add_cascade(label="Menu", menu=self.menu_bar)
        self.window.config(menu=self.menu_)

        # upload_list = ['Ibrahim', 'Niger', 'Mali', 'Burkina Faso', 'Guinea', 'Afghanistan', 'Iraq', 'Jordan', 'Iraq',
        #                'Kiribati', 'Kazakhstan', 'Russia',
        #                'United States', 'United kingdom', 'North Africa', 'Morocco', 'Algeria', 'Tunisia', 'Albania']
        # entry = AutocompleteEntryListbox(self.frame, completevalues=upload_list)
        # entry.grid(row=2, column=0)

        """
            # Everything about functions
        """

    # Exit function
    def exit_01(self):
        if messagebox.askokcancel(title='Quitter', message='Voulez-vous quitter ?'):
            self.window.destroy()

    # Clear function
    def clear(self):
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.place_combobox.delete(0, END)
        self.title_combox.delete(0, END)
        self.time_start_entry.delete(0, END)
        self.time_end_entry.delete(0, END)
        self.department_combobox.delete(0, END)
        self.break_start_entry.delete(0, END)
        self.break_end_entry.delete(0, END)
        self.annexe_entry.delete(0, END)
        self.annexe_entry_01.delete(0, END)
        self.site_exit.delete(0, END)
        self.site_exit_01.delete(0, END)
        self.site_entry.delete(0, END)
        self.site_entry_01.delete(0, END)
        self.annexe_exit_01.delete(0, END)
        self.annexe_exit.delete(0, END)

        ################################################################
        # Calculate function

    def calculate_total_time(self):
        start_time_str = self.time_start_entry.get()
        end_time_str = self.time_end_entry.get()
        break_start_time_str = self.break_start_entry.get()  # fixed break start time
        break_end_time_str = self.break_end_entry.get()  # fixed break end time
        break_taken = self.break_check_button_var.get()

        start_time = datetime.datetime.strptime(start_time_str, "%H:%M %p").time()
        end_time = datetime.datetime.strptime(end_time_str, "%H:%M %p").time()
        break_start_time = datetime.datetime.strptime(break_start_time_str, "%H:%M %p").time()
        break_end_time = datetime.datetime.strptime(break_end_time_str, "%H:%M %p").time()

        # total_time = datetime.timedelta()  # Initialize total_time to zero

        if end_time < start_time:
            end_time += datetime.timedelta(days=1)

        if break_taken:
            if start_time < break_start_time and end_time >= break_end_time:
                total_time = datetime.timedelta(hours=9, minutes=30) - (
                        datetime.datetime.combine(datetime.date.today(), break_end_time) -
                        datetime.datetime.combine(datetime.date.today(), break_start_time))
            elif start_time >= break_end_time:
                total_time = datetime.timedelta(hours=9, minutes=30)
            elif end_time <= break_start_time:
                total_time = datetime.timedelta(hours=8, minutes=30) - (
                        datetime.datetime.combine(datetime.date.today(), break_end_time) -
                        datetime.datetime.combine(datetime.date.today(), break_start_time))
            else:
                time_before_break = datetime.datetime.combine(datetime.date.today(),
                                                              break_start_time) - datetime.datetime.combine(
                    datetime.date.today(), start_time)
                time_after_break = datetime.datetime.combine(datetime.date.today(),
                                                             end_time) - datetime.datetime.combine(
                    datetime.date.today(), break_end_time)
                total_time = time_before_break + time_after_break - (break_end_time - break_start_time)
        else:
            total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
                datetime.date.today(), start_time)

        total_time_str = str(total_time)

        self.result_label.config(text=total_time_str)
        return total_time  # Return the total_time value

    ############## Excel File Generator function ###############

    # Excel file generator
    def save_to_excel(self):

        nom = self.first_name_entry.get()
        prenom = self.last_name_entry.get()
        fonction = self.title_combox.get()
        departement = self.department_combobox.get()
        arrivee = self.time_start_entry.get()
        pause = self.break_check_button_var.get()
        debut_pause = self.break_start_entry.get()
        retour_pause = self.break_end_entry.get()
        descente = self.time_end_entry.get()
        site = self.place_combobox.get()
        total = self.calculate_total_time()
        jour_semaine = self.week_combobox.get()
        daily_date = datetime.date.today()
        save_date = datetime.date.today()

        # Validate input
        if not (
                nom and prenom and fonction and departement and site and arrivee and debut_pause and retour_pause and descente and jour_semaine and daily_date and total):
            messagebox.showerror("Erreur", "Veuillez remplir tout les champs.")
            return
        # Save data to Excel file
        try:
            file_path = f"Sauvegarde du {save_date}" + ".xlsx"
            if not os.path.exists(file_path):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                sheet.append(["Nom", "Prenom", "Fonction", "Departement", "Site", "Arrivee", "Pause", "Debut Pause",
                              "Retour Pause", "Descente", "Jour de Semaine", "Date", "Temps total"])
                workbook.save(file_path)
                workbook.close()
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            sheet.append([nom, prenom, fonction, departement, site, arrivee, pause, debut_pause, retour_pause, descente,
                          jour_semaine, daily_date, total])
            workbook.save(file_path)
            workbook.close()

            messagebox.showinfo("Success", "Data saved successfully.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ### Running function

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = JobTimeCalculator()
    # unittest.main()
    gui.run()
