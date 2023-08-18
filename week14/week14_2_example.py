
#: Imports

import json
import sklearn_json as skljson
import pickle
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import plotly.express as px
import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

#: Load dataset
df = pd.read_excel("week14_satisfaction.xlsx")

#: Feature mapping
df['satisfaction_v2'] = df['satisfaction_v2'].map({'satisfied': 1, 'neutral or dissatisfied': 0})
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Customer Type'] = df['Customer Type'].map({'Loyal Customer': 1, 'disloyal Customer': 0})
df['Type of Travel'] = df['Type of Travel'].map({'Personal Travel': 1, 'Business travel': 0})
df['Class'] = df['Class'].map({'Eco': 0, 'Eco Plus': 0, 'Business': 1})

#: Sort values
df = df.sort_values(by = ['id'])

#: Remove unnecessary
del df['id']

#: Discarding Outliers, : CLIPPING, REMOVING
# Filter the DataFrame to keep only the data points within the specified range
def drop_outliers_custom(dataframe, column_name, lower_threshold, upper_threshold):
    return dataframe[(dataframe[column_name] >= lower_threshold) & (dataframe[column_name] <= upper_threshold)]

def drop_outliers( dataframe, column_name, threshold = 3 ):
    lower = (dataframe[ column_name ] - dataframe[ column_name ].mean()) / df[column_name].std()
    return dataframe[lower < threshold]

df = drop_outliers_custom( df, 'Age', df['Age'].quantile(0.01), df['Age'].quantile(0.99) )
df = drop_outliers_custom( df, 'Flight Distance', df['Flight Distance'].quantile(0.01), df['Flight Distance'].quantile(0.99) )
df = drop_outliers_custom( df, 'Arrival Delay in Minutes', df['Arrival Delay in Minutes'].quantile(0.01), df['Arrival Delay in Minutes'].quantile(0.99) )
df = drop_outliers_custom( df, 'Departure Delay in Minutes', df['Departure Delay in Minutes'].quantile(0.01), df['Departure Delay in Minutes'].quantile(0.99) )
#! df = drop_outliers( df, 'Flight Distance', 3 )

#: Filling empties, drop + fillwith0 + fillwithmean + fillwithmode
df = df.fillna(0)
#* df = df.dropna()

"""
plt.hist(df['Arrival Delay in Minutes'].sample(n = 10000))
plt.show()

std_ = df['Arrival Delay in Minutes'].std()
mean_ = df['Arrival Delay in Minutes'].mean()
print(df['Arrival Delay in Minutes'].fillna(pd.Series(np.random.normal(loc= mean_,scale= std_ ,size= len(df)))).isnull().sum())
df['Arrival Delay in Minutes'] = df['Arrival Delay in Minutes'].fillna(pd.Series(np.random.normal(loc= mean_,scale= std_ ,size= len(df))))
"""


#: Normalize
for i in df.columns:
    if i != 'Flight Distance':
        df[i] = (df[i] - df[i].min())/(df[i].max() - df[i].min()) 


"""
columns_to_standardize = ['Flight Distance', 'Age', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']
scaler = StandardScaler()
df[columns_to_standardize] = scaler.fit_transform(df[columns_to_standardize])
"""
"""
columns_to_normalize = ['Flight Distance', 'Age', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']
means = df[columns_to_normalize].mean()
stds = df[columns_to_normalize].std()
df[columns_to_normalize] = (df[columns_to_normalize] - means) / stds
"""

#: Transform
# flight distance turn into categoric var in a range
range_mapping = {
    (0, 800): '1',
    (801, 1300): '2',
    (1301, 3000): '3',
    (3001, 4000): '4',
    (4001, 7000): '5'
}

# Function to map values to categories
def map_to_category(value):
    for range_, category in range_mapping.items():
        if range_[0] <= value <= range_[1]:
            return category
    return None

# Apply the mapping function to create the categorical column
df['flight_distance_cat'] = df['Flight Distance'].apply(map_to_category)

print(df)
print(df['flight_distance_cat'].describe())

# -- type casting
# -- log, sqrt
# -- dummy


#: Feature mining + tenure
df['Entertainment Score'] = df['Inflight wifi service'] * df['Inflight entertainment']
service_rating_columns = ['Seat comfort', 'Food and drink', 'Inflight wifi service', 'Inflight entertainment',
                          'On-board service', 'Leg room service', 'Baggage handling', 'Checkin service',
                          'Cleanliness', 'Online boarding']
df['Service Rating'] = df[service_rating_columns].mean(axis=1)
df['Total Online Support Score'] = df['Online support'] * df['Ease of Online booking']





# -- merging
# -- creating new
# -- heatmap

#: Feature elimination

# -- unique
# -- same

# -- intercorrelation
print(df.corr())
# YUSIF BAKTI --> Cola

# -- low corelation
del df['Departure/Arrival time convenient']
del df['Flight Distance']
del df['Departure Delay in Minutes']



# -- feature importance
rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_classifier.fit(df.drop(columns = ['satisfaction_v2']), df['satisfaction_v2'])
feature_importances = rf_classifier.feature_importances_

importance_df = pd.DataFrame({'Feature': df.drop(columns  = ['satisfaction_v2']).columns, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=True)
importance_df = list(importance_df['Feature'].values)[0:5]
for f in importance_df:
    del df[f]
print(importance_df)



# Create a PCA model
pca = PCA(n_components=1)
# Apply PCA 

new= pca.fit_transform(df.drop(columns = ['satisfaction_v2']))
with open('pca.pickle', 'wb') as handle:
    pickle.dump(pca, handle, protocol=pickle.HIGHEST_PROTOCOL)

# add new column
df['pca_column'] = new


# =========================================
minmaxes = {}
#: Normalize
for i in df.columns:
    if i != 'Flight Distance':
        minmaxes[ i ] = {'min': df[i].min(), 'max': df[i].max()}
with open('minmaxes.json', 'w') as f:
    json.dump(minmaxes, f)
# =========================================


#: Row aging
"""

new = []
now = 2023
for y in df['year'].unique():
    yearly = df[ df['year'] == y ]
    
    ratio = 1.0 - (now - y) / 10.0
    yearly = yearly.sample(frac = ratio)

    new.append( yearly )
df = pd.concat( new )

"""

#: Re-balancing
# iptal

#: Shuffling, sub-sampling
# -- shuffle
# -- sample only some part of the dataset
df = df.sample(frac = 1.0)




#: Problem representation: splitting etc
#! for students


#: Modelling
rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)

print(df.drop(columns = ['satisfaction_v2']).columns)
import sys
sys.exit(1)
rf_classifier.fit(df.drop(columns = ['satisfaction_v2']), df['satisfaction_v2'])



# -- train test



#: Testing

#: Error modeling
# -- error relating
# -- threshold
# -- cost matrix



#: Saving to pickle, saving the constants

with open('rf_classifier.pickle', 'wb') as handle:
    pickle.dump(rf_classifier, handle, protocol=pickle.HIGHEST_PROTOCOL)
