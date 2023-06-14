import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

# Load the example diamonds dataset
diamonds = sns.load_dataset("diamonds")

print(diamonds)
"""
# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds, ax=ax)

plt.show()
"""

data1 = [100, 120, 90, 80, 140, 150, 160, 20, 80, 90, 120]
data2 = [190, 220, 190, 180, 240, 170, 200, 50, 150, 150, 175]
#plt.plot(data1)
#plt.plot(data2)
#plt.show()


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# Create the data
rs = np.random.RandomState(1979)
x = rs.randn(500)
g = np.tile(list("ABCDEFGHIJ"), 50)
df = pd.DataFrame(dict(x=x, g=g))
print(df)


# df['g'] = df.g

import sys
print(g)
m = df.g.map(ord)
print(m)
df["x"] += m


sys.exit(1)


unit = {
    'km': 1000,
    'mile': 1620
}

#: Empty data frame, with columns
df = pd.DataFrame(columns = ['distance', 'unit'])
#: df's row at "loc" [number] = [values!]
df.loc[len(df)] = [10, 'km'] # 10 ==> distance, 'km' ==> unit
df.loc[len(df)] = [20, 'mile']
df.loc[len(df)] = [10, 'mile']
df.loc[len(df)] = [50, 'km']
print(df)


df['distanceInMeters'] = df['distance'] * df['unit'].map(unit)
print(df)


print(ord('Z'))


