
#: Imports
import pickle
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import sys
import json

#: Declare general variables
scaler = MinMaxScaler()
target = 'price'

#: Load the dataframe
df = pd.read_csv("week12_data.csv")

#: Remove some columns
del df['street']
del df['country']
del df['date']

#: Convert the categorical variables
city = df.groupby(by = ['city'])[target].mean().to_dict()
statezip = df.groupby(by = ['statezip'])[target].mean().to_dict()
#df['city_value'] = df['city'].map(city)
df['statezip_value'] = df['statezip'].map(statezip)
del df['statezip']
del df['city']

#: Save the state zip values
with open('week12_5_statezip.json', 'w') as outfile:
    json.dump(statezip, outfile)

#: Scale the dataset
values = df[target]
del df[target]

scaler.fit(df)
columns = df.columns
df = scaler.transform(df)

df = pd.DataFrame(data = df, columns = columns)
df[target] = values

#: Filter the data
df = df[ df['price'] >= 100000 ]
df = df[ df['price'] <= 5000000 ]

#: Dump the scaler into a pickle file
file = open('week12_5_scaler.pickle', 'wb')
pickle.dump(scaler, file)
file.close()

#: Shuffle and split
df = df.sample(frac = 1.0)
count = int(len(df) * 0.7)
train = df[:count]
test = df[count:]

train_y = train[target]
train_x = train.drop(columns = target)

test_y = test[target]
test_x = test.drop(columns = target)

#: Create the model
regr = RandomForestRegressor(max_depth=6, random_state=0)
regr.fit(  train_x, train_y )
print(regr.score( train_x, train_y ))
print(regr.score( test_x, test_y ))

print(train_x.columns)

#: Dump the model into a pickle file
file = open('week12_5_model.pickle', 'wb')
pickle.dump(regr, file)
file.close()
