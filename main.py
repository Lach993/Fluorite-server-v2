"""IMPORTS"""
import os
import json
from bot import Fluorite_Bot
from utils import to_seconds, Rate_Limit
from server import Server
import asyncio
import logging
import requests

"""SETTINGS"""
Logging_Level = "WARNING" # DEBUG, INFO, WARNING, ERROR, CRITICAL

CREATE_DISCORD_BOT = False

CREATE_WEBSERVER = True

BYPASS_VERSION_EXIT = True # if true, the program will not exit if a new version is available

# time before old data in the database is ignored. this is to prevent spamming the api with requests for data that is not necessary to update
Time_To_Update = to_seconds(weeks=1) 

"Tokens"
Hypixel_Token = os.getenv("Hypixel-Token") # Alternativly: json.load(open("data/Tokens.json"))["Hypixel-Token"]

if CREATE_DISCORD_BOT:
    Discord_Token = os.getenv("Discord-Token") # Alternativly: json.load(open("data/Tokens.json"))["Discord-Token"]

"""Rate Limits"""
Hypixel_RateLimit = Rate_Limit(300, to_seconds(minutes=5), name="Hypixel API")
Mojang_RateLimit = Rate_Limit(600, to_seconds(minutes=10), name="Mojang API")


"""Vars"""
loop = asyncio.get_event_loop()

"""Start"""
logging.basicConfig(level=Logging_Level)


# check for new version
logging.info("Checking for new version")
try:
    with open("data/version.json", "r") as f:
        version = json.load(f)["version"]
except FileNotFoundError:
    version = "0.0.0"
logging.info(f"Current version: {version}")
# https://github.com/Lach993/Fluorite-server-v2
try:
    new_version = requests.get("https://raw.githubusercontent.com/Lach993/Fluorite-server-v2/main/data/version.json").json()["version"]
except:
    logging.warning("Could not check for new version")
    new_version = "Not found"

if new_version != version:
    logging.warning(f"New version available: {new_version}")
    logging.warning("Please update to the new version")
    if not BYPASS_VERSION_EXIT:
        exit()


if CREATE_WEBSERVER:
    # initialise the webserver
    webserver = Server(Hypixel_RateLimit, Mojang_RateLimit)
    
    # start the server
    asyncio.create_task(webserver.start())

if CREATE_DISCORD_BOT:
    logging.error("Discord bot is not yet implemented")
    # # initialise the bot
    # bot = Fluorite_Bot(Discord_Token, loop=loop)

    # # start the bot
    # asyncio.create_task(bot.start())
if CREATE_DISCORD_BOT or CREATE_WEBSERVER:
    loop.run_forever()