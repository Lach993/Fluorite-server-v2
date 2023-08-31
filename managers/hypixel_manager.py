import asyncio
import aiohttp
from utils import ratio
class HypixelManager:
    def __init__(self, hypixel_queue, processing_queue, hypixel_ratelimit, sql_manager):
        self.hypixel_queue = hypixel_queue
        self.processing_queue = processing_queue
        self.ratelimit = hypixel_ratelimit
        self.sql_manager = sql_manager

        asyncio.run(asyncio.create_task(self.hypixel_worker()))

    async def hypixel_worker(self):
        """Worker for the hypixel queue"""
        loop = asyncio.get_event_loop()
        while True:
            a = await self.hypixel_queue.get()
            await asyncio.create_task(self.hypixel_worker_slave(*a), loop=loop)

    async def hypixel_worker_slave(self, key, uuid):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.hypixel.net/player?key={self.hypixel_token}&uuid={uuid}") as resp:
                data = await resp.json()

        # check for dead player
        if data["player"] is None or not data["success"]:
            self.sql_manager.put_dead_user(key)
            self.processing_queue.remove(key)
        else:
            # get data 
            could_not_find_player = False
            bedwars_final_kills = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
            bedwars_final_deaths = data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]
            bedwars_kills = data["player"]["stats"]["Bedwars"]["kills_bedwars"]
            bedwars_deaths = data["player"]["stats"]["Bedwars"]["deaths_bedwars"]
            bedwars_wins = data["player"]["stats"]["Bedwars"]["wins_bedwars"]
            bedwars_losses = data["player"]["stats"]["Bedwars"]["losses_bedwars"]
            bedwars_beds_broken = data["player"]["stats"]["Bedwars"]["beds_broken_bedwars"]
            bedwars_beds_lost = data["player"]["stats"]["Bedwars"]["beds_lost_bedwars"]
            bedwars_games_played = data["player"]["stats"]["Bedwars"]["games_played_bedwars"]
            bedwars_winstreak = data["player"]["stats"]["Bedwars"]["winstreak"]

            # put data into database
            self.sql_manager.put_user(
                key, could_not_find_player,
                bedwars_final_kills, bedwars_final_deaths, bedwars_kills, bedwars_deaths, bedwars_wins, 
                bedwars_losses, bedwars_beds_broken, bedwars_beds_lost, bedwars_games_played, bedwars_winstreak
                )

            # get game data
            Bedwars_Ones_wins = data["player"]["stats"]["Bedwars"]["eight_one_wins_bedwars"]
            Bedwars_Ones_losses = data["player"]["stats"]["Bedwars"]["eight_one_losses_bedwars"]
            Bedwars_Ones_WLR = ratio(Bedwars_Ones_wins, Bedwars_Ones_losses)

            Bedwars_Ones_FKDR = ratio(data["player"]["stats"]["Bedwars"]["eight_one_final_kills_bedwars"], data["player"]["stats"]["Bedwars"]["eight_one_final_deaths_bedwars"])
            Bedwars_Ones_BBLR = ratio(data["player"]["stats"]["Bedwars"]["eight_one_beds_broken_bedwars"], data["player"]["stats"]["Bedwars"]["eight_one_beds_lost_bedwars"])


            Bedwars_Twos_wins = data["player"]["stats"]["Bedwars"]["eight_two_wins_bedwars"]
            Bedwars_Twos_losses = data["player"]["stats"]["Bedwars"]["eight_two_losses_bedwars"]
            Bedwars_Twos_WLR = ratio(Bedwars_Twos_wins, Bedwars_Twos_losses)

            Bedwars_Twos_FKDR = ratio(data["player"]["stats"]["Bedwars"]["eight_two_final_kills_bedwars"], data["player"]["stats"]["Bedwars"]["eight_two_final_deaths_bedwars"])
            Bedwars_Twos_BBLR = ratio(data["player"]["stats"]["Bedwars"]["eight_two_beds_broken_bedwars"], data["player"]["stats"]["Bedwars"]["eight_two_beds_lost_bedwars"])

            Bedwars_Threes_wins = data["player"]["stats"]["Bedwars"]["four_three_wins_bedwars"]
            Bedwars_Threes_losses = data["player"]["stats"]["Bedwars"]["four_three_losses_bedwars"]
            Bedwars_Threes_WLR = ratio(Bedwars_Threes_wins, Bedwars_Threes_losses)

            Bedwars_Threes_FKDR = ratio(data["player"]["stats"]["Bedwars"]["four_three_final_kills_bedwars"], data["player"]["stats"]["Bedwars"]["four_three_final_deaths_bedwars"])
            Bedwars_Threes_BBLR = ratio(data["player"]["stats"]["Bedwars"]["four_three_beds_broken_bedwars"], data["player"]["stats"]["Bedwars"]["four_three_beds_lost_bedwars"])

            Bedwars_Fours_wins = data["player"]["stats"]["Bedwars"]["four_four_wins_bedwars"]
            Bedwars_Fours_losses = data["player"]["stats"]["Bedwars"]["four_four_losses_bedwars"]
            Bedwars_Fours_WLR = ratio(Bedwars_Fours_wins, Bedwars_Fours_losses)

            Bedwars_Fours_FKDR = ratio(data["player"]["stats"]["Bedwars"]["four_four_final_kills_bedwars"], data["player"]["stats"]["Bedwars"]["four_four_final_deaths_bedwars"])
            Bedwars_Fours_BBLR = ratio(data["player"]["stats"]["Bedwars"]["four_four_beds_broken_bedwars"], data["player"]["stats"]["Bedwars"]["four_four_beds_lost_bedwars"])

            # put game data into database
            self.sql_manager.put_user_gamemode(key, 
                        Bedwars_Ones_wins, Bedwars_Ones_losses, Bedwars_Ones_FKDR, Bedwars_Ones_WLR, Bedwars_Ones_BBLR, 
                        Bedwars_Twos_wins, Bedwars_Twos_losses, Bedwars_Twos_FKDR, Bedwars_Twos_WLR, Bedwars_Twos_BBLR, 
                        Bedwars_Threes_wins, Bedwars_Threes_losses, Bedwars_Threes_FKDR, Bedwars_Threes_WLR, Bedwars_Threes_BBLR, 
                        Bedwars_Fours_wins, Bedwars_Fours_losses, Bedwars_Fours_FKDR, Bedwars_Fours_WLR, Bedwars_Fours_BBLR)

