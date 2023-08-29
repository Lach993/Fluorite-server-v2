"""imports"""
import logging
import sqlite3


class SqlManager:
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        logging.info(f"Connected to database '{self.database}'")
    
    def create_uuid_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uuid (key NUM, username TEXT, uuid TEXT)")
        self.connection.commit()

    

    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                            Key NUM, 
                            Time INTEGER,

                            Could_Not_Find_Player INTEGER,

                            Bedwars_Final_Kills INTEGER,
                            Bedwars_Final_Deaths INTEGER,
                            Bedwars_Kills INTEGER,
                            Bedwars_Deaths INTEGER,
                            Bedwars_Wins INTEGER,
                            Bedwars_Losses INTEGER,
                            Bedwars_Beds_Broken INTEGER,
                            Bedwars_Beds_Lost INTEGER,
                            Bedwars_Games_Played INTEGER,
                            Bedwars_Winstreak INTEGER,
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



    def put_uuid(self, key, username, uuid):
        self.cursor.execute("INSERT INTO uuid VALUES (?, ?, ?)", (key, username, uuid))
        self.connection.commit()

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
    

    #
    def put_user(
            self, 
            key, time, could_not_find_player,
            bedwars_final_kills, bedwars_final_deaths, bedwars_kills, bedwars_deaths, bedwars_wins, 
            bedwars_losses, bedwars_beds_broken, bedwars_beds_lost, bedwars_games_played, bedwars_winstreak
            ):
        
        self.cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    key, time, could_not_find_player,
                    bedwars_final_kills, bedwars_final_deaths, bedwars_kills, bedwars_deaths, bedwars_wins, 
                    bedwars_losses, bedwars_beds_broken, bedwars_beds_lost, bedwars_games_played, bedwars_winstreak
                )
            )
        self.connection.commit()

    def put_user_gamemode(
            self, key, time, 
            Bedwars_Ones_Wins, Bedwars_Ones_Losses, Bedwars_Ones_FKDR, Bedwars_Ones_WLR, Bedwars_Ones_BBLR, 
            Bedwars_Twos_Wins, Bedwars_Twos_Losses, Bedwars_Twos_FKDR, Bedwars_Twos_WLR, Bedwars_Twos_BBLR, 
            Bedwars_Threes_Wins, Bedwars_Threes_Losses, Bedwars_Threes_FKDR, Bedwars_Threes_WLR, Bedwars_Threes_BBLR, 
            Bedwars_Fours_Wins, Bedwars_Fours_Losses, Bedwars_Fours_FKDR, Bedwars_Fours_WLR, Bedwars_Fours_BBLR):
        
        self.cursor.execute(
            "INSERT INTO users_gamestats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                key, time,
                Bedwars_Ones_Wins, Bedwars_Ones_Losses, Bedwars_Ones_FKDR, Bedwars_Ones_WLR, Bedwars_Ones_BBLR, 
                Bedwars_Twos_Wins, Bedwars_Twos_Losses, Bedwars_Twos_FKDR, Bedwars_Twos_WLR, Bedwars_Twos_BBLR, 
                Bedwars_Threes_Wins, Bedwars_Threes_Losses, Bedwars_Threes_FKDR, Bedwars_Threes_WLR, Bedwars_Threes_BBLR, 
                Bedwars_Fours_Wins, Bedwars_Fours_Losses, Bedwars_Fours_FKDR, Bedwars_Fours_WLR, Bedwars_Fours_BBLR
            )
        )
        self.connection.commit()
        

    def get_user(self, key):
        self.cursor.execute("SELECT * FROM users WHERE key=?", (key,))
        return self.cursor.fetchone()