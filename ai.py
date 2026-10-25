from abc import ABC, abstractmethod
from board import Board
import random

class AIPlayer(ABC):
    """Base class for every computer opponent."""

    @abstractmethod
    def choose_move(self, board: Board, mark: str) -> tuple[int, int]:
        """Return a (row, col) tuple for an empty cell on the board."""

class EasyAI(AIPlayer):
    """Picks any empty cell at random."""

    def __init__(self, rng=None) -> None:
        if rng is None:
            rng = random.Random()

        self._rng = rng

    def choose_move(self, board: Board, mark: str) -> tuple[int, int]:
        return self._rng.choice(board.empty_cells())

class HardAI(AIPlayer):
    """Uses Minimax Algorithm to select best row and column"""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()

        self._rng = rng

    def choose_move(self, board : Board, mark : str) -> tuple[int, int]:
        empty_cells = board.empty_cells()

        if not empty_cells:
            raise ValueError("The board has no empty cells.")

        best_moves = []
        best_score = float("-inf")

        for row, col in empty_cells:
            board.place_mark(row, col, mark)

            if board.has_won(mark):
                board.remove_mark(row, col)
                return row, col

            score = self._minimax(board, False)
            board.remove_mark(row, col)

            if score > best_score:
                best_score = score
                best_moves = [(row, col)]

            elif score == best_score:
                best_moves.append((row, col))

        return self._rng.choice(best_moves)

    def _minimax(self, board : Board, maximizing_players: bool) -> int:
        if board.has_won("O"):
            return 1 
        
        if board.has_won("X"):
            return -1
        
        if board.is_full():
            return 0

        if maximizing_players:
            player = "O"
            best_score = float("-inf")
        else:
            player = "X"
            best_score = float("inf")

        for row, col in board.empty_cells():
            board.place_mark(row, col, player)

            score = self._minimax(board, not maximizing_players)

            board.remove_mark(row, col)

            if maximizing_players:
                best_score = max(best_score, score)
            else:
                best_score = min(best_score, score)

        return int(best_score)
