import pandas as pd

# import os
# os.getcwd()

# Import as csv
df1 = pd.read_csv(r"D:\POWER BI PROJECTS\ADVENTURE WORKS\DATASETS\AdventureWorks_Customers.csv",encoding='latin1')

print(df1.head(20))


# To export dataframe
df1.to_csv("output.csv")         # Index is showing
df1.to_csv("output.csv",index=False)   # Index is not showing


# Import as Excel
df2 = pd.read_excel(r"D:\ASSINGMENTS\POWER BI  ASSINGMENT\Mobile Sales Analysis\Mobile Sales Data.xlsx",sheet_name=0)
print(df2.head(20))

# To export dataframe(Excel)
df2.to_excel("Output2.xlsx",index=False)