# This code is working fine
# Using Pandas -
# This code will take an excel file with multiple sheets
# and output a csv file with a single sheet with all aggregate Data

import pandas as pd
import csv

headers = ['Value', 'Name', 'Category', 'Comment', 'Favorite', 'Score', 'Notes', 'Image']

# We will use bookmarks data exported in an Excel File,
# where the LinkStore has generated separate sheet for each category

x1 = pd.ExcelFile('linkstoredata.xlsx')
listOfSheets = x1.sheet_names

# We will dump list of Lists in aggregate_list
aggregate_list = []

for sheet in listOfSheets:
    #df stnads for Dataframe
    df = pd.read_excel(x1, sheet)
    #converting dataframe into list
    dfl = df.values.tolist()
    aggregate_list.append(dfl)


# Writing Output Data in CSV File
with open ("exported_bookmarks_from_linkstore.csv", "w", newline="", encoding='utf-8') as f:
    data_handler = csv.writer(f, delimiter=",")
    for list in aggregate_list:
        for item in list:
            data_handler.writerow(item)