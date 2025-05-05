import database.connect as connect
from models.profile import Profile

def register_profile(user_id: int, username: str):
    collection = connect.users_collection # Mengambil user collection

    profile = collection.find_one({"user_id": user_id}) # Mencari salah satu id yang sama

    if profile:
        return Profile.from_dict(profile) # Load profile yang sudah ada

    new_profile = Profile(user_id, username) # profile baru

    collection.insert_one(new_profile.to_dict()) # simpan ke DB
    return new_profile