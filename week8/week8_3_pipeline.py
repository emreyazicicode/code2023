
# Pipeline

#: Imports
import numpy as np
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
#        blood type, %99.9 == > empty, %0.01 == filled
#        gender [female] = %99.9, male ==> %0.01 [e.g: make up products]
#        in this situation, gender can also be discarded

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

# city = 80
# top1, top2, top3, top4, Others ==> 5 tane 
# City
# - London:  %40
# - Baku     %25
# - Istanbul %20
# - Others   %15



#* STEP7: Remove the outliers
#* STEP8: Remove unlogical values

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


"""
df['tenure_log'] = df['tenure'].apply(lambda value: 0 if value == 0 else np.log(value))
df['tenure_sqrt'] = np.sqrt(df['tenure'])
df['tenure_pow2'] = np.power(df['tenure'], 2)
df['tenure_pow13'] = np.power(df['tenure'], 1.3)
df['tenure_pow06'] = np.power(df['tenure'], 0.6)
df['tenure_med'] = df['tenure'] > df['tenure'].median()
"""

# method: __singleValid__
# Validates that the newly created features gain is more important
# @base, float: The base importance
# @new, float: The new importances
# @minAddition, float: The minimum additional amount to be gained
# @minRatio, float: The minimum ratio amount to be gained
# @threshold, float: The minimum limit
# @return, bool: Valid or not
# @completed
def __singleValid__( base, new, minAddition, minRatio, threshold = 0.0 ):
    return new > base and \
        new > base + minAddition and \
        new > base * minRatio and \
        new > threshold

index = 0
for c1 in df: # 20
    for c2 in df: # 20
        if c1 > c2 and c1 != target and c2 != target:
            index += 1
            df['TEMP' + str(index)] = df[c1] + df[c2]
            
            c1c = abs(df[c1].corr(df[target]))
            c2c = abs(df[c2].corr(df[target]))
            combined = abs(df['TEMP' + str(index)].corr(df[target]))

            # FILTERING
            #if __singleValid__( c1c, combined, 0.05, 1.10, 0.20):
                
            if combined > c1c + 0.05 and combined > c2c + 0.05: 
                print( c1, c2, combined, c1c, c2c )
            else:
                del df['TEMP' + str(index)]


print(df.columns)

df.corr().to_csv("week8_corr.csv")



sys.exit(1)
df['TEMP'] = df['StreamingTV'] + df['SeniorCitizen'] + df['PaperlessBilling']
print(df['TEMP'].corr(df[target]))

df['#ofservices'] = df['TechSupport'] + df['Contract_One year'] + df['InternetService_DSL']
print(df['#ofservices'].corr(df[target]))

df['TEMP3'] = df['Dependents'] * -0.169245073397867 + \
    df['TotalCharges'] * -0.158350363277118 + \
    df['InternetService_0'] * -0.215943574509394

print(df['TEMP3'].corr(df[target]))


ones = df[ df[target] == 1 ].mean().to_dict()
zeros = df[ df[target] == 0 ].mean().to_dict()

diff = {k:abs(ones[k] - zeros[k]) for k,v in ones.items()}
diff = {k:v for k,v in diff.items() if v > 0.2}

print(ones)
print(zeros)
print(diff)


del df['TEMP']
sys.exit(1)





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


limit = int(len(df) * 0.60)

train = df[:limit]
test = df[limit:]

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


correct = test_y == test_y_predicted


test['REAL'] = test_y
test['PRED'] = test_y_predicted
test['CORRECT'] = test['PRED'] == test['REAL']
test['TP'] = (test['PRED'] == 1) & (test['REAL'] == 1)
test['TN'] = (test['PRED'] == 0) & (test['REAL'] == 0)
test['FP'] = (test['PRED'] == 1) & (test['REAL'] == 0)
test['FN'] = (test['PRED'] == 0) & (test['REAL'] == 1)

for c in ['CORRECT','TP','TN','FP','FN']:
    test[c] = test[c].astype(int)


fn = test['FN'].mean() * 20
fp = test['FP'].mean() * 3
tp = test['TP'].mean() * 1
tn = test['TN'].mean() * 20

weighted_accuracy = (tp + tn) / ( fn+fp+tp+tn )

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

print("Accuracy", accuracy_score( test_y, test_y_predicted  ))
print("Weighted_Accuracy", weighted_accuracy)
print("f1_score", f1_score(test_y, test_y_predicted))
print("correlation", test_y.corr(pd.Series(test_y_predicted)))

test.to_csv("week8_2_out.csv")
"""
    Accuracy 0.735981308411215
    Weighted_Accuracy 0.8128860991887266
    f1_score 0.438  [0-1]
    correlation 0.02 [0-1] (regression)
"""


