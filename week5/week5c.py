
import sys
import pandas as pd

#: Read the csv file and assign to to a "df" dataframe (note, only read 10000 rows)
#: Read the file at the beginning, it will be loaded into memory
df = pd.read_csv("Telecom_customer churn.csv", nrows = 100000)

print(df['Customer_ID'].dtype)

#: astype(typename) => converts [[ str --> object ]]
df['Customer_ID'] = df['Customer_ID'].astype(str)
# We overwrite the original one

# Select only those type of columns
df2 = df.select_dtypes(exclude = ['object'])
print(df2.columns)


df3 = df.select_dtypes(include = ['object'])
df3.to_csv("week5_categoriconly.csv")

"""
df = df.replace('Y', 1)  # Yes
df = df.replace('N', 0)  # No
df = df.replace('O', 1)  # Owner  # manually assigned
df = df.replace('R', 0)  # Rent

df = df.replace('S', 0)  # Small
df = df.replace('M', 1)  # Medium
"""
df = df.replace('U', 0) # NOT ALWAYS A CORRECT WAY
df = df.replace('Y', 1)
df = df.replace('N', 0)


"""
for c in ['creditcd', 'asl_flag', 'kid0_2', 'kid3_5']:
    df[c] = df[c].replace('Y', 1)
    df[c] = df[c].replace('N', 0)
"""

for c in df3:
    n = df[c].nunique()
    if n == 2:
        print("FLAG", c, n, df[ df[c].notnull() ][c].unique())
    elif n < 10:
        print("CATEGORIC", c, n, df[ df[c].notnull() ][c].unique())
    else:
        print("CATEGORIC", c, n)


# PROBLEM: HOW CAN I USE !!!!! categorical variables
# No mathematical operation can be applied to them, so what?


"""
CATEGORIC new_cell 3 ['U' 0 1]
CATEGORIC crclscod 41
FLAG asl_flag 2 [0 1]
CATEGORIC prizm_social_one 4 [0 'U' 'T' 'C' nan]
CATEGORIC area 18
CATEGORIC dualband 4 [1 0 'T' 'U']
CATEGORIC refurb_new 1 [0]
CATEGORIC hnd_webcap 3 ['WCMB' 'WC' nan 'UNKW']
FLAG ownrent 2 [ 1. nan  0.]
FLAG dwlltype 2 [ 0.  1. nan]
CATEGORIC marital 5 [0 1 'A' 'U' 'B' nan]
CATEGORIC infobase 1 [ 1. nan]
CATEGORIC HHstatin 6 ['C' 'I' nan 'B' 'A' 'G' 'H']
CATEGORIC dwllsize 14
CATEGORIC ethnic 13
FLAG kid0_2 2 ['U' 1 nan]
FLAG kid3_5 2 ['U' 1 nan]
FLAG kid6_10 2 ['U' 1 nan]
FLAG kid11_15 2 ['U' 1 nan]
FLAG kid16_17 2 ['U' 1 nan]
FLAG creditcd 2 [ 1.  0. nan]
CATEGORIC Customer_ID 10000

"""








