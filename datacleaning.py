# data cleaning :  it is the process of fixing removing , incomplete data, irrelevant data .
                    # ~75% of the work done with pandas is data cleaning .
import numpy as np
import pandas as pd

df = pd.read_csv("allpokemon.csv")
df = df.replace(" ",np.nan)         #this numpy function is used to replace empty strings with  NaN
#drop(columns = ["columns"])  can be used to delete or remove a whole column from a data frame

df = df.drop(columns = ["Defense","Sp. Def","Sp. Atk","Speed","HP","Attack"])



#dropna can be used to drop rows with no value in certain columns

# df = df.dropna(subset = ["Type2"])

#fillna can be used to fill values with NaN with some other value you want

df = df.fillna({"Type2":"None"})

#Replacement of data in the dataFrames

df["Type1"] = df["Type1"].replace({"Fire":"MKB Aaagg","Water":"Wet pussy", "Grass":"Zoro's Hair"})


#standardize strings in any columns fog eg make all of it lower case

df["Name"] = df["Name"].str.lower()
print(df)