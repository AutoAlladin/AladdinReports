from bson.objectid import ObjectId
from pymongo import MongoClient
from string import Template
from selenium import webdriver
import gridfs

client = MongoClient('192.168.80.121', 27017)
db = client['aladdin_tests']
test_params = db["test_params"]
test_result = db["test_reGsults"]
print(test_params)

query = {"_id" : ObjectId("5a659573f776481ff019bfd6")}
result = test_result.find_one(query)

print(result)

with(open('templates\\new 1.html', mode="r", encoding="UTF8")) as f:
    file1 = f.read()
print(file1)

s = Template('$_id')
print(s.substitute(_id = 654654654))


# with(open('warfile.txt', mode="w", encoding="UTF8")) as f:
#     f.write(str(result))



# result_many = test_result.find({})
#
# for result_one in result_many:
#     print(result_one)


# db.getCollection('test_results').find({"test_name":{$regex:'test dev'} $and :(find({$group :"test_name"} $and :(find({$min : "test_timestamp"}) )   
#
# db.getCollection('test_results').find({$last : "test_timestamp"})
#
# db.getCollection('test_results').find({"test_name":{$regex:'test dev'}})


