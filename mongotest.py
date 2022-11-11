import pymongo
client = pymongo.MongoClient("mongodb+srv://Lsagar97:Likith97@cluster0.jvo7pib.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"likith",
    "email":"likith@gamil.com",
    "surname":"sagar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
