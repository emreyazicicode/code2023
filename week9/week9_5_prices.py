# Second hand, used car price estimation
target = 'Price'

import pandas as pd
import numpy as np
path = "week9_true_car_listings.csv"

df = pd.read_csv(path)
#! df = df.sample(n = 100000)

df['State'] = df['State'].str.strip()

df['CarAge'] = 2019 - df['Year']

df['State'] = df['State'].str.upper()
df['City'] = df['City'].str.upper()
df['Make'] = df['Make'].str.upper()
df['Model'] = df['Model'].str.upper()


df['Mileage_2'] = np.sqrt( df['Mileage'] )

print(df['Mileage'].corr(df[target]))
print(df['Mileage_2'].corr(df[target]))
print(df['CarAge'].corr(df[target]))


for c in ['City','State','Make','Model']:
    print(c, df[c].nunique())

"""
import json
import urllib
import requests

car_brands = ['Car_Model_List_Acura','Car_Model_List_Alfa_Romeo','Car_Model_List_Aston_Martin','Car_Model_List_Audi','Car_Model_List_Bentley','Car_Model_List_BMW','Car_Model_List_Buick','Car_Model_List_Cadillac','Car_Model_List_Chevrolet','Car_Model_List_Chrysler','Car_Model_List_Daewoo','Car_Model_List_Daihatsu','Car_Model_List_Dodge','Car_Model_List_Eagle','Car_Model_List_Ferrari','Car_Model_List_Fiat','Car_Model_List_Fisker','Car_Model_List_Ford','Car_Model_List_Freightliner','Car_Model_List_Genesis','Car_Model_List_Geo','Car_Model_List_GMC','Car_Model_List_Honda','Car_Model_List_Hummer','Car_Model_List_Hyundai','Car_Model_List_Infinity','Car_Model_List_Isuzu','Car_Model_List_Jaguar','Car_Model_List_Jeep','Car_Model_List_Kla','Car_Model_List_Lamborghini','Car_Model_List_Land_Rover','Car_Model_List_Lexus','Car_Model_List_Lincoln','Car_Model_List_Lotus','Car_Model_List_Maserati','Car_Model_List_Maybach','Car_Model_List_MAZDA','Car_Model_List_McLaren','Car_Model_List_Mercedes_Benz','Car_Model_List_Mercury','Car_Model_List_Mini','Car_Model_List_Mitsubishi','Car_Model_List_Nissan','Car_Model_List_Oldsmobile','Car_Model_List_Panoz','Car_Model_List_Plymouth','Car_Model_List_Pontiac','Car_Model_List_Porsche','Car_Model_List_Ram','Car_Model_List_Rolls_Royce','Car_Model_List_Saab','Car_Model_List_Saturn','Car_Model_List_Smart','Car_Model_List_Subaru','Car_Model_List_Susuki','Car_Model_List_Tesla','Car_Model_List_Toyota','Car_Model_List_Volkswagen','Car_Model_List_Volvo']

for cb in car_brands:
    print(cb)
    url = f'https://parseapi.back4app.com/classes/{cb}'
    headers = {
        'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z', # This is the fake app's application id
        'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW' # This is the fake app's readonly master key
    }
    data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
    with open(f"cardata/{cb}.json", "w") as outfile:
        outfile.write(json.dumps(data))
"""

import json
car_brands = ['Car_Model_List_Acura','Car_Model_List_Alfa_Romeo','Car_Model_List_Aston_Martin','Car_Model_List_Audi','Car_Model_List_Bentley','Car_Model_List_BMW','Car_Model_List_Buick','Car_Model_List_Cadillac','Car_Model_List_Chevrolet','Car_Model_List_Chrysler','Car_Model_List_Daewoo','Car_Model_List_Daihatsu','Car_Model_List_Dodge','Car_Model_List_Eagle','Car_Model_List_Ferrari','Car_Model_List_Fiat','Car_Model_List_Fisker','Car_Model_List_Ford','Car_Model_List_Freightliner','Car_Model_List_Genesis','Car_Model_List_Geo','Car_Model_List_GMC','Car_Model_List_Honda','Car_Model_List_Hummer','Car_Model_List_Hyundai','Car_Model_List_Infinity','Car_Model_List_Isuzu','Car_Model_List_Jaguar','Car_Model_List_Jeep','Car_Model_List_Kla','Car_Model_List_Lamborghini','Car_Model_List_Land_Rover','Car_Model_List_Lexus','Car_Model_List_Lincoln','Car_Model_List_Lotus','Car_Model_List_Maserati','Car_Model_List_Maybach','Car_Model_List_MAZDA','Car_Model_List_McLaren','Car_Model_List_Mercedes_Benz','Car_Model_List_Mercury','Car_Model_List_Mini','Car_Model_List_Mitsubishi','Car_Model_List_Nissan','Car_Model_List_Oldsmobile','Car_Model_List_Panoz','Car_Model_List_Plymouth','Car_Model_List_Pontiac','Car_Model_List_Porsche','Car_Model_List_Ram','Car_Model_List_Rolls_Royce','Car_Model_List_Saab','Car_Model_List_Saturn','Car_Model_List_Smart','Car_Model_List_Subaru','Car_Model_List_Susuki','Car_Model_List_Tesla','Car_Model_List_Toyota','Car_Model_List_Volkswagen','Car_Model_List_Volvo']
car_types = {}

for cb in car_brands:
    data = json.load(open( f'cardata/{cb}.json' ))
    data = data['results']
    for c in data:
        key = c['Make'] + ":" + str(c['Model'])
        val = c['Category']

        car_types[ key ] = val

print(car_types)


df['MakeModel'] = df['Make'] + ":" + df['Model']
df['StateCity'] = df['State'] + ":" + df['City']
#! we saw that it is not usefull df['CarType'] = df['MakeModel'].map( car_types )
#! print(df[df['CarType'].notnull()]) # faiz 10
# Make = Brand
"""
TO SEE THAT A MODEL NAME CAN BE USED IN TWO DIFFERENT MAKES: such that Dakota2WD
for model in df['Model'].unique():
    da = df[ df['Model'] == model ]['Make'].nunique() # select distinct count make from ....
    if da > 1:
        print(model, da)
"""

for m in df.groupby(by=['State']):
    print(m[0], len(m[1]), m[1]['Price'].mean())

#! NOTE THAT, people in a city, may buy some specific cars
#! NOTE THAT, cars in texas(for example), may have been used so much (mileage > 50000), so that
#! their prices may be low

makemodel = {}
for m in df.groupby(by=['MakeModel']):
    makemodel[ m[0] ] = m[1]['Price'].mean()

statecity = {}
for m in df.groupby(by=['StateCity']):
    statecity[ m[0] ] = m[1]['Price'].mean()

df['StateCityPrice'] = df['StateCity'].map( statecity )
df['MakeModelPrice'] = df['MakeModel'].map( makemodel )

df['StateMake'] = df['State'] + ":" + df['Make']
statemake = {}
for m in df.groupby(by=['StateMake']):
    statemake[ m[0] ] = m[1]['Price'].mean()
df['StateMakePrice'] = df['StateMake'].map( statemake )

"""
lux = ['BMW','Audi','Mercedes-Benz','Volvo','Lexus','Porsche','Ferrari','Lamborghini','Land Rover','Jaguar','Tesla','Cadillac','Chrysler','Bugatti','Alfa Romeo']
df['Lux'] = df['Make'].isin(lux)
df['Lux'] = df['Lux'].astype(int)
"""

state = {}
for m in df.groupby(by=['State']):
    state[ m[0] ] = m[1]['Price'].mean()
df['StatePrice'] = df['State'].map( state )

"""
make = {}
for m in df.groupby(by=['Make']):
    make[ m[0] ] = m[1]['Price'].mean()
df['MakePrice'] = df['Make'].map( make )
"""


df['MileagePerYear'] = df['Mileage'] / df['CarAge']
df['Fe1'] = df['CarAge'] * df['Mileage_2']

df['LUX2'] = df['Make'].isin(['BMW', 'FORD'])
df['ISFL'] = df['State'] == 'FL'

df['ISFL'] = df['ISFL'].astype(int)
df['LUX2'] = df['LUX2'].astype(int)

df = df.sample(frac = 1.0)
limit = int(len(df) * 0.50)

df = df.fillna(0)

"""
del df['City']
del df['State']
del df['Make']
del df['Model']
del df['MakeModel']
del df['StateCity']
del df['StateMake']
del df['Year']
del df['Mileage']
"""

train = df[:limit]
test = df[limit:]

train_d = train[ ['City','State','Make','Model','MakeModel','StateCity','StateMake','Year','Mileage'] ]
train_y = train[target]
del train[target]
for t in ['City','State','Make','Model','MakeModel','StateCity','StateMake','Year','Mileage']:
    del train[t]


test_d = test[ ['City','State','Make','Model','MakeModel','StateCity','StateMake','Year','Mileage'] ]
test_y = test[target]
del test[target]
for t in ['City','State','Make','Model','MakeModel','StateCity','StateMake','Year','Mileage']:
    del test[t]

from sklearn.ensemble import RandomForestRegressor


regr = RandomForestRegressor(max_depth=4, random_state=0)
regr.fit(train, train_y)
print(regr.score( test, test_y ))

test['pred'] = regr.predict( test )
test['pred'] = test['pred'].astype(int)
test['real'] = test_y

for t in test_d:
    test[t] = test_d[t]

test.to_csv("week9_5_car.csv")


test['abspererror'] = np.abs(test['pred'] - test['real']) / test['real']

A = test[ test['abspererror'] > 0.20 ]  # they have too high errors
B = test[ test['abspererror'] <= 0.20 ] # their errors can be accepted

A_State = A['State'].value_counts(normalize=True).to_dict()
B_State = B['State'].value_counts(normalize=True).to_dict()

A_Make = A['Make'].value_counts(normalize=True).to_dict()
B_Make = B['Make'].value_counts(normalize=True).to_dict()

for a in A_State:
    if a in B_State:
        diff = A_State[ a ] - B_State[ a ]
        print(a, diff)

for a in A_Make:
    if a in B_Make:
        diff = A_Make[ a ] - B_Make[ a ]
        print(a, diff)




