#aggregate functions =Reduces a set of values into a single summary value used to summarize and analyze data

import pandas as pd

df = pd.read_csv("allpokemon.csv",index_col="Name")

#this applies to whole dataframe

# print(df.min(numeric_only = True))
# print(df.max(numeric_only = True))
# print(df.count(numeric_only = True))
# print(df.mean(numeric_only = True))
# print(df.std(numeric_only = True))
# print(df.var(numeric_only = True))


#this applies to certain columns only

# print(df["Total"].min())
# print(df["Total"].max())
# print(df["Total"].count())
# print(df["Total"].mean())
# print(df["Total"].std())
# print(df["Total"].var())

#groupby functon
group1 = df.groupby("Type1")
df = group1["Total"].count()
print(df)


