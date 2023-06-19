import openpyxl

# Load the Excel spreadsheet
wb = openpyxl.load_workbook('my_spreadsheet.xlsx')

# Get the worksheet
ws = wb.active

# Iterate over the rows and columns
for row in ws.rows:
    for cell in row:
        # Get the cell value
        value = cell.value

        # Resize the row and column
        row.height = max(row.height, len(value))
        column = ws.columns[cell.column]
        column.width = max(column.width, len(value))

# Save the Excel spreadsheet
wb.save('my_spreadsheet.xlsx')