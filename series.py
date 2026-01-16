import pandas as pd

#series : a panda 1 dimensional array that can hold any type of data
#think of it as a single column spreadsheet

list = pd.Series(["charmander","charmeleon","charizard"],index=['a','b','c'])    #the index can also be selected in the series
list.loc['a']= "bulbasaur"     #loc locate function can be used to locate or print or change the contents of series in certain indexes

# print(list)

studyhour  = {"sunday":12,"monday":11,"tuesday":5,"wednesday":2}   #using dictionaries in series to show data connection
series = pd.Series(studyhour)    
# print(series.loc["monday"])
print(series[series >= 6])    



