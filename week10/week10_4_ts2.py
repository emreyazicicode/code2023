import numpy as np
path = "week10_MLTollsStackOverflow.csv"
import pandas as pd
df = pd.read_csv(path)



def linreg(X, Y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det



print( df['r'] )


df['r-LAG1'] = df['r'].shift(1)
df['r-MA3'] = df['r'].rolling(3).mean()

columns = [c for c in df.columns if c.startswith('r-') or c == 'r']

rdf = df[ columns ] 
rdf = rdf.dropna()


rdf['Index'] = range(len(rdf))
values = rdf['r']
m,n = linreg(range(len(values)), values) 
rdf['r-Trend'] = m * rdf['Index'] + n
del rdf['Index']

print(rdf.corr())
print( np.mean(rdf.corr().mean()))



ndf = df[ ['month', 'numpy'] ]
ndf['before2011'] = ndf['month'].contains("09") | ndf['month'].contains("10")


