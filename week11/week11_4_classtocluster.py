from sklearn.cluster import KMeans
import pandas as pd
df = pd.read_csv("Telecom_customer churn.csv")
df = df.fillna(0)
df = df.sample(frac = 0.50)

df = df.select_dtypes(exclude=['object'])
del df['Customer_ID']
target = 'churn'

X = df.drop(columns=[target]) # Remove the target for now
kmeans = KMeans(n_clusters=50, random_state=0).fit(X)

X['Labels'] = kmeans.labels_ # Assign the cluster label
X[target] = df[target] # Assign the target

print(X)

for c in X.groupby(by = ['Labels']):
    print(c[0], c[1][target].mean())


