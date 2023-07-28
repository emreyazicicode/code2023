import datetime
import json
import sys
import numpy as np
import pandas as pd
df = pd.read_csv("city_temperature.csv")


df=df[df['City']=='Charleston']
df=df[df['State']=='South Carolina']

# NO BEHAVIOUR!!!
# SO THAT, LAG 7 WILL NOT BE IMPORTANT

df = df[ ['Month',  'Day','Year','AvgTemperature'] ]

#: Replace -99.0 with none, it is like they are empty!
df = df.replace(-99.0, None)
df['AvgTemperature'] = (df['AvgTemperature'] - 32) / 1.8  # celcius!!!!
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




"""
x = df.dropna()['AvgTemperature'].values
a,b = linreg(range(len(x)),x) 
df['INDEX'] = range(len(df))
df['TREND'] = df['INDEX'] * 0.00011443240554451695 + 18.31045477916251
df['DE-TREND'] = df['AvgTemperature'] - df['TREND']
print(df)
"""

"""
# Alternative approach
# If empty, put the average of the month
df['Month'] = df['Date'].dt.month
avgs = {}
for g in df.groupby(by = ['Month']):
    avgs[ g[0] ] = g[1]['AvgTemperature'].mean()

df['AvgTemperature'] = df.apply(lambda row: 
                                row['AvgTemperature']
                                 if row['AvgTemperature'] != None 
                                 else avgs[ row['Month'] ] , axis = 1)
"""

df = df.bfill() # 25 tane, cok onemli degil!  BACK FILL, REPLACE THE NONE VALUE WITH PREVIOUS

# Alternative
# MEAN FILL
# fill the empties with mean
# df['AvgTemperature'] = df['AvgTemperature'].fillna( df['AvgTemperature'].mean() )

x = df.dropna()['AvgTemperature'].values
m,n= linreg(range(len(x)),x) 
df['x'] = range(len(df))# create an index
df['TREND'] = df['x'] * m + n
df['DE-TREND'] = df['AvgTemperature'] - df['TREND']


print(df)

for i in [1,2,3,4,5,6,7,10,14,28,30,31,60,180,360,365,366]:
    print( i, df['DE-TREND'].autocorr(i) )
    #print( i, df['DE-TREND'].shift(i).corr( df['DE-TREND'] ) )
    

for i in [1,2,180,365]:
    df[f'LAG{i}'] = df['DE-TREND'].shift(i)



# MOVING AVERAGE N days before for M days
# ROLLING = MA = (last r days)

for r in [3, 5, 7, 30]:
    df[f'MA{r}'] = df['DE-TREND'].rolling(r).mean()
    print("MA", r, df[f'MA{r}'].corr(df['DE-TREND']))


# ROLLING = MAP = (last r days, before r2 days)
"""
for r in [3, 5, 7, 30]:
    for r2 in [3, 5, 7, 30]:
        df[f'MAP{r}-{r2}'] = \
        (df['DE-TREND'].rolling(r+r2).sum() - df['DE-TREND'].rolling(r2).sum()) / (r)

print(df)
"""
df['MAP7-3'] = (df['DE-TREND'].rolling(10).sum() - df['DE-TREND'].rolling(3).sum()) / (7)
df = df.dropna()

TREND = df['TREND']

del df['TREND']
del df['x']
del df['AvgTemperature']

df['Month'] = df['Date'].dt.month

df['M-X'] = df['Month'].isin([11,12,1,2])
df['M-Y'] = df['Month'].isin([6,7,8,9])

trend_info = {'m':m, 'n':n, 'last': len(df), 
              'maxdate': str(df['Date'].max()), 
              'mindate': str(df['Date'].min()) }

#! df = pd.get_dummies(df, columns = ['Month'])
del df['Month']

date = df['Date']
del df['Date']


y = df['DE-TREND']
X = df.drop(columns=['DE-TREND'])

from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=5)
regr.fit(X, y)

print( regr.score(X, y) )


import pickle # pickle module, can save in binary mode!!
dbfile = open('week11_model.pickle', 'wb')
pickle.dump(regr, dbfile)
dbfile.close()


TREND.to_csv("week11_TREND.csv")


def save_dict_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Save the dictionary to JSON file
save_dict_to_json(trend_info, 'week11_trendinfo.json')

# TRAIN IS COMPLETED


print(X.columns)


X['DE-TREND'] = y
X['DATE'] = date
X.to_csv("week11_5_out.csv")

