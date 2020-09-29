from src.kata import update_score, GameScore, PlayerScore, Player

def test_0_0_server_wins():
    current_score = GameScore(
        server_score=PlayerScore.Zero,
        receiver_score=PlayerScore.Zero)
    
    new_score = current_score.update_score(
        current_score, 
        winner=Player.Server)

    expected_score = GameScore(
        server_score=PlayerScore.Fifteen,
        receiver_score=PlayerScore.Zero)

    assert new_score == expected_score