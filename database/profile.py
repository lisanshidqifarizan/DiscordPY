from database.connect import users_collection
from models.profile import Profile

def get_profile(user_id: int):
    data = users_collection.find_one({"user_id": user_id})
    if data:
        return Profile.from_dict(data)
    return None

def update_profile(user_profile):
    users_collection.update_one(
        {"user_id": user_profile.user_id},
        {
            "$set": {
                "username": user_profile.username,
                "level": user_profile.level,
                "hp": user_profile.hp,
                "exp": user_profile.exp,
                "coins": user_profile.coins,
                "equipment": user_profile.equipment
            }
        }
    )