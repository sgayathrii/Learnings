from asyncio.windows_events import NULL
from unicodedata import name
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['myDB_using_python']
print("List of Database in MongoDB: ")
print(myclient.list_database_names())
mycol = mydb["persons"]
print("Collection currently using: " )
print(mydb.list_collection_names())

"""
mydict = {"name": "Remo", "address": "Sky st 339"}
mycol.insert_one(mydict)
print("Record inserted:")
print(mydict)

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
  ]

mycol.insert_many(mylist)


for z in mycol.find():
    print(z)

readAll = mycol.find()
print("Documents in collection:")
for data in readAll:
    print(data)



readSpecificCol = mycol.find({},{"name":1, "address" : 1})
for data in readSpecificCol:
    print(data)



filterData = mycol.find({"name":"Remo"})
for data in filterData:
    print(data)


distinctData = mycol.distinct("name")
for data in distinctData:
    print(data)


filterData = mycol.find().limit(5).skip(5)
for data in filterData:
    print(data)




mydict = {"name": "Uddhav", "address": " "}
mycol.insert_one(mydict)


countData = mycol.count_documents({})
print(countData)
countData = mycol.count_documents({"address":" "})
print(countData)
countData = mycol.count_documents({"address":{"$ne":" "}})
print (mycol.name, "has", countData, "total documents.")

updateNw = mycol.update_many({}, {"$set":{"roll_no":NULL}})



sorting = mycol.find().sort("name")

"""

myquery = {"address" : {"$regex":"^S"}}
newValues = {"$set":{"name" : "Linn"}}

updateVal = mycol.update_many(myquery, newValues)
print(updateVal.modified_count, "document updated")


     
    





