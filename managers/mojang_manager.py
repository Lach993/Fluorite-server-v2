import asyncio
import aiohttp
import json

class MojangManager:
    """The goal with this manager is to optimise sending the requests to the mojang api,
     sending the requests individually is inefficient, so we will use the mojang call which
     allows us to send up to 10 requests at once when able, but if we cannot saturate all 10
     it will send in accordance with the api rate limit"""
    def __init__(self, mojang_queue, hypixel_queue, sql_manager, mojang_rate_limiter):
        self.mojang_queue = mojang_queue
        self.hypixel_queue = hypixel_queue
        self.sql_manager = sql_manager
        self.ratelimit = mojang_rate_limiter

        self.mojang_worker = asyncio.create_task(self.mojang_worker(self.mojang_queue))

    async def mojang_worker(self, queue, hypixel_queue, ):
        """Worker for the mojang queue"""
        # optimises the mojang api by waiting 1.5 second between requests (or as soon as more than 10 are available) as this will help with ratelimit controll
        sleep_time = self.ratelimit.time_between_calls
        current_sleep_time = 0
        tasks = []
        
        while True:
            while queue.qsize() >= 10:
                task = []
                for j in range(10):
                    task.append(await queue.get())
                    queue.task_done()