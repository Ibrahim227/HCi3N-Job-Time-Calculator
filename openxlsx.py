from tkinter import *
from tkinter import messagebox

import openpyxl
import os


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Excel Data Entry")

        # Create labels and entries
        Label(self.master, text="First Name:").grid(row=0, column=0)
        self.first_name_entry = Entry(self.master)
        self.first_name_entry.grid(row=0, column=1)

        Label(self.master, text="Last Name:").grid(row=1, column=0)
        self.last_name_entry = Entry(self.master)
        self.last_name_entry.grid(row=1, column=1)

        Label(self.master, text="Age:").grid(row=2, column=0)
        self.age_entry = Entry(self.master)
        self.age_entry.grid(row=2, column=1)

        # Create a button to save data to Excel
        Button(self.master, text="Save Data", command=self.save_to_excel).grid(row=3, column=1)

    def save_to_excel(self):
        # Get data from entries
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()

        # Validate input
        if not (first_name and last_name and age):
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        # Save data to Excel file
        try:
            file_path = "data.xlsx"
            if not os.path.exists(file_path):
                # Create a new workbook and add a header row
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                sheet.append(["First Name", "Last Name", "Age"])
                workbook.save(file_path)
                workbook.close()

            # Load existing workbook and add data to a new row
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            sheet.append([first_name, last_name, age])
            workbook.save(file_path)
            workbook.close()

            messagebox.showinfo("Success", "Data saved successfully.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Create the GUI window
root = Tk()
app = App(root)
root.mainloop()
