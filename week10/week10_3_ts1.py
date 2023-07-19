

import pandas as pd
df = pd.read_csv("week10_3_sample1.csv")
y = df['target']
del df['target']

X = df

from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))

# SINGLE DIMENSION DATA
# ENRICHMENT


#* FEATURE 1: AutoCorr
# AutoCorr ! (N Days Before)
# 1 days before
# 2 days before
# 3 days before
# 4 days before
# 7, 15, 30, 60 (day)  DAY
# 6,12,24,48 (hour)    HOUR
# 3, 6, 12 (month)     

# 12/12/2020 # gunluk!!!
# 2020,  12
# 12/12/2022 05:56 # minute --> hourly


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



original = pd.read_excel("week10_tsdata_original.xlsx")
original['Index'] = range(len(original))
original['WeekDayIndex'] = original['Index'] % 7
print(original.shape)
# KNOWHOW


# WE DO NOT LIKE INTRA CORRELATIONS
# KISS = Keep it simple stupid
# SMILE = Simple makes it lots easier
# Keep it simple, as simple as possible, but not simpler (Einstein)

original = original.dropna()

values = original['Value']

m,n = linreg(range(len(values)), values) 
print(m,n)
# y = mx + n

original['Trend'] = m * original['Index'] + n
original['DeTrend'] = original['Value'] - original['Trend']

print(original)

import matplotlib.pyplot as plt


for i in [1,2,3,4,5,6,7,14,15,30]:
    original[f'{i}DB'] = original['DeTrend'].shift(i)
    

#plt.plot(original['Value'])
#plt.plot(original['Trend'])


for i in [1,2,3,4,5,6,7,14,15,30]:
    print(i, original['DeTrend'].autocorr(i))  # SAME AS original[f'{i}DB'].corr(original['DeTrend'])



weekly = {}
for g in original.groupby(by = ['WeekDayIndex']):
    weekly[g[0]] = g[1]['DeTrend'].mean()

print(weekly)



original['WeeklyAvg'] = original[ 'WeekDayIndex' ].map( weekly )

print(original)

"""
                TODAY YEST
0   2018-02-01   4321 NaN
1   2018-02-02   3491 4321
2   2018-02-03   2794 3491
3   2018-02-04   2794 3491
4   2018-02-05   3716
..         ...    ...
874 2020-10-04   1263
875 2020-10-05   2398
876 2020-10-06   2262
877 2020-10-07   2726
878 2020-10-08   2182



Age Gender ..... 
NAN 
"""