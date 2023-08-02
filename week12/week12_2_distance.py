
import sys
import distance

from euclidean.R2 import V2

print( V2(0, 1).cross(V2(1, 1)) )

print(dir(distance))

from md5hash import scan
print(scan('week12_2.py'))


sys.exit(1)


import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
scaler=MinMaxScaler()

path = "week12_erzak.csv"
df = pd.read_csv(path)
dt = scaler.fit_transform(df)
f_col=df.columns
df=pd.DataFrame(dt,columns=f_col)

import math

def euclidean( r1, r2 ) -> float:
    s = 0
    for i in range(len(r1)):
        s += math.pow(r1[i] - r2[i],2)
    return math.sqrt(s)


for i0 in range(len(df)):
    minvalue = 10000000
    minindex = 0
    for i1 in range(len(df)):
        if i0 != i1:
            r0 = df.iloc[i0]
            r1 = df.iloc[i1]

            r0 = list(r0.values)
            r1 = list(r1.values)

            dis = euclidean(r0, r1)
            if dis < minvalue:
                minvalue = dis
                minindex = i1


    
    print(i0, minindex, minvalue)
