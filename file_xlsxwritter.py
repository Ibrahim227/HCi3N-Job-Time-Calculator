import xlsxwriter

# from xlsxwriter import worksheet

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet01 = workbook.add_worksheet()

test = (['name', 4690],
        ['surname', 2300],
        ['age', 23],
        ['gender', 5000])

row = 0
col = 0
for item, info in test:
    worksheet01.write(row, col,  item)
    worksheet01.write(row, col + 1, info)
    row += 1
worksheet01.write(row, 0, 'Total')
worksheet01.write(row, 1, '=SUM(B1:B4)')
workbook.close()
