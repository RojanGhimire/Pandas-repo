# filtering : keeping the rows that meet certain conditions
import pandas as pd

df = pd.read_csv("allpokemon.csv",index_col = "ID")

#filters pokemon with high stats above 650

strong_pokemon = df[df["Total"]>=650]
# print(strong_pokemon)

#filters pokemon with low stats below 200

weak_pokemon = df[df["Total"]<=200]
# print(weak_pokemon)


#filters any two types of pokemon in type 1 or in type 2 and vice versa


type1=input("enter type1:")
type2=input("enter type2:")
wf_pokemon = df[((df["Type1"]==f"{type1}")&(df["Type2"]==f"{type2}"))|(df["Type1"]==f"{type2}")&(df["Type2"]==f"{type1}")]
print(wf_pokemon)