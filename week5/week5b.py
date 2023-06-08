
import sys
import pandas as pd

#: Read the csv file and assign to to a "df" dataframe (note, only read 10000 rows)
#: Read the file at the beginning, it will be loaded into memory
df = pd.read_csv("Telecom_customer churn.csv", nrows = 10000)
#! df2 = pd.read_excel("week5_HotelCustomersDataset.xlsx")


# version: 1.0
def createInformationTable( df: pd.DataFrame ) -> pd.DataFrame:
    #: Prepare table
    infoTable = df.describe() # Get the description of the table
    infoTable = infoTable.T # Get the transpose version
    infoTable['name'] = infoTable.index
    #! infoTable['skew'] = df['rev_Mean'].skew() # Add a new column to infoTable, set its value to None
    infoTable['skew'] = df.skew() # Add a new column to infoTable, set its value to None
    infoTable['kurt'] = df.kurt() # Add a new column to infoTable, set its value to None
    infoTable['iqr'] = infoTable['75%'] - infoTable['25%']
    infoTable['upper'] = infoTable['75%'] + infoTable['iqr'] * 1.5
    infoTable['lower'] = infoTable['25%'] - infoTable['iqr'] * 1.5
    infoTable['upper2'] = infoTable['mean'] + 3 * infoTable['std']
    infoTable['lower2'] = infoTable['mean'] - 3 * infoTable['std']
    #: Return
    return infoTable



# PANDAS: the importance of brackets --> []
# Usage 1:
# if we use a string to read inside brackets
# df["rev_Mean"], it means, select the "column", 
# it is like clicking and selecting the column in excel
# a = df['rev_Mean']
# Usage 2:
# If we use a string, and the name of the column not exists
# df['emre']
# It creates the column!!
# To create a new column, we just use "string" and assign it to something
# Usage 3:
# If we use a list of string!, it selects the columns



# Columns likely to be deleted:
# Mostly null, high cardinality, not useful, wrong information, 
# low correlation(target), very high correlation(any)






# NOTE: if we assign a single value to a column, all values in the column will be same
# NOTE: if we assign a list of values to a column, it will be assigned accordingly

# How to substract a list from a list
# list - list = list (pairwise)


infoTable = createInformationTable( df )
infoTable.to_csv("week5_infotable.csv")
print(infoTable)

#: Accessing to a column
print( df['rev_Mean'] )
#: Calling a method
print( "df['rev_Mean'].skew()", df['rev_Mean'].skew() )
#: Calling a method of dataframe
print( "df.skew()", df.skew() )



a = [1,2,3]
b = [10,20,30]
# print(a+b) # Concat
# print(a+3) # Not supported


#: Make a comparison to a column will return a "true/false" list
print( df['rev_Mean'] > 30 )
# df['rev_Mean'] --> list, vector, series
# 30 --> single value
# [list] [op] [singlevalue]


print(df['rev_Mean'].mean())
#: A dynamic comparison
print( df['rev_Mean'] > df['rev_Mean'].mean() )


# creates a new column       [assigns the values of each row]    
df['is_greater_than_mean'] = df['totcalls'] > df['totcalls'].mean() * 1.5
df['how_much_grater_than_mean'] = df['totcalls'] - df['totcalls'].mean()
#                                 list of values -  only a single value  [element wise]
df['how_many_times_grater_than_mean'] = df['totcalls'] / df['totcalls'].mean()



df.to_csv("temp.csv")

print("a", df.shape)
df2 = df.drop(columns=['da_Mean', 'ovrrev_Mean']) # returns a NEW DATAFRAME
print("b", df.shape)
print("c", df2.shape)


columns = ['totmrc_Mean', 'da_Mean','ovrmou_Mean','ovrrev_Mean']
dx = df[ columns ]
dx.to_csv("week5_subselect.csv")


#: Removing a column
print("first",df.shape)
del df['Customer_ID']
print("second", df.shape)

#: Removing a list of columns
df = df.drop(columns=['da_Mean', 'ovrrev_Mean'])
#! exactly same, df.drop(columns=['da_Mean', 'ovrrev_Mean'], inplace=True)
# OVERWRITE to original one

print("third",df.shape)



print( df.head(30) )

# df.head   ---> returns a new dataframe
# df.drop
# .... 



df.head(30).to_csv("week5_30recordsonly.csv")
df.head(30).to_html("week5_30recordsonly.html")
df.head(30).to_json("week5_30recordsonly.json")
#! df.head(30).to_sql("week5_30recordsonly.sql")
df.head(30).to_pickle("week5_30recordsonly.pickle")

print(df.head(3).to_dict())


print(df.head(5)) # from the beginning
print(df.tail(5)) # from the end


# DATAFRAME FORMAT!!!
# NOT A LIKE REGULAR TEXT FILE
"""
with open('telecomsmall.csv') as file:
   df = file.read()
   print(df)
   print(type(df))
"""

print(type(pd.read_csv('telecomsmall.csv')))



#: Take 375 sample items
print( df.sample(n = 375) ) # not from top (head), not from bottom (tail), randomly SELECT
# 9516   40.3100    263.25  ...                 -3347.8945                         0.461051
# 2452   86.0600    902.50  ...                 12880.1055                         3.073459
# 1382   45.8600    600.00  ...                   585.1055                         1.094191



print( df.sample(frac = 0.25) ) # %50 tanesini

nof_items = int(len(df) * 0.25)
print(df.sample(n = nof_items))








# PANDAS: the importance of brackets --> []
# Usage 4:
# Most useful
# If we use a list of "bool" boolean, it filters data
"""
df[ 'rev_Mean' ] ==> selects the column
df['emre'] ==> creates a column
df[ ['rev_Mean', 'mou_Mean'] ] ==> selects the columns!
df[ [True, False, True] ] ==> Selects the first and last row (Trues only)
SQL: where
"""

print( df[ 'rev_Mean' ] > 60 )


true_false_list = df[ 'rev_Mean' ] > 60


print(df)
# [10000 rows x 100 columns]
print( df[ true_false_list ] ) # Shows only the rows with "True"
# [3398 rows x 100 columns]


print(list(true_false_list[0:20]))
# [False, False, False, False, False, True, False, False, True, False, True, False, True, False, True, False, True, False, False, False]
#                                     5.row               8.row        10.row


print( df[ true_false_list ] ) # Shows only the rows with "True"
# [3398 rows x 100 columns] # 3398 rows!!

"""
SELECT ..
FROM ...
WHERE rev_Mean > 60
"""



print( df[ df[ 'rev_Mean' ] > 60 ] ) # Shows only the rows with "True"


x = df[ df[ 'rev_Mean' ] > 60 ]
print( x[ ['rev_Mean', 'roam_Mean', 'datovr_Mean'] ] )


q = df[ df[ 'rev_Mean' ] > 60 ][ ['rev_Mean', 'roam_Mean', 'datovr_Mean'] ]
#       [only this column]       [ select only these columns                ]    
#       [condition           ]
#     [filter only these rows ]

"""
SELECT rev_Mean, roam_Mean, datovr_Mean
FROM TABLE 
WHERE rev_Mean > 60
"""




q = df[ (df[ 'rev_Mean' ] > 60) & (df['rev_Mean'] < 100) ]
"""
SELECT *
FROM TABLE 
WHERE rev_Mean > 60 AND rev_Mean < 100
"""

for c in df.columns:
    # out of concept
    if str(df.dtypes[c]) in ['int64', 'float64'] and c not in ['income', 'lor']:

        nof_uniuqe = df[c].nunique()

        if nof_uniuqe > 10: # if there are more than 10 different value
            q1 = df[ c ].quantile(0.25)
            q3 = df[ c ].quantile(0.75)
            iqr = q3 - q1
            upper = q3 + 1.5 * iqr
            lower = q1 - 1.5 * iqr

            mean = df[c].mean()
            std = df[c].std()
            upper2 = mean + 3 * std
            lower2 = mean - 3 * std
            
            dx = df[  (df[c] >= lower2) & (df[c] <= upper2)  ]
            print(c, 10000 - len(dx))

            #! df = df[  (df[c] >= lower2) & (df[c] <= upper2)  ]
            #! print(c, len(df))

# most of the data cannot be outlier!

# adults 1438
# income 1599
# numbcars 3970
# forgntvl 923


# NOTE: We may use tranformation functions (we will see them later), after we can eliminate 
#       outliers


#: Object olmayan tipteki kolonlari sec!
da = df.select_dtypes(exclude = ['object'])
print(da)










