from abc import ABC, abstractmethod
from board import Board
import random

class AIPlayer(ABC):
    """Define the move-selection interface for computer opponents."""

    @abstractmethod
    def choose_move(self, board: Board, mark: str) -> tuple[int, int]:
        """Return an empty cell's zero-based coordinates without changing the board."""

class EasyAI(AIPlayer):
    """Select a random empty cell."""

    def __init__(self, rng=None) -> None:
        """Use the supplied random generator, or create one."""
        if rng is None:
            rng = random.Random()

        self._rng = rng

    def choose_move(self, board: Board, mark: str) -> tuple[int, int]:
        """Return a random empty cell without changing the board."""
        return self._rng.choice(board.empty_cells())

class HardAI(AIPlayer):
    """Use minimax to choose the best move for the computer playing O."""

    def __init__(self, rng=None):
        """Use the random generator to break ties between equally good moves."""
        if rng is None:
            rng = random.Random()

        self._rng = rng

    def choose_move(self, board : Board, mark : str) -> tuple[int, int]:
        """Choose O's best move, raising ValueError if no empty cells remain."""
        empty_cells = board.empty_cells()

        if not empty_cells:
            raise ValueError("The board has no empty cells.")

        best_moves = []
        best_score = float("-inf")

        for row, col in empty_cells:
            board.place_mark(row, col, mark)

            # Prefer an immediate win over other moves with the same minimax score.
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
        """Score a position: 1 for an O win, -1 for an X win, and 0 for a draw.
        O maximizes the score and X minimizes it. Undo simulated moves so each branch 
        starts from the same board position.
        """
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
