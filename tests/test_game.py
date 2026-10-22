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

def test_new_game_winner_is_None(game: Game):
    assert game.winner is None

def test_make_valid_X_move(game : Game):
    result = game.make_move(0, 0)
    assert result is True
    # Players switch after a valid move.
    assert game.current_player == "O"

def test_make_valid_O_move(game : Game):
    game.make_move(1,1)
    result = game.make_move(0, 0)
    assert result is True
    # Players switch after a valid move.
    assert game.current_player == "X"

def test_make_invalid_X_move(game : Game):
    game.make_move(1, 1)
    game.make_move(0, 1)
    result = game.make_move(0, 1)
    assert result is False
    # Players don't switch after an invalid move.
    assert game.current_player == "X"

def test_make_invalid_O_move(game : Game):
    game.make_move(1, 1)
    result = game.make_move(1, 1)
    assert result is False
    # Players don't switch after an invalid move.
    assert game.current_player == "O"

def test_get_winner_with_X(game: Game):
    game.make_move(0, 1)
    game.make_move(0, 2)
    game.make_move(1, 1)
    game.make_move(1, 2)
    result = game.make_move(2, 1)
    assert game.state is GameState.WON
    assert result is True
    assert game.winner == "X"

def test_get_winner_with_O(game: Game):
    game.make_move(0, 1)
    game.make_move(0, 2)
    game.make_move(1, 1)
    game.make_move(1, 2)
    game.make_move(0, 0)
    result = game.make_move(2, 2)
    assert game.state is GameState.WON
    assert result is True
    assert game.winner == "O"

def test_full_board_without_winner_is_draw(game: Game):
    moves = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 0), (2, 2),
    ]

    for row, col in moves:
        assert game.make_move(row, col) is True

    assert game.board.is_full() is True
    assert game.board.has_won("X") is False
    assert game.board.has_won("O") is False
    assert game.state is GameState.DRAW
    assert game.get_winner() is None