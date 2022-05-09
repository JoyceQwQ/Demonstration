import pandas as pd

def add_additional_fields(filename):
    xl = pd.ExcelFile(filename+".xlsx")
    [sheetname] = xl.sheet_names
    print(sheetname)
    data = pd.read_excel(filename+".xlsx")
    file_to_merge = ""
    data_barcode_additional = pd.read_excel(file_to_merge)
    common = ""
    result = pd.merge(data, data_barcode_additional, how="left", on=common)
    result.to_excel(filename+'_additional_fields.xlsx', sheet_name=sheetname, index=False)
            
filenames = []

for filename in filenames:
    add_additional_fields(filename)
