import json
import pandas as pd
from colorutils import Color
import re

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 927: invalid start byte

# error_bad_lines = False
# encoding = 'utf-8'
# engine = 'c'

df = pd.read_csv("week9_gender_classifier.csv", encoding = "ISO-8859-1")

#: Discard golden
df = df[ df['_golden'] == False ]
#: Remove unused
del df['_golden']
del df['_unit_state']
del df['gender_gold']
del df['profile_yn_gold']
del df['tweet_coord']
del df['profile_yn']
del df['_trusted_judgments']
del df['retweet_count']
del df['tweet_id']
del df['tweet_created']

#: Only "valid, confident" items
df = df[ df['gender:confidence'] > 0.50 ]
del df['gender:confidence']

#: Only "valid, confident" items
df = df[ df['profile_yn:confidence'] > 0.80]
del df['profile_yn:confidence']

#: Yes No to 1/0
#for c in ['profile_yn']:
#    df[c] = df[c].map({'yes': 1, 'no': 0})




# description
# text

print(df.columns)

print(df['link_color'].nunique())

def hex2rgb(hex_value):
    while len(hex_value) < 6:
        hex_value = "0" + hex_value
    if len(hex_value) != 6:
        hex_value = "000000"
    h = hex_value.strip("#") 
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb





# sidebar_color
# link_color

df['sidebar_color_H'] = df['sidebar_color'].apply(lambda value: Color(hex2rgb(value)).hsv[0])
df['link_color_H'] = df['link_color'].apply(lambda value: Color(hex2rgb(value)).hsv[0])

df['sidebar_color_S'] = df['sidebar_color'].apply(lambda value: Color(hex2rgb(value)).hsv[1])
df['link_color_S'] = df['link_color'].apply(lambda value: Color(hex2rgb(value)).hsv[1])

df['sidebar_color_V'] = df['sidebar_color'].apply(lambda value: Color(hex2rgb(value)).hsv[2])
df['link_color_V'] = df['link_color'].apply(lambda value: Color(hex2rgb(value)).hsv[2])

most_side_bar = df['sidebar_color'].mode()[0]
df['sidebar_color_ismost'] = df['sidebar_color'] == most_side_bar

most_link = df['link_color'].mode()[0]
df['link_color_ismost'] = df['link_color'] == most_link

print(df['sidebar_color_ismost'].mean())
print(df['link_color_ismost'].mean())

del df['sidebar_color']
del df['link_color']

del df['sidebar_color_H']
del df['sidebar_color_S']
del df['sidebar_color_V']
del df['link_color_V']

# 
# 
# 0123456789ABCDEF
# a = 10
# b = 11
# c = 12

#: Load the first public dataset from json file and convert it to "key-value: key==name, value==gender"
names = json.load(open('week9_fb-gender.json'))
names = {k.lower():v['most_likely'] for k,v in names.items()}

names2 = json.load(open('week9_names.json'))
for n in names2:
    names[ n['name'].lower() ] = n['gender']


def name_analyze( name: str ) -> str:
    # cleanup
    name2 = re.sub("[^a-z]", "", name.lower())
    if name2 in names:
        return names[name2]

    # Camelcaps
    name = re.sub(r"([a-z])([A-Z])", r"\1_\2", name)

    # paul_hembo
    parts = re.split("[\-\_]", name)
    for p in parts:
        if p.lower() in names:
            return names[p.lower()]

    # EmpireGameNews
    # ['Empire', 'Game', 'News']

    
    """
    for i in range(len(name)):
        if i < len(name) - 1:
            if name[i].islower() and name[i+1].isupper():
                .....
    """ 


    return None


df['name_analyze'] = df['name'].apply( name_analyze )
del df['name']


# 0-9, _\,! ==
# "AbcdEfgh" ==> "abcdefgh" ==> isim


"""
[
  {
    "name": "Aaron",
    "gender": "male",
    "country": "gb"
  },
"""


"""
def extractInfo( d: dict ) -> str:
    if 'M' not in d: return 'female'
    if 'F' not in d: return 'male'
    if d['M'] > d['F']: return 'male'
    return 'female'

names3 = json.load(open('week9_first_names.json'))
names3 = {k:extractInfo(v['gender']) for k,v in names3.items() if ' ' not in k}
print(names3)
"""
"""
{
  "Ahmet":  {
      "F": 0.145,
      "M": 0.855
    },

"""

name = "EmreYazici"
print( re.split("[A-Z]", name) )
# Zeka = sorun cozebilmek # of problems
# Zeka = how many different ways you can think

print( re.sub(r"([a-z])([A-Z])", r"\1_\2", name) )

"""
name = "EmreYazici"

name_parts = re.findall(r'[A-Z][a-z]+', name)

print(name_parts)
"""


df = pd.get_dummies( df, columns = ['gender'])



#: Convert to date time
df['created'] = pd.to_datetime( df['created'] )
print(df.dtypes)
print(df['created'].max())
print(df['created'].min())

today = df['created'].max()
df['dayspassed'] = (today - df['created']).dt.days
df['tweet_per_day'] = df['tweet_count'] / (1+df['dayspassed'])
del df['created']
# distance between two dates is "time range"

print(df[ ['dayspassed', 'tweet_per_day', 'tweet_count'] ])


for c in df.select_dtypes(exclude = ['object', 'datetime']):
    if 'gender' not in c:
        print(c, df[c].corr(df['gender_brand']))
        print(c, df[c].corr(df['gender_female']))
        print(c, df[c].corr(df['gender_male']))
        print(c, df[c].corr(df['gender_unknown'])) # bot account, robot

# beyler, erkekler, twittera daha once register olmaya basladi!
# firmalar/brand/company cok daha yeni

df.to_csv("week9_4_gender-out.csv")



print( df[ df['gender_brand'] == 1 ].sample(10)['description'].values )
# dataframe icinde, brand'in 1 olanlarinin, 10 tane rasgele row secip, icinden description kolonlarinin, degerlerini goster
print('===========================')
print( df[ df['gender_brand'] == 0 ].sample(10)['description'].values )
