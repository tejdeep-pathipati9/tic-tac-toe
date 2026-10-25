import pytest
from board import Board, EMPTY

@pytest.fixture
def board():
    """A fresh, empty 3x3 board for each test."""
    return Board()

def test_new_board_has_nine_empty_cells(board):
    assert len(board.empty_cells()) == 9

def test_place_mark_puts_mark_on_cell(board):
    assert board.place_mark(1, 1, "X") is True
    assert board.cell(1, 1) == "X"

def test_cannot_place_on_taken_cell(board):                         
    board.place_mark(0, 0, "X")
    result = board.place_mark(0, 0, "O")
    assert result is False
    assert board.cell(0, 0) == "X"

@pytest.mark.parametrize("mark", ["X", "O"])
def test_remove_mark_clears_cell_and_preserves_other_marks(board, mark):
    board.place_mark(1, 1, mark)
    board.place_mark(0, 0, "O")

    assert board.remove_mark(1, 1) is None

    assert board.cell(1, 1) == EMPTY
    assert (1, 1) in board.empty_cells()
    assert board.cell(0, 0) == "O"
    assert len(board.empty_cells()) == 8

def test_removed_cell_can_be_used_again(board):
    board.place_mark(1, 1, "X")
    board.remove_mark(1, 1)

    assert board.place_mark(1, 1, "O") is True
    assert board.cell(1, 1) == "O"

def test_removing_from_empty_cell_leaves_board_empty(board):
    assert board.remove_mark(1, 1) is None
    assert len(board.empty_cells()) == 9

@pytest.mark.parametrize("row, col", [(-1, 0), (0, -1), (3, 0), (0, 3)])
def test_remove_mark_outside_board_leaves_board_unchanged(board, row, col):
    board.place_mark(2, 0, "X")
    board.place_mark(0, 2, "O")
    before = [[board.cell(r, c) for c in range(3)] for r in range(3)]

    assert board.remove_mark(row, col) is None

    assert [[board.cell(r, c) for c in range(3)] for r in range(3)] == before

def test_removing_a_winning_mark_clears_the_win(board):
    for col in range(3):
        board.place_mark(0, col, "X")
    assert board.has_won("X") is True

    board.remove_mark(0, 1)

    assert board.has_won("X") is False
    assert board.cell(0, 1) == EMPTY

@pytest.mark.parametrize("row, col", [(-1, 0), (0, -1), (3, 0), (0, 3)])
def test_off_board_moves_are_rejected(board, row, col):
    assert board.place_mark(row, col, "X") is False
    assert len(board.empty_cells()) == 9

@pytest.mark.parametrize("mark", ["X", "O"])
@pytest.mark.parametrize("positions", [
    # top row
    [(0, 0), (0, 1), (0, 2)],
    # last row
    [(2, 0), (2, 1), (2, 2)],
    # mid row
    [(1, 0), (1, 1), (1, 2)],

    # first column
    [(0, 0), (1, 0), (2, 0)],
    # mid column
    [(0, 1), (1, 1), (2, 1)],
    # last column
    [(0, 2), (1, 2), (2, 2)],

    # diagonal - left to right
    [(0, 0), (1, 1), (2, 2)], 
    # diagonal - right to left
    [(0, 2), (1, 1), (2, 0)], 
    
])
def test_has_won_for_winning_line(mark, positions):
    board = Board()

    for row, col in positions:
        board.place_mark(row, col, mark)

    assert board.has_won(mark) is True