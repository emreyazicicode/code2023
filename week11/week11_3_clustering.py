import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("segmentation data.csv")



for c in df:
    df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min()) # 1 0 arasi scale ettik
del df['ID']

print(df)
print(df.dtypes)

# TRAIN TEST YOK
# X, Y YOK [target, input]




#{'Sex': 1.0, 'Marital status': 1.0, 'Age': 0.28, 'Education': 0.44, 'Income': 0.37, 'Occupation': 0.59, 'Settlement size': 0.68, 'Label': 0.0}
#{'Sex': 0.0, 'Marital status': 1.0, 'Age': 0.28, 'Education': 0.42, 'Income': 0.32, 'Occupation': 0.47, 'Settlement size': 0.46, 'Label': 1.0}

"""
def difference( first, second ):
    total_diff = 0

    for c in first:
        total_diff += abs(first[c] - second[c])

    return float(total_diff) / len(first)


for k in [2,3,4,5,6]:
    print(f"K == {k}")
    # random forest, tree count = 1000
    kmeans = KMeans(n_clusters=k).fit(df) # the algo divided the data into clusters
    labels = kmeans.labels_ # LABELS ARE THE PREDICTED CLUSTER RESULTS

    df['Label'] = labels

    stds = []
    means_group = []
    for g in df.groupby(by = ['Label']):
        mean = g[1].mean().to_dict()
        mean = {k:round(v,2) for k,v in mean.items()}

        del mean['Label']

        std = g[1].std().to_dict()
        std = {k:round(v,2) for k,v in std.items()}

        del std['Label']

        std_mean = np.mean(list(std.values()))
        stds.append( std_mean )

        print(mean)


    print(f"For k={k}, the average std is {np.mean(stds)}")
    print("=======================")


"""


for k in [2,3,4,5,6,7,8,9,10]:
    #: Cluster
    kmeans = KMeans(n_clusters=k).fit(df) # the algo divided the data into clusters
    df['Label'] = kmeans.labels_



    general_stds = []

    means = []

    for i in range(k):
        cluster_data = df[ df['Label'] == i ]
        del cluster_data['Label']

        avgofdata = cluster_data.mean().to_dict()
        stdofdata = cluster_data.std().to_dict()

        avgofdata = {k:round(v,2) for k,v in avgofdata.items()}
        stdofdata = {k:round(v,2) for k,v in stdofdata.items()}

        stdofdata = np.mean(list(stdofdata.values()))
        means.append( list(avgofdata.values()) )
        general_stds.append(stdofdata)


    general_means = []

    for i1 in range(len(means)):
        for i2 in range(len(means)):
            if i1 < i2: #???
                general_means.append(np.mean(np.abs(np.array(means[i1]) - np.array(means[i2]))))


    print(f"for K = {k}, CRITERIA", np.mean(general_means)  / np.mean(general_stds) )

