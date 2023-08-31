from managers.sql_manager import SqlManager


class CosmeticsManager:
    def __init__(self):
        sql = SqlManager("data/database.db")

    def _cosmetics_wings(self, user):
        """get wings for user"""
        raise NotImplementedError
    
    def _cosmetics_particles(self, user):
        """get particles for user"""
        raise NotImplementedError
    
    def _cosmetics_hats(self, user):
        """get hats for user"""
        raise NotImplementedError
    
    def _cosmetics_ears(self, user):
        """get ears for user"""
        raise NotImplementedError
    
    def _cosmetics_capes(self, user):
        """get capes for user"""
        raise NotImplementedError
    
    
    