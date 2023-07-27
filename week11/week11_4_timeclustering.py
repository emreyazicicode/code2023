import numpy as np
import pandas as pd
df = pd.read_excel("week10_tsdata_original.xlsx")


print(df)


# 7 
for i in [2,3,4,5,6,7,8,9,10]:
    print(i, df['Value'].autocorr(i))

# 7 days

values = df['Value'].values

cluster_data = []
import matplotlib.pyplot as plt
import random
for i in range(len(values) - 7):
    sub = list(values[i:i+7])
    sub = [round(q/np.mean(sub),2) for q in sub]
    cluster_data.append( sub )

print(len(cluster_data))
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=10, random_state=0).fit( np.array(cluster_data) )
for c in kmeans.cluster_centers_:
    plt.plot(c)
    plt.show()

