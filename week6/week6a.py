
import sys
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Telecom_customer churn.csv", nrows = 10000)

for c in df:
    print(c, df[c].dtype, df[c].nunique())

target = 'totcalls' # total number calls

# most basic
"""
for c in df.select_dtypes( exclude = ['object'] ):
    print(c)
    plt.title(c)
    plt.hist(df[c])
    plt.show() # jupyter kullaniyorsaniz, buna gerek yok
"""

"""
for c in df.select_dtypes( include = ['object'] ): # categorical
    print(c, df[c].dtype)
    if df[c].nunique() < 50:
        plt.title(c)
        plt.hist(df[ df[c].notnull() ][c] ) # skips the null values
        plt.show() # jupyter kullaniyorsaniz, buna gerek yok
"""


a = 'x'
if a in ['x', 'y', 'z']:
    print('ok')

# For the categorical variables, show only first 5 




def findBestNumberForPieChart( valuecounts: dict, total: int ) -> int:
    # all ranges = 0 to N-1
    for i in range(5, len(valuecounts)):
        ss = list(valuecounts.values)
        ss = ss[0:i]
        ratio = sum(ss)/ total
        if ratio > 0.85:
            return i
    return 5

# [a,b,c,d,e, f,g,h,i,j]  10 items 
# 0                   9


# DYNAMIC
"""
for c in df.select_dtypes( include = ['object'] ): # categorical
    
    cardinality = df[c].nunique() / len(df)
    if cardinality < 0.95:
        # It is not useful to plot a "UNIQUE" variable in a graph

        print(c, df[c].dtype, cardinality)
        
        data = df[c]  # skips the null values
        data = data.value_counts()
        N = findBestNumberForPieChart( data, len(df[ df[c].notnull() ]) )
        topNitems = list(data.keys())[0:N]
        data2 = df[ df[c].isin(topNitems) ][c]  # skips the null values, and take only top 5 items
        data2 = data2.value_counts()
        data2 = dict(data2)


        length = df[c].nunique()
        if length > N:
            data2['others'] =  len(df[ (~df[c].isin( topNitems )) & df[c].notnull() ] )
            # len(df[ (~df[c].isin( top5items )) & df[c].notnull() ] )
            # top 5 olmayanlar : (~df[c].isin( top5items ))
            # null olmayanlar  : df[c].notnull()
            # length ini alalim
        # ~ PANDAS NOT 

        nulls = len(df[ df[c].isnull() ]) # number of nulls in "c" columns
        if nulls > 0:
            data2['nulls'] = nulls

        plt.title(c)
        plt.pie( data2.values(), labels=data2.keys() )
        plt.show() # jupyter kullaniyorsaniz, buna gerek yok
"""


from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="white")
# Compute the correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.show()



