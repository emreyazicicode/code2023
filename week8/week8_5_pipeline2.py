from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import warnings
from sklearn.metrics import f1_score

warnings.filterwarnings("ignore")


path = "Churn_Modelling.csv"
df = pd.read_csv(path)

del df['RowNumber']
del df['CustomerId']
del df['Surname']
df['Gender'] = df['Gender'].map({"Female": 1, "Male": 0})
df = pd.get_dummies(df, columns = ['Geography'])

target = 'Exited'
df = df.sample(frac = 1.0)
limit = int(len(df) * 0.70)

train = df[:limit]
test = df[limit:]

train_y = train[ target ]
del train[ target ]

test_y = test[ target ]
del test[ target ]

clf = RandomForestClassifier(max_depth=6, random_state=0)

clf.fit(train, train_y)
PRED = clf.predict(test)            # 1/0
PROB = clf.predict_proba(test)[:,1] # probability 0.33,0.68, 0.90

test['PRED'] = PRED
test['PROB'] = PROB
test['REAL'] = test_y
test['CERTAIN'] = np.abs(0.5 - PROB)

from sklearn.metrics import accuracy_score


TS = []
AS = []
maxvalue = 0
maxat = 0

COST_VECTOR = {
    'TP': 7,
    'TN': 1,
    'FP': 5,
    'FN': 10
}

for t in range(0,100):

    threshold = float(t) / 100.0
    test['regenerated'] = test['PROB'] > threshold

    test['TP'] = (test['REAL'] == 1) & (test['regenerated'] == 1)
    test['TN'] = (test['REAL'] == 0) & (test['regenerated'] == 0)
    test['FP'] = (test['REAL'] == 0) & (test['regenerated'] == 1)
    test['FN'] = (test['REAL'] == 1) & (test['regenerated'] == 0)

    tp = test['TP'].mean() * COST_VECTOR['TP']
    tn = test['TN'].mean() * COST_VECTOR['TN']
    fp = test['FP'].mean() * COST_VECTOR['FP']
    fn = test['FN'].mean() * COST_VECTOR['FN']

    a = accuracy_score(test['REAL'], test['regenerated'])
    #: weighted accuracy
    a = (tp + tn) / (tp + tn + fn + fp)

    print( "T", threshold, "A", a)
    TS.append(threshold)
    AS.append(a)

    if a > maxvalue:
        maxvalue = a
        maxat = threshold

import matplotlib.pyplot as plt

print("MAXIMUM ACCURACY HAS BEEN ACHIEVED with", maxvalue, "at", maxat)

plt.scatter(TS, AS)
plt.show()


#! 1. Istifade: Ne kadar emin, how certain we are
# ---> 0.85 - 1.00 [kesin gidecek gibi olanlar] ==> bunlara mudahele, call center
# the aim is saving, do not spend the budget on wrong (or uncertain) ones




test.to_csv("week8_5_out.csv")


