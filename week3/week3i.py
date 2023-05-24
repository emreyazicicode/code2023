

import re


words = [
    "oxu",
    "ahmet",
    "salaaaaaaaaaaaaam",
    "salaaam",
    "yaqshiiiiiiiiiiii",
    "lalalalalalla",
    "coooooooooooq",
    "emre ssssssssalam"
]

for word in words:
    if re.match( r".*(\w)\1{5,}.*", word ):
        print(word)



# xaaxaaxaa

q = r"(\w)(\w)\2"
"""
for word in words:
    if re.match( r".*(\w)(\w)\1\2.*", word ):
        print(word)
"""

# 
# \d{7}[02468]

# "(\d)\1$"
# 55$
# 44$
