
import pandas as pd

df = pd.read_csv("week9_shoes2.csv")

print(df)

for c in df:
    print(c, df[c].nunique())



price = 'prices.amountAvg'

for g in df.groupby(by = ['id']):
    id = g[0]
    dt = g[1]
    print(id, dt[price].mean(), dt[price].std(), len(dt))



ELIMINATE = [
    'womens', 'shoes', 'womens shoes', 'all womens shoes', 'womens footwear',
    'clothing', 'womens footwear', 'womens dress shoes', 'womens clothing',
    'all mens shoes'
             ]

def cleanup( cat: str, brn: str ) -> str:
    
    # croft barrow	==> croft,barrow
    brn2 = brn.replace(" ", ",")

    result = cat.replace(","+brn, "") # replace the brand names in category
    result = result.replace(","+brn2, "") # replace the brand names in category 

    # 'womens,shoes,sandals,clothing,womens shoes,all womens shoes'
    result = result.split(",")
    result = [r for r in result if r not in ELIMINATE]
    # ['womens','shoes','sandals','clothing','womens shoes','all womens shoes']
    result = ",".join(result)
    # 'womens,shoes,sandals,clothing,womens shoes,all womens shoes'

    return result

print( df['categories'].nunique() )
df['categories'] = df['categories'].str.lower()
df['categories'] = df['categories'].str.replace("'", "") # quote removal
df['categories'] = df.apply(
    lambda row: 
    cleanup(row['categories'], row['brand']),
    axis = 1
)


# croft barrow	
# Womens,Shoes,Boots,Croft,Barrow
# print( df['categories'].nunique() )
# categories = list(df['categories'].value_counts().to_dict().keys())
"""
['boots', 'pumps,heels', 'sandals', 'flats', 'athletic shoes,sneakers', 'clogs,mules', 'loafers', 'pumps,heels,womens dress shoes', 'athletic shoes,sneakers,womens casual shoes,womens athletic shoes', 'womens casual boots & shoes,womens casual shoes', 'athletic shoes,sneakers,womens casual shoes', 'sandals,boots', 'pumps,heels,womens boots', 'sandals,lifestride', 'pumps,heels,flats,comfort', 'womens running shoes,womens road running shoes', 'womens running shoes,women
"""

"""
for c in categories:
    print( c )
"""

#print( "\n".join( categories ) )


"""
boots
pumps,heels
sandals
"""


def parseUnit( text ) -> float:
    text = str(text)
    if text == "nan": return 0
    if text == "": return 0

    if "lb" in text and "oz" in text:
        # 3 lb 2 oz
        parts = text.split(" ")
        return float(parts[0]) * 453 + float(parts[2]) * 28
    
    if "lbs" in text:
        # 2.0
        text = text.replace("lbs", "").strip()
        units = float(text)
        return units * 453
    if "lb" in text:
        # 2.0
        text = text.replace("lb", "").strip()
        units = float(text)
        return units * 453
    if "oz" in text:
        text = text.replace("oz", "").strip()
        units = float(text)
        return units * 28
    if "g" in text:
        text = text.replace("g", "").strip()
        units = float(text)
        return units

    return 0



import re

weights = list(df['weight'].unique())
weights = [re.sub("[0-9\.]", "", str(w)) for w in weights]
weights = list(set(weights))
# print(weights)

df['weight'] = df['weight'].apply( parseUnit )

#! AFTERNOON EXERCISE, use the function from previous lectures to make this variable (category) dummy, with only 5 top most item, keep them others as "OTHER"

df.isnull().astype(int).to_csv("week10_2_nulls.csv")
#df.isnull().corr().to_csv("week10_2_corr.csv")

for c in df:
    print(c, df[c].nunique())

df.corr().to_csv("week10_2_correlation.csv")

df.to_csv("week10_2_processed.csv")

# Create a new dataframe with only items whose weight is KNOWN!!!!, not null
da = df[ df['weight'] > 0 ]
# There cannot be a shoe with "0 grams"
print( da[price].corr(da['weight']) )


# because there are only 300 items in the dataset (weight>0), the correlation may not be consistent
# Correlation ( price, weight                )      == 0.19  # the zeros in this are problem!! (0 == null, unknown)
# Correlation ( price, weight == null        )      == 0.39  # if there "weight" information, the price gets higher
# Correlation ( price, weight ) for only weight > 0 == -0.75 # if there "weight" information, the prices correlated to "NEGATIVE" weight

# Business insight, business fact

#: delete the items, which have not got upcs, we lost 360 items
df = df[ df['upc'].notnull() ]


print(df.shape)
for c in df:
    filled = len(df) - sum(df[c].isnull())
    print(c,"RATIO:", filled / len(df), "# UN", df[c].nunique())

print(df.corr())


"""
colors = ['Black', 'Gray']

df['prices.color'] = df['prices.color'].apply(lambda value: value if value in colors else 'Other' )

for c in df.groupby(by = ['prices.color']):
    print(c[0], c[1][price].mean(), len(c[1]))
"""



brand_cat = {}
for b in df.groupby(by = ['brand']):
    brand_cat[ b[0] ] = b[1]['categories'].nunique()
    print(b[0], b[1]['categories'].nunique())

df['brand_#_cat'] = df['brand'].map( brand_cat )
print(df['brand_#_cat'].corr(df[price]))



# AFTERNOON EXERCISE 2: Plot the heatmap

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

pivot = df.pivot("brand", "categories", price)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(pivot, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()

