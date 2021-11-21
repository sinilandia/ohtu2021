import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality']=="FIN":
            player = Player(
                player_dict['name'],
                player_dict['goals'],
                player_dict['assists']
            )
            players.append(player)
    
    def player_sort(player):
        return player.sum    
    sorted_players = sorted(players,key=player_sort, reverse=True)
    
    print("Oliot:")
    for player in sorted_players:
        print(player)
        
if __name__ == "__main__":
    main()
