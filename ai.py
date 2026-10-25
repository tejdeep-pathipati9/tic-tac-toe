from abc import ABC, abstractmethod
import random

class AIPlayer(ABC):
    """Base class for every computer opponent."""

    @abstractmethod
    def choose_move(self, board, mark):
        """Return a (row, col) tuple for an empty cell on the board."""

class EasyAI(AIPlayer):
    """Picks any empty cell at random."""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()
        self._rng = rng

    def choose_move(self, board, mark):
        return self._rng.choice(board.empty_cells())

class HardAI(AIPlayer):
    """Uses Minimax Algorithm to select best row and column"""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()
        self._rng = rng

    def choose_move(self, board, mark):
        pass
