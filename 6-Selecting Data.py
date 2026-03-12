import pandas as pd

df = pd.read_csv(r"D:\POWER BI PROJECTS\INDIAN BIKES SALES DATA\Datasets\bike_sales_100k.csv",encoding="latin1")
print(df)

# Selecting Columns
print(df["brand"])

# Selecting Columns
print(df[["brand","onroad_price",'accessories_value']])
print(df.head(20)[["brand","onroad_price",'accessories_value']])    # for first 20 rows


# .iloc → Index Location (Integer-based indexing)

# .iloc selects rows and columns by integer position: (0, 1, 2, 3 … like list indexing).
# .loc → Label Location (Label-based indexing)

# .loc selects rows and columns by label/name.
# Key Differences (Very Important)

# Feature	          .iloc	                                 .loc
# Type	              Integer-based	                        Label-based
# Rows selection	  uses numbers	                        uses index labels
# Columns selection	  uses numbers	                        uses column names
# Range behavior	  end is excluded	                    end is included
# Errors	          raises error if index out of range	raises error if label does not exist

# iloc
print("\n",df.iloc[1])

# loc
print("\n",df.loc[1])

print("\n",df.iloc[0:2])    # first two rows

print("\n",df.iloc[0:10:2])

print("\n",df.iloc[:,2])    # Third(sale_year) column

print('\n',df.loc[:,"sale_year"])
print('\n',df.loc[:,["sale_year","sale_month"]])

print('\n',df.iloc[1,2])    # row 2, column 3

print('\n',df.iloc[0:10,0:5])

print('\n',df.loc[0:10,["brand","onroad_price","ex_showroom_price"]])

print('\n',df.iloc[[1,2,3,4],[4,14,15]])
print('\n',df.loc[[1,2,3,4],["brand","onroad_price","ex_showroom_price"]])


