import pandas as pd


df = pd.read_csv("allpokemon.csv",index_col = ["Name"])    #index_col can be used to set any column as index in the dataframe


#selection by column

# df = df[["Name", "Type1","Type2"]].to_string()   #selects columns in the dataframe

#selecton by row

print(df.loc["Treecko":("Turtwig"),["Type1","Type2","Generation","ID"]].to_string())  #USE LOC FUNCTION FOR SELECTION BY ROW
