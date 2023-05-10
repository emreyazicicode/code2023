
#
#! warning
#? 
#* 

# perl, js, php, .... 
# Scripting language
# Runs without compiling
# Fast deployment - a little slow runtime
# Late-binding
# No spaghetti code, smart indentations
# No class needed
# No main is required
i = 3
print(i, type(i))
i = 3.0
print(i, type(i))
i = '3'
print(i, type(i))
i = [3]
print(i, type(i))
#!!! string s = "emre"

def x(a):
	
	if a > 3:
		return True


"""
print(i * 3)
if __name__ == "__main__":
	pass
magic function
"""

print(__file__)
print(__name__)


a = """emre
yazici"""


a = '''
emre
'''

a = "emre"
a = 'emre'
b = "emre"
a = f"salam {b.upper()}" # ==> \n
print(a)
print("\u018F")


# list = mutable, degisebilir
# sirasi ONEMLI!!!
# duplike deger alabilir
# farkli turlerde degerler alabilir
a = [5,1,2,3,4, "emre", False, 3.5]
print(type(a), a)

a = [3,6,12,35,37,23,1,304]
print(a[0])
print(a[0:2])
print(a[:2])
print(a[2:])
print(a[-1])
print(a[-3:])


a.append(4999)
print(a)

a.remove(3)
print(a)

del a[0]
print(a)

print("======================")
print(a.pop())
print(a)

print(a.pop(0))
print(a)

import pandas as pd

# pd.read_csv("xxx.csv", keep_date_col = True, usecols = ['a', 'b', 'c'])
# ===================================================
# IMPORTS
# 1. variation
# import week1c
# print( week1c.ftoc(70) )
# 2. variation
# import week1c as w1
# w1.ftoc(70)
# 3. variation
# from week1c import *
# ftoc()
# 4. variation
# from week1c import ftoc, x
# ftoc()

# from keras.layers import Dense, Dropout, Activation

# import matplotlib.pyplot as plt
# plt.plot([3,4,5])
# plt.show()
# ===========================

a = {'salary': 3400,  'name': 'Ahmet', 'age': 34}
# key-value
# mutable
# KEY, immutable
# SORT IS NOT IMPORTANT

print(a['name'])


values = []
for x in sorted(a):
	print(" >>>", x, "====>",  a[x])
	values.append( a[x] )

print(values)

# Adding
a['experience'] = 3
# Deletion
del a['age']


# List, Dict
# len(  )

# print(int.bit_length(10))
i = 1324242
# i(32 bit, 4 byte) = [-2.5 milyar, +2.5milyar]
# byte = 0..255
# short / small int = -32676, 32768
# from pyzip import PyZip

# ! pip install
# ! requirements 

a = "emre"
print(a)
print(list(a))
b = ['e', 'm', 'r', 'e']

print(b)
print("".join(b))


d = {"age": 34, "gender": "male", "name": "ali"}
print(list(d))
print(list(d.values()))


isimler = ['ahmet', 'mehmet', 'ali', 'emre']

print(range(len(isimler)))
# print(dict(isimler))

keys = range(len(isimler))
vals = isimler

print( dict( zip(keys, vals)  ) )


a = ( 34, 'male', 'ahmet' )
print(a)


a = {3, 4, 5, 5}
print(a)


numaralar = [3, 4, 5, 5]

print( list(set(numaralar))  )

# True == False

a = (3, 4)

a = None

import numpy as np

np.inf









