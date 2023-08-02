
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
scaler=MinMaxScaler()

path = "week12_erzak.csv"
df = pd.read_csv(path)
dt = scaler.fit_transform(df)
f_col=df.columns
df=pd.DataFrame(dt,columns=f_col)

print(df)

from sklearn.cluster import DBSCAN

cols = list(df.columns)
cols.append('cluster')
cluster_list = pd.DataFrame(columns = cols)

#: RULE BASED APPROACH IS NOT APPRORIATE


#: Loop for each epsilon

for e in [0.1,0.3,0.5,0.7,0.9, 1, 1.4, 1.6, 1.8, 1.9, 2.0, 2.5]:
    #: Loop for each minimum samples
    for m in [2,3,4,5,6]:
        epsilon = e  # The maximum distance between two samples to be considered as neighbors
        min_samples = m  # The number of samples in a neighborhood for a point to be considered as a core point

        # Initialize and fit the DBSCAN model
        dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
        dbscan_clusters = dbscan.fit_predict( df )

        df['cluster'] = dbscan_clusters

        #: There should not be more than 0.05 anomaly
        if len(df[ df['cluster'] == -1]) < 0.05 * len(df):

            #: There should be more than 1 cluster
            if df['cluster'].nunique() > 1:
                
                #: There should be at least one cluster 
                vals = list(df['cluster'].unique())
                if len(vals) == 2 and -1 in vals:        # [0] anomalies 
                    pass
                else:
                    vc = df['cluster'].value_counts().to_dict() 
                    for c in vc: vc[c] = vc[c] / len(df)

                    if vc[0] < 0.80:
                        print("e=", e, "m=", m, "# unique", df['cluster'].nunique(), "# Anomalies", len(df[ df['cluster'] == -1]))
                        print(vc[0], np.mean(list(vc.values())))
                        
                        for q in df.groupby(by = ['cluster']):
                            #print(q[0], q[1].mean().to_dict())
                            cluster_list.loc[len(cluster_list)] = list(q[1].mean().to_dict().values())
                        
                        print("===================")



        del df['cluster']
        

            
cluster_list.to_csv("week12_2_output.csv")




