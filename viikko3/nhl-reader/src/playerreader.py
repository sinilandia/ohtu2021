import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self.players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['nationality']
            )
            self.players.append(player)
        
    def get_players(self):
        return self.players