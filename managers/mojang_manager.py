import asyncio
import aiohttp
import logging
import time

class MojangManager:
    """The goal with this manager is to optimise sending the requests to the mojang api,
     sending the requests individually is inefficient, so we will use the mojang call which
     allows us to send up to 10 requests at once when able, but if we cannot saturate all 10
     it will send in accordance with the api rate limit"""
    def __init__(self, mojang_queue, hypixel_queue, sql_manager, mojang_rate_limiter, processing_queue):
        self.mojang_queue = mojang_queue
        self.hypixel_queue = hypixel_queue
        self.sql_manager = sql_manager
        self.ratelimit = mojang_rate_limiter
        self.processing_queue: list = processing_queue
        self.call_queue = asyncio.Queue()
        self.next = asyncio.Queue()

        asyncio.run(self.start_workers())

        

    async def start_workers(self):
        """start all workers"""
        asyncio.create_task(self.mojang_batch_worker())
        asyncio.create_task(self.lost_player_worker())
        
    
    async def lost_player_worker(self):
        """
        if a player is not found on the mojang api, the api will not return a player, so we need to add them to the database as a dead player so we dont spam the api
        all players that are found will then be sent to the hypixel queue. this is to prevent spamming the hypixel api with requests for players that don't have uuid's
        """
        while True:
            [sent, recived] = await self.next.get()
            for i in recived:
                sent.remove(i["name"])
                key = self.sql_manager.put_uuid(i["name"], i["id"])
                # send to the hypixel queue
                self.hypixel_queue.put_nowait([key, i["id"]])
            for i in sent:
                key = self.sql_manager.put_uuid(i, None)
                self.sql_manager.put_dead_user(key)
                self.processing_queue.remove(i)

    async def mojang_batch_worker(self):
        """Worker for the mojang queue"""
        # optimises the mojang api by waiting the minimum time requests before a ratelimit happens (or as soon as more than 10 are available) as this will help with ratelimit controll
        sleep_time = self.ratelimit.time_between_calls()

        loop = asyncio.get_event_loop()
        while True:
            temp = []
            temp.append(await self.mojang_queue.get()) # this waits until something happens so we dont need to sleep
            start = time.time()

            while len(temp) < 10 and (time.time() - start) < sleep_time and self.mojang_queue.qsize() > 0:
                temp.append(await self.mojang_queue.get())

            asyncio.create_task(self.fetch_multi_uuid(temp), loop=loop)

        
    async def fetch_multi_uuid(self, names):
        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(self.ratelimit.time_until_ready())
            self.ratelimit.add_call()
            async with session.post(f"https://api.mojang.com/users/profiles/minecraft", json=names) as mojang_resp:
                data = await mojang_resp.json()
                self.next.put_nowait([names, data])

    async def _uuid_from_username(self, username):
        """get uuid from username, standalone"""
        logging.debug(f"getting uuid from username: {username}")
        if self.sql_manager.in_uuid(username):
            logging.debug("uuid found in database")
            return self.sql_manager.get_uuid_from_username(username)
        else:    
            logging.debug("uuid not found in database")
            async with aiohttp.ClientSession() as session:
                await asyncio.sleep(self.ratelimit.time_until_ready())
                self.ratelimit.add_call()
                async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{username}") as resp:
                    data = await resp.json()
        if "errorMessage" in data:
            id = None
        else:
            id = data["id"]
        key = self.sql_manager.put_uuid(username, id)
        if id is None:
            self.sql_manager.put_dead_user(key)
        else:
            await self.hypixel_queue.put([key, id])
        return id
        

