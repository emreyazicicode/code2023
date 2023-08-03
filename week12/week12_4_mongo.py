
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

"""
mydict = { "name": "John", "address": "Highway 37", "gender": "male" }
x = mycol.insert_one(mydict)
print(x)


mydict = { "name": "Company", "address": "Highway 37", "sector": "IT", "NofEmp": 300 }
x = mycol.insert_one(mydict)
print(x)
"""



for c in mycol.find():  # SELECT * FROM [customers]
    if 'gender' in c:
        print(c, c['gender'])

# DIFFERENT STRUCTURE

print("==============")
print(mycol.find_one()) # SELECT * FROM [customers] LIMIT 1

print("==============")
for x in mycol.find({}, { "_id": 0, "name": 1, "gender": 1 }): # SELECT name, address FROM .....
  print(x) 



for x in mycol.find({ 'sector': 'Health' }): # SELECT name, address FROM .....
    print(x)
