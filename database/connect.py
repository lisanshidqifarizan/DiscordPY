import os
from dotenv import load_dotenv
from pymongo import MongoClient
client = MongoClient() # client mongo

load_dotenv() # Membaca dotenv
MONGO_URI = os.getenv("MONGO_URI") # Mengambil value MONGO_URI

client = MongoClient(MONGO_URI)
db = client["veodbdc"]
users_collection = db["users"]