import pandas as pd
import numpy as np

# **What is Time Series?**

# A time series is data collected at successive points in time.

# Examples:
# - Stock market prices per day
# - Sales per month
# - Temperature per hour

# In Pandas, time series = Date/Time index + values.


# Creating Date Ranges

dates = pd.date_range(start='2026-01-01',end='2026-01-31')
print(dates)

# Creating a Time Series DataFrame

# Common frequencies:

# "D" → Day
# "M" → Month end
# "MS" → Month start
# "H" → Hourly
# "W" → Weekly
# "Y" → Yearly

dates2 = pd.date_range('2026-01-01',periods=7,freq='D')
values = np.random.randint(10,100,size=7)

table = pd.DataFrame({'dates':dates2,'Sales':values})
print(table)

# Setting Date as Index
print(table.set_index('dates',inplace=True))

df = pd.read_excel(r'D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx')
# print(df)

print(df['Signup Date'].info())

df['Signup Date'] = pd.to_datetime(df['Signup Date'])
print(df['Signup Date'].info())

# Extracting Date/Time Parts
df['year'] = df['Signup Date'].dt.year
df['Month'] = df['Signup Date'].dt.month
df['month name'] = df['Signup Date'].dt.month_name()
df['day'] = df['Signup Date'].dt.day
df['day name'] = df['Signup Date'].dt.day_name()
print(df[['Signup Date','year','Month','month name','day','day name']].head(50))

df['total bill'] = df['Number of Profiles'] * df['Monthly Payment (INR)']
print(df)
# Resampling Time Series
df2 = df[['Signup Date','total bill']]
df2 = df2.set_index('Signup Date')
print(df2)

# Monthly total sales
# "ME" = month-end
# "MS" = month-start
ms = df2.resample('MS').sum()
print(ms)

# Weekly average sales
wa = df2.resample('W').mean()
print(wa)

# Group rows by week, calculate sum per week
# dataframe.resample('W').sum()

# Group by two weeks, calculate mean
#dataframe.resample('2W').mean()

# Group by month, count rows
#dataframe.resample('M').count()

# Shifting and Lagging
ms['pev mth sales'] = ms['total bill'].shift(1).fillna(0)      # Previous month's sales
ms['diff1'] = ms['total bill'].diff()
print(ms)

ms['next mth sales'] = ms['total bill'].shift(-1).fillna(0)      # next month's sales
ms['diff2'] = ms['total bill']-ms['next mth sales']
print(ms)

# shift(1) → Lag (previous row)

# shift(-1) → Lead (next row)