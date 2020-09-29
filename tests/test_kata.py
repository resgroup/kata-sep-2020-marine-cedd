import pytest
from src.kata import GameScore, PlayerScore

server_wins = [
    (
        PlayerScore.Zero,
        PlayerScore.Zero, 
        GameScore(
            server_score=PlayerScore.Fifteen,
            receiver_score=PlayerScore.Zero)
    ),
    (
        PlayerScore.Fifteen,
        PlayerScore.Zero, 
        GameScore(
            server_score=PlayerScore.Thirty,
            receiver_score=PlayerScore.Zero)
    ),
    (
        PlayerScore.Thirty,
        PlayerScore.Zero, 
        GameScore(
            server_score=PlayerScore.Fourty,
            receiver_score=PlayerScore.Zero)
    ),
    (
        PlayerScore.Fourty,
        PlayerScore.Zero,
        # GameScore(winner=Players.server)
        GameScore(server_score=PlayerScore.Wins, receiver_score=PlayerScore.Loses)
        # ServerWins()
        # GameResult(winner=Players.server)
    )
]


@pytest.mark.parametrize("server_score,receiver_score,expected_score", server_wins)
def test_server_wins(server_score, receiver_score, expected_score):
    current_score = GameScore(
        server_score=server_score,
        receiver_score=receiver_score)
    
    new_score = current_score.server_wins_point()

    assert new_score == expected_score
