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
"""
                      name  f_importance  correlation  fillness     inter  averages
0      Air temperature [K]      0.080634     0.082556       1.0  1.964068  0.001519
1  Process temperature [K]      0.048258     0.035946       1.0  1.952294  0.000475
2   Rotational speed [rpm]      0.292495     0.044188       1.0  1.927398  0.014415
3              Torque [Nm]      0.439598     0.191321       1.0  1.914118  0.117358
4          Tool wear [min]      0.125590     0.105448       1.0  1.048651  0.148070
5                   Type_H      0.002960     0.023916       1.0  1.677281  0.242669
6                   Type_L      0.006472     0.035643       1.0  2.236537  0.074799
7                   Type_M      0.003995     0.022432       1.0  2.046689  0.103918

"""


data['L_Rotational speed [rpm]'] = np.log( data['Rotational speed [rpm]'] )
data['P_Torque [Nm]'] =np.power( data['Torque [Nm]'], 7.0)

"""
for c in data:
    if c != target:
        data['temp'] = np.power(data[c], 2.0)
        data['temp'] = data['temp'].fillna(0)
        data['temp'] = data['temp'].replace(np.nan, 0) # NAN = not a number
        data['temp'] = data['temp'].replace(np.inf, 0) # INF = infinite
        print(c, "POWER", data['temp'].corr(data[target]), "SELF", data[c].corr(data[target]) )

del data['temp']
"""
# Torque [Nm] P_Torque [Nm] 0.29935747056673107 0.19132077505949327 0.25158558101145806


# (x2 * x) = x3
"""

for c0 in data:
    for c1 in data:
        if c0 != target and c1 != target and c0 > c1 and c0 != 'temp' and c1 != 'temp':
            data['temp'] = data[c0] * data[c1]

            corr = abs(data['temp'].corr(data[target]))
            corr0 = abs(data[c0].corr(data[target]))
            corr1 = abs(data[c1].corr(data[target]))

            if corr > corr0 + 0.03 and corr > corr1 + 0.03:
                print(c0, c1, corr, corr0, corr1)



sys.exit(1)
"""

del data['Rotational speed [rpm]']
del data['Torque [Nm]']








sys.exit(1)

# FEATURE IMPORTANCE, FEATURE RELATION
# 1 ---> Correlation
# 2 ---> Feature importance
# 3 ---> Fillness
# 4 ---> Intercorrelated
# 5 ---> Different of averages



correlation = {}
for c in data:
    correlation[ c ] = abs(data[c].corr(data[target]))
    print(data[c].corr(data[target]))



averages = {}
for c in data:
    if c!= target:
        c0 = data[ data[target] == 0 ][c].mean()
        c1 = data[ data[target] == 1 ][c].mean()
        averages[c] = abs(c0-c1) / (c0 + c1)

y = data[target]
del data[target]
clf = RandomForestClassifier(max_depth=5, random_state=0) #  dummy model, temporary
clf.fit(data, y)
cl = list(data.columns)
fi = clf.feature_importances_
# NOTE: Feature importance is usually, sum of 1, faiz dagilim
# NOTE: we cannot compare it to correlation
feature_importances = {cl[f]:fi[f] for f in range(len(data.columns))}

print(feature_importances)
print(sum(feature_importances.values()))


fillness = {}
for c in data:
    fillness[c] = data[c].count() / len(data)


inter = {}
for c0 in data: # loop for each columns
    s = 0.0
    for c1 in data: # loop for each columns, twice
        if c0 != target and c1 != target:
            s += abs( data[c0].corr(data[c1]) )
    inter[c0] = s


general_feature_map = pd.DataFrame( data = feature_importances.keys(), columns = ['name'])
general_feature_map['f_importance'] = general_feature_map['name'].map(feature_importances)
general_feature_map['correlation'] = general_feature_map['name'].map(correlation)
general_feature_map['fillness'] = general_feature_map['name'].map(fillness)
general_feature_map['inter'] = general_feature_map['name'].map(inter)
general_feature_map['averages'] = general_feature_map['name'].map(averages)



print(general_feature_map)

print(data)
print(y)
"""
# PROVE
import re
from sklearn.tree import export_text
mainlist = []
for i in range(100):
    r = export_text(clf.estimators_[i], feature_names=cl)
    r = re.sub(r"[0-9\.\<\>\= ]", "", r)
    r = r.split('\n')
    for q in r:
        mainlist.append(q)
features = pd.DataFrame(data = mainlist, columns = ['feature'])
pp.pprint(features['feature'].value_counts().to_dict())
"""
