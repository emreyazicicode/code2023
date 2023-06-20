import numpy as np
import pandas as pd
path = "week7_Sales Transaction v.4a.csv"
#: Load the file
#* df = pd.read_csv(path, nrows=100000)
df = pd.read_csv(path)

print(df['Quantity'].describe())

print(df['Quantity'].value_counts())

print( df[ df['Quantity'] < 0 ] )


# -80995
print(df[ df['Quantity'] == 80995 ])

#: We do reject the negative ones, we are only interested in sales, not returns
df = df[ df['Quantity'] > 0 ]

def convert(value):
    return int(value)

#: Customer no seen as float, we do convert it into numeric
#! df['CustomerNo'] = df['CustomerNo'].apply(convert)
#! df['CustomerNo'] = df['CustomerNo'].astype(int)
df['CustomerNo'] = df['CustomerNo'].astype(str)

#: Create a dashboard statistics
dashboard = {
    'avg.basket.size': 0,
    'avg.basket.kiymet': 0,
    'avg.basket.count': 0,
}


dashboard['avg.basket.size'] = len(df) / df['TransactionNo'].nunique()
dashboard['avg.basket.count'] = df['Quantity'].sum() / df['TransactionNo'].nunique()
df['Kiymet'] = df['Price'] * df['Quantity']
dashboard['avg.basket.kiymet'] = df['Kiymet'].sum() / df['TransactionNo'].nunique() 


transactions = []
for g in df.groupby(by = ['CustomerNo']):
    transactions.append( g[1]['TransactionNo'].nunique() )
print(np.mean(transactions))


# group by date


print(dashboard)
