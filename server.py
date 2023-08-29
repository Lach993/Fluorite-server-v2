"""Imports"""
from quart import Quart, request
import asyncio
import aiohttp
import os

import sql_manager

app = Quart(__name__)
SQL = sql_manager.SQL_Manager()


hypixel_queue = asyncio.Queue()
mojang_queue = asyncio.Queue()



            





@app.post("/api/v2/username_from_uuid")
async def username_from_uuid():
    """get uuid from username"""
    uuid = request.args.get("uuid")
    return await _username_from_uuid(uuid)

async def _username_from_uuid(uuid):
    """get username from uuid"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{uuid}") as resp:
            return await resp.json()

@app.post("/api/v2/uuid_from_username")
async def uuid_from_username():
    """get uuid from username"""
    username = request.args.get("username")
    return await _uuid_from_username(username)

async def _uuid_from_username(username):
    """get uuid from username"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{username}") as resp:
            return await resp.json()
        
@app.post("/api/v2/stats/get")
async def stats_get():
    """get stats from uuid"""
    # puts stats onto a queue to be processed, if the stats can be found, then returns the stats
    if sql_manager.get_stats(request.args.get("uuid")):
        pass