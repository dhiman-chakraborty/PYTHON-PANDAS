import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

df['Total Bill']=df['Number of Profiles'] * df['Monthly Payment (INR)']      # New column
print(df)

df['Is active'] = df['Account Status']=='Active'     # Boolean column
print(df)

print(df.loc[df['Monthly Payment (INR)']==499])

df.loc[df['Monthly Payment (INR)']==499,'Monthly Payment (INR)']=599
print(df)


# Create a new column based on multiple conditions

# Create a new column category:
#             Salary > 50k AND experience > 3 → "Senior"
#             Salary > 50k AND experience ≤ 3 → "Mid"
#             Otherwise → "Junior"


# Method 1 - using np.select()
import numpy as np

conditions = [((df['Monthly Payment (INR)']>400) & (df['Number of Profiles']>=4)),
              ((df['Monthly Payment (INR)']>200) & (df['Number of Profiles']>=2))]

choices = ['Premium','Gold']

df['Status'] = np.select(conditions,choices,default='Silver')
print(df)


# Method 2 - Using np.where() (Nested)
df['Status2'] = np.where(((df['Monthly Payment (INR)']>400) & (df['Number of Profiles']>=4)),'Premium',
                         np.where(((df['Monthly Payment (INR)']>200) & (df['Number of Profiles']>=2)),'Gold','Silver'))

print(df)


# Method 3 – Using .apply()
def categorize(df):
    if df['Monthly Payment (INR)']>400 & df['Number of Profiles']>=4:
        return 'Premium'
    elif df['Monthly Payment (INR)']>200 & df['Number of Profiles']>=2:
        return 'Gold'
    else:
        return 'Silver'
    
df['Status3'] = df.apply(categorize,axis=1)
print(df)