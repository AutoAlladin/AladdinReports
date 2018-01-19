from bson.objectid import ObjectId
from pymongo import MongoClient
from selenium import webdriver
import gridfs

client = MongoClient('192.168.80.121', 27017)
db = client['aladdin_tests']
test_params = db["test_params"]
test_result = db["test_results"]
print(test_params)

query = {"_id" : ObjectId("5a60a44bf776482deca40469")}
result = test_result.find_one(query)

print(result)

with(open('warfile.txt', mode="w", encoding="UTF8")) as f:
    f.write(str(result))


# result_many = test_result.find({})
#
# for result_one in result_many:
#     print(result_one)




