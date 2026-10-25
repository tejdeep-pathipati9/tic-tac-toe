from game import Game, GameState
from ai import EasyAI, HardAI
import random
import pytest

@pytest.fixture
def game():
    """A new game."""
    return Game()


@pytest.fixture
def game_before_computer_win() -> Game:
    """A game where O can win on its next move."""
    game = Game(ai=HardAI(random.Random(7)))
    moves = [(0, 1), (0, 2), (1, 1), (1, 2), (0, 0)]
    for row, col in moves:
        assert game.make_move(row, col) is True
    return game


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

@pytest.mark.parametrize("ai_class", [EasyAI, HardAI])
def test_computer_move_places_one_o(ai_class):
    game = Game(ai_class(random.Random(7)))
    assert game.make_move(1, 1) is True

    assert game.make_computer_move() is True
    assert game.board.cell(1, 1) == "X"
    assert len(game.board.empty_cells()) == 7

    o_count = 0
    for row in range(game.board.size):
        for col in range(game.board.size):
            if game.board.cell(row, col) == "O":
                o_count += 1
    assert o_count == 1


@pytest.mark.parametrize("ai_class", [EasyAI, HardAI])
def test_computer_move_returns_turn_to_x(ai_class):
    game = Game(ai_class(random.Random(7)))
    assert game.make_move(1, 1) is True

    assert game.make_computer_move() is True

    assert game.get_player() == "X"
    assert game.is_computer_turn() is False
    assert game.state is GameState.IN_PROGRESS


def test_computer_winning_move_sets_winner(game_before_computer_win: Game):
    game = game_before_computer_win

    assert game.make_computer_move() is True

    assert game.state is GameState.WON
    assert game.get_winner() == "O"
    assert game.get_player() == "O"


def test_computer_move_is_rejected_after_win(game_before_computer_win: Game):
    game = game_before_computer_win
    assert game.make_computer_move() is True
    before = str(game.board)

    assert game.is_computer_turn() is False
    assert game.make_computer_move() is False

    assert str(game.board) == before
    assert game.state is GameState.WON
    assert game.get_winner() == "O"


def test_human_move_is_rejected_after_computer_win(game_before_computer_win: Game):
    game = game_before_computer_win
    assert game.make_computer_move() is True
    before = str(game.board)

    assert game.make_move(2, 0) is False

    assert str(game.board) == before
    assert game.state is GameState.WON
    assert game.get_winner() == "O"
