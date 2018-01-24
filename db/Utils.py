from bson.objectid import ObjectId
from pymongo import MongoClient

def get_MD_collection(ip='192.168.80.121',
                      db_name='aladdin_tests',
                      collection_name="test_results"):
    client = MongoClient(ip, 27017)
    db = client[db_name]
    test_result = db[collection_name]
    return test_result

def get_result(_col, id=None, maxdate=None) :
    if id is not None:
        query = {"_id": ObjectId(id)}
        return _col.find_one(query)
    if maxdate is not None:
        query = {}
        return _col.find_one(query)




