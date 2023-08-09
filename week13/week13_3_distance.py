
import pandas as pd

df = pd.read_csv("Telecom_customer churn.csv")
df = df.select_dtypes(exclude = ['object'])
del df['Customer_ID']
del df['churn']
df = df.dropna()

import numpy as np
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca.fit(df)


print(pca.explained_variance_ratio_) # importance, weight, ratio
df_transformed = pca.transform(df)

print(df_transformed)
df_transformed = pd.DataFrame(df_transformed)
weights = [0.97500074,       0.01868536,      0.00330258]
r1 = [-4.77302450e+03,  1.56112090e+02,  7.79367142e+02]
r2 = [ 2.48879249e+04, -2.43939422e+03,  1.86773921e+03]

# weighted euclidean distance ==> mahalanobis distance

import random
p1 = random.randint(0, len(df_transformed) - 1)
p2 = random.randint(0, len(df_transformed) - 1)

r1 = df_transformed.iloc[ p1 ].values
r2 = df_transformed.iloc[ p2 ].values


diff= np.sqrt(weights[0]*(r1[0]-r2[0])*(r1[0]-r2[0]) + weights[1]*(r1[1]-r2[1])*(r1[1]-r2[1]) + weights[2]*(r1[2]-r2[2])*(r1[2]-r2[2]))

print(p1, p2)
print(r1, r2)
print(diff)