"""Imports"""
from quart import Quart, request
import asyncio

from managers.mojang_manager import MojangManager
from managers.cosmetics_manager import CosmeticsManager
from managers.sql_manager import SqlManager


class Server:
    def __init__(self, hypixel_ratelimit, mojang_ratelimit):
        self.app = Quart(__name__)
        self.SQL = SqlManager("data/database.db")
        self.hypixel_queue = asyncio.Queue()
        self.mojang_queue = asyncio.Queue()

        self.processing_queue = [] # if a name is in this queue or in the database, do NOT add it to mojang queue 

        self.hypixel_ratelimit = hypixel_ratelimit
        self.mojang_ratelimit = mojang_ratelimit

        self.mojangManager = MojangManager(self.mojang_queue, self.hypixel_queue, self.SQL, self.mojang_ratelimit, self.processing_queue)
        self.cosmeticsManager = CosmeticsManager()

    def in_queue(self, name):
        """check if name is in queue"""
        return name in self.processing_queue or self.in_database(name)
    
    def in_database(self, name):
        """check if name is in database"""
        return self.SQL.in_uuid(name)
    
    def start(self, loop=None):
        if loop == None:
            loop = asyncio.get_event_loop()

        self.app.run(host="0.0.0.0", port=80, debug=False, loop=loop)

    
        ### POST ENDPOINTS ###
        @self.app.post("/api/v2/uuid_from_username")
        async def uuid_from_username():
            """get uuid from username"""
            form = await request.form
            username = form["username"]
            resp = await self.mojangManager._uuid_from_username(username)
            if resp == None or resp == (None,):
                return {"status": "error", "error": "username not found"}
            else:
                print(resp)
                print(type(resp))
                return {"status": "success", "uuid": resp}
             

        @self.app.post("/api/v2/stats/get")
        async def stats_get():
            """get stats from uuid"""
            pass

        ### GET ENDPOINTS ###
        @self.app.get("/api/v2/cosmetics/capes")
        async def cosmetics_capes():
            """get cosmetics from name"""
            name = request.args.get("name")
            return await self.cosmeticsManager._cosmetics_capes(name)

        @self.app.get("/api/v2/cosmetics/ears")
        async def cosmetics_ears():
            """get cosmetics from name"""
            name = request.args.get("name")
            return await self.cosmeticsManager._cosmetics_ears(name)

        @self.app.get("/api/v2/cosmetics/hats")
        async def cosmetics_hats():
            """get cosmetics from name"""
            name = request.args.get("name")
            return await self.cosmeticsManager._cosmetics_hats(name)

        @self.app.get("/api/v2/cosmetics/particles")
        async def cosmetics_particles():
            """get cosmetics from name"""
            name = request.args.get("name")
            return await self.cosmeticsManager._cosmetics_particles(name)

        @self.app.get("/api/v2/cosmetics/wings")
        async def cosmetics_wings():
            """get cosmetics from name"""
            name = request.args.get("name")
            return await self.cosmeticsManager._cosmetics_wings(name)
