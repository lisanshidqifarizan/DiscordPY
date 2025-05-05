import discord
import random
import asyncio

async def slot_command(ctx):
    items = ['🍒','🪙','💎','🍌','💰']
    slot1 = random.choice(items)
    slot2 = random.choice(items)
    slot3 = random.choice(items)

    baris_pertama = f'{slot1} | {slot2} | {slot3}'
    slot4 = random.choice(items)
    slot5 = random.choice(items)
    slot6 = random.choice(items)
    baris_kedua = f'{slot4} | {slot5} | {slot6}'
    slot7 = random.choice(items)
    slot8 = random.choice(items)
    slot9 = random.choice(items)
    baris_ketiga = f'{slot7} | {slot8} | {slot9}'

    await ctx.send("ROLL ROLL ROLL!!! ROLLIIINNGGG...!!")
    await asyncio.sleep(2)

    embed = discord.Embed(
        title="✨SLOT✨",
        description="",
        color=discord.Color.dark_gold()
    )

    results = f'\n    {baris_pertama}\n    {baris_kedua}\n    {baris_ketiga}'
    if slot4 == slot5 == slot6:
        embed.add_field(name="", value=f'{results}\nCongratulation!\nYou win!')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name="", value=f'{results}')
        await ctx.send(embed=embed)