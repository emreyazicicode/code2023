import pandas as pd
path = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
df = pd.read_csv(path)

df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
df['BusinessTravel'] = df['BusinessTravel'].map(
    {'Non-Travel': 0, 'Travel_Rarely': 1, 'Travel_Frequently': 6}
)

del df['Over18']

df = pd.get_dummies(df, columns = ['MaritalStatus'])
df = pd.get_dummies(df, columns = ['Department'])

for c in df.select_dtypes(exclude = ['object']):
    corr = df[c].corr(df['Attrition'])
    if abs(corr) > 0.10:
        print(c, corr)


print(df['Attrition'].mean())

da = pd.DataFrame(columns = ['yes', 'no'])

for g in df.groupby(['Attrition']):
    print(g[0])
    print(g[1].mean())
    if g[0] == 0:
        da['no'] = g[1].mean()
    else:
        da['yes'] = g[1].mean()
    print("============")

print(da)


for c in df.select_dtypes(exclude = ['object']):
    df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())

df['KACANLAR'] = df['Age'] + df['DailyRate'] + df['Education'] + \
    df['EnvironmentSatisfaction'] + df['JobLevel'] + df['MonthlyIncome'] + \
    df['RelationshipSatisfaction']

df['KACANLAR2'] = df['DistanceFromHome'] + df['NumCompaniesWorked'] + df['OverTime']
df['KACANLAR3'] = df['NumCompaniesWorked'] * df['OverTime']

print(df['KACANLAR'].corr(df['Attrition']))
print(df['KACANLAR2'].corr(df['Attrition']))
print(df['KACANLAR3'].corr(df['Attrition']))
"""
                                            yes            no
Age                                   33.607595     37.561233
Attrition                              1.000000      0.000000
BusinessTravel                         2.405063      1.731549
DailyRate                            750.362869    812.504461
DistanceFromHome                      10.632911      8.915653
Education                              2.839662      2.927007
EmployeeCount                          1.000000      1.000000
EmployeeNumber                      1010.345992   1027.656123
EnvironmentSatisfaction                2.464135      2.771290
Gender                                 0.632911      0.593674
HourlyRate                            65.573840     65.952149
JobInvolvement                         2.518987      2.770479
JobLevel                               1.637131      2.145985
JobSatisfaction                        2.468354      2.778589
MonthlyIncome                       4787.092827   6832.739659
MonthlyRate                        14559.308017  14265.779400
NumCompaniesWorked                     2.940928      2.645580
OverTime                               0.535865      0.234388
PercentSalaryHike                     15.097046     15.231144
PerformanceRating                      3.156118      3.153285
RelationshipSatisfaction               2.599156      2.733982
StandardHours                         80.000000     80.000000
StockOptionLevel                       0.527426      0.845093
TotalWorkingYears                      8.244726     11.862936
TrainingTimesLastYear                  2.624473      2.832928
WorkLifeBalance                        2.658228      2.781022
YearsAtCompany                         5.130802      7.369019
YearsInCurrentRole                     2.902954      4.484185
YearsSinceLastPromotion                1.945148      2.234388
YearsWithCurrManager                   2.852321      4.367397
MaritalStatus_Divorced                 0.139241      0.238443
MaritalStatus_Married                  0.354430      0.477697
MaritalStatus_Single                   0.506329      0.283861
Department_Human Resources             0.050633      0.041363
Department_Research & Development      0.561181      0.671533
Department_Sales                       0.388186      0.287105
"""