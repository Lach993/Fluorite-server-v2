"""IMPORTS"""
import os
import json
from utils import to_seconds, Rate_Limit

"""SETTINGS"""

CREATE_DISCORD_BOT = False
CREATE_WEBSERVER = True

# time before old data in the database is ignored. this is to prevent spamming the api with requests for data that is not necessary to update
Time_To_Update = to_seconds(weeks=1) 

"Tokens"
Hypixel_Token = os.getenv("Hypixel-Token")

if CREATE_DISCORD_BOT:
    Discord_Token = os.getenv("Discord-Token")


"""
Alternatively, you can use this:
Hypixel_Token = json.load(open("data/Tokens.json"))["Hypixel-Token"]

if CREATE_DISCORD_BOT:
    Discord_Token = json.load(open("data/Tokens.json"))["Discord-Token"]
"""



"""Vars"""
Hypixel_RateLimit = Rate_Limit(120, to_seconds(minutes=1), name="Hypixel API")
Mojang_RateLimit = Rate_Limit(600, to_seconds(minutes=10), name="Mojang API")
