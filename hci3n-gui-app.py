import datetime
import os
import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox, END, BOTH

import openpyxl
from ttkwidgets.autocomplete import AutocompleteEntryListbox


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
        self.window.config(background="lightgreen", highlightthickness=False, relief="groove", border=5, )
        self.window.iconposition(x=5, y=1)

        ######## Main Frame

        self.frame = ttk.Frame(self.window)
        self.frame.pack(side='top', fill=BOTH)

        ################################# Configure First LabelFrame ############################
        # Saving user Information
        self.user_info_frame = ttk.Labelframe(self.frame, text='Information Employee', underline=0)
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=15, sticky='news')

        # Create name and last name  labels
        self.first_last_name_label = ttk.Label(self.frame, text='Nom & Prenom:', background="lightgrey",
                                               underline=0)
        self.first_last_name_label.grid(row=0, column=1)

        # create  first name and last name entry widgets
        self.name_list = ["ALI BETY", "ABDOULAYE MAIZAMA", "VINCENT PARAISO MOUSSA", "Mme RABO MARIA MOHAMED YAROH",
                          "BOUKARY ABDOU RAZAK", "ABDOU KASSO",
                          "ABOUBACAR DJIMRAOU", "ABOUBA SAIDOU", "IDRISSA CHIPKAOU", "KORAO ABOUBACAR",
                          "Mme DOUDOU HALIDOU MAIMOUNA", "GAMATIE BOUBACAR", "Mme ABDOUL NASSER MARIA",
                          "RABIATOU HABIBOU",
                          "ALASSANE ABDOU ALMOUSTAPHA", "ALI OUMAROU", "OUSMANE FODI", "Mme MOUSTAPHA FOURERA",
                          "Mme MARIAMA AROUNA ANOUAR", "Mme IDRISSA NANA AICHATOU",
                          "Mme ABDOURAHAMANE FOURERATOU DIALLO", "Mme DJIBO ZEYNABOU COULIBALY",
                          "MAHAMADOU MAHAMANE NAFISSATOU", "Mme AMINATOU MAHAMAN ALTINÉ", "Mme FATIMA ISSA BOUKARI",
                          "ABDOU MOUSSA OUSMANE",
                          "GOUMAR ALHASSANE", "ABDOULAYE TANKARI AMADOU", "HAMANI TAHIROU SAIDOU RACHID",
                          "TRAPSIDA ABDOULAY ALAIN", "BOUBACAR HAMADOU", "IBRAHIM MOUSSA", "IBRAHIM DJIBRILLA",
                          "MA AROUF TIDJANI", "LAWAN DARMANE",
                          "BABA BAFRAGI BOUBACAR", "HAMA AMADOU", "GN ABOUBACAR OUMAROU KAILOU",
                          "GN HAROUNA MAAZOU LEYO",
                          "GN LAOUALI MAAZOU MAMANE", "ALI OUMAROU", "Mme SALAMATOU AMADOU", "BOGARI ZOURKALEINI",
                          "MOCTAR BACHIR", "MALAM ROUFAI MAMAN SANI", "ELHADJI SEYBOU DJIBO", "MOUSTAPHA AHMET",
                          "AMADOU BACHIR", "OUSMANE YERIMA YAHAYA", "MAMOUDOU MAHAMAN BACHAR",
                          "SALAMATOU SOUMANA MOUSSA",
                          "SAHABI ABDOU", "GN KABIROU ABDOUL MOUMOUNI", "GN ADAHIR IDI DJIBAGÉ",
                          "Dr MAHAMADOU ABOUBACAR",
                          "AMINA IDRISSA BAGNOU", "ABDOU ADAMOU LILWANI", "ABDOUL WAHABOU ZAKARI DAGOU",
                          "ISSA HAMANI ABDOULAYE", "ALI OUSSEINI MOUSTAPHA", "ALI SOUMAILA FOUREIRATOU",
                          "YAHAYA RHISSA ZAKARI", "ABDALLAH MAHAMAT YAHAYA", "ABASS ADAM MELLY HADIZA",
                          "SOULEY BOUKAR", "HAMIDOU AMANI SOULEYMANE", "KOUNKOUROU AHAMADOU",
                          "Mme SEYDOU ABDOULAYE FOUREYRATOU", "GN RABIOU ABDOULAYE WACHEL", "GN ALMOUSTAPHA DJIBAGÉ"]

        self.first_last_name_entry = AutocompleteEntryListbox(self.frame, completevalues=self.name_list,
                                                              allow_other_values=False, autohidescrollbar=True)
        self.first_last_name_entry.grid(row=0, column=2, ipadx=57)

        # # Create the time and minute Combobox
        # self.hour_spinbox = ttk.Spinbox(self.frame, from_=0, to=23, width=10, format="%02.0f")
        # self.minute_spinbox = ttk.Spinbox(self.frame, from_=0, to=59, width=10, format="%02.0f")
        # self.hour_spinbox.grid(row=2, column=3)
        # self.minute_spinbox.grid(row=2, column=4)

        # create the observation and date Entry
        self.observation_entry_label = ttk.Label(self.frame, text="Observation:", background="lightgrey", underline=0)
        self.date_entry_label = ttk.Label(self.frame, text="Date JJ/MM/ANNEE:", background="lightgrey", underline=0)
        self.observation_entry = ttk.Entry(self.frame)
        self.date_entry = ttk.Entry(self.frame)

        self.observation_entry_label.grid(row=1, column=1)
        self.date_entry_label.grid(row=2, column=1)
        self.observation_entry.grid(row=1, column=2, ipadx=20)
        self.date_entry.grid(row=2, column=2, ipadx=20)

        #
        # Create the title combo box
        self.title = ttk.Label(self.user_info_frame, text='Fonction:', background="lightgrey", underline=0)
        self.title_combox = ttk.Combobox(self.user_info_frame,
                                         values=["HAUT-COMMISSAIRE", "SECRETAIRE GENERAL", "SECRETAIRE GENERAL ADJOINT",
                                                 "DIRECTRICE DAFC", "SECRETAIRE DE DIRECTION",
                                                 "SECRETAIRE DE DIRECTION/BO", "CONSEILLER TECHNIQUE",
                                                 "CHEF DE CABINET", "PROTOCOLE", "DIRECTEUR DPSFCI",
                                                 "CHEF DIV INFORMATIQUE", "CHEF DIV AFFAIRES FINANCIERE",
                                                 "CHEF DIV. MARCHES PUBLIC/DSP",
                                                 "GESTIONNAIRE DES CONVENTIONS", "CHEF DIV PATRIMOINE LOGISTIQUE",
                                                 "APPELEE SERV CIVIQUE", "STAGIAIRE",
                                                 "CHEF DIV RH", "DIRECTEUR DMRC", "CHEF DIV RENFORCEMENT CAPACITE",
                                                 "CHEF DIV MOBILISATION SOCIAL", "SECURITÉ RAPPROCHÉ",
                                                 "DIRECTEUR DSEC", "CHEF DIV CAPITALISATION", "CHEF DIV SISAN",
                                                 "CHEF DIV SUIVI-EVALUATION STATISTIQUE",
                                                 "DIRECTEUR DPEP", "CHEF DIV PROGRAMMATION", "COORDINATEUR",
                                                 "CHEF SERV CARTOGRAPHY", "CHEF SERV COM/CELLULE NUTRITION",
                                                 "CHEF SERV BIO-STATISTIQUE", "ING STATISTICIEN ECONOMISTE P",
                                                 "MEDECIN NUTRITIONISTE", "COORDINATRICE Proj NEXUS",
                                                 "Resp ADMINISTRATIF FINANCE", "Resp SUIVI-EVALUATION",
                                                 "SECRETAIRE COMPTABLE", "CR/TAHOUA", "AT CRi3N NIAMEY",
                                                 "ASSISTANTE SG", "ASSISTANTE SGA", "Resp SECURITÉ", "AGENT SECURITÉ",
                                                 "CHAUFFEUR", "PLANTON"])
        self.title.grid(row=0, column=0)
        self.title_combox.grid(row=1, column=0, ipadx=50)

        # Create department label and combobox
        self.department_label = ttk.Label(self.user_info_frame, text="Departement:", background='lightgrey',
                                          underline=0)
        self.department_combobox = ttk.Combobox(self.user_info_frame, values=["CABINET", "SECRETARIAT GENERAL", "DAFC",
                                                                              "DEPARTMENT PARTENARIAT",
                                                                              "CELLULE NUTRITION", "NEXUS",
                                                                              "COORDINATION REGIONALE",
                                                                              "DMRC", "DSEC", "DPEP", "GNN-SECURITY",
                                                                              "AUXILIAIRES"])
        self.department_label.grid(row=0, column=1)
        self.department_combobox.grid(row=1, column=1, ipadx=20)

        # The place/SIEGE combobox
        self.place_label = ttk.Label(self.user_info_frame, text='Lieu:', background='lightgrey', underline=0)
        self.place_label.grid(row=0, column=2)
        self.place_combobox = ttk.Combobox(self.user_info_frame, values=['SIEGE', 'ANNEXE 1', 'ANNEXE 2'],
                                           validate='focus')
        self.place_combobox.grid(row=1, column=2)

        # Create break time start and end labels
        self.break_start_label = ttk.Label(self.user_info_frame, text="Debut Pause (HH:MM):", background="orange",
                                           underline=0)
        self.break_end_label = ttk.Label(self.user_info_frame, text="Retour Pause (HH:MM):", background="orange",
                                         underline=0)
        self.break_start_label.grid(row=2, column=1)
        self.break_end_label.grid(row=2, column=2)

        # Create  start and end time labels
        self.time_start_label = ttk.Label(self.user_info_frame, text="Heure Entree (HH:MM):",
                                          background="lightgreen", underline=0)
        self.time_end_label = ttk.Label(self.user_info_frame, text="Descente (HH:MM):", background="red",
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
        combobox = ttk.Combobox(self.user_info_frame,
                                values=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"])
        self.week_combobox = combobox
        self.week_label.grid(row=0, column=3)
        self.week_combobox.grid(row=1, column=3)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=20, pady=5, sticky="news")

        # Create message to display
        self.ourmessage = "HCi3N"
        self.display_message = tk.Message(self.frame, text=self.ourmessage, font='italic', relief='raised')
        self.display_message.config(bg="orange")
        self.display_message.grid(row=4, column=1, ipadx=20, ipady=5)

        ############################################### Second LabelFrame ###################################################

        # Create the exit/entry label and Buttons from HQ to annexe1-2

        self.exit_entry_frame = ttk.LabelFrame(self.frame, text="Equipe SIEGE vers (ANNEXE-1 et ANNEXE-2)", underline=0)
        self.exit_entry_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

        self.exit_entry_status_var_1 = tk.BooleanVar(self.exit_entry_frame, value=False)
        self.exit_entry_status_check_1 = ttk.Checkbutton(self.exit_entry_frame, text="Verify Presence ANNEXE-1",
                                                         variable=self.exit_entry_status_var_1, onvalue=True,
                                                         offvalue=False)
        self.exit_entry_status_check_1.grid(row=0, column=0)

        # Create Entry widgets for exit/entry from Site
        self.exit_entry_label_entry = ttk.Label(self.exit_entry_frame, text="Heure Entree (HH:MM):",
                                                background="lightgreen", underline=0)
        self.exit_entry_label_exit = ttk.Label(self.exit_entry_frame, text="Sortie (HH:MM):",
                                               background="red", underline=0)
        self.exit_entry_label_entry.grid(row=1, column=0)
        self.exit_entry_label_exit.grid(row=1, column=1)

        self.site_entry = ttk.Entry(self.exit_entry_frame)
        self.site_exit = ttk.Entry(self.exit_entry_frame)
        self.site_entry.grid(row=2, column=0)
        self.site_exit.grid(row=2, column=1)

        ############# second entry/exit Entry widget #############

        self.exit_entry_status_var_2 = tk.BooleanVar(self.exit_entry_frame, value=False)
        self.exit_entry_status_check_2 = ttk.Checkbutton(self.exit_entry_frame, text="Verify Presence Annexe-2",
                                                         variable=self.exit_entry_status_var_2, onvalue=True,
                                                         offvalue=False)
        self.exit_entry_status_check_2.grid(row=0, column=3)

        # Create Entry Exit Status from HQ to annexe1-2
        self.exit_entry_label_entry_01 = ttk.Label(self.exit_entry_frame, text="Heure Entree (HH:MM):",
                                                   background="lightgreen", underline=0)
        self.exit_entry_label_exit_01 = ttk.Label(self.exit_entry_frame, text="Sortie (HH:MM):",
                                                  background="red", underline=0)
        self.exit_entry_label_entry_01.grid(row=1, column=3)
        self.exit_entry_label_exit_01.grid(row=1, column=4)

        self.site_entry_01 = ttk.Entry(self.exit_entry_frame)
        self.site_exit_01 = ttk.Entry(self.exit_entry_frame)
        self.site_entry_01.grid(row=2, column=3)
        self.site_exit_01.grid(row=2, column=4)

        for widget in self.exit_entry_frame.winfo_children():
            widget.grid_configure(padx=20, pady=5, sticky="news")

        ###################################### Configure Third LabelFrame ################################

        # Create the labelFrame annexe 1 to hq and annexe 2
        ################# first check, entries and labels
        self.verify_frame = ttk.LabelFrame(self.frame, text="Equipe ANNEXE-1 vers (SIEGE et ANNEXE-2)", underline=0)
        self.verify_frame.grid(row=2, column=0, padx=20, pady=20, sticky="news")
        self.presence_check_var = tk.BooleanVar(self.verify_frame, value=False)
        self.presence_check = ttk.Checkbutton(self.verify_frame, text="Verify Presence SIEGE",
                                              variable=self.presence_check_var,
                                              onvalue=True, offvalue=False)
        self.presence_check.grid(row=0, column=0)

        # Verify presence Entry and Exit / label and entry widgets
        self.annexe_entry_label = ttk.Label(self.verify_frame, text="Heure Entree (HH:MM):",
                                            background="lightgreen",
                                            underline=0)
        self.annexe_exit_label = ttk.Label(self.verify_frame, text="Sortie (HH:MM):", background="red",
                                           underline=0)
        self.annexe_entry_label.grid(row=1, column=0)
        self.annexe_exit_label.grid(row=1, column=1)

        self.annexe_entry = ttk.Entry(self.verify_frame)
        self.annexe_exit = ttk.Entry(self.verify_frame)
        self.annexe_entry.grid(row=2, column=0)
        self.annexe_exit.grid(row=2, column=1)

        ####################

        # second check variable, labels and Entries widgets
        self.annexe_to_annexe_var = tk.BooleanVar(self.verify_frame, value=False)
        self.annexe_to_annexe = ttk.Checkbutton(self.verify_frame, text="Verify Presence ANNEXE-2",
                                                variable=self.annexe_to_annexe_var, onvalue=True, offvalue=False)
        self.annexe_to_annexe.grid(row=0, column=3)

        self.check_annexe_entry_label = ttk.Label(self.verify_frame, text="Heure Entree (HH:MM):",
                                                  background="lightgreen", underline=0)
        self.check_annexe_exit_label = ttk.Label(self.verify_frame, text="Sortie (HH:MM):", background="red",
                                                 underline=0)

        self.check_annexe_entry_label.grid(row=1, column=3)
        self.check_annexe_exit_label.grid(row=1, column=4)

        # Create entry widget
        self.annexe_entry_01 = ttk.Entry(self.verify_frame)
        self.annexe_exit_01 = ttk.Entry(self.verify_frame)
        self.annexe_entry_01.grid(row=2, column=3)
        self.annexe_exit_01.grid(row=2, column=4)

        for widget in self.verify_frame.winfo_children():
            widget.grid_configure(padx=20, pady=5, sticky="news")

        ############################################ Configure Fourth LabelFrame ################################

        self.third_frame = ttk.LabelFrame(self.frame, text="Equipe ANNEXE-2 vers (SIEGE-ANNEXE-1)", underline=0)
        self.third_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        self.verification_button_var = tk.BooleanVar(self.third_frame, value=False)
        self.verification_button = ttk.Checkbutton(self.third_frame, text="Verify Presence SIEGE",
                                                   variable=self.verification_button_var,
                                                   onvalue=True, offvalue=False)
        self.verification_button.grid(row=0, column=0)

        self.value_entry_label = ttk.Label(self.third_frame, text="Heure Entree (HH:MM):",
                                           background="lightgreen", underline=0)
        self.value_exit_label = ttk.Label(self.third_frame, text="Sortie (HH:MM):", background="red", underline=0)
        self.value_entry_widget = ttk.Entry(self.third_frame)
        self.value_exit_widget = ttk.Entry(self.third_frame)

        self.value_entry_label.grid(row=1, column=0)
        self.value_exit_label.grid(row=1, column=1)
        self.value_entry_widget.grid(row=2, column=0)
        self.value_exit_widget.grid(row=2, column=1)

        ###### second verification check button, entries

        self.second_verification_check_var = tk.BooleanVar(self.third_frame, value=False)
        self.second_verification_check_button = ttk.Checkbutton(self.third_frame, text="Verify Presence ANNEXE-1",
                                                                variable=self.second_verification_check_var,
                                                                onvalue=True, offvalue=False)
        self.second_verification_check_button.grid(row=0, column=3)

        self.second_ver_label1 = ttk.Label(self.third_frame, text="Heure Entree (HH:MM):",
                                           background="lightgreen", underline=0)
        self.second_ver_label2 = ttk.Label(self.third_frame, text="Sortie (HH:MM):", background="red",
                                           underline=0)
        self.second_annexe_entry = ttk.Entry(self.third_frame)
        self.second_annexe_exit = ttk.Entry(self.third_frame)
        self.second_ver_label1.grid(row=1, column=3)
        self.second_ver_label2.grid(row=1, column=4)
        self.second_annexe_entry.grid(row=2, column=3)
        self.second_annexe_exit.grid(row=2, column=4)

        for widget in self.third_frame.winfo_children():
            widget.grid_configure(padx=20, pady=5, sticky="news")

        ############################################ Configure Fifth LabelFrame ################################

        self.registration_frame = ttk.LabelFrame(self.frame, text='Pause & Affichage', underline=0)
        self.registration_frame.grid(row=4, column=0, sticky='news', padx=20, pady=20)

        self.break_check_button_var = tk.BooleanVar(self.registration_frame, value=False)
        self.break_check_button = ttk.Checkbutton(self.registration_frame, text="Pause entre 13:30 PM et 14:15 PM",
                                                  variable=self.break_check_button_var, onvalue=True, offvalue=False)
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

        ################# Auto fill Button
        self.auto_fill_button = ttk.Button(self.registration_frame, text='Auto Fill', command=self.fill_entries)
        self.auto_fill_button.grid(row=3, column=4)

        #################################### Configure the Menu #################################
        # Create Menu menubar
        self.menu_ = tk.Menu(self.frame, tearoff=0)
        self.menu_bar = tk.Menu(self.menu_, tearoff=0)
        self.menu_bar.add_command(label="A propos HCi3N", command=on_click)
        self.menu_bar.add_separator()
        self.menu_bar.add_command(label="Quitter", accelerator='Alt+F4', command=self.exit_01)

        self.menu_.add_cascade(label="Menu", menu=self.menu_bar)
        self.window.config(menu=self.menu_)

        #
        """
            # Everything about functions
        """

    # Exit function
    def exit_01(self):
        if messagebox.askokcancel(title='Quitter', message='Voulez-vous quitter ?'):
            self.window.destroy()

        # Clear function

    def clear(self):
        # self.first_last_name_entry.delete(0, END)
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
        self.value_entry_widget.delete(0, END)
        self.value_exit_widget.delete(0, END)
        self.second_annexe_entry.delete(0, END)
        self.second_annexe_exit.delete(0, END)
        self.week_combobox.delete(0, END)
        self.observation_entry.delete(0, END)
        self.date_entry.delete(0, END)

        # fill function

    def fill_entries(self):
        value = "00:00"  # Predefined value to fill the entries
        self.break_start_entry.insert(0, value)
        self.break_end_entry.insert(0, value)
        self.annexe_entry.insert(0, value)
        self.annexe_entry_01.insert(0, value)
        self.site_exit.insert(0, value)
        self.site_exit_01.insert(0, value)
        self.site_entry.insert(0, value)
        self.site_entry_01.insert(0, value)
        self.annexe_exit_01.insert(0, value)
        self.annexe_exit.insert(0, value)
        self.value_entry_widget.insert(0, value)
        self.value_exit_widget.insert(0, value)
        self.second_annexe_entry.insert(0, value)
        self.second_annexe_exit.insert(0, value)

    ################################################################

    #  Calculate function

    def calculate_total_time(self):
        start_time_str = self.time_start_entry.get()
        end_time_str = self.time_end_entry.get()
        break_start_time_str = self.break_start_entry.get()  # fixed break start time
        break_end_time_str = self.break_end_entry.get()  # fixed break end time
        break_taken = self.break_check_button_var.get()

        start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
        end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
        break_start_time = datetime.datetime.strptime(break_start_time_str, "%H:%M").time()
        break_end_time = datetime.datetime.strptime(break_end_time_str, "%H:%M").time()

        # # TEAM HQ TO (ANNEXE"1-2")
        # hq_to_annexe1_entry_str = self.site_entry.get()
        # hq_to_annexe1_exit_str = self.site_exit.get()
        # hq_to_annexe2_entry_str = self.site_entry_01.get()
        # hq_to_annexe2_exit_str = self.site_exit_01.get()
        #
        # # Conditional Verification Team HQ
        # hq_to_annexe1_entry = datetime.datetime.strptime(hq_to_annexe1_entry_str, "%H:%M").time()
        # hq_to_annexe1_exit = datetime.datetime.strptime(hq_to_annexe1_exit_str, "%H:%M").time()
        # hq_to_annexe2_entry = datetime.datetime.strptime(hq_to_annexe2_entry_str, "%H:%M").time()
        # hq_to_annexe2_exit = datetime.datetime.strptime(hq_to_annexe2_exit_str, "%H:%M").time()
        # hq_visit_to_annexe1_check = self.exit_entry_status_var_1.get()
        # hq_visit_to_annexe2_check = self.exit_entry_status_var_2.get()
        #
        # # Team ANNEXE 1 TO (HQ-ANNEXE 2)
        # annexe1_to_hq_entry_str = self.annexe_entry.get()
        # annexe1_to_hq_exit_str = self.annexe_exit.get()
        # annexe1_to_annexe2_entry_str = self.annexe_entry_01.get()
        # annexe1_to_annexe2_exit_str = self.annexe_exit_01.get()
        #
        # # Conditional Verification Team annexe1
        # annexe1_to_hq_entry = datetime.datetime.strptime(annexe1_to_hq_entry_str, "%H:%M").time()
        # annexe1_to_hq_exit = datetime.datetime.strptime(annexe1_to_hq_exit_str, "%H:%M").time()
        # annexe1_to_annexe2_entry = datetime.datetime.strptime(annexe1_to_annexe2_entry_str, "%H:%M").time()
        # annexe1_to_annexe2_exit = datetime.datetime.strptime(annexe1_to_annexe2_exit_str, "%H:%M").time()
        # annexe1_visit_to_hq_check = self.presence_check_var.get()
        # annexe1_visit_to_annexe2_check = self.annexe_to_annexe_var.get()
        #
        # # TEAM ANNEXE 2 TO (HQ-ANNEXE 1)
        # annexe2_to_hq_entry_str = self.value_entry_widget.get()
        # annexe2_to_hq_exit_str = self.value_exit_widget.get()
        # annexe2_to_annexe1_entry_str = self.second_annexe_entry.get()
        # annexe2_to_annexe1_exit_str = self.second_annexe_exit.get()
        #
        # # Conditional Verification Team Annexe2
        # annexe2_to_hq_entry = datetime.datetime.strptime(annexe2_to_hq_entry_str, "%H:%M").time()
        # annexe2_to_hq_exit = datetime.datetime.strptime(annexe2_to_hq_exit_str, "%H:%M").time()
        # annexe2_to_annexe1_entry = datetime.datetime.strptime(annexe2_to_annexe1_entry_str, "%H:%M").time()
        # annexe2_to_annexe1_exit = datetime.datetime.strptime(annexe2_to_annexe1_exit_str, "%H:%M").time()
        # annexe2_visit_to_hq_check = self.verification_button_var.get()
        # annexe2_visit_to_annexe1_check = self.second_verification_check_var.get()

        # Usage of whole conditionals variables

        # total_time = datetime.timedelta()  # Initialize total_time to zero
        # (datetime.datetime.combine(datetime.date.today(), break_end_time) - datetime.datetime.combine(datetime.date.today(), break_start_time))
        if end_time <= start_time:
            messagebox.showerror("Erreur", message="l'Heure d'Arrivee est superieure ou egal a l'Heure de Descente")
            return

        if break_taken:
            messagebox.showinfo(title="Information", message="L'Employee a prit une pause.")
            if start_time < break_start_time and end_time >= break_end_time:
                total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
                    datetime.date.today(), start_time) - (
                                     datetime.datetime.combine(datetime.date.today(), break_end_time) -
                                     datetime.datetime.combine(datetime.date.today(), break_start_time))

            elif start_time >= break_end_time:
                total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
                    datetime.date.today(), start_time)

            elif end_time <= break_start_time:
                total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
                    datetime.date.today(), start_time) - (break_end_time - break_start_time)

            else:
                time_before_break = datetime.datetime.combine(datetime.date.today(),
                                                              break_start_time) - datetime.datetime.combine(
                    datetime.date.today(), start_time)
                time_after_break = datetime.datetime.combine(datetime.date.today(),
                                                             end_time) - datetime.datetime.combine(
                    datetime.date.today(), break_end_time)
                total_time = time_before_break + time_after_break - (
                        datetime.datetime.combine(datetime.date.today(), break_end_time) -
                        datetime.datetime.combine(datetime.date.today(), break_start_time))

        else:
            messagebox.showinfo(title="Information", message="L'employee n'a pas prit de pause.")
            total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
                datetime.date.today(), start_time)

        total_time_str = str(total_time)

        self.result_label.config(text=total_time_str)
        return total_time  # Return the total_time value

    ############## Excel File Generator function ###############

    # Excel file generator
    def save_to_excel(self):
        nom_prenom = self.first_last_name_entry.get()
        fonction = self.title_combox.get()
        departement = self.department_combobox.get()
        arrivee = self.time_start_entry.get()
        pause = self.break_check_button_var.get()
        debut_pause = self.break_start_entry.get()
        retour_pause = self.break_end_entry.get()
        descente = self.time_end_entry.get()
        lieu = self.place_combobox.get()
        total = self.calculate_total_time()
        jour_semaine = self.week_combobox.get()
        observation = self.observation_entry.get()
        daily_date = self.date_entry.get()

        # Validate input
        if not (
                nom_prenom and fonction and departement and lieu and arrivee and descente and total and jour_semaine and daily_date):
            required_list = ["Nom & Prenom", "Fonction", "Departement", "Lieu", "Heure Arrivee", "Descente", "Total",
                             "Jour", "Date"]
            messagebox.showerror(f"Erreur", f"Veuillez remplir tout les champs requis:\n {list(required_list)}")
            return
        # Save data to Excel file
        try:
            file_path = "data.xlsx"
            if not os.path.exists(file_path):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                sheet.append(["NOM & PRENOM", "FONCTION", "DEPARTEMENT", "LIEU", "ENTREE", "PAUSE", "DEBUT PAUSE",
                              "RETOUR PAUSE", "DESCENTE", "TEMPS TOTAL JOURNALIER", "JOUR", "DATE", "OBSERVATION"])
                workbook.save(file_path)
                workbook.close()
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            sheet.append([nom_prenom, fonction, departement, lieu, arrivee, pause, debut_pause, retour_pause, descente,
                          total, jour_semaine, daily_date, observation])
            workbook.save(file_path)
            workbook.close()

            messagebox.showinfo("Succès", "Donnée enregistrée avec succès.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ### Running function

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = JobTimeCalculator()
    # unittest.main()
    gui.run()
