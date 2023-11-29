# For reading pandas file
# if file is Excel :- read_excel
# CSV :- read_CSV
# html :- read_html
# sql :- read_sql

import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/YBIFoundation/Dataset/main/Titanic.csv')
print(data)
# .head() it will show you the first 5 lines
# .inf0() its gives you  information about data
# .describe()
print(data.head())
print(data.info())
print(data.describe())