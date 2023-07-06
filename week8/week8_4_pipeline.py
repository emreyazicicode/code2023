
import pandas as pd
path = "Churn_Modelling.csv"
df = pd.read_csv(path)

print(df.shape)

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


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=6, random_state=0)

clf.fit(train, train_y)
test['PRED'] = clf.predict(test)
test['REAL'] = test_y

test.to_csv("week8_4_out.csv")

from sklearn.metrics import f1_score

print(f1_score(test['REAL'], test['PRED']))

# 2 = 0.09
# 3 = 0.20
# 4 = 0.37
# 5 = 0.45
# 6 = 0.51
# 7 = 0.52
# 8 = 0.53
# 10 = 0.55

#  import numpy as np
# np.random.normal(0, 1, size=(2,4))


a = [0.2, 0.45]
b = [0.5, -0.4]
c = [0.1, 0.01]
d = [-0.99, 0.55]

e = [0.02, 0.5, -0.6, 0.92]


MODEL = [
    a,b,c,d,e
]

def fire(age, creditscore):
    a_ = a[0] * age + a[1] * creditscore
    b_ = b[0] * age + b[1] * creditscore
    c_ = c[0] * age + c[1] * creditscore
    d_ = d[0] * age + d[1] * creditscore
    e_ = a_ * e[0] # +......
    return e_


for iteration in range(100):

    totalerror = 0
    for i in range(len(df)):
        d = df[i].to_dict()
        prediction = fire( d['age'], d['creditscore'])
        
        
        error = d['churn'] - prediction
        if i % 4 == 0:
            updateWeight( error )
        totalerror += error

    if totalerror < 0.05:
        break





