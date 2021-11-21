from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        player_list = self.reader.players

        sorted_nationality = filter(lambda p: p.get_nationality() == nationality, list(player_list))
        sorted_players = sorted(sorted_nationality, key=lambda p:p.sum, reverse=True)
        
        return sorted_players