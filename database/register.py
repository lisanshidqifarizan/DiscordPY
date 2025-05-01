# register.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# Setup MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client['vedbdc']
users_collection = db['users']

# Auto Register Function
def create_user(user_id, username):  # Changed function name
    user = users_collection.find_one({"user_id": user_id})
    if not user:
        users_collection.insert_one({
            "user_id": user_id,
            "username": username,
            "coins": 100,  # Start coins
            "wins": 0,
            "losses": 0
        })
        print(f"Registered new user: {username}")