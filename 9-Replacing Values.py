import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

# Make one value NaN
df.loc[3,'Full Name'] = None
print(df)

# Replace NaN with "Unknown"
df['Full Name'] = df['Full Name'].fillna('Dhiman Chakraborty')
print(df)

df.loc[3,'Full Name'] = None
print(df)

df = df['Full Name'].replace({None : 'Dhiman Chakraborty'})
print(df)


