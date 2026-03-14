import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

df['Total Bill'] = df['Number of Profiles'] * df['Monthly Payment (INR)']
print(df)

# Pivot Table
print(pd.pivot_table(df,index='Device Used',columns='Preferred Genre',values='Total Bill',aggfunc='sum'))

# Multiple aggregration
print(pd.pivot_table(df,index='Device Used',columns='Preferred Genre',values='Total Bill',aggfunc=['sum','count']))