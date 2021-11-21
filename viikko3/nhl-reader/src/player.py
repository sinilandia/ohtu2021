class Player:
    def __init__(self, name, goals, assists, nationality):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.sum = goals + assists
        self.nationality = nationality     

    def get_nationality(self):
        return str(self.nationality)   
    
    def get_sum(self):
        return self.sum

    def __str__(self):
        return f"{self.name:20}{str(self.goals):5}{str(self.assists):5}{str(self.nationality):5}"