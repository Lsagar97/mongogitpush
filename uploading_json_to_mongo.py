import pymongo
import pandas as pd
df=pd.read_csv("D:/attributedataset_testcsv.csv")
data = df.to_dict(orient="records")





client = pymongo.MongoClient("mongodb+srv://Lsagar97:Likith97@cluster0.jvo7pib.mongodb.net/?retryWrites=true&w=majority")
db = client.test


db1 = client["likith's_uploadingtest"]
coll=db1['attributedataset']

#coll.insert_many(data)
d=coll.find({'Dress_ID':})
for i in d:
    print(i)


    liki

