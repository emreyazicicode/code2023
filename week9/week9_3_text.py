import re
import pandas as pd
import warnings
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
data = pd.read_csv("week9_music_train.csv")
data = data.fillna(0)
data = data[ ['Track Name', 'Class'] ]
data['Class'] = data['Class'].map(classnames)

data['Feat'] = data['Track Name'].apply(lambda value: 'feat' in value.lower())
data['Length'] = data['Track Name'].apply(lambda value: len(value))
data['WordCount'] = data['Track Name'].apply(lambda value: len(value.split(' ')))
data['ng'] = data['Track Name'].apply(lambda value: "n'" in value)
data['Remix'] = data['Track Name'].apply(lambda value: 'remix' in value.lower())
data['Invalid'] = data['Track Name'].apply(lambda value: '◊' in value.lower())



data.to_csv("week9_3_sample.csv")

def letterRatio( text: str ) -> float:
    return len(re.sub("[^a-zA-Z\s]", "", text)) / len(text)

data['LetterRatio'] = data['Track Name'].apply(letterRatio)


df = pd.DataFrame(columns = ['Class', 'Feat', 'Length', 'WordCount', 'ng', 'LetterRatio', 'Remix', 'Invalid'])


for g in data.groupby( by = ['Class']):
    df.loc[len(df)] = [ 
        g[0], 
        g[1]['Feat'].mean(), 
        g[1]['Length'].mean(), 
        g[1]['WordCount'].mean(),
        g[1]['ng'].mean(),
        g[1]['LetterRatio'].mean(),
        g[1]['Remix'].mean(),
        g[1]['Invalid'].mean(),
    ]

print(df)
"""
def pattern( text: str ) -> str:
    text = re.sub("[A-Z\s]", "", text)
    text = re.sub("[a-z]", "", text)
    text = re.sub("[0-9]", "", text)
    return text

for t in data['Track Name'].values:
    print( pattern(t) )
"""

# AFTERNOON, Think how can we use the textual information (Track Name)



