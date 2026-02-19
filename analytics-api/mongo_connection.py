from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_mongo_connection():
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_BAME")
    db_collection = os.getenv("DB_COLLECTION")
    client = MongoClient(mongo_uri)
    mydb = client[db_name]
    mycollection = mydb[db_collection]
    return mycollection
