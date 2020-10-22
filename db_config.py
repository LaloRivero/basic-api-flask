import os
from flask_pymongo import pymongo

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

client = pymongo.MongoClient(f"mongodb+srv://admin:{DB_PASSWORD}@db-test.cgrgj.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")
db = client.test
