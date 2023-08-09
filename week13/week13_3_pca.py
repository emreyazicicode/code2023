import sys
import pandas as pd
import re
path = "changed_03-01-2018.csv"
df = pd.read_csv(path, header=0) # 329291
df.columns = ['Dst Port','Protocol','Timestamp','Flow Duration','Tot Fwd Pkts','Tot Bwd Pkts','TotLen Fwd Pkts','TotLen Bwd Pkts','Fwd Pkt Len Max','Fwd Pkt Len Min','Fwd Pkt Len Mean','Fwd Pkt Len Std','Bwd Pkt Len Max','Bwd Pkt Len Min','Bwd Pkt Len Mean','Bwd Pkt Len Std','Flow Byts/s','Flow Pkts/s','Flow IAT Mean','Flow IAT Std','Flow IAT Max','Flow IAT Min','Fwd IAT Tot','Fwd IAT Mean','Fwd IAT Std','Fwd IAT Max','Fwd IAT Min','Bwd IAT Tot','Bwd IAT Mean','Bwd IAT Std','Bwd IAT Max','Bwd IAT Min','Fwd PSH Flags','Bwd PSH Flags','Fwd URG Flags','Bwd URG Flags','Fwd Header Len','Bwd Header Len','Fwd Pkts/s','Bwd Pkts/s','Pkt Len Min','Pkt Len Max','Pkt Len Mean','Pkt Len Std','Pkt Len Var','FIN Flag Cnt','SYN Flag Cnt','RST Flag Cnt','PSH Flag Cnt','ACK Flag Cnt','URG Flag Cnt','CWE Flag Count','ECE Flag Cnt','Down/Up Ratio','Pkt Size Avg','Fwd Seg Size Avg','Bwd Seg Size Avg','Fwd Byts/b Avg','Fwd Pkts/b Avg','Fwd Blk Rate Avg','Bwd Byts/b Avg','Bwd Pkts/b Avg','Bwd Blk Rate Avg','Subflow Fwd Pkts','Subflow Fwd Byts','Subflow Bwd Pkts','Subflow Bwd Byts','Init Fwd Win Byts','Init Bwd Win Byts','Fwd Act Data Pkts','Fwd Seg Size Min','Active Mean','Active Std','Active Max','Active Min','Idle Mean','Idle Std','Idle Max','Idle Min','Label']

TARGET = 'Label'

print(df.dtypes)

# {'Benign': 238036, 'Infilteration': 93063}
target_map = {'Benign': 0, 'Infilteration': 1}

df[TARGET] = df[TARGET].map(target_map)

print(df[TARGET].value_counts().to_dict())

print("SELECTING ONLY NUMERICS")

df = df.select_dtypes(exclude= ['object', 'datetime'])


print("NORMALIZING")
for c in df:
    df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())
df = df.fillna(df.mean())

print("FINDING CORRELATIONS")

low_corr = []
for c in df:
    cc = df[c].corr(df[TARGET])
    if abs(cc) < 0.10:
        low_corr.append(c)
    print(c, df[c].corr(df[TARGET]))

print("TRAINING PCA MODEL")

print("low_corr", low_corr)

import numpy as np
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
sub = df[ low_corr ]
pca.fit(sub)
sub = pca.transform(sub)
print(sub)

print(pca.explained_variance_)
df['PCA_c1'] = sub
print("FINAL VALUE", df['PCA_c1'].corr(df[TARGET]))



sys.exit(1)
def tryParse( values ):
    
    output = []
    for v in values:
        if re.match(r"^[0-9\,\.]+$", str(v)):
            output.append('num')
        else:
            output.append('str')
    return output

# Dst Port,Protocol,Timestamp,Flow Duration,Tot Fwd Pkts,Tot Bwd Pkts,TotLen Fwd Pkts,TotLen Bwd Pkts,Fwd Pkt Len Max,Fwd Pkt Len Min,Fwd Pkt Len Mean,Fwd Pkt Len Std,Bwd Pkt Len Max,Bwd Pkt Len Min,Bwd Pkt Len Mean,Bwd Pkt Len Std,Flow Byts/s,Flow Pkts/s,Flow IAT Mean,Flow IAT Std,Flow IAT Max,Flow IAT Min,Fwd IAT Tot,Fwd IAT Mean,Fwd IAT Std,Fwd IAT Max,Fwd IAT Min,Bwd IAT Tot,Bwd IAT Mean,Bwd IAT Std,Bwd IAT Max,Bwd IAT Min,Fwd PSH Flags,Bwd PSH Flags,Fwd URG Flags,Bwd URG Flags,Fwd Header Len,Bwd Header Len,Fwd Pkts/s,Bwd Pkts/s,Pkt Len Min,Pkt Len Max,Pkt Len Mean,Pkt Len Std,Pkt Len Var,FIN Flag Cnt,SYN Flag Cnt,RST Flag Cnt,PSH Flag Cnt,ACK Flag Cnt,URG Flag Cnt,CWE Flag Count,ECE Flag Cnt,Down/Up Ratio,Pkt Size Avg,Fwd Seg Size Avg,Bwd Seg Size Avg,Fwd Byts/b Avg,Fwd Pkts/b Avg,Fwd Blk Rate Avg,Bwd Byts/b Avg,Bwd Pkts/b Avg,Bwd Blk Rate Avg,Subflow Fwd Pkts,Subflow Fwd Byts,Subflow Bwd Pkts,Subflow Bwd Byts,Init Fwd Win Byts,Init Bwd Win Byts,Fwd Act Data Pkts,Fwd Seg Size Min,Active Mean,Active Std,Active Max,Active Min,Idle Mean,Idle Std,Idle Max,Idle Min,Label
# 331126
# 331100

""" 
for c in df:
    louv = list(df[c].unique()) # LIST OF UNIQUE VALUES
    output = tryParse(louv)
    output = list(set(output))
    print(c, output)
"""

for c in df:
    if c != 'Label':
        df = df[df[c].apply(lambda x: isinstance(x, str))]

print(df)


#df = df.select_dtypes(exclude= ['object', 'datetime'])
#print(df.dtypes)
#print(df)
sys.exit(1)
df = df.select_dtypes(exclude= ['object', 'datetime'])

TARGET = 'log_price'



low_corr = []
for c in df:
    cc = df[c].corr(df[TARGET])
    if abs(cc) < 0.10:
        low_corr.append(c)
        print(c, df[c].corr(df[TARGET]))

# INSTEAD OF REMOVING THOSE COLUMNS, GIVE IT A CHANCE

df = df.fillna(df.mean())

print(df)
for c in df:
    df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())


import numpy as np
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
sub = df[ low_corr ]
pca.fit(sub)
sub = pca.transform(sub)
print(sub)

df['PCA_c1'] = sub

print(df)


print(df['PCA_c1'].corr(df[TARGET]))

