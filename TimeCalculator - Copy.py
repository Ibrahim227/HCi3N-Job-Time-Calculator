import datetime
import tkinter as tk


class TimeCalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Time Calculator")
        # self.root.geometry("1024x500")

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.start_label = tk.Label(self.input_frame, text="Start time (HH:MM:SS AM/PM):")
        self.start_label.grid(row=0, column=0, padx=5, pady=5)

        self.start_entry = tk.Entry(self.input_frame)
        self.start_entry.grid(row=0, column=1, padx=5, pady=5)

        self.end_label = tk.Label(self.input_frame, text="End time (HH:MM:SS AM/PM):")
        self.end_label.grid(row=1, column=0, padx=5, pady=5)

        self.end_entry = tk.Entry(self.input_frame)
        self.end_entry.grid(row=1, column=1, padx=5, pady=5)

        self.break_checkbutton_var = tk.BooleanVar(value=True)
        self.break_checkbutton = tk.Checkbutton(self.input_frame, text="Take a break between 1:00 PM and 3:00 PM", variable=self.break_checkbutton_var)
        self.break_checkbutton.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack(padx=5, pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(padx=5, pady=5)

    def calculate(self):
        start_time_str = self.start_entry.get()
        end_time_str = self.end_entry.get()

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
                time_before_break = datetime.datetime.combine(datetime.date.today(), break_start_time) - datetime.datetime.combine(datetime.date.today(), start_time)
                time_after_break = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(datetime.date.today(), break_end_time)
                total_time = time_before_break + time_after_break - datetime.timedelta(hours=2)
        else:
            total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(datetime.date.today(), start_time)

        total_time_str = str(total_time)
        self.result_label.config(text=f"Total time worked: {total_time_str}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = TimeCalculatorGUI()
    gui.run()
