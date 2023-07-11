from sklearn.metrics import f1_score
import sys
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pprint

pp = pprint.PrettyPrinter()

data = pd.read_csv('week9_predictive_maintenance.csv')
print(data)
target = 'Target'

del data['UDI']
del data['Product ID']
del data['Failure Type']

#! data = pd.get_dummies( data, columns=['Type'] )
#! We do not need to have Type column
del data['Type']
del data['Process temperature [K]']

data['L_Rotational speed [rpm]'] = np.log( data['Rotational speed [rpm]'] )
data['P_Torque [Nm]'] =np.power( data['Torque [Nm]'], 7.0)

del data['Rotational speed [rpm]']
del data['Torque [Nm]']


print(data[target].mean()) # 0.0339 HIGHLY IMBALANCED

data = data.sample(frac = 1.0)
limit = int(len(data) * 0.70)
train = data[:limit]  # 0.033 ==> 1, rest of them 0,

# RE-BALANCING
# RE-BALANCING THE DATA SET, IF THE ORIGINAL DATA SET IS HIGHLY IMBALANCED!,
# NOTE AGAIN, DO NOT REPEAT THIS FOR TEST OR VALIDATION SET!!!!!!!!
print("BEFORE", train[target].mean())
train0 = train[ train[target] == 0 ].sample(frac = 0.10)
train1 = train[ train[target] == 1 ]

train = pd.concat( [train0, train1] )
train = train.sample(frac = 1.0) # Shuffle
print("AFTER", train[target].mean())


#! NOTE, TEST KUMESINE DOKUNMAYALIM, ASLA!!

test = data[limit:]

train_y = train[target]
del train[target]

test_y = test[target]
del test[target]


clf = RandomForestClassifier(max_depth=5, random_state=0) #  dummy model, temporary
clf.fit(train, train_y)


print( "f1", f1_score(test_y, clf.predict(test)) ) 



