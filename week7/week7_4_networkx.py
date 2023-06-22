
#: Imports
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random
import pandas as pd
import itertools


#: Set the path
path = "week7_Sales Transaction v.4a.csv"
#: Read the file
df = pd.read_csv(path, parse_dates=['Date'])

#: Get the frequency of each product!
product_freq = dict( df['ProductName'].value_counts() )

#: Get the frequency of two product combinaions
product_product_freq = {}

for g in df.groupby('TransactionNo'):
    #: Get the products in this basket!
    products_in_this_transaction = list(set(g[1]['ProductName'].tolist()))
    if len(products_in_this_transaction) > 2 and len(products_in_this_transaction) < 100:
        for comb in list(itertools.combinations(products_in_this_transaction, 2)):
            key = "|".join(comb)
            if key not in product_product_freq:
                product_product_freq[key] = 1
            else:
                product_product_freq[key] += 1


recommendation = pd.DataFrame( columns = ['P1', 'P2', 'A', 'B', 'AnB', 'AuB', 'Jaccard'])

for k in product_product_freq:
    AnB = product_product_freq[k]
    A, B = k.split("|")
    A = product_freq[A]
    B = product_freq[B]
    AuB = A + B - AnB
    jaccard = AnB / AuB

    if jaccard > 0.10 and AuB > 5:
        names = k.split("|")
        recommendation.loc[ len(recommendation ) ] = [ names[0], names[1], A, B, AnB, AuB, jaccard ]

#: Limit the rows so that it can fit to screen
recommendation = recommendation[ recommendation['Jaccard'] > 0.25 ]
print(len(recommendation))


def nameToShorter(s):
    result = hashlib.md5(s.encode())
    return (result.hexdigest())


G = nx.Graph()

l1 = list(recommendation['P1'].unique())
l1.extend( list(recommendation['P2'].unique()) )
l1 = list(set(l1))

for i in l1:
    G.add_node(nameToShorter(i))


"""
G.add_node(1)
G.add_node("emre")
G.add_nodes_from([2, 3])

G.add_edge(1, 2)
"""

for i in range(len(recommendation)):
    row = recommendation.iloc[i].to_dict()
    G.add_edge(   nameToShorter(row['P1']), nameToShorter(row['P2']), weight = row['Jaccard'], length = row['Jaccard'] * 2  )

nx.draw(G,  font_color='red', font_size=7)

plt.show()