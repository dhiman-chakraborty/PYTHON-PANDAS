import pandas as pd

# Handling Missing Data
import numpy as np

data = {'A':[1,6,3,np.nan,4],
       'B':[5,9,np.nan,6,10]}

df1 = pd.DataFrame(data)
print(df1)

# Check missing values
print(df1.isnull())

# Count missing values per column
print(df1.isnull().sum())

# Fill missing values
print(df1.fillna(0))

 # Drop rows with missing values
print(df1.dropna())
