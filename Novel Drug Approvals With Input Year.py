# Novel Drug Approvals with input year
# enter year
year = str(input("Enter year: "))
url = "https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-" + year
name_file_cvs = year + ".csv"
name_file_excel = year + ".xlsx"
data_year = "data_" + year

# get and save csv file
import pandas as pd
df = pd.read_html(url)
df1 = df[0]
df2 = pd.DataFrame(df1)
data_year = df2.to_csv(name_file_cvs, index=None)

# convert csv to xlsx
from openpyxl import Workbook
import csv
wb = Workbook()
ws = wb.active
with open(name_file_cvs, 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save(name_file_excel)
print("Done!")

# merge all csv to xlsx
from pyexcel.cookbook import merge_all_to_a_book
# import pyexcel.ext.xlsx # no longer required if you use pyexcel >= 0.2.2 
import glob

merge_all_to_a_book(glob.glob("*.csv"), "_Novel_Drug_Approval_Data_All.xlsx")