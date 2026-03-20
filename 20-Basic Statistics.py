import pandas as pd

df = pd.read_excel(r'D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx')

df['Total Bill'] = df['Number of Profiles'] * df['Monthly Payment (INR)']
print(df)

# Basic Statistics
print('Mean:',df['Total Bill'].mean(),'\n')
print('Median:',df['Total Bill'].median(),'\n')
print('Mode:',df['Total Bill'].mode(),'\n')
print('Min:',df['Total Bill'].min(),'\n')
print('Max:',df['Total Bill'].max(),'\n')
print('Standard Deviation:',df['Total Bill'].std(),'\n')
print('Variance:',df['Total Bill'].var(),'\n')