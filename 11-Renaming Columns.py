import pandas as pd

df = pd.read_excel(r"D:\POWER BI PROJECTS\NETFLIX DASHBOARD\netflix_indian_customers_100k.xlsx")
print(df)

# Rename specific columns using rename()
print(df.rename(columns={'Full Name' : 'Name'}))

df = df.rename(columns={'Full Name' : 'Name'})
print(df)

# inplace=True controls whether pandas modifies the original DataFrame or creates a new one
# The original DataFrame df is changed directly. No new DataFrame is returned
df.rename(columns={'Name' : 'Customer Name'},inplace=True)
print(df)

# Renaming columns using axis=1
# axis = 0 means rows and axis = 1 means columns
print(df.rename({'Customer Name' : 'Full Name'},axis=1))     # Same thing using columns= {'Name': 'Employee_Name'}

df.rename({'Full Name' : 'Customer Full Name'},axis=1,inplace=True)
print(df)

print(df.columns)
# Rename using set_axis()
print(df.set_axis(['Customer ID', 'Customer Name', 'SEX', 'Age', 'Email',
       'Phone Number', 'Subscription Plan', 'Signup Date', 'Last Active Date',
       'State', 'City', 'Device Used', 'Watch Time (mins/day)',
       'Preferred Genre', 'Number of Profiles', 'Monthly Payment (INR)',
       'Account Status'],axis=1))

df = df.set_axis(['Customer ID', 'Customer Name', 'SEX', 'Age', 'Email',
       'Phone Number', 'Subscription Plan', 'Signup Date', 'Last Active Date',
       'State', 'City', 'Device Used', 'Watch Time (mins/day)',
       'Preferred Genre', 'Number of Profiles', 'Monthly Payment (INR)',
       'Account Status'],axis=1)
print(df)

# Rename ALL columns at once use set_axis