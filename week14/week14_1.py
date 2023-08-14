
import pandas as pd
df = pd.read_excel("week14_satisfaction.xlsx")
#df = df.sample(n = 20000)

"""
from ydata_profiling import ProfileReport
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("week14_report.html")
"""


df['satisfaction_v2'] = df['satisfaction_v2'].map({'satisfied': 1, 'neutral or dissatisfied': 0})
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Customer Type'] = df['Customer Type'].map({'Loyal Customer': 1, 'disloyal Customer': 0})
df['Type of Travel'] = df['Type of Travel'].map({'Personal Travel': 1, 'Business travel': 0})
df['Class'] = df['Class'].map({'Eco': 0, 'Eco Plus': 0, 'Business': 1})

df = df.sort_values(by = ['id'])
del df['id']

df.corr().to_csv("week14_1_corr.csv")
df.to_csv("week14_1_processed.csv")





