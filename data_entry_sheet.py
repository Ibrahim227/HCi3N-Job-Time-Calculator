import openpyxl
import os


file_path = "C:\\Users\\Maman Sani Ibrahim\\Documents\\HCi3N Job Time Calculator"

if not os.path.exists(file_path):
    workbook = openpyxl.Workbook(file_path)
    sheet = workbook.active()
    head = ['Nom', 'Prenom', 'Poste']
    sheet.append(head)
    workbook.save(file_path)
workbook = openpyxl.load_workbook(file_path)
sheet.append([Nom, Prenom, Poste])
workbook.save(file_path)
