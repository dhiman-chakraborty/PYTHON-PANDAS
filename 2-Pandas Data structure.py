import pandas as pd

# Pandas Data Structures
# Pandas provides two main data structures (built on top of NumPy arrays):

# 1.Series (1D)
# 2.DataFrame (2D)


# Series (1D): Think of it like a single column in Excel or a labeled 1D array.
# Definition: One-dimensional array with labels (index).

# Homogeneous: All elements usually of the same dtype (int, float, string, etc.).

# Built on NumPy arrays but adds labels (index).

# Properties:

# .values → underlying NumPy array
# .index → labels
# .dtype → data type

a = pd.Series([10,20,30,40,50])

print(a)
print("Values :",a.values)
print("Index :",a.index)
print("Dtype :",a.dtype)

b = pd.Series([10,20,30,40,50],index=[1,2,3,4,5])

print(a)
print("Values :",b.values)
print("Index :",b.index)
print("Dtype :",b.dtype)


c = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])

print(a)
print("Values :",c.values)
print("Index :",c.index)
print("Dtype :",c.dtype)