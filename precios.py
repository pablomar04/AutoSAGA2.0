from openpyxl import load_workbook

wb = load_workbook("precios.xlsx", data_only=True)
sh = wb["Nafta"]
n1 = [int(sh["e26"].value), int(sh["e27"].value), 
      int(sh["g26"].value), int(sh["g27"].value),
      int(sh["i26"].value), int(sh["i27"].value),
      int(sh["k26"].value), int(sh["k27"].value),
      int(sh["m26"].value), int(sh["m27"].value),
      int(sh["o26"].value), int(sh["o27"].value),
      int(sh["q26"].value), int(sh["q27"].value)]
n2 = [int(sh["e53"].value), int(sh["e54"].value), 
      int(sh["g53"].value), int(sh["g54"].value),
      int(sh["i53"].value), int(sh["i54"].value),
      int(sh["k53"].value), int(sh["k54"].value),
      int(sh["m53"].value), int(sh["m54"].value),
      int(sh["o53"].value), int(sh["o54"].value),
      int(sh["q53"].value), int(sh["q54"].value)]
for x in n2:
    print(x)
