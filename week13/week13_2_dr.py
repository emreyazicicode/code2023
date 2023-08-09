
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
pca0 = PCA(n_components=2)
pca0.fit(df0)

pca1 = PCA(n_components=2)
pca1.fit(df1)

import matplotlib.pyplot as plt

# how much a component CAN EXPLAIN the ratio of the data
"""
df.corr().to_csv("week13_corr.csv")
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.cumsum()) # cumulative sum
# THERE ARE HIGHLY CORRELATED COLUMNS IN DATA
"""

projected0 = pca0.transform(df0)
projected1 = pca1.transform(df1)
plt.scatter( projected0[:,0], projected0[:,1] )
plt.show()

plt.scatter( projected1[:,0], projected1[:,1] )
plt.show()


m0 = pca0.transform(df0)[:,0]
m1 = pca1.transform(df0)[:,0]
df0['SELF'] = m0
df0['OTHER'] = m1

df0['SELF'] = np.sqrt(df0['SELF'] * df0['SELF'])
df0['OTHER'] = np.sqrt(df0['OTHER'] * df0['OTHER'])

m0 = pca0.transform(df1)[:,0]
m1 = pca1.transform(df1)[:,0]
df1['SELF'] = m1
df1['OTHER'] = m0

df1['OTHER'] = np.sqrt(df1['OTHER'] * df1['OTHER'])
df1['SELF'] = np.sqrt(df1['SELF'] * df1['SELF'])

print(df0)
print(df1)


print(df0.mean())
print(df1.mean())



dfmain = pd.concat( [df0, df1] )


import math
"""
for i in range(len(projected)):
    anomaly_score = math.sqrt( pow(projected[i][0] - 0, 2.0) + pow(projected[i][1] - 0, 2.0) )
    if anomaly_score > 100000:
        print(projected[i], anomaly_score)
"""
#print(df.shape)
#print(df.corr())

# PROBLEM(WARNING): PCA only explains THE linear correlation / relationships!!

"""
1- ok
2- ok
3- ?
4- ok
5- -
6- Generate new (realistic) data!!
7- ok
8- ok
9- ok
10- ok
11- ok

"""