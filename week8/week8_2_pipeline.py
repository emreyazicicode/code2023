
# Pipeline

#: Imports
from sklearn.model_selection import train_test_split
import sys
from sklearn.preprocessing import MinMaxScaler
import warnings
from sklearn import tree
import time
import pandas as pd
import matplotlib.pyplot as plt

#: Startup, initial operations
warnings.filterwarnings("ignore")
# TODO: Logging

#: Configs, settings
path = 'week8_churn.csv'
target = 'Churn'

#: Load the dataset
df = pd.read_csv(path)

#* STEP0: Descriptive analytics
# max, min, std, mean...., correlation

#* STEP1: Transform the representation of variables
df['gender'] = df['gender'].map({'Female': 1, 'Male': 0})
df = df.replace('Yes', 1)
df = df.replace('No', 0)
df = df.replace('No internet service', 0)
df = df.replace('No phone service', 0)

#* STEP2: Remove unnecessary variables
# ==> A: The columns which are "UNIQUE"
del df['customerID']
# ==> B: The columns which have only one value
#      df[c].nunique(), cardinality is very low
# ==> C: The columns which are highly correlated with others
#      df.corr()
# ==> D: The columns which are highly empty

#* STEP3: Cleanup invalid values!!
# ==> A: Decimal separator
#        34.56 
#        34,56
# ==> B: Date
#        12/12/2002
# ==> C: None - Null - Empty
# ==> D: Textual (" ", "" empty string or space)
# ==> E: -inf, na, NaN (not a number)

#* STEP4: Fill up nulls
df = df[ df['TotalCharges'].notnull() ]
df = df[ df['TotalCharges'] != ' ' ]
#df['TotalCharges'] = df['TotalCharges'].fillna( df['TotalCharges'].mean() )
df['TotalCharges'] = df['TotalCharges'].astype(float)
print(df.dtypes)

#* STEP5: Transform, normalize
"""
for c in ['MonthlyCharges','TotalCharges', 'tenure']:
    df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())
"""
scaler = MinMaxScaler()
scaler.fit(df[ ['MonthlyCharges','TotalCharges', 'tenure'] ])
df[['MonthlyCharges','TotalCharges', 'tenure']] = (scaler.transform(df[ ['MonthlyCharges','TotalCharges', 'tenure'] ]))

#* STEP6: Categorical variables
df = pd.get_dummies( df, columns = ['InternetService', 'Contract', 'PaymentMethod'] )

#* STEP7: Remove the outliers
#* STEP8: Remove unlogical values

print(df)
df.to_csv("week8_2_out.csv")

#! Two conditions are important
#! All must be numeric
#! There should be no null! - empty


#* STEP9: Shuffle, Make it time independed
df = df.sample(frac = 1.0)
# df = df.sample(n = 15000)

#* STEP10: Limit only according project, and time
df = df[df['tenure'] > 0] # Skip the rows which are fresh new
# We do not have enough information
df = df[df['tenure'] < 10] # Skip the rows which are very old, out of date
# The best way:
# 2023,   %100  [exclude last month]  10.000
# 2022,   %80                         27.000 %80 == >
# 2021,   %50                         26.000 %50 == > ....
# 2020,   %30
# before, %5
# Data frame i re-decorate edelim
"""
df = pd.concat( [
    df[ df['tenure'] == 1 ].sample(frac = 1.0), # LAST YEAR MOST IMPORTANT
    df[ df['tenure'].isin([2,3]) ].sample(frac = 0.8),
    df[ df['tenure'].isin([4,5,6]) ].sample(frac = 0.5),
    df[ df['tenure'].isin([7,8]) ].sample(frac = 0.2),
    df[ df['tenure'].isin([9]) ].sample(frac = 0.05) # LEAST IMPORTANT  984, 0.05 = 50
])
df = df.sample(frac = 1.0)
"""
# Row weighting!!

#* STEP11: Split into parts

limit = int(len(df) * 0.60)
# If there are very few rows (1000-5000), we can use %90 percent as train
# But normally people use %80 percent as the train
# I suggest, to use 60-70 

#             VERY LOW    |    VERY HIGH
# UNDERFIT:       x       |                     , very low accuracy, does not learn!!!
# OVERFIT:                |       x             , very high accuracy, but not in TEST set

# 0, 5000 ==> %90
# 5K, 10K ==> %80
# ....
# complexity
# Repeat the step below 3-4 times
# %70 train =============== > 0.85 (test)
# %75 train =============== > 0.88 (test)
# %80 train =============== > 0.87 (test)


train = df[:limit]
test = df[limit:]

print(train.shape, test.shape)

train_y = train[target]
test_y = test[target]

del train[target]
del test[target]


#! X_train, X_test, y_train, y_test = train_test_split( df.drop(columns = [target]), df[target], train_size=0.60)

#* STEP12: Train
clf = tree.DecisionTreeClassifier() # clf = classifier
clf.fit( train, train_y )

#* STEP13: Predict and test, measure
test_y_predicted = clf.predict( test )

print(test_y_predicted) # TAHMIN, PREDICTED
print(test_y)           # REAL, GERCEK
correct = test_y == test_y_predicted
print(correct.mean())


test['REAL'] = test_y
test['PRED'] = test_y_predicted
test['CORRECT'] = test['PRED'] == test['REAL']
test['TP'] = (test['PRED'] == 1) & (test['REAL'] == 1)
test['TN'] = (test['PRED'] == 0) & (test['REAL'] == 0)
test['FP'] = (test['PRED'] == 1) & (test['REAL'] == 0)
test['FN'] = (test['PRED'] == 0) & (test['REAL'] == 1)

for c in ['CORRECT','TP','TN','FP','FN']:
    test[c] = test[c].astype(int)

test.to_csv("week8_2_out.csv")

