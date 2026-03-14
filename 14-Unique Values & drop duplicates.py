import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

# Get unique names
print("Unique Names:",df['Full Name'].unique())
print("Unique Device Used :",df['Device Used'].unique())

# nunique(): Returns the count of unique values.
print("No of Unique Names :",df['Full Name'].nunique())

# value_counts(): Returns unique values with their frequency (very useful for analysis).
print('\n',df['Gender'].value_counts())

print(df['Gender'].value_counts().index)
print(df['Gender'].value_counts().values)


# drop_duplicates(): Removes duplicate rows in a DataFrame
df_unique = df.drop_duplicates()
print(df_unique)

# You can also consider specific columns only
df_unique_name = df.drop_duplicates(subset=['Full Name'])
print(df_unique_name)

# Reset Index
df_unique_name = df_unique_name.reset_index(drop=True)
print(df_unique_name)

