
import numpy as np 
path = "week10_tsdata_original.xlsx"
import pandas as pd
df = pd.read_excel(path)

org = df.copy()
del org['Date']

"""
FIRST APPROACH
ONE DAY LATER
        Date  Value
0 2018-02-01   4321  
1 2018-02-02   3491  we can predict 3491 with 4321
2 2018-02-03   2794  we can predict 2794 with 3491
3 2018-02-04   1924
4 2018-02-05   3716
5 2018-02-06   3496
6 2018-02-07   3502 [TAHMIN], ===> sanki gercek gibi dusunup 
7 2018-02-08   3226
8 2018-02-09   3012
9 2018-02-10   2456


1924, 3716,3496 ==> 3505!(T)
1924, 3716,3496,3505!(T) ==> 3240!(T)
1924, 3716,3496,3505!(T),3240!(T),3000!(T)


"""

df['L1'] = df['Value'].shift(1)
df['L7'] = df['Value'].shift(7)
df['MA3'] = df['Value'].rolling(3).mean()
df['MA7'] = df['Value'].rolling(7).mean()

df = df.dropna()

y = df['Value']
del df['Value']
del df['Date']


from sklearn.linear_model import LinearRegression
# TRAIN !!!!!
reg = LinearRegression().fit(df, y)



# INFERENCE, RUN TIME, REAL TIME, RUNNING, PREDICTING, FORECASTING

predictdata = [ # LISTE
    [2182, 2308, 2390, 2142] # ==> ROW
] # matrix = array of array
predictdata = np.array(predictdata)

results = reg.predict( predictdata )
today = int(results[0]) # 0.94 accuracy
print(today)

org.loc[ len(org) ] = [ today ]
org['L1'] = org['Value'].shift(1)
org['L2'] = org['Value'].shift(7)
org['MA3'] = org['Value'].rolling(3).mean()
org['MA7'] = org['Value'].rolling(7).mean()


# sequence based, next (2nd) day forecasting
predictdata = [ # LISTE
    [org.tail(1)['L1'], org.tail(1)['L7'], org.tail(1)['MA3'], org.tail(1)['MA7']] # ==> ROW
] # matrix = array of array
predictdata = np.array(predictdata)



results = reg.predict( predictdata )
nextday = int(results[0]) # 0.94 accuracy
print(nextday)




def forecast( dataFrame, valueColumnName: str, nDaysLater: int = 3):
    pass

forecast( df, "Value", 3)










"""
SECOND APPROACH
N DAYS LATER
        Date  Value      L3      L4
0 2018-02-01   4321     NaN     NaN
1 2018-02-02   3491     NaN     NaN
2 2018-02-03   2794     NaN     NaN
3 2018-02-04   1924  4321.0     NaN
4 2018-02-05   3716  3491.0     NaN  <====== on this date
5 2018-02-06   3496  2794.0     NaN
6 2018-02-07   3502  1924.0     NaN
7 2018-02-08   3226  3716.0  4321.0  <====== we can predict this date
8 2018-02-09   3012  3496.0  3491.0
9 2018-02-10   2456  3502.0  2794.0
"""


