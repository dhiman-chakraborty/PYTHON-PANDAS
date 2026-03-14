import pandas as pd

df = pd.read_csv(r"D:\POWER BI PROJECTS\INDIAN BIKES SALES DATA\Datasets\bike_sales_100k.csv",encoding='latin1')
print(df.head(10))

# conditions
    # and - &
    # or - | (pipe)
print(df[df['onroad_price']>100000])
print(df[['sale_id','brand','onroad_price']][df['onroad_price']>100000])

print(df[(df['brand']=='Benelli') & ((df['onroad_price']>100000) | (df['fuel_type']=='Electric'))])

print(df[(df['brand']=='Harley-Davidson') & (df['transmission']=='Automatic')])

print(df[(df['brand']=='KTM') | (df['engine_cc']>=100)])

