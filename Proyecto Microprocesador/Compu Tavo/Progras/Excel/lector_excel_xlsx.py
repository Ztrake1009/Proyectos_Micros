import openpyxl

def lector_excel(nombre):  # La extención debe ser xlsx
    wb = openpyxl.load_workbook(nombre)
    sh = wb.active
    lista=[]

    for i in range(1,6):
        for j in range(1,6):
            c = sh.cell(row = i,column = j)
            lista.append(c.value)    

    return lista

print(lector_excel("Prueba.xlsx"))