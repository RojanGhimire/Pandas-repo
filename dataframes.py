import pandas as pd

#TOPIC : DataFrame
#data frames are used to list data in tabular form like in excel or google docs

data = {"pokemon":["bulbasaur","ivysaur","venasaur","squirtle","wartotle","blastoise"],"level":[12,23,40,5,18,37]}


df = pd.DataFrame(data,index = [1,2,3,4,5,6])

 #this is used to add columns in existing dataframe

df["nature"]=["shy","arrogant","introvert","extrovery","shy","playful"]  

 #this is used to add rows in existiong dataframe

new_row1 = pd.DataFrame([{"pokemon":"charizard","level":69,"nature":"pookie"}],index = [7])
df = pd.concat([df,new_row1])





print(df)
