
import pandas as pd

df = pd.read_csv("Telecom_customer churn.csv")
df = df.select_dtypes(exclude = ['object'])
del df['Customer_ID']
del df['churn']
df = df.dropna()


print(df.mean())


import numpy as np
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(df)

import matplotlib.pyplot as plt

# how much a component CAN EXPLAIN the ratio of the data

df.corr().to_csv("week13_corr.csv")
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.cumsum()) # cumulative sum
# THERE ARE HIGHLY CORRELATED COLUMNS IN DATA

projected = pca.transform(df)
plt.scatter( projected[:,0], projected[:,1] )
plt.show()
import math

for i in range(len(projected)):
    anomaly_score = math.sqrt( pow(projected[i][0] - 0, 2.0) + pow(projected[i][1] - 0, 2.0) )
    if anomaly_score > 100000:
        print(projected[i], anomaly_score)
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
8- Distance (!)
9- Clustering
10- how complex the dataset is
11- centroid distance

"""