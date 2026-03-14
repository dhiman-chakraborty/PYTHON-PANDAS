import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

# Set Name column as index
df.set_index('Full Name',inplace=True)
print(df)

# Reset index
df.reset_index(inplace=True)
print(df)


# Sort by column ascending order
print(df.sort_values('Age'))

# To sort in descending order
print(df.sort_values('Age',ascending=False))

# Multiple columns
print(df.sort_values(['Full Name','Age'],ascending=[True,False]))     # Name Ascending,Age Decending

