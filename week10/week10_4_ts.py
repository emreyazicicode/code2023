
import pandas as pd
path = "week10_raw_sales.csv"
df = pd.read_csv(path)

# ===================================
# TRANSFORMATION PHASE
# ===================================
df = df.sort_values(by = ['datesold'])

keyvalue = {}

for g in df.groupby(by = ['datesold']):
    keyvalue[ g[0].replace(' 00:00:00', '') ] = len(g[1])

print(keyvalue)

keyvalue2 = df["datesold"].value_counts().to_dict()
print(keyvalue2)

# MISSING DATE PROBLEM, HOW TO SOLVE?
# date ozunden ve sonrakindan 1 gun farkli deyilse sart verelim
# 
# 
# df['datesold'].shift( 1 )  - df['datesold'] > 1 ===> PROBLEM

# baslangic tarihden search yapsin date olaraq ev satisi yoksaa 0 yazsin

# DATE RANGE!!

df['datesold'] = pd.to_datetime( df['datesold'] )
print(df['datesold'].dtype)
print(df['datesold'].min())
print(df['datesold'].max())
td = df['datesold'].max() - df['datesold'].min()
print(type(td), td, td.days, type(td.days))

ts = pd.DataFrame( columns = ['date', 'count'] )

import datetime
for single_date in (df['datesold'].min() + datetime.timedelta(n) for n in range(td.days)):
    s = str(single_date)
    n = keyvalue2[s] if s in keyvalue2 else 0 
    #print(single_date, '===>', n)
    ts.loc[ len(ts) ] = [single_date, n] # INSERT IS COSTLY

# ====================================
# FINALLY WE GOT A TIME SERIES DATASET
# ====================================
avg = ts['count'].mean()
ts['count'] = ts['count'] - avg
ts['Index'] = range(len(ts))
ts['WeekDayIndex'] = ts['Index'] % 7

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

values = ts['count']
m,n = linreg(range(len(values)), values) 


for ac in [1,2,3,4,5,6,7,14,30,60,90]:
    print(ac, ts['count'].autocorr(ac))

# Get the averages of each "WEEKDAY"
weekdayavg = {}
for g in ts.groupby(by = ['WeekDayIndex']):
    weekdayavg[ g[0] ] = g[1]['count'].mean()

ts['WeekDayAvg'] = ts['WeekDayIndex'].map( weekdayavg )

ts['Remaining1'] = ts['count'] - ts['WeekDayAvg']
ts.to_csv("week10_4_output.csv")

print(ts)
