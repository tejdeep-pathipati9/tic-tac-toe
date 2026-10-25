import random
import pytest

from ai import AIPlayer, EasyAI, HardAI
from board import Board


@pytest.fixture
def board() -> Board:
    """A fresh board for each AI test."""
    return Board()


def test_abstract_ai_cannot_be_created():
    with pytest.raises(TypeError):
        AIPlayer()


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


def test_hard_ai_takes_an_immediate_winning_move(board: Board):
    occupied_cells = [
        (0, 0, "O"), (0, 1, "O"),
        (1, 1, "X"), (1, 2, "X"), (2, 1, "X"),
    ]
    for row, col, mark in occupied_cells:
        board.place_mark(row, col, mark)
    ai = HardAI(random.Random(0))

    assert ai.choose_move(board, "O") == (0, 2)


def test_hard_ai_blocks_an_immediate_loss(board: Board):
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(1, 1, "O")
    ai = HardAI(random.Random(7))

    assert ai.choose_move(board, "O") == (0, 2)


def test_hard_ai_never_loses_when_playing_second(board: Board):
    
    def check_all_human_moves(position: Board):
        for row, col in position.empty_cells():
            trial = position.copy()
            assert trial.place_mark(row, col, "X") is True
            assert trial.has_won("X") is False

            if trial.is_full():
                continue

            ai = HardAI(random.Random(7))
            move = ai.choose_move(trial, "O")
            assert move in trial.empty_cells()
            assert trial.place_mark(move[0], move[1], "O") is True

            if trial.has_won("O") or trial.is_full():
                continue

            check_all_human_moves(trial)

    check_all_human_moves(board)
