
import pandas as pd
from ydata_profiling import ProfileReport

"""
df = pd.read_csv("week5_training_sample.csv", nrows=10000)
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("week6_profiling.html")
print(df['sort_by'].value_counts())
"""

# CAY ICMEYE GIDIN [4-6 MINUTES]


d = {'Plot Names': ['implot','scatterplot','lineplot','displot','relplot','catplot','boxplot','violinplot','jointplot','histplot','striptplot','jointgrid','facedgrid','boxenplot','heatmap','kdeplot','displot','pair grid','pairgrid','residplot','swarmplot','violinplot','clustermap'], 'Composition': ['NN','CNN','CNN','CCN','CCNN','CNN','CCN','CCN','CCNN','CNN','CCN','CCN','CCN','CNN','CCN','CNN','CCN','NN','CCN','CNN','CCN','CNN','CNN']}
df = pd.DataFrame(data=d)

print(df)
target = "N"

print(df[ df['Composition'] == target ]['Plot Names'])


df = pd.read_csv("Telecom_customer churn.csv", nrows=100)

print(df.columns)
vals = df['rev_Mean'].to_list()
vals.sort()
print(vals)
print( df['rev_Mean'].quantile(0.95) ) # percentile
print( df['rev_Mean'].quantile(0.05) ) # percentile

da = df[ (df['rev_Mean'] > df['rev_Mean'].quantile(0.05)) & (df['rev_Mean'] < df['rev_Mean'].quantile(0.95)) ]
# REMOVE THE ITEMS OF DATA, FIRST %5, AND LAST %5

# 100 * 0.95 nth row


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import sys
data = sns.load_dataset('mpg')
print(data)

# sklearn = scikit-learn
data['origin_encoded'] = LabelEncoder().fit_transform(data['origin'])
print(data['origin'].unique())
print(data[ ['origin', 'origin_encoded']  ])


fig = px.parallel_coordinates(
    data,
    color="origin_encoded",
    labels={
        "mpg": "MPG",
        "cylinders": "Cylinders",
        "displacement": "Displacement",
        "horsepower": "Horsepower",
        "weight": "Weight",
        "acceleration": "Acceleration",
        "model_year": "Model Year",
        "origin_encoded": "Origin",
    },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2,
)

fig.show()


