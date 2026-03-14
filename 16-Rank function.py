import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

df['Total Bill'] = df['Number of Profiles'] * df['Monthly Payment (INR)']
print(df)

# Rank Customer by total bill
df['Rank1'] = df['Total Bill'].rank(method='min',ascending=False).apply(int)
print(df)

# sort by rank
print(df.sort_values('Rank1'))

# Rank Customer by total bill within each Gender
df['Rank2'] = df.groupby('Gender')['Total Bill'].rank(method='min',ascending=False).apply(int)
print(df)

print(df.sort_values(['Gender','Rank2']))

# Top 10
print(df.sort_values('Full Name')[df['Rank1']<=10].head(50))


# To replicate SQL DENSE_RANK() in Pandas, you just need to change the method parameter in rank() from 'min' to 'dense'.

# Dense rank within each class
df['nth_rank'] = df['Total Bill'].rank(method='dense',ascending=False).apply(int)
print(df.sort_values('nth_rank'))

