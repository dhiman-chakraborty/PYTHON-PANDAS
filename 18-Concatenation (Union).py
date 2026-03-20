import pandas as pd

df1 = pd.DataFrame({'A' :[4,5],'B' :[11,23]})
df2 =pd.DataFrame({'A' :[4,6],'B' :[11,21]})

print(df1,'\n')
print(df2,'\n')

print(pd.concat([df1,df2]))    # UNION ALL (but does not remove duplicates by default)


df3 = pd.DataFrame({'A' :[4,5],'B' :[11,23],'C' :[21,26]})
df4 =pd.DataFrame({'A' :[6,5],'B' :[11,14]})

print(df3,'\n')
print(df4,'\n')

print(pd.concat([df3,df4]))

print(pd.concat([df1,df2]).drop_duplicates().reset_index(drop=True))


# Horizontal concatenation
print(pd.concat([df3,df4],axis=1))
print(pd.concat([df1,df2],axis=1))