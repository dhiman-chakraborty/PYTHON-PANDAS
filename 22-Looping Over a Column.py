import pandas as pd

df = pd.read_excel(r'D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx')

df['Total Bill'] = df['Number of Profiles'] * df['Monthly Payment (INR)']
print(df)

# Looping Over a Single Column
for i in df['Age']:
    print(i)

# Loop with Conditional Logic
for i in df['Age']:
    if i>25:
        print(f'{i} is greater than 25')
    else:
        print(f'{i} is less than 25')


# Looping with Index - If you also need the index, use .iteritems()
for index,row in df.iterrows():
    print(f'{row['Full Name']} is live in {row['City']} and {row['Age']} years old')

# Applying Operations Without Loop
df['Category'] = df['Age'].apply(lambda x: 'Adult' if x>25 else 'Young')
print(df) 