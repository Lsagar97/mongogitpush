import pymongo
client = pymongo.MongoClient("mongodb+srv://Lsagar97:Likith97@cluster0.jvo7pib.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db1 = client['mongotest']
coll=db1['test']

record = coll.find()
for i in record:
#   print(i)

data = coll.find({'companyName': "likith-s"})
for i in data:
 #  print(i)

data = coll.find({'courseoffered':{'$gt' : "E"}})
for i in data:
    print(i)




