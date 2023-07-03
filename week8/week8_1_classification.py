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

from sklearn import tree
clf = tree.DecisionTreeClassifier() # clf = classifier

# DECISION TREE CLASSIFIER ===> ALGORITMA!!!!!
# BU ALGORITMA SONUCUNDA, BIR MODEL CIKIYOR

print(time.time())
clf = clf.fit(df, y) # TRAIN!!!!, LEARN
print(time.time())
# 50 milliseconds

tree.plot_tree(clf)
#plt.show()

print(df.columns)

text_representation = tree.export_text(clf)
for i in range(len(df.columns) - 1, 0, -1):
    text_representation = text_representation.replace(f"feature_{i}", df.columns[i])

print(text_representation)


fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf, 
                   feature_names=list(df.columns),  
                   class_names=["NoC", "Churn"],
                   filled=True)
#plt.show()




import graphviz
# DOT data
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=list(df.columns),  
                                class_names=["NoC", "Churn"],
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png") 
graph.render('dtree_render',view=True)
plt.show()

def predict( x ):
    if x['Complain'] == 0 and x['Points'] < 184: return 1
    #if x[ ////] : return 0
    return 0
