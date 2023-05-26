# # Usage of whole conditionals variables
#
#         # total_time = datetime.timedelta()  # Initialize total_time to zero
#         # (datetime.datetime.combine(datetime.date.today(), break_end_time) - datetime.datetime.combine(datetime.date.today(), break_start_time))
#         if end_time <= start_time:
#             messagebox.showerror("Erreur", message="l'Heure d'Arrivee est superieure ou egal a l'Heure de Descente")
#             return
#
#         if break_taken:
#             messagebox.showinfo(title="Information", message="L'Employee a prit une pause.")
#             if start_time < break_start_time and end_time >= break_end_time:
#                 total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
#                     datetime.date.today(), start_time) - (
#                                      datetime.datetime.combine(datetime.date.today(), break_end_time) -
#                                      datetime.datetime.combine(datetime.date.today(), break_start_time))
#
#             elif start_time >= break_end_time:
#                 total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
#                     datetime.date.today(), start_time)
#
#             elif end_time <= break_start_time:
#                 total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
#                     datetime.date.today(), start_time) - (break_end_time - break_start_time)
#
#             else:
#                 time_before_break = datetime.datetime.combine(datetime.date.today(),
#                                                               break_start_time) - datetime.datetime.combine(
#                     datetime.date.today(), start_time)
#                 time_after_break = datetime.datetime.combine(datetime.date.today(),
#                                                              end_time) - datetime.datetime.combine(
#                     datetime.date.today(), break_end_time)
#                 total_time = time_before_break + time_after_break - (
#                         datetime.datetime.combine(datetime.date.today(), break_end_time) -
#                         datetime.datetime.combine(datetime.date.today(), break_start_time))
#
#         else:
#             messagebox.showinfo(title="Information", message="L'employee n'a pas prit de pause.")
#             total_time = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(
#                 datetime.date.today(), start_time)
