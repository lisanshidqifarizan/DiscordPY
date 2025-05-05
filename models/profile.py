class Profile:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.attack = 1
        self.defense = 1
        self.coins = 0
        self.level = 1
        self.exp = 0
        self.hp = 100

        # Equipment kosong di awal
        self.equipment = {
            "sword": None,
            "accessory": None,
            "armor": None,
        }

    # ➡️ Convert jadi dictionary untuk disimpan ke MongoDB
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "attack": self.attack,
            "defense": self.defense,
            "coins": self.coins,
            "level": self.level,
            "exp": self.exp,
            "hp": self.hp,
            "equipment": self.equipment
        }
    
    # ➡️ Load dari database (dict) ke object Profile lagi
    @classmethod
    def from_dict(cls, data):
        profile = cls(data["user_id"], data["username"])
        profile.attack = data.get("attack", 1)
        profile.defense = data.get("defense", 1)
        profile.coins = data.get("coins", 0)
        profile.level = data.get("level", 1)
        profile.exp = data.get("exp", 0)
        profile.hp = data.get("hp", 100)
        profile.equipment = data.get("equipment", {
            "sword": None,
            "accessory": None,
            "armor": None,
        })
        return profile