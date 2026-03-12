import pandas as pd

df = pd.read_csv(r"D:\POWER BI PROJECTS\INDIAN BIKES SALES DATA\Datasets\bike_sales_100k.csv",encoding="latin1")
print(df)     # To view entire table

print(df.head())     # First 5 rows (by default)
print(df.head(10))   # First 10 rows (you can change the number)

print(df.tail())     # Last 5 rows (by default)
print(df.tail(10))   # Last 10 rows

# Info Command
# In pandas, .shape is an attribute (not a function) that returns the dimensions of a DataFrame or Series
print(df.shape)      # (rows, columns)

# The .info() method provides a concise summary of a pandas DataFrame. It helps you understand the structure of your dataset.
print(df.info())     # Column data types & memory usage)

# The describe() function in pandas is used to generate summary statistics of numerical columns (by default)
print(df.describe())

# describe() for categorical data
print(df.describe(include='str'))

# Describe entire DataFrame (numeric + categorical)
print(df.describe(include='all'))

# .columns is an attribute of a pandas DataFrame that returns the list of column names.
print(df.columns)
print(list(df.columns))

# .dtypes is an attribute of a DataFrame that shows the data type of each column
print(df.dtypes)     # Data types

# The .index attribute returns the index (row labels) of a DataFrame or Series
print(df.index)      # Row index