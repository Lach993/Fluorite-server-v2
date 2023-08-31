"""imports"""
import logging
import sqlite3
import time

class SqlManager:
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        logging.info(f"Connected to database '{self.database}'")
        self.create_uuid_table()
        self.create_user_table()
        self.create_gamemodes_table()
    
    def create_uuid_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uuid (key NUM, username TEXT, uuid TEXT)")
        self.connection.commit()

    

    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                            Key NUM, 
                            Time INTEGER,
                            Could_Not_Find_Player INTEGER,

                            star INTEGER,

                            Bedwars_Final_Kills INTEGER,
                            Bedwars_Final_Deaths INTEGER,
                            Bedwars_Kills INTEGER,
                            Bedwars_Deaths INTEGER,
                            Bedwars_Wins INTEGER,
                            Bedwars_Losses INTEGER,
                            Bedwars_Beds_Broken INTEGER,
                            Bedwars_Beds_Lost INTEGER,
                            Bedwars_Games_Played INTEGER,
                            Bedwars_Winstreak INTEGER
                            )""")
        self.connection.commit()

    def create_gamemodes_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users_gamestats (
                            Key NUM, 
                            Time INTEGER,

                            Bedwars_Ones_Wins INTEGER,
                            Bedwars_Ones_Losses INTEGER,
                            Bedwars_Ones_FKDR INTEGER,
                            Bedwars_Ones_WLR INTEGER,
                            Bedwars_Ones_BBLR INTEGER,

                            Bedwars_Twos_Wins INTEGER,
                            Bedwars_Twos_Losses INTEGER,
                            Bedwars_Twos_FKDR INTEGER,
                            Bedwars_Twos_WLR INTEGER,
                            Bedwars_Twos_BBLR INTEGER,

                            Bedwars_Threes_Wins INTEGER,
                            Bedwars_Threes_Losses INTEGER,
                            Bedwars_Threes_FKDR INTEGER,
                            Bedwars_Threes_WLR INTEGER,
                            Bedwars_Threes_BBLR INTEGER,

                            Bedwars_Fours_Wins INTEGER,
                            Bedwars_Fours_Losses INTEGER,
                            Bedwars_Fours_FKDR INTEGER,
                            Bedwars_Fours_WLR INTEGER,
                            Bedwars_Fours_BBLR INTEGER
                            )""")
        self.connection.commit()

    

    def put_uuid(self, username, uuid):
        """puts uuid into database, returns key for further fetching"""
        key = self.cursor.execute("SELECT MAX(key) FROM uuid").fetchone()[0]
        if key == None:
            key = 0
        else:
            key += 1
        logging.debug(f"putting uuid into database: {username} {uuid} {key}")
        self.cursor.execute("INSERT INTO uuid VALUES (?, ?, ?)", (key, username, uuid))
        self.connection.commit()
        return key


    def in_uuid(self, key):
        """checks if name is in database"""
        self.cursor.execute("SELECT * FROM uuid WHERE username=?", (key,))
        return self.cursor.fetchone() is not None
    
    # get uuid
    def get_uuid_from_key(self, key):
        self.cursor.execute("SELECT uuid FROM uuid WHERE key=?", (key,))
        return self.cursor.fetchone()
    
    def get_uuid_from_username(self, username):
        self.cursor.execute("SELECT uuid FROM uuid WHERE username=?", (username,))
        return self.cursor.fetchone()
    
    # get username
    def get_username_from_uuid(self, uuid):
        self.cursor.execute("SELECT username FROM uuid WHERE uuid=?", (uuid,))
        return self.cursor.fetchone()
    
    def get_username_from_key(self, key):
        self.cursor.execute("SELECT username FROM uuid WHERE key=?", (key,))
        return self.cursor.fetchone()
    
    # get key
    def get_key_from_username(self, username):
        self.cursor.execute("SELECT key FROM uuid WHERE username=?", (username,))
        return self.cursor.fetchone()
    
    def get_key_from_uuid(self, uuid):
        self.cursor.execute("SELECT key FROM uuid WHERE uuid=?", (uuid,))
        return self.cursor.fetchone()
    

    
    def put_user(
            self, 
            key, could_not_find_player, star,
            bedwars_final_kills, bedwars_final_deaths, bedwars_kills, bedwars_deaths, bedwars_wins, 
            bedwars_losses, bedwars_beds_broken, bedwars_beds_lost, bedwars_games_played, bedwars_winstreak
            ):
        t = int(time.time())
        self.cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    key, t, could_not_find_player, star,
                    bedwars_final_kills, bedwars_final_deaths, bedwars_kills, bedwars_deaths, bedwars_wins, 
                    bedwars_losses, bedwars_beds_broken, bedwars_beds_lost, bedwars_games_played, bedwars_winstreak
                )
            )
        self.connection.commit()

    def put_user_gamemode(
            self, key, 
            Bedwars_Ones_Wins, Bedwars_Ones_Losses, Bedwars_Ones_FKDR, Bedwars_Ones_WLR, Bedwars_Ones_BBLR, 
            Bedwars_Twos_Wins, Bedwars_Twos_Losses, Bedwars_Twos_FKDR, Bedwars_Twos_WLR, Bedwars_Twos_BBLR, 
            Bedwars_Threes_Wins, Bedwars_Threes_Losses, Bedwars_Threes_FKDR, Bedwars_Threes_WLR, Bedwars_Threes_BBLR, 
            Bedwars_Fours_Wins, Bedwars_Fours_Losses, Bedwars_Fours_FKDR, Bedwars_Fours_WLR, Bedwars_Fours_BBLR):
        
        t = int(time.time())
        self.cursor.execute(
            "INSERT INTO users_gamestats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                key, t,
                Bedwars_Ones_Wins, Bedwars_Ones_Losses, Bedwars_Ones_FKDR, Bedwars_Ones_WLR, Bedwars_Ones_BBLR, 
                Bedwars_Twos_Wins, Bedwars_Twos_Losses, Bedwars_Twos_FKDR, Bedwars_Twos_WLR, Bedwars_Twos_BBLR, 
                Bedwars_Threes_Wins, Bedwars_Threes_Losses, Bedwars_Threes_FKDR, Bedwars_Threes_WLR, Bedwars_Threes_BBLR, 
                Bedwars_Fours_Wins, Bedwars_Fours_Losses, Bedwars_Fours_FKDR, Bedwars_Fours_WLR, Bedwars_Fours_BBLR
            )
        )
        self.connection.commit()

    
    def put_dead_user(self, key):
        t = int(time.time())
        self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (key, t, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.connection.commit()

    def get_user(self, key):
        self.cursor.execute("SELECT * FROM users WHERE key=?", (key,))
        return self.cursor.fetchone()