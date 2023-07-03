import warnings
warnings.filterwarnings("ignore")
from sklearn import tree
import time
import pandas as pd
import matplotlib.pyplot as plt
path = 'week8_churn.csv'
target = 'Churn'

df = pd.read_csv(path)
df = df.replace('Yes', 1)
df = df.replace('No', 0)

df = df.select_dtypes(exclude=['object'])

# SPLIT THE DATA INTO TRAIN AND TEST PARTS
faiz = 0.60
count = int(len(df) * faiz)

# SHUFFLE, RANDOMLY SORT!!!
df = df.sample(frac = 1.0)

train = df[:count]  # RANGE = select from ... to ... rows only
test = df[count:]
#! prevent overfitting

print(train.shape)
print(test.shape)

print(train.head(2))
print(test.head(2))

train_y = train[target]
del train[target]
train_x = train

test_y = test[target]
del test[target]
test_x = test

# 4 parts
print("train_x", train_x.shape)
print("train_y", train_y.shape)
print("test_x", test_x.shape)
print("test_y", test_y.shape)

clf = tree.DecisionTreeClassifier() # clf = classifier
clf.fit(train_x, train_y)

prediction = clf.predict( test_x )
print(prediction)

# pandas.Series = numpy.ndarray = numpy.array = vector

result = (test_y == prediction)
print(result)
print(result.mean())

test_x['PRED'] = prediction
test_x['REAL'] = test_y
test_x['CORRECT'] = test_x['PRED'] == test_x['REAL']
test_x['TP'] = (test_x['PRED'] == 1) & (test_x['REAL'] == 1)
test_x['TN'] = (test_x['PRED'] == 0) & (test_x['REAL'] == 0)
test_x['FP'] = (test_x['PRED'] == 1) & (test_x['REAL'] == 0)
test_x['FN'] = (test_x['PRED'] == 0) & (test_x['REAL'] == 1)



print(test_x.dtypes)
for c in ['CORRECT','TP','TN','FP','FN']:
    test_x[c] = test_x[c].astype(int)

#for c in test_x.select_dtypes( include = ['bool'] ).columns:
#    test_x[c] = test_x[c].astype(int)



# test_x['TP'] = test_x.apply(lambda row: ....) (test_x['PRED'] == 1) & (test_x['REAL'] == 1)

test_x.to_csv("week8_out.csv")

# FARK = DIFFERENCE = ERROR


for c in ['CORRECT','TP','TN','FP','FN']:
    ones = test_x[ test_x[c] == 1 ].mean().to_dict()
    zeros = test_x[ test_x[c] == 0 ].mean().to_dict()

    diff = {
        x:round(abs(ones[x] - zeros[x])/test_x[x].mean(), 3) 
        for x,y in ones.items() 
        if x not in ['CORRECT','TP','TN','FP','FN', 'REAL', 'PRED']
    }

    print(c, diff)

# senior citizen is important!

#! Train with, train_x and train_y
#! That is, try to find a way to predict train_y using train_x
#! Later, we give test_x, and get some PREDICTIONS
#! Finally, we test the PREDICTIONS ARE SAME WITH test_y
#  


# 85.60879
# 84.0757576
# 85.1023190341
# 86.139303
