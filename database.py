import pymongo as pm
client=pm.MongoClient('localhost', 27017) #connecting to mongodb
db=client['thinkit'] #connecting to database
offers=db.offers #getting collection
db.offers.delete_many({})
