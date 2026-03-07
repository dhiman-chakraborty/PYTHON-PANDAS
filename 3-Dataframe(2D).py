import pandas as pd

# DataFrame (2D): Think of it like an Excel sheet or SQL table.
# Definition: Two-dimensional, size-mutable, heterogeneous tabular data structure with labeled axes (rows and columns).
# Heterogeneous: Each column can have a different dtype.
# Built from dicts, lists, Series, NumPy arrays, or another DataFrame.


# Creating a DataFrame From a Dictionary

# Keys become column names, values become column data.
data1 = {"Name":['Dhiman','Subho','Abir','Somu'],
        "Age":[24,20,29,23],
        "City":['Kolkata','Delhi','Mumbai','Kolkata']}

df1 = pd.DataFrame(data1)
print(df1)


# Creating a DataFrame From a Lists

# You can provide column names separately using the columns parameter.
data2 = [['Dhiman',24,'delhi'],
         ['Somu',21,'Kolkata'],
         ['Abir',30,'Mumbai']]

df2 = pd.DataFrame(data2,columns=['Name','Age','City'])
print(df2)


data3 = [['Dhiman',24,'delhi'],
         ['Somu',21,'Kolkata'],
         ['Abir',30,'Mumbai']]

col = ['Name','Age','City']

df3 = pd.DataFrame(data3,columns=col)
print(df3)


# Creating a DataFrame From a List of Dictionaries
data4 = [{"Name":"Alice","Age":34,"City":"London"},
         {"Name":"Broad","Age":40,"City":"Paris"},
         {"Name":"Stuart","Age":39,"City":"Manchester"},
         {"Name":"Jhon","Age":26,"City":"Verginia"}]

df4 = pd.DataFrame(data4)
print(df4)


# Creating a DataFrame From a NumPy Arrays
import numpy as np

data5 = np.array([[1,6,8],
                  [5,8,3],
                  [1,4,6]])

df5 = pd.DataFrame(data5,columns=["A","B","C"])
print(df5)