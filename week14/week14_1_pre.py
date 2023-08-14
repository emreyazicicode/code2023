
import pandas as pd
df = pd.read_csv("week14_1_processed.csv")


#! 
for t in df['Flight Distance'].unique():
    sub = df[ df['Flight Distance'] == t ]
    if len(sub) > 90:
        print(t, len(sub))

print(df['Flight Distance'].value_counts())
del df['Unnamed: 0']

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