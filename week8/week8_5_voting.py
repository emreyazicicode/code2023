from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import warnings
from sklearn.metrics import f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC

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

clf1 = RandomForestClassifier(max_depth=6, random_state=0)
clf1.fit(train, train_y)

clf2 = MLPClassifier(random_state=1, max_iter=300)
clf2.fit(train, train_y)

clf3 = LinearSVC()
clf3.fit(train, train_y)

clf4 = BalancedRandomForestClassifier(n_estimators=100)
clf4.fit(train, train_y)

# VOTING
PRED1 = clf1.predict(test)
PRED2 = clf2.predict(test)
PRED3 = clf3.predict(test)
PRED4 = clf4.predict(test)

test['PRED1'] = PRED1
test['PRED2'] = PRED2
test['PRED3'] = PRED3
test['PRED4'] = PRED4
test['REAL'] = test_y

test.to_csv("week8_5_out.csv")
# Validation, certainity
# 4 out of 4 ==> (P/N), strong
# 3 out of 3 ==> (P/N), moderate

# ODD NUMBER OF CLASSIFIERS MUST BE USED
# majority voting
# 3, 5, 7



