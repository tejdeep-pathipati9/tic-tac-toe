import random
import pytest

from ai import AIPlayer, EasyAI
from board import Board


@pytest.fixture
def board() -> Board:
    """A fresh board for each AI test."""
    return Board()

@pytest.mark.parametrize("mark", ["X", "O"])
@pytest.mark.parametrize("seed", [0, 7, 42])
def test_easy_ai_returns_an_empty_cell(board: Board, mark: str, seed: int):
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "O")
    ai = EasyAI(random.Random(seed))
    move = ai.choose_move(board, mark)

    assert move in board.empty_cells()

def test_easy_ai_leaves_board_unchanged(board: Board):
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "O")

    before = []
    for row in range(board.size):
        row_cells = []
        for col in range(board.size):
            row_cells.append(board.cell(row, col))
        before.append(row_cells)

    ai = EasyAI(random.Random(7))

    ai.choose_move(board, "O")

    for row in range(board.size):
        for col in range(board.size):
            assert board.cell(row, col) == before[row][col]
