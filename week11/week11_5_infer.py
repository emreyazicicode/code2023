#: Imports
import pandas as pd
import datetime
import pickle
import json

#: Load the dataset
df = pd.read_csv("week11_5_out.csv")
df['DATE'] = pd.to_datetime(df['DATE'])
if 'Unnamed: 0' in df.columns:
    del df['Unnamed: 0']

# 1: Load the model file (pickle)
regr = None
file_path = 'week11_model.pickle'
with open(file_path, 'rb') as file:
    regr = pickle.load(file)

# 2: Load the config (m, n, last, max)
trend_info = None
with open('week11_trendinfo.json', 'r') as file:
    trend_info = json.load(file)

trend_info['maxdate'] = datetime.datetime.strptime(trend_info['maxdate'].replace(" 00:00:00", ""), "%Y-%m-%d")

def forecastInModel( LAG1, LAG2, LAG180, LAG365, MA3, MA5, MA7, MA30, MAP73, MX, MY ) -> float:
    return regr.predict([ [LAG1, LAG2, LAG180, LAG365, MA3, MA5, MA7, MA30, MAP73, MX, MY] ])[0]








def forecastTomorrow( ) -> float:
    # LAG1, LAG2, LAG180, LAG365, MA3, MA5, MA7, MA30, MAP73, MX, MY
    # ADD A NEW LINE TO DATAFRAME

    today = df['DATE'].max() + datetime.timedelta(1)

    l1 = df.iloc[-1]['DE-TREND']
    l2 = df.iloc[-2]['DE-TREND']
    l180 = df.iloc[-180]['DE-TREND']
    l365 = df.iloc[-365]['DE-TREND']

    #: Get the last 3 rows( and then, get  the mean)
    
    ma3 = df[-3:]['DE-TREND'].mean()
    ma5 = df[-5:]['DE-TREND'].mean()
    ma7 = df[-7:]['DE-TREND'].mean()
    ma30 = df[-30:]['DE-TREND'].mean()

    map73 = (df[-10:]['DE-TREND'].sum() - df[-3:]['DE-TREND'].sum()) / 7.0
    mx = today.month in [11,12,1,2]
    my = today.month in [6,7,8,9]
    detrend = None
    date = today
    #: Calculate the trend
    #! WARNING
    trend = trend_info['m'] * (trend_info['last'] + 1) + trend_info['n']
    #: ADD A NEW LINE TO DATAFRAME
    df.loc[ len(df) ] = [ l1, l2, l180, l365, ma3, ma5, ma7, ma30, map73,mx,my,detrend,date ]
    X = df.drop( columns = ['DE-TREND', 'DATE'])
    output = regr.predict( [ X.iloc[-1].values ] )
    output = output[ 0 ]
    #: Add the trend 
    output = output + trend
    #: Return
    return output


print(forecastTomorrow())


# what is the LAG1 of today, ==> yesterday
# what is the LAG1 of 6 days later ==> 5 days later 