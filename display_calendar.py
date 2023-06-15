# from tkinter import Tk, ttk
# from tkcalendar import Calendar, DateEntry
#
#
# def show_calendar():
#     def get_selected_date():
#         selected_date = cal.get_date()
#         spinbox.delete(0, "end")
#         spinbox.insert(0, selected_date)
#         top.destroy()
#
#     top = Tk()
#     cal = Calendar(top, selectmode="day")
#     cal.pack()
#
#     confirm_button = ttk.Button(top, text="Confirmer", command=get_selected_date)
#     confirm_button.pack()
#
#     top.mainloop()
#
#
# root = Tk()
#
# spinbox = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)
# spinbox.pack(padx=10, pady=10)
#
# button = ttk.Button(root, text="Choisir Date", command=show_calendar)
# button.pack(pady=5)
#
# root.mainloop()
#
# from tkinter import Tk
# from tkcalendar import Calendar, DateEntry
#
#
# def get_selected_date():
#     selected_date = cal.get_date()
#     spinbox.delete(0, "end")
#     spinbox.insert(0, selected_date)
#     top.destroy()
#
#
# top = Tk()
#
# spinbox = DateEntry(top, width=12, background="darkblue", foreground="white", borderwidth=2)
# spinbox.pack(padx=10, pady=10)
#
# cal = Calendar(top, selectmode="day", date_pattern="dd/mm/yyyy")
# cal.pack()
#
# cal.bind("<<DateEntrySelected>>", lambda event: get_selected_date())
#
# top.mainloop()

from tkinter import Tk
from tkcalendar import DateEntry


def get_selected_date():
    selected_date = spinbox.get_date()
    print(selected_date)  # You can replace this line with your desired functionality


root = Tk()

spinbox = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)
spinbox.pack(padx=10, pady=10)

spinbox.bind("<<DateEntrySelected>>", lambda event: get_selected_date())

root.mainloop()
