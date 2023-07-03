from sklearn import tree
import time
import pandas as pd
import matplotlib.pyplot as plt
path = 'week8_Customer-Churn-Records.csv'
target = 'Exited'

df = pd.read_csv(path)

#: Split the data set into INPUT/OUTPUT
y = df[target]
del df[target] # x1....xN

#: Remove the non-numerics FOR NOW!!!
df = df.select_dtypes(exclude = ['object'])

print("Y", type(y), y.shape)
print("X", type(df), df.shape)

# PRE-PROCESSING
# Tranformation
# Feature Selection
# Data selection
# Feature mining
# Normalization
# Filling
# Correcting
# Representing



# DECISION TREE CLASSIFIER ===> ALGORITMA!!!!!
# BU ALGORITMA SONUCUNDA, BIR MODEL CIKIYOR
clf = tree.DecisionTreeClassifier() # clf = classifier


print(time.time())
clf = clf.fit(df, y) # TRAIN!!!!, LEARN, WE BUILD MODEL HERE
print(time.time())

# y = real, gercek
# p = predicted, tahmin

predictions = clf.predict( df ) # WE USE THE MODEL HERE

print("P", predictions, type(predictions), predictions.shape)
print("Y", y.values, type(y.values), y.shape)


df['Y'] = y             # Y = REAL
df['P'] = predictions   # P = predictions
#! MEASUREMENT
df['C'] = df['P'] == df['Y'] # CORRECT OR NOT (tahmin ne kadar faiz gercek ile ayni)
df['C'] = df['C'].astype(int) # make it 0/1 instead of True/False
print(df)
print(df['C'].mean())
# 1.0 == %100 Harika ! degil

# NOTE: Cikan %100 sonuc, %100 hatalidir
# OVERFIT
# PROBLEM IS VERY VERY SIMPLE

