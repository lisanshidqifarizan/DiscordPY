import discord
from discord.ext import commands
import random
from database.register import users_collection, create_user

# Battle command
@commands.command()
async def hunt(ctx):
    user_id = str(ctx.author.id)
    username = ctx.author.name

    # Auto register
    create_user(user_id, username)

    # Chance gagal (20%)
    chance = random.randint(1, 100)
    if chance <= 20:  # 20% gagal
        await ctx.send(f"🏹 {ctx.author.name} went hunting but found nothing... Better luck next time!")
        return

    # Daftar hewan & rewardnya
    animals = {
        "Rabbit": random.randint(5, 10),
        "Deer": random.randint(10, 20),
        "Boar": random.randint(15, 25),
        "Bear": random.randint(20, 40),
        "Legendary Phoenix": random.randint(50, 100)  # hewan langka
    }

    # Pilih hewan secara random
    animal, coins_earned = random.choice(list(animals.items()))

    # Tambahkan koin ke user
    users_collection.update_one({"user_id": user_id}, {"$inc": {"coins": coins_earned}})

    await ctx.send(f"🏹 {ctx.author.name} went hunting and caught a **{animal}**!\nYou earned **{coins_earned} coins**!")

@commands.command()
async def battle(ctx, opponent: discord.User):
    user_id = str(ctx.author.id)
    username = ctx.author.name
    opponent_id = str(opponent.id)
    opponent_name = opponent.name

    # Auto register players
    create_user(user_id, username)
    create_user(opponent_id, opponent_name)

    actions = ["Attack", "Defend", "Heal"]
    user_action = random.choice(actions)
    opponent_action = random.choice(actions)

    # Health stats for both players
    user_health = 100
    opponent_health = 100

    # Battle simulation
    await ctx.send(f"{ctx.author.name} vs {opponent.name} - Battle Start!")
    
    for round_num in range(1, 6):  # Battle has 5 rounds
        await ctx.send(f"\nRound {round_num}!")

        # Determine actions and health changes
        if user_action == "Attack":
            damage = random.randint(10, 30)
            opponent_health -= damage
            await ctx.send(f"{ctx.author.name} attacks! {opponent.name} loses {damage} HP.")
        elif user_action == "Defend":
            heal = random.randint(5, 10)
            user_health += heal
            await ctx.send(f"{ctx.author.name} defends and heals {heal} HP.")
        elif user_action == "Heal":
            heal = random.randint(10, 20)
            user_health += heal
            await ctx.send(f"{ctx.author.name} heals for {heal} HP.")

        if opponent_action == "Attack":
            damage = random.randint(10, 30)
            user_health -= damage
            await ctx.send(f"{opponent.name} attacks! {ctx.author.name} loses {damage} HP.")
        elif opponent_action == "Defend":
            heal = random.randint(5, 10)
            opponent_health += heal
            await ctx.send(f"{opponent.name} defends and heals {heal} HP.")
        elif opponent_action == "Heal":
            heal = random.randint(10, 20)
            opponent_health += heal
            await ctx.send(f"{opponent.name} heals for {heal} HP.")

        # Update actions for next round
        user_action = random.choice(actions)
        opponent_action = random.choice(actions)

        # Check for victory conditions
        if user_health <= 0 or opponent_health <= 0:
            break

    if user_health > opponent_health:
        result = f"{ctx.author.name} wins the battle!"
        users_collection.update_one({"user_id": user_id}, {"$inc": {"coins": 30, "wins": 1}})
        users_collection.update_one({"user_id": opponent_id}, {"$inc": {"coins": -20, "losses": 1}})
    elif user_health < opponent_health:
        result = f"{opponent.name} wins the battle!"
        users_collection.update_one({"user_id": opponent_id}, {"$inc": {"coins": 30, "wins": 1}})
        users_collection.update_one({"user_id": user_id}, {"$inc": {"coins": -20, "losses": 1}})
    else:
        result = "It's a tie!"

    await ctx.send(f"\nBattle Over! {result}")