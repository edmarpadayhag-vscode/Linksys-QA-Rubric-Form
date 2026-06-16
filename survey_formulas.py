
import openpyxl
wb = openpyxl.load_workbook(r"d:\Visual Studio Code\QA Rubric\QA Scoring Form Template.xlsx")
ws = wb["Scoring Form"]

print("=== FORMULA / KEY CELLS ===")
formula_rows = []
for row in ws.iter_rows(min_row=24, max_row=207):
    for cell in row:
        if cell.value and isinstance(cell.value, str) and cell.value.startswith("="):
            formula_rows.append(f"  {cell.coordinate}: {cell.value}")

for f in formula_rows:
    print(f)

print()
print("=== MERGE RANGES ===")
for merge in ws.merged_cells.ranges:
    print(f"  {merge}")

print()
print("=== DATA VALIDATIONS ===")
for dv in ws.data_validations.dataValidation:
    print(f"  sqref={dv.sqref}  formula1={dv.formula1}")
