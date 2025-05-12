from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") 
db =client["estoque_db"]
collection = db["produtos"]
