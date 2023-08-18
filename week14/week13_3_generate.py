
import sys
import pandas as pd

df = pd.read_csv("Telecom_customer churn.csv")
df = df.select_dtypes(exclude = ['object'])
df = df.dropna()
del df['Customer_ID']

df0 = df[ df['churn'] == 0 ]
df1 = df[ df['churn'] == 1 ]

del df0['churn']
del df1['churn']

import numpy as np
from sklearn.decomposition import PCA
pca0 = PCA(n_components=1)
pca0.fit(df0)

pca1 = PCA(n_components=1)
pca1.fit(df1)

columns = list(df.columns)
import random
import numpy as np

def method0_purerandom(length):
    return [round(np.random.normal( df[columns[i]].mean(), df[columns[i]].std()), 2) for i in range(length)]

for _ in range(5):
    print(method0_purerandom( len(df.columns) ))


print(df.iloc[2].values)

print(df)



r = random.random() - 0.5
# random.random = [0, 1]
# -0.5, +0.5

asamplerow = list(df.iloc[2].values)
print(asamplerow)
asamplerow = [k + k * (random.random() - 0.5) for k in asamplerow]
print(asamplerow)



da = pd.DataFrame(columns = df.columns)
for _ in range(5):
    ind = random.randint(0, len(df[ df['churn'] == 1 ]) - 1)
    row = df[ df['churn'] == 1 ].iloc[ind]

    da.loc[ len(da) ] = row


print(da)
print(list(da.mean()))

print("=========================")
for x in range(10):
    print(x, df[ df['churn'] == 1 ].sample(n = 5).mean().values )



# 78'li space ==> 1'li PCA space projection
projected0 = pca0.transform(df0)


projected0 = projected0[:,0]
mn = np.min(projected0)
mx = np.max(projected0)

random_value = random.random() * (mx - mn) + mn


print(mn, mx, random_value)

generated_row = pca0.inverse_transform( [random_value] )
print("============")
print(generated_row)

cols = list(df0.columns)

for i in range(len(cols)):
    print(cols[i], "====>", generated_row[i])

