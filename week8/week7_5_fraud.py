
import sys
import pandas as pd
"""
df1 = pd.read_csv("AZVotersList2016_part_1.csv", engine='c', error_bad_lines = False)
df1 = df1[['Name']]

df2 = pd.read_csv("AZVotersList2016_part_2.csv", engine='c', error_bad_lines = False)
df2 = df2[['Name']]

df3 = pd.read_csv("AZVotersList2016_part_3.csv", engine='c', error_bad_lines = False)
df3 = df3[['Name']]

df = pd.concat( [df1, df2, df3] )
df.to_csv("names.csv")
"""



da = pd.DataFrame(columns = ['father', 'name', 'surname'])
df = pd.read_csv("names.csv")
df = df.sample(n = 10000)

for i in range(10000):
    row = df.iloc[i]
    names = row['Name'].split(" ")
    if len(names) == 3:
        surname = names[0]
        name = names[1]
        father = names[2]

        #print("Father=", father, "Name=", name, "Surname=", surname)
        da.loc[ len(da) ] = [father, name, surname]

#da.drop_duplicates()
da.to_csv("week_7_names_split.csv")

for c in da.groupby(da.columns.tolist(),as_index=False):
    if len(c[1]) > 1:
        print(c[0], c[1])


# text = input("lutfen kisinin ismini giriniz")
