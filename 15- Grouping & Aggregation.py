import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

# Groupby with single column
# Direct groupby on column
print(df.groupby('Device Used')['Monthly Payment (INR)'].sum())

# Groupby with single column
# Using .agg()
print(df.groupby('Device Used').agg({'Monthly Payment (INR)':'sum'}))

# Groupby with single column
# Selecting columns after groupby
print(df.groupby('Device Used').sum(numeric_only=True)['Monthly Payment (INR)'])

# Reset index
print(df.groupby('Device Used')['Monthly Payment (INR)'].sum().reset_index())

# Groupby Single column with MULTIPLE agg functions
print(df.groupby('Device Used')['Monthly Payment (INR)'].agg(['sum','min','max']))
print(df.groupby('Device Used').agg({'Monthly Payment (INR)':['sum','count','min','max']}))

# Groupby with MULTIPLE columns
print(df.groupby(['Device Used','Gender'])['Monthly Payment (INR)'].sum())

# Groupby with MULTIPLE columns and agg functions
print(df.groupby(['Device Used','Gender']).agg({'Monthly Payment (INR)':['sum','count'],'Age':['min','max']}))       # it used to perform different calculation on differemt columns

print(df.groupby(['Device Used','Gender'])[['Monthly Payment (INR)','Age']].agg(['sum','count','min','max']))        # it performs same calculation on different columns

print(df.groupby(['Device Used','Gender']).agg({'Monthly Payment (INR)':['sum','count'],'Age':['min','max']}).reset_index())

