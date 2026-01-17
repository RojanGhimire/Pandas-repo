import pandas as pd

student_dict = {"name":["rojan","sangam","kritika","sunita","ram"],"roll no":[1,5,10,12,15]}
df = pd.DataFrame(student_dict,index = [1,2,3,4,5])
# print(df.loc[3])

#add column
df["class"] = [11,12,11,12,12]

#add rows
rows = pd.DataFrame([{"name":"shyam","roll no":69,"class":12},
                     {"name":"angelico","roll no":70,"class":11}],index = [6,7])

df = pd.concat([df,rows])  #connecting or joining tyo dataframes using concat.


print(df)