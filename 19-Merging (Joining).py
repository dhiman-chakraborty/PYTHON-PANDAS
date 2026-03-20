import pandas as pd

# Merge (equivalent to SQL JOIN)
df1 = pd.read_csv(r'D:\POWER BI PROJECTS\ADVENTURE WORKS\DATASETS\AdventureWorks_Product_Subcategories.csv',encoding='latin1')
df2 = pd.read_csv(r'D:\POWER BI PROJECTS\ADVENTURE WORKS\DATASETS\AdventureWorks_Products.csv',encoding='latin1')

print(df1,'\n')
print(df2,'\n')

# Inner Join (only matching rows)
print(pd.merge(df1,df2,on='ProductSubcategoryKey',how='inner'))

# Left Join (all rows from left, match from right)
print(pd.merge(df1,df2,on='ProductSubcategoryKey',how='left'))

# Right Join (all rows from right, match from left)
print(pd.merge(df1,df2,on='ProductSubcategoryKey',how='right'))

# Outer Join (all rows from both)
print(pd.merge(df1,df2,on='ProductSubcategoryKey',how='outer'))


# Join on multiple columns

df3 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Dept": ["HR", "IT", "HR"],
    "Name": ["Alice", "Bob", "Charlie"]
})

df4 = pd.DataFrame({
    "ID": [2, 3, 4],
    "Dept": ["IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000]
})

print(df3,'\n')
print(df4,'\n')

print(pd.merge(df3,df4,on=['ID','Dept'],how='inner'))

# If column name is different
df5 = pd.DataFrame({"ID":[1,2,3], "Name":["A","B","C"]})
df6 = pd.DataFrame({"E_ID":[1,2,4], "Salary":[100,200,300]})

print(df5,'\n')
print(df6,'\n')

print(pd.merge(df5,df6,left_on='ID',right_on='E_ID',how='inner'))