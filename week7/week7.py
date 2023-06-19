
import pandas as pd
path = "week7_Customer-Churn-Records.csv"

df = pd.read_csv(path)

print(df.shape)

print(df.describe())

print(df.isnull().sum())


print(df['CustomerId'].nunique())

colsToDelete = ['RowNumber', 'CustomerId']
for c in colsToDelete:
    del df[c]


del df['Complain']
df['Gender'] = df['Gender'].map( {'Female': 1, 'Male': 0} )
# df['Geography'] = df['Geography'].map( {'F': 1, 'Male': 0} )
df = pd.get_dummies( df, columns = ['Geography'] )
print(df.columns)

print(df.corr()['Exited'])



for i in range(df['Age'].min(), df['Age'].max()):
    print(i, df[ df['Age'] == i ]['Exited'].mean())


for i in range(df['Age'].min(), df['Age'].max()):
    df['AgeGreater'] = df['Age'] > i

    print(i, df['AgeGreater'].corr(df['Exited']))


d = 'CreditScore'
import numpy as np
df['VAR1'] = np.sqrt(df[d])
df['VAR2'] = np.power(df[d], 2)
df['VAR3'] = np.log(df[d] + 1)
df['VAR4'] = df[d] > 42
df['VAR5'] = df[d] > df[d].mean()
print(d, df[d].corr(df['Exited']))
print("VAR1        ", df['VAR1'].corr(df['Exited']))
print("VAR2        ", df['VAR2'].corr(df['Exited']))
print("VAR3        ", df['VAR3'].corr(df['Exited']))
print("VAR4        ", df['VAR4'].corr(df['Exited']))
print("VAR5        ", df['VAR5'].corr(df['Exited']))


df['Balance'] = np.round(df['Balance'])
df['Balance'] = df['Balance'].astype(int)
df['BalanceLength'] = df['Balance'].astype(str)
df['BalanceLength'] = df['BalanceLength'].apply(lambda value: len(value))
# df['BalanceLength'] = df['BalanceLength'].apply(len)
df['Balance0'] = df['Balance'] > 0
print(df['Balance0'].corr(df['Exited']))
print(df['BalanceLength'].corr(df['Exited']))


