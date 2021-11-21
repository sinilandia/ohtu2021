class Player:
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.sum = goals + assists

    def player_sort(player):
        return self.sum    
            
    def __str__(self):
        return f"{self.name:20}{str(self.goals):5}{str(self.assists):5}"