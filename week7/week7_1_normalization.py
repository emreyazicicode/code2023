
import sys
import pandas as pd
path = "week7_Retail_Data_Transactions.csv"

#: Read the csv file
df = pd.read_csv(path)
print(df)
#: We want to group the items and get some information out of it
# NOTE: there are many ways to do


"""
for g in df.groupby(by=['customer_id']):
    transaction_amount[ g[0] ] = 0.0000000
    group_value = g[0]
    group_data = g[1]


listoftuple = [
    ('CS1112', pd.DataFrame),
    ('CS1113', pd.DataFrame),
    ('CS1114', pd.DataFrame),
]
"""

transaction_amount_mean = {}

#: Loop for each unique customer value
for g in df['customer_id'].unique():
    #: Get a subset of transactions for the user
    subset = df[ df['customer_id'] == g ]
    m = subset['tran_amount'].mean()
    #s = subset['tran_amount'].std()

    transaction_amount_mean[ g ] = m


print(transaction_amount_mean)


