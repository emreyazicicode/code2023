import math
import warnings
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.neural_network import MLPClassifier

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


train = pd.read_csv("week9_music_train.csv")
train = train.fillna(0)
train = train.sample(frac = 1.0)

del train['Artist Name']
del train['Track Name']

train['Class'] = train['Class'].map(classnames)

train.to_csv("week9_3_mlp.csv")

y = train['Class']
del train['Class']

# PARAMETER TUNING
for hls1 in [30, 45, 50, 55, 70]:
    for hls2 in [30, 45, 50, 55, 70]: # try to avoid

        clf = MLPClassifier(random_state=1, max_iter=1000, hidden_layer_sizes=(hls1, hls2,))
        clf.fit(train, y)
        print( hls1, hls2, clf.score(train,y))




