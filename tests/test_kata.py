import pytest
from src.kata import GameScore, PlayerScore

server_wins = [
    (
        GameScore(
            PlayerScore.Zero,
            PlayerScore.Zero),
        GameScore(
            server_score=PlayerScore.Fifteen,
            receiver_score=PlayerScore.Zero)
    ),
    (
        GameScore(
            PlayerScore.Fifteen,
            PlayerScore.Zero),
        GameScore(
            server_score=PlayerScore.Thirty,
            receiver_score=PlayerScore.Zero)
    ),
    (
        GameScore(
            PlayerScore.Thirty,
            PlayerScore.Zero),
        GameScore(
            server_score=PlayerScore.Fourty,
            receiver_score=PlayerScore.Zero)
    ),
    (
        GameScore(
            PlayerScore.Fourty,
            PlayerScore.Zero),
        GameScore(
            server_score=PlayerScore.Wins,
            receiver_score=PlayerScore.Zero)
        # GameScore(winner=Players.server)
        # ServerWins()
        # GameResult(winner=Players.server)
    ),
    (
        GameScore(
            PlayerScore.Fourty,
            PlayerScore.Fourty),
        #duece_game_Score(),
        #GameScore(duece=True),
        GameScore(server_score=PlayerScore.Advantage, receiver_score=PlayerScore.Fourty)
    ),
    (
        GameScore(
            PlayerScore.Advantage,
            PlayerScore.Fourty),
        GameScore(server_score=PlayerScore.Wins, receiver_score=PlayerScore.Fourty)
    )
]


@pytest.mark.parametrize("current_score, expected_score", server_wins)
def test_server_wins(current_score, expected_score):
    new_score = current_score.server_wins_point()

    assert new_score == expected_score


receiver_wins = [
    (
        GameScore(
            receiver_score=PlayerScore.Zero,
            server_score=PlayerScore.Zero),
        GameScore(
            receiver_score=PlayerScore.Fifteen,
            server_score=PlayerScore.Zero)
    ),
    (
        GameScore(
            receiver_score=PlayerScore.Fifteen,
            server_score=PlayerScore.Zero),
        GameScore(
            receiver_score=PlayerScore.Thirty,
            server_score=PlayerScore.Zero)
    ),
    (
        GameScore(
            receiver_score=PlayerScore.Thirty,
            server_score=PlayerScore.Zero),
        GameScore(
            receiver_score=PlayerScore.Fourty,
            server_score=PlayerScore.Zero)
    ),
    (
        GameScore(
            receiver_score=PlayerScore.Fourty,
            server_score=PlayerScore.Zero),
        GameScore(
            receiver_score=PlayerScore.Wins,
            server_score=PlayerScore.Zero)
    ),
    (
        GameScore(
            receiver_score=PlayerScore.Fourty,
            server_score=PlayerScore.Fourty),
        GameScore(
            receiver_score=PlayerScore.Advantage,
            server_score=PlayerScore.Fourty)
    ),
    (
        GameScore(
            receiver_score=PlayerScore.Advantage,
            server_score=PlayerScore.Fourty),
        GameScore(
            receiver_score=PlayerScore.Wins,
            server_score=PlayerScore.Fourty)
    )
]


@pytest.mark.parametrize("current_score,expected_score", server_wins)
def test_receiver_wins(current_score, expected_score):
    new_score = current_score.receiver_wins_point()

    assert new_score == expected_score
