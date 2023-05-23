
import re

# Regular expression
# Reg     Ex 
# R       E    

# Universal Bir Dil
# Java, C, C#, Php, Javascript, Python....

# GOAL IS TO:
# - STRING MATCHING
# - STRING REPLACING
# - STRING SPLITTING

# [DYNAMIC] MATCH, REPLACE, SPLOT

news = """
Drones strike Russian border region of Belgorod, governor says

From CNN’s Mariya Knight and Josh Pennington 

test 12.12.2005 test

Belgorod in southwestern Russia was hit by drone attacks overnight, its governor said, as the border region reels from an incursion claimed by anti-Putin Russians aligned with the Ukrainian army.

In a series of 06-06-2000 Telegram post late Monday and early Tuesday, Belgorod Gov. Vyacheslav Gladkov said two homes were struck by drones in the town of Grayvoron — the site of an earlier attack claimed by pro-Ukraine Russian volunteers.
"“The houses caught fire after explosive devices were dropped from the UAV,” Gladkov said."
In the village of Borisovka, Gladkov said explosive devices were dropped from drones onto an administrative building and a house in two separate attacks.
No casualties were reported in any of the drone incidents, the governor said.
No one has claimed responsibility klm35213@hotmail.com for the alleged drone attacks. 
Russian partisans: Earlier Monday, Gladkov said most of Grayvoron's residents had evacuated the town after eight people were injured in an attack by a "sabotage group" linked to the Ukrainian army.
The Freedom of Russia Legion and Russian Volunteer Corps earlier claimed they had "fully liberated the settlement of Kozinka" and "entered Grayvoron," after crossing from Ukraine into Belgorod on Monday.
A Ukrainian official said the group was made up of Russian nationals and insisted they were acting independently.
His email address was yaziciemre@gmail.com so that .....
They paid 500$.
"""

# news = news.replace(".", " ")
# news = news.replace(",", " ")
# news = news.replace('"', " ")
# news = news.replace('\n', " ")

# print(news.split(" "))

# Regex pattern
# Consists of 2 types of element
# - What to match?
# - How?

# \s = " "
# \n = new line
# \t = "    "

# Modifier 
# [abc] -->  one of them
# [^abc] --> none of them
# A-Z    --> ABCDEFG....Z
# a-z    --> abcdef.....z
# 0-9    --> 0123456789

# +      --> ONE OR MORE
# *      --> ZERO OR MORE -- any count 0, 1, 2,3 ,... 3000
# ?      --> ZERO OR ONE

parts1 = re.split("[\s\.\,\n\”\"]", news) # === news.split(" ")
parts2 = re.split("[^A-Za-z0-9]", news)   # === news.split(" ")
print(parts2)


# REPLACE
# sub( FIND, REPLACE, INSIDE )
print( re.sub( "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com", "<email>", news) )



# yaziciemre@gmail.com


# ^([a-zA-Z0-9\_\.\-]+)@([a-zA-Z0-9]+)\.[a-zA-Z0-9]+$
# ^([a-zA-Z0-9\_\.\-]+)@([a-zA-Z0-9]+)\.[a-zA-Z0-9]+$
# Baglangic
#                                                   Bitis
# (isim kismi         )@(domain kismi) .(com/net   )
"""
yaziciemre@gmail.com
y@ga.com
y@y.c
0@0.net
emre_yazici84@hotmail.com
ahmetov193842@wewrw.com
emre.yazici@gmail.com
.23.hamid@gmail.com
_dsadf@gma.com
32433-dasfs.@adfs.com
AHmetov193842@wewrw.com.tr
AHMET_323-ewriijo@axc.code.az
__.hotma@fdas.com
@gmail.com

"""


# REGEX IS USED FOR DATA VALIDATION


# Month
# 10
# 11
# 12
# 1...9

# 1?[0-9]
# OLABILIR      1
# OLMAYABILIR   0
# var / yok
# True / False




# 1?[0-9]
# [0-9]
# 1[0-9]



# DAY
# 31, 30... 29... 19, 0-9

# [123]?[0-9]


# [123]?[0-9][\.\/\-]1?[0-9][\.\/\-]([12])[0-9]{3}
# 1?[0-9][\.\/\-][123]?[0-9][\.\/\-]([12])[0-9]{3}

items_to_test = [
    "12.12.2022",
    "6/5/1956",
    "06-06-1999",
    "18-6-2005",
    "45-12-2007",
    "45-12-20047",
    "04.05.4007",
    "04.05.200",
    "4.05.2007",
    "04.5.2007",
    "4.5.2007",
    "8.9.5007",
    "8.9.3007"
]


pattern = "[0123]?[0-9][\.\/\-][01]?[0-9][\.\/\-][12][0-9]{3}"
#                                                   2000
# match == pattern & extract == paranthesis


for item in items_to_test:
    print(item, re.match(pattern, item))


q = re.findall(pattern, news)
print(q)



# $ == end of line
# ^ == begin of line

# . == ANYTHING!!!!
# .* == ANY COUNT of ANYTHING [everything]

# His email address was yaziciemre@gmail.com so that .....


# Sitemize kayit olmak icin, email adresinizi giriniz
# yaziciemre@Gmail.com emre


s = "emre yazici"
s.startswith("emre")

# [0-9] = \d
