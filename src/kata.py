from enum import IntEnum


class PlayerScore(IntEnum):
    Zero = 0
    Fifteen = 1
    Thirty = 2
    Fourty = 3
    Wins = 6
    # Loses = 7
    Advantage = 7
    # Duece = 9


class GameScore(object):    
    def __init__(self, server_score: PlayerScore, receiver_score: PlayerScore):
        self.server_score = server_score
        self.receiver_score = receiver_score

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def server_wins_point(self):
        if self.server_score == PlayerScore.Zero:
            return GameScore(
                server_score=PlayerScore.Fifteen,
                receiver_score=self.receiver_score)
        elif self.server_score == PlayerScore.Fifteen:
            return GameScore(
                server_score=PlayerScore.Thirty,
                receiver_score=self.receiver_score)
        elif self.server_score == PlayerScore.Thirty:
            return GameScore(
                server_score=PlayerScore.Fourty,
                receiver_score=self.receiver_score)
        elif self.server_score == PlayerScore.Fourty and self.receiver_score != PlayerScore.Fourty:
            return GameScore(
                server_score=PlayerScore.Wins,
                receiver_score=self.receiver_score)
        elif self.server_score == PlayerScore.Fourty and self.receiver_score == PlayerScore.Fourty:
            return GameScore(
                server_score=PlayerScore.Advantage,
                receiver_score=self.receiver_score)
        elif self.server_score == PlayerScore.Advantage:
            return GameScore(
                server_score=PlayerScore.Wins,
                receiver_score=self.receiver_score)

    def receiver_wins_point(self):
        if self.receiver_score == PlayerScore.Zero:
            return GameScore(
                server_score=self.server_score,
                receiver_score=PlayerScore.Fifteen)
        elif self.receiver_score == PlayerScore.Fifteen:
            return GameScore(
                server_score=self.server_score,
                receiver_score=PlayerScore.Thirty)
        elif self.receiver_score == PlayerScore.Thirty:
            return GameScore(
                server_score=self.server_score,
                receiver_score=PlayerScore.Fourty)
        elif self.receiver_score == PlayerScore.Fourty and self.server_score != PlayerScore.Fourty:
            return GameScore(
                server_score=self.server_score,
                receiver_score=PlayerScore.Wins)
        elif self.receiver_score == PlayerScore.Fourty and self.server_score == PlayerScore.Fourty:
            return GameScore(
                server_score=self.server_score,
                receiver_score=PlayerScore.Advantage)
        elif self.receiver_score == PlayerScore.Advantage:
            return GameScore(
                server_score=self.server_score,
                receiver_score=PlayerScore.Wins)
