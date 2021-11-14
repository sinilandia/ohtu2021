import unittest
from stats import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())
        self.players = PlayerReaderStub.get_players(self)

    



    
    
    """  
    def test_konstruktori_luo_oikein(self):
        self.assertEquals(self.stats, PlayerReaderStub().get_players)
    """
    

    def test_search(self):
        player = Player("Semenko", "EDM", 4, 12)
        player_info = self.stats.search("Semenko")
        self.assertEquals(player_info.name, player.name)
    
    def test_search_palauttaa_tyhjan(self):
        player_info = self.stats.search("daflkjienaefkn")
        self.assertEquals(player_info, None)

    def test_team(self):
        players_of_team = self.stats.team("PIT")
        name = players_of_team[0].name
        self.assertEquals(name, "Lemieux")

    def test_top_scorers(self):
        player = self.stats.top_scorers(1)
        name = player[0].name
        self.assertEquals(name, "Gretzky")

"""
        for player in self.players:
            if name in player.name:
                return player

        return None
        """
    
   
    
