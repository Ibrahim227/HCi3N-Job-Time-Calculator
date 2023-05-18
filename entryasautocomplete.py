import tkinter as tk
from tkinter import ttk

# Create a tkinter window
window = tk.Tk()

# Create a combobox
combobox = ttk.Combobox(window, values=["12:00 AM", "01:00 AM", "02:00 AM", "03:00 AM", "04:00 AM", "05:00 AM",
                                        "06:00 AM", "07:00 AM", "08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM",
                                        "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM",
                                        "06:00 PM", "07:00 PM", "08:00 PM", "09:00 PM", "10:00 PM", "11:00 PM"])
combobox.pack()


# Create an AutocompleteEntryListbox
class AutocompleteEntryListbox(tk.Entry):
    def __init__(self, *args, **kwargs):
        self.listbox = None
        self.var = tk.StringVar()
        super().__init__(*args, **kwargs, textvariable=self.var)
        self.var.trace("w", self.update_listbox)
        self.bind("<KeyRelease>", self.on_key_release)

    def on_key_release(self, event):
        if event.keysym == "Down":
            self.show_listbox()
        elif event.keysym == "Up":
            self.hide_listbox()
        elif event.keysym == "Escape":
            self.hide_listbox()
        else:
            self.update_listbox()

    def update_listbox(self, *args):
        if self.listbox is not None:
            self.listbox.destroy()
        values = [value for value in time_values if self.var.get().lower() in value.lower()]
        if values:
            self.listbox = tk.Listbox(width=self.winfo_width())
            for value in values:
                self.listbox.insert(tk.END, value)
            self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
            self.listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
        else:
            self.hide_listbox()

    def on_listbox_select(self, event):
        index = self.listbox.curselection()
        if index:
            self.var.set(self.listbox.get(index[0]))
            self.icursor(tk.END)

    def hide_listbox(self):
        if self.listbox is not None:
            self.listbox.destroy()
            self.listbox = None

    def show_listbox(self):
        if self.listbox is not None:
            self.listbox.destroy()
            self.listbox = None
        else:
            self.update_listbox()

time_values = ["12:00 AM", "01:00 AM", "02:00 AM", "03:00 AM", "04:00 AM", "05:00 AM", "06:00 AM", "07:00 AM",
               "08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM",
               "04:00 PM", "05:00 PM", "06:00 PM", "07:00 PM", "08:00 PM", "09:00 PM", "10:00 PM", "11:00 PM"]

autocomplete_entry_listbox = AutocompleteEntryListbox(window)
autocomplete_entry_listbox.pack()

# Start the tkinter event loop
window.mainloop()


# import tkinter as tk
# from tkinter import ttk
#
# # Create a tkinter window
# window = tk.Tk()
#
# # Create a combobox for hours
# hours_combobox = ttk.Combobox(window, values=[str(h).zfill(2) for h in range(24)])
# hours_combobox.pack(side=tk.LEFT)
#
# # Create a combobox for minutes
# minutes_combobox = ttk.Combobox(window, values=[str(m).zfill(2) for m in range(60)])
# minutes_combobox.pack(side=tk.LEFT)
#
# # Create a label to display the total worked time
# total_label = ttk.Label(window, text="Total Worked Time: ")
# total_label.pack()
#
# # Function to calculate the total worked time
# def calculate_total():
#     hours = int(hours_combobox.get())
#     minutes = int(minutes_combobox.get())
#     total_minutes = hours * 60 + minutes
#     total_label.config(text=f"Total Worked Time: {total_minutes} minutes")
#
# # Create a button to trigger the calculation
# calculate_button = ttk.Button(window, text="Calculate", command=calculate_total)
# calculate_button.pack()
#
# # Start the tkinter event loop
# window.mainloop()
# import tkinter as tk
# from tkinter import ttk
#
# # Create a tkinter window
# window = tk.Tk()
#
# # Create a time field using Spinbox
# hour_spinbox = ttk.Spinbox(window, from_=0, to=23, width=2, format="%02.0f")
# hour_spinbox.pack(side=tk.LEFT)
# minute_spinbox = ttk.Spinbox(window, from_=0, to=59, width=2, format="%02.0f")
# minute_spinbox.pack(side=tk.LEFT)
#
#
# # Start the tkinter event loop
# window.mainloop()
