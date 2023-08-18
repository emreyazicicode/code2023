
import pandas as pd
df = pd.read_csv("week14_1_processed.csv")


print(df['Flight Distance'].value_counts())

cols = ['Gender','Customer Type','Age','Type of Travel','Class']

sub = df[cols]
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(sub)
sub = scaler.transform(sub)
from sklearn.cluster import KMeans
sub = pd.DataFrame(sub)
print(sub)
print(sub.dtypes)
kmeans = KMeans(n_clusters=5).fit(sub)   
df['labels'] = kmeans.labels_

#! kmeans.cluster_centers_

da = df.groupby(by=['labels']).mean()
da.to_csv("week14_1_clusters.csv")

da = da.reset_index()
print(da)
da = dict( zip( da['labels'], da['satisfaction_v2'] ) )
print(da)

# {0: 0.7483260828447135, 1: 0.720628218661037, 2: 0.2113461898520876, 3: 0.2013494129522393, 4: 0.7256696931042245}
df['labels'] = df['labels'].map(da)

print(df['labels'].corr(df['satisfaction_v2']))


"""

import numpy as np

for r in [2, 5, 10, 15, 20, 25,30,60,90,120,180,240,360,480]:
    df['ft'] = df['Departure Delay in Minutes'] > r
    print(r, df['ft'].corr(df['satisfaction_v2']))





"""


# PCA
# LDA
# Flight Count
# Age

df = df.fillna(0)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
clf = LinearDiscriminantAnalysis()
clf.fit( df.drop(columns=['satisfaction_v2']), df['satisfaction_v2']  )
df['lda'] = clf.predict( df.drop(columns=['satisfaction_v2']) )
print(df['lda'].corr(df['satisfaction_v2']))

# PCA 
# LDA 
# Kmeans / DBScan
# Feature mining


import matplotlib.pyplot as plt

xs = []
ys = []

df['FlightRound'] = df['Flight Distance'].apply(lambda value: value) # round(value, -1)


for g in df.groupby(by=['FlightRound']):
    xs.append(g[0])
    ys.append(g[1]['satisfaction_v2'].mean())
plt.scatter( xs, ys )
plt.show()

df['A3'] = df['Age'].apply(lambda value: 1 if value > 39 and value < 61 else 0)

del df['Arrival Delay in Minutes']
del df['Departure Delay in Minutes']
del df['FlightRound']

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=5, random_state=0)
clf.fit( df.drop(columns=['satisfaction_v2']), df['satisfaction_v2']  )
cols = df.drop(columns=['satisfaction_v2']).columns


xs = []
ys = []
ts = []

da = pd.DataFrame(columns = ['index', 'col', 'fi', 'cor'])
for i in range(len(cols)):
    da.loc[len(da)] = [i, cols[i], clf.feature_importances_[i], abs(df[cols[i]].corr(df['satisfaction_v2']))]
    print(i, cols[i], clf.feature_importances_[i], df[cols[i]].corr(df['satisfaction_v2']))
    xs.append( clf.feature_importances_[i] )
    ys.append( abs(df[cols[i]].corr(df['satisfaction_v2'])) )
    ts.append( cols[i] )


fig, ax = plt.subplots()
ax.scatter(xs, ys)

for i in range(len(ts)):
    ax.annotate(ts[i], (xs[i], ys[i]))

plt.show()

da.to_csv("week14_1_out.csv")




# remove inter correlate
