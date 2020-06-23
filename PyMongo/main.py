import pymongo
from pymongo import MongoClient, IndexModel, ASCENDING, DESCENDING


myClient = MongoClient('localhost', 27017)
db = myClient.mydb
users = db.users
user1 = {"username": "Nobert", "password": "password", "fav_number": "1234", "hobbies": ["python", "games", "havoc"]}
user_id = users.insert_one(user1).inserted_id

index1 = IndexModel([("hello", DESCENDING),("world", ASCENDING)], name="hello_world")
index2 = IndexModel([("goodbye", DESCENDING)])
users.create_indexes([index1, index2])
print("Index created.")
print(user_id)
