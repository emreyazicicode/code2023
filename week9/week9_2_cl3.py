import math
import warnings
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

warnings.filterwarnings("ignore")

classnames = {
    0:'Rock',
    1:'Indie',
    2:'Alt',
    3:'Pop',
    4:'Metal',
    5:'HipHop',
    6:'Alt',
    7:'Blues',
    8:'Acoustic_Folk',
    9:'Instrumental',
    10:'Country',
    11:'Indie'
}

# MULTI CLASS CLASSIFICATION

# 12 different classifiers
# 0: Rock mi degil mi? (other)   [1/0]
# 1: Indie, other                [1/0]
# 2: Alt                         [1/0]

train = pd.read_csv("week9_music_train.csv")
train = train.fillna(0)

del train['Artist Name']
del train['Track Name']

train['Class'] = train['Class'].map(classnames)

print(train['Class'].value_counts())
print(train)

cols = list(train.columns)
cols.remove('Class')

dfx = pd.DataFrame(columns = cols)

#: Loop for each group to find means of each group! (class)
for g in train.groupby( by = ['Class'] ):
    print(g[0], g[1].mean().to_dict())
    #: From the dictionary get only the values and append it to a "new" dataframe
    dfx.loc[ len(dfx) ] = g[1].mean().to_dict().values()

print(dfx)
dfx.to_csv("week9_2_dfx.csv")

proportion = train['Class'].value_counts(normalize=True).to_dict()



for cls in list(set(list(classnames.values()))):
    # Rock
    copied = train.copy()
    copied[ 'Class' ] = copied[ 'Class' ].apply(lambda value: 1 if value == cls else 0) # if class == rock 1, else 0
    # copied.to_csv(f"week9_2_music_{cls}.csv" )

    limit = int(len(copied) * 0.70)
    tr = copied[:limit]
    te = copied[limit:]

    #: REBALANCING
    # ASSIGNMENT - 1:
    # ASSIGN THE VALUE OF FRAC IN REBALANCING, ACCORDING TO PROPRTION OF THE DATASET, DYNAMICALLY
    # [12 July]

    # ASSIGNMENT - 2:
    # TRY TO USE THE COLUMN ARTIST NAME IN A WAY, WHICH BECOMES USEFUL
    # [14 July]

    #! p = 0.15
    p = math.sqrt(proportion[ cls ])
    #p = math.pow( proportion[cls], 0.5) # 0.4, 0.6

    tr1 = tr[ tr['Class'] == 1 ]
    tr0 = tr[ tr['Class'] == 0 ].sample(frac = p) # rebalancing
    #! tr0 = tr[ tr['Class'] == 0 ].sample(n = len(tr1)) # rebalancing

    tr = pd.concat( [tr0, tr1] )
    tr = tr.sample(frac = 1.0) # shuffle

    print("PROPORTION", cls, p, "RATIO", len(tr0) / len(tr1))

    clf = RandomForestClassifier(max_depth=5, random_state=0) #  dummy model, temporary
    y = tr['Class']
    del tr['Class']
    clf.fit(tr, y)

    te_y = te['Class']
    del te['Class']

    print( cls, f1_score(te_y, clf.predict(te)) )


# HOW TO DECIDE SOMETHING
# 

"""
DYNAMIC RATIO
Rock 0.5506072874493928
Pop 0.689419795221843
Metal 0.5783132530120483
HipHop 0.6936829558998807
Alt 0.499774062358789
Blues 0.9048843187660668
Acoustic_Folk 0.5883306320907616
Instrumental 0.4907275320970043
Country 0.5063291139240507
Indie 0.004728132387706856
"""


"""
AFTER
Rock 0.46554364471669213
Pop 0.6239554317548747
Metal 0.5602094240837695
HipHop 0.5864045864045864
Alt 0.42585692995529056
Blues 0.8841607565011821
Acoustic_Folk 0.4603555982700625
Instrumental 0.3851560303626651
Country 0.48923679060665365
Indie 0.20790513833992094
"""

"""
BEFORE
Rock 0.024390243902439022
Indie 0.0
Alt 0.018803418803418803
Pop 0.1037037037037037
Metal 0.0
HipHop 0.5392156862745099
Alt 0.00859106529209622
Blues 0.8732394366197183
Acoustic_Folk 0.4099037138927098
Instrumental 0.09725685785536159
Country 0.0
Indie 0.0
"""