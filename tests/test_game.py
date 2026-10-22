from game import Game, GameState
import pytest

@pytest.fixture
def game():
    """A new game."""
    return Game()

def test_new_game_starts_with_x(game: Game):
    assert game.get_player() == "X"

def test_new_game_state_in_progress(game: Game):
    assert game.state == GameState.IN_PROGRESS