import pandas as pd

# Applying a Function Over All Elements in a Column
# In Pandas, if you want to apply some operation to every element in a column, you can use:

# .apply()
# Vectorized operations (direct arithmetic)
df = pd.read_excel(r'D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx')

df['Total Bill'] = df['Number of Profiles'] * df['Monthly Payment (INR)']
print(df)

# Applying a Function Using .apply()

# Applying a Custom Function - You can define your own function and apply it
def categoryt(x):
    if x>=1500:
        return 'Premium'
    elif x>=800:
        return 'Gold'
    else:
        return 'Silver'

df['Category'] = df['Total Bill'].apply(categoryt)
print(df)

# Let’s say we want to increase each monthly fee by 10%
df['New monthly fee'] = df['Monthly Payment (INR)'].apply(lambda x:x*1.10)
print(df.head(50))

# Applying a Built-in Python Function
df['Name len'] = df['Full Name'].apply(len)
print(df.head(50))

# Using Vectorized Operations (Fastest Way) - Instead of using .apply(), sometimes you can use direct operations
df['New monthly fee 2'] = df['Monthly Payment (INR)']*1.10   # No function, no looping — fast and efficient
print(df.head())