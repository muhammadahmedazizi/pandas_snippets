# https://www.learnpython.org/en/Pandas_Basics

# Import pandas as pd
import pandas as pd

# Import the scrapped_data.csv data: coreyms website data
df = pd.read_csv('scrapped_data.csv', encoding = "ISO-8859-1") # used this encoding - ISO-8859-1 for utf-8

# Print out dataframe
print(df)