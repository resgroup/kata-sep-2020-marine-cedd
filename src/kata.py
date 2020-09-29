from enum import IntEnum


class PlayerScore(IntEnum):
    Zero = 0
    Fifteen = 1
    Thirty = 2
    # etc


class GameScore(object):    # enum?
    def __init__(self, server_score: PlayerScore, receiver_score: PlayerScore):
        self.server_score = server_score
        self.receiver_score = receiver_score

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def server_wins_point(self):
        if self.server_score == PlayerScore.Zero:
            return GameScore(
                server_score=PlayerScore.Fifteen,
                receiver_score=PlayerScore.Zero)
        else:
            return GameScore(
                server_score=PlayerScore.Thirty,
                receiver_score=PlayerScore.Zero)


#
# class Player(object):
