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

# for shape
print(data.shape)

# display column label
print(data.columns)

# select a column as a series
print(data['sex'])
print(data.shape)

# select a column as a dataframe
print(data[['sex']])

#unique category in a column
print(data['sex'].unique())

#number of unique category in a column
print(data['sex'].nunique())

#categories wise number in a column
print(data['sex'].value_counts())

# count of missing value
print(data.isna().sum())
print(data.isnull().sum())

