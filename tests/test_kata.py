from src.kata import GameScore, PlayerScore


def test_0_0_server_wins():
    current_score = GameScore(
        server_score=PlayerScore.Zero,
        receiver_score=PlayerScore.Zero)
    
    new_score = current_score.server_wins_point()

    expected_score = GameScore(
        server_score=PlayerScore.Fifteen,
        receiver_score=PlayerScore.Zero)

    assert new_score == expected_score


def test_15_0_server_wins():
    current_score = GameScore(
        server_score=PlayerScore.Fifteen,
        receiver_score=PlayerScore.Zero)

    new_score = current_score.server_wins_point()

    expected_score = GameScore(
        server_score=PlayerScore.Thirty,
        receiver_score=PlayerScore.Zero)

    assert new_score == expected_score
