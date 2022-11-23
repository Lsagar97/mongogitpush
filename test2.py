import pymongo



data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

client = pymongo.MongoClient("mongodb+srv://Lsagar97:Likith97@cluster0.jvo7pib.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db1 = client['inventory']
coll=db1['table']
#coll.insert_many(data)

#d=coll.find()
#for i in d:
  #  print(i)

#d = coll.find({'status':'A'})
#for i in d:
  #  print(i)

#d= coll.find({'status':{'$in':['A','P']}}) ##$ is inbuilt keyword
#for i in d:
 #   print(i)

#d=coll.find({'status':{'$gt':'C'}})
#for i in d:
 #  print(i)

#d=coll.find({'qty':100})
#d=coll.find({'qty':{'$gte':75}})
#d=coll.find({'item': 'sketch pad','qty':95})
#d=coll.find({'item':'sketch pad','qty':{'$gte':75}})  #similar to AND condition
#d=coll.find({'$or': [{'item':'sketch pad'  }, {'qty':{'$gte': 75}}]})
#coll.update_one({'item':'canvas'},{'$set':{'item':'likith'}})
#d=coll.find({'item':'likith'})
c#oll.delete_one({'item':'likith'})
d#= coll.find({'item':'likith'})


f#or i in d:
  #  print(i)


show collections

#client = pymongo.MongoClient("mongodb+srv://Lsagar97:<password>@cluster0.jvo7pib.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
