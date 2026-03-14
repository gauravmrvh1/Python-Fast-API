import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

#######################################  Create DB #######################################
# mydb = myclient["customers"]
# mycol = mydb["users"]
# mylist = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mylist)
# print(x)
# print(x.inserted_id)
#######################################  Create DB #######################################


# **************************** INSERT ********************************************
# mydb = myclient["customers"]
# mycol = mydb["users"]
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# print(x)
# **************************** INSERT ********************************************


# **************************** Update***************************
# mydb = myclient["customers"]
# mycol = mydb["users"]
# myquery = { "address": "Ocean blvd 2" }
# newvalues = { "$set": { "address": "Hno 27 Ram Ganj Railway Road Hapur" } }
# mycol.update_one(myquery, newvalues)



mydb = myclient["customers"]
mycol = mydb["users"]
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)

# **************************** Update***************************



# **************************** Find One***************************
# mydb = myclient["customers"]
# mycol = mydb["users"]
# x = mycol.find_one()
# print(x)
# **************************** Find One***************************


# **************************** Find Many***************************
# mydb = myclient["customers"]
# mycol = mydb["users"]

# myresult = mycol.find()
# myresult = mycol.find().limit(5)
# for x in myresult:
#   print(x)
# **************************** Find Many***************************

  
# **************************** Find With Column***************************
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
    # print(x)
# **************************** Find With Column***************************


# **************************** Find With Column***************************
# mydb = myclient["customers"]
# mycol = mydb["users"]
# for x in mycol.find({},{
#     "_id": 0,
#     "address": 0
# }):
#     print(x)
# **************************** Find With Column***************************

  
# **************************** Find With Query***************************
# mydb = myclient["customers"]
# mycol = mydb["users"]
# myquery = { "address": "Hno 27 Ram Ganj Railway Road Hapur" }
# myquery = { "address": { "$gt": "S" } }
# myquery = { "address": { "$regex": "^S" } }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)


# mydb = myclient["customers"]
# mycol = mydb["users"]
# mydoc = mycol.find().sort("name")
# mydoc = mycol.find().sort("name", -1)
# for x in mydoc:
#   print(x)

# **************************** Find With Query***************************



# **************************** Delete***************************
# mydb = myclient["customers"]
# mycol = mydb["users"]
# myquery = { "address": "Valley 345" }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#     print(x)
# mycol.delete_one(myquery)

# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")

# **************************** Delete***************************





print(myclient.list_database_names())


delist = myclient.list_database_names()
if "admin" in delist:
  print("The database exists.")


