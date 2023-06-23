import pprint
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

pp = pprint.PrettyPrinter()

data = {}
data['habiba'] = {}
data['adil'] = {}
data['Riyad'] = {}
data['Mahizar'] = {}
# data['rafiq'] = {}
data['lala taghiyeva'] = {}
data['anar'] = {}
data['Lala'] = {}
data['madina'] = {}
data['Riyad Abdurahimov'] = {}
data['yusif'] = {}
data['ilyas']={}


data['ilyas']['T'] = 77
data['ilyas']['H'] = 71
data['ilyas']['E'] = 149
data['ilyas'][' '] = 99
data['ilyas']['Q'] = 113
data['ilyas']['I'] = 84
data['ilyas'][' '] = 159
data['ilyas']['U'] = 89
data['ilyas']['I'] = 115
data['ilyas']['C'] = 121
data['ilyas']['K'] = 96
data['ilyas'][' '] = 95
data['ilyas']['B'] = 89
data['ilyas']['R'] = 106
data['ilyas']['O'] = 79
data['ilyas']['W'] = 102
data['ilyas']['N'] = 80

data['Riyad']['T'] = 111
data['Riyad']['H'] = 104
data['Riyad']['E'] = 112
data['Riyad']['Q'] = 120
data['Riyad']['U'] = 80
data['Riyad']['I'] = 80
data['Riyad']['C'] = 88
data['Riyad']['K'] = 64
data['Riyad']['B'] = 56
data['Riyad']['R'] = 96
data['Riyad']['O'] = 96
data['Riyad']['W'] = 88
data['Riyad']['N'] = 64

data['Mahizar']['T'] = 80
data['Mahizar']['H'] = 24
data['Mahizar']['E'] = 120
data['Mahizar']['Q'] = 112
data['Mahizar']['U'] = 72
data['Mahizar']['I'] = 72
data['Mahizar']['C'] = 112
data['Mahizar']['K'] = 112
data['Mahizar']['B'] = 88
data['Mahizar']['R'] = 96
data['Mahizar']['O'] = 72
data['Mahizar']['W'] = 88
data['Mahizar']['N'] = 104

"""
data['rafiq']['T'] = 94
data['rafiq']['H'] = 96
data['rafiq']['E'] = 112
data['rafiq']['Q'] = 112
data['rafiq']['U'] = 55
data['rafiq']['I'] = 55
data['rafiq']['C'] = 113
data['rafiq']['K'] = 95
data['rafiq']['F'] = 112
data['rafiq']['O'] = 64
data['rafiq']['X'] = 78
data['rafiq']['X'] = 78
data['rafiq']['X'] = 63
"""

data['lala taghiyeva']['T'] = 96
data['lala taghiyeva']['H'] = 112
data['lala taghiyeva']['E'] = 112
data['lala taghiyeva'][' '] = 95
data['lala taghiyeva']['Q'] = 87
data['lala taghiyeva']['U'] = 96
data['lala taghiyeva']['I'] = 79
data['lala taghiyeva']['C'] = 88
data['lala taghiyeva']['K'] = 48
data['lala taghiyeva'][' '] = 71
data['lala taghiyeva']['B'] = 80
data['lala taghiyeva']['R'] = 112
data['lala taghiyeva']['O'] = 80
data['lala taghiyeva']['W'] = 87
data['lala taghiyeva']['N'] = 48

data['anar']['T'] = 101
data['anar']['H'] = 104
data['anar']['E'] = 86
data['anar'][' '] = 72
data['anar']['Q'] = 99
data['anar']['U'] = 116
data['anar']['I'] = 83
data['anar']['C'] = 90
data['anar']['K'] = 92
data['anar'][' '] = 90
data['anar']['B'] = 72
data['anar']['R'] = 78
data['anar']['O'] = 80
data['anar']['W'] = 93
data['anar']['N'] = 83

data['Lala']['T'] = 106
data['Lala']['T'] = 107
data['Lala']['H'] = 80
data['Lala']['E'] = 81
data['Lala'][' '] = 72
data['Lala']['Q'] = 96
data['Lala']['U'] = 80
data['Lala']['I'] = 79
data['Lala']['C'] = 57
data['Lala']['K'] = 72
data['Lala'][' '] = 112
data['Lala']['B'] = 96
data['Lala']['R'] = 104
data['Lala']['O'] = 88
data['Lala']['W'] = 88
data['Lala']['N'] = 88



data['madina']['T'] = 32
data['madina']['H'] = 96
data['madina']['E'] = 120
data['madina'][' '] = 97
data['madina']['Q'] = 72
data['madina']['U'] = 54
data['madina']['I'] = 57
data['madina']['C'] = 48
data['madina']['K'] = 47
data['madina'][' '] = 48
data['madina']['B'] = 73
data['madina']['R'] = 48
data['madina']['O'] = 65
data['madina']['W'] = 63
data['madina']['N'] = 32

data['Riyad Abdurahimov']['T'] = 111
data['Riyad Abdurahimov']['H'] = 104
data['Riyad Abdurahimov']['E'] = 112
data['Riyad Abdurahimov'][' '] = 184
data['Riyad Abdurahimov']['Q'] = 161
data['Riyad Abdurahimov']['U'] = 87
data['Riyad Abdurahimov']['I'] = 160
data['Riyad Abdurahimov']['C'] = 137
data['Riyad Abdurahimov']['K'] = 95
data['Riyad Abdurahimov'][' '] = 143
data['Riyad Abdurahimov']['B'] = 96
data['Riyad Abdurahimov']['R'] = 104
data['Riyad Abdurahimov']['O'] = 104
data['Riyad Abdurahimov']['W'] = 96
data['Riyad Abdurahimov']['N'] = 88

data['yusif']['T'] = 95
data['yusif']['H'] = 103
data['yusif']['E'] = 78
data['yusif'][' '] = 102
data['yusif']['Q'] = 71
data['yusif']['U'] = 76
data['yusif']['I'] = 76
data['yusif']['C'] = 59
data['yusif']['K'] = 89
data['yusif'][' '] = 95
data['yusif']['B'] = 87
data['yusif']['R'] = 76
data['yusif']['O'] = 83
data['yusif']['W'] = 60
data['yusif']['N'] = 79

data['adil']['null'] = 1687498223988
data['adil']['T'] = 103
data['adil']['G'] = 16
data['adil'][' '] = 142
data['adil']['H'] = 81
data['adil']['E'] = 125
data['adil'][' '] = 77
data['adil']['Q'] = 145
data['adil']['U'] = 71
data['adil']['I'] = 104
data['adil']['C'] = 94
data['adil']['K'] = 68
data['adil'][' '] = 58
data['adil']['B'] = 74
data['adil']['R'] = 103
data['adil']['O'] = 133
data['adil']['W'] = 125
data['adil']['N'] = 88

data['habiba']['T'] = 47
data['habiba']['H'] = 64
data['habiba']['E'] = 40
data['habiba'][' '] = 56
data['habiba']['Q'] = 80
data['habiba']['U'] = 55
data['habiba']['I'] = 64
data['habiba']['C'] = 39
data['habiba']['K'] = 72
data['habiba'][' '] = 49
data['habiba']['B'] = 63
data['habiba']['R'] = 64
data['habiba']['O'] = 63
data['habiba']['W'] = 48
data['habiba']['N'] = 56

# DATA VALIDATION AND DATA CLEANING

letters = list("thequickbrown".upper())
letters.sort()
correct = ''.join(letters)

#: Remove the data for blanks!
for user in data:
    #: If space
    if ' ' in data[user]:
        del data[user][' ']
    #: If null
    if 'null' in data[user]:
        del data[user]['null']

    data[user] = {k:v for k,v in data[user].items() if k in letters}


#: Create a dataframe of all values
df = pd.DataFrame( columns = ['user', 'letter', 'time'] )
for user in data:
    for letter in data[user]:
        df.loc[ len(df) ] = [user, letter, data[user][letter] ]

df = df[ df['time'] > 16 ]
for i in [0.90, 0.95, 0.98, 0.99]:
    print(i, df['time'].quantile(i))
print(df.describe())


for g in df.groupby('user'):
    l = list(g[1]['letter'].unique())
    l.sort()
    l = ''.join(l)
    print(l == correct, g[0])

print(df)

df = df.pivot_table('time', ['user'], 'letter')
df.to_csv("week7_5_keystoke.csv")

weight = {}
# AYNI LETTER'I BASKA NEFERLERIN BASMA SURESI ARASINDAKI DEGISIM
weight['B'] = 13.1023939519741
weight['C'] = 31.3011762776359
weight['E'] = 29.6439477189465
weight['H'] = 25.7879464443794
weight['I'] = 28.9083190291464
weight['K'] = 20.7706086049057
weight['N'] = 21.1956256207394
weight['O'] = 19.8297297464736
weight['Q'] = 28.956707497416
weight['R'] = 20.3769031459194
weight['T'] = 26.3100395632196
weight['U'] = 17.7272261071648
weight['W'] = 21.4060314355133

# 32 + 32x31 = 1024
# WEIGHTED EUCLIDEAN DISTANCE
import random
import math

for _ in range(5):
    person1 = random.choice( list(data.keys()) )
    person2 = random.choice( list(data.keys()) )

    d1 = data[person1]
    d2 = data[person2]

    distance = 0
    for i in d1:
        distance += (d1[i] - d2[i]) * (d1[i] - d2[i])
        #* distance += math.pow(d1[i] - d2[i], 2)
        #* distance += (d1[i] - d2[i]) ** 2

    distance = math.sqrt(distance)
    print(person1, person2, distance)

print("---------------------")
da = pd.DataFrame(columns = ['u1', 'u2', 'distance'])

for person1 in data.keys():
    G.add_node( person1 )

for person1 in data.keys():
    for person2 in data.keys():

        if person1 > person2:
        

            d1 = data[person1]
            d2 = data[person2]

            distance = 0
            for i in d1:
                distance += (d1[i] - d2[i]) * (d1[i] - d2[i]) * weight[i]
                #* distance += math.pow(d1[i] - d2[i], 2)
                #* distance += (d1[i] - d2[i]) ** 2

            distance = math.sqrt(distance)
            print(person1, person2, distance)
            distance = distance / sum(weight.values())

            da.loc[ len(da) ] = [person1, person2, distance]
            G.add_edge( person1, person2, length = distance * distance * distance, weight = distance * distance * distance )




da.to_csv("week7_5_userdistance.csv")

pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G, pos)

# nx.draw(G,  font_color='red', font_size=12, with_labels = True)
#! nx.draw_networkx

plt.show()
