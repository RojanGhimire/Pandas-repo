# i am gonna make a program to show data of a pokemon after name is entered

import pandas as pd

df = pd.read_csv("allpokemon.csv",index_col="Name")
name = input("enter a name of a pokemon : ")
df = df.loc[f"{name}"]

try:
    print(df)
except KeyError:
    print(f"{name} not found")