import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

# Drop a column using drop()
print(df.drop(['Age'],axis=1))             # df = df.drop(['City'], axis=1)
                                           # df.drop(['City'], axis=1, inplace=True)   # This changes the original DataFrame

# Drop multiple columns
print(df.drop(['Email','Phone Number'],axis=1))        # df.drop(['Age', 'City'], axis=1, , inplace=True)   # This changes the original DataFrame

# Drop a column using .columns index
print(df.drop(df.columns[3],axis=1))      # drops 4th column 'Age'

# Drop a row by index
print(df.drop(3))           # drops the row with index 3
                            # df.drop(3, inplace=True)    # This changes the original DataFrame

# Drop multiple rows
print(df.drop([1,2]))       # df.drop([0, 2], inplace=True)    # This changes the original DataFrame

print(df.drop(1,axis=0))    # df.drop(1, axis=0, inplace=True)

print(df.drop([0,5],axis=0))        # df.drop([0,5], axis=0, inplace=True)


# Drop rows using a condition
print(df[df['Age']>25])

df = df[df['Age']>25]        # doing same work as inplace=True
print(df)

# Reset Indet
df = df.reset_index(drop=True)
print(df)