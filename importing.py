import pandas as pd 

#to read data out of csv file

df = pd.read_csv("allpokemon.csv")
print(df.to_string())

#to read data out of json file

df2 = pd.read_json("allpokemon.json")
# print(df2.to_string())         #this prints all data at once all of it
