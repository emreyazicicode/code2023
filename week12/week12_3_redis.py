
import redis
import json

REDIS = redis.Redis(host='localhost')

print( json.loads( REDIS.get('15647311').decode() ) )


"""
import pandas as pd

df = pd.read_csv("week7_Customer-Churn-Records.csv")

print(df)




for i in range(len(df)):
    row = df.iloc[i].to_dict()
    cid = row['CustomerId']
    REDIS.set( cid, json.dumps(row) )

# REDIS = dictionary [key, value]
"""