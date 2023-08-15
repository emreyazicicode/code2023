
#: Imports
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
#!

#: Filling empties, drop + fillwith0 + fillwithmean + fillwithmode
#! 

#: Normalize
#!

#: Transform
# -- type casting
# -- log, sqrt
# -- dummy

#: Feature mining + tenure
# -- merging
# -- creating new
# -- heatmap

#: Feature elimination
# -- intercorrelation
# -- low corelation
# -- unique
# -- same

#: Data aging
# iptal

#: Re-balancing
# iptal

#: Shuffling, sub-sampling
# -- shuffle
# -- sample only some part of the dataset




#: Problem representation: splitting etc

#: Modelling

#: Testing

#: Error modeling

#: Saving to pickle, saving the constants
