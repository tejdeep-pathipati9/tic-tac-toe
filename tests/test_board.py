import pytest
from board import Board

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