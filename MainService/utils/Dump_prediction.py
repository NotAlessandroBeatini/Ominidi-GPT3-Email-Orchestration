import openpyxl

path = r'C:\Users\Ale\Downloads\GPT-3-Hackaton-Dataset-handout(2).xlsx'

def dump_on_excel(json,index=2,PATH=path):

    file = openpyxl.load_workbook(PATH)
    ind = "G"+str(index)
    sheet =  file.active
    sheet[ind] = json
    file.save(path)
 
