# start_time_str = self.time_start_entry.get()
#         end_time_str = self.time_end_entry.get()
#         break_start_time_str = self.break_start_entry.get()
#         break_stop_time_str = self.break_end_entry.get()
#
#         start_time = datetime.datetime.strptime(start_time_str, "%I:%M:%S %p").time()
#         end_time = datetime.datetime.strptime(end_time_str, "%I:%M:%S %p").time()
#         break_start = datetime.datetime.strptime(break_start_time_str, "%I:%M:%S %p").time()
#         break_end = datetime.datetime.strptime(break_stop_time_str, "%I:%M:%S %p").time()
#
#         # totaltime = datetime.timedelta()
#         if end_time < start_time:
#             end_time += datetime.timedelta(days=1)
#
#         if self.break_check_button_var.get():
#             break_start_time = datetime.time(hour=13)
#             break_end_time = datetime.time(hour=13, minute=45)
#
#             if start_time < break_start_time and end_time >= break_end_time:
#                 total_time = datetime.timedelta(hours=8, minutes=30) - datetime.timedelta(hours=2)
#             elif start_time >= break_end_time:
#                 total_time = datetime.timedelta(hours=8, minutes=30)
#             elif end_time <= break_end_time:
#                 total_time = datetime.timedelta(hours=8, minutes=30) - datetime.timedelta(hours=2)
#             else:
#                 time_before_break = datetime.datetime.combine(datetime.datetime.today(),
#                                                               break_start_time) - datetime.datetime.combine(
#                     datetime.datetime.today(), start_time)
#                 time_after_break = datetime.datetime.combine(datetime.datetime.today(),
#                                                              end_time) - datetime.datetime.combine(
#                     datetime.datetime.today(), break_end_time)
#
#                 total_time = time_before_break + time_after_break - datetime.timedelta(hours=2)
#         else:
#             total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
#                 datetime.date.today(), start_time)
#
#         total_time_str = str(total_time)
#         self.result_label.config(text=f"Temps Total:  {total_time_str}", background='lightgreen')