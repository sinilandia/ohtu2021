class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        highest_player = self.highest_score()

        if self.winner():
            score = "Win for " + highest_player
        
        elif self.deuce():
            score = "Deuce"
        
        elif self.all():
            if self.m_score1 == 0:
                score = "Love"
            elif self.m_score1 == 1:
                score = "Fifteen"
            elif self.m_score1 == 2:
                score = "Thirty"
            elif self.m_score1 == 3:
                score = "Forty"
            score = score + "-All"

        elif self.advantage():
            score = "Advantage " + highest_player
            
        else:
            score = self.running_score()

        return score
    
    def highest_score(self):
        if self.m_score1 > self.m_score2:
            return self.player1_name
        return self.player2_name
    
    def winner(self):
        if self.m_score1 >= 4 and self.m_score1 >= self.m_score2 + 2:
            return True; #player1 wins
        
        if self.m_score2 >= 4 and self.m_score2 >= self.m_score1 +2:
            return True; #player2 wins
        
        return False
    
    def deuce(self):
        if self.m_score1 == self.m_score2 and self.m_score1 > 3:
            return True
        return False

    def advantage(self):
        difference = 0
        if self.m_score1 >= 3 and self.m_score2 >= 3:
            difference = self.m_score1 - self.m_score2
        if difference == 1 or difference == -1:
            return True
        return False
    
    def all(self):
        if self.m_score1 == self.m_score2:
            return True
        return False
    
    def running_score(self):
        temp_score = ""
        if self.m_score1 == 0:
            temp_score = "Love-"
        if self.m_score1 == 1:
            temp_score = "Fifteen-"
        if self.m_score1 == 2:
            temp_score = "Thirty-"
        if self.m_score1 == 3:
            temp_score = "Forty-"
        
        if self.m_score2 == 0:
            temp_score = temp_score + "Love"
        if self.m_score2 == 1:
            temp_score = temp_score + "Fifteen"
        if self.m_score2 == 2:
            temp_score = temp_score + "Thirty"
        if self.m_score2 == 3:
            temp_score = temp_score + "Forty"

        return temp_score
        
        
    

    

        

