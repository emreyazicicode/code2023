import numpy as np
import pandas as pd
df = pd.read_csv("city_temperature.csv")

df=df[df['City']=='Charleston']
df=df[df['State']=='South Carolina']


df = df[ ['Month',  'Day','Year','AvgTemperature'] ]

df = df.replace(-99.0, None)
df['AvgTemperature'] = (df['AvgTemperature'] - 32) / 1.8
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df = df[ ['Date','AvgTemperature'] ]




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



x = df.dropna()['AvgTemperature'].values
a,b = linreg(range(len(x)),x) 

df['INDEX'] = range(len(df))

df['TREND'] = df['INDEX'] * 0.00011443240554451695 + 18.31045477916251

df['DE-TREND'] = df['AvgTemperature'] - df['TREND']
print(df)