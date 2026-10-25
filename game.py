from board import Board
from ai import AIPlayer
from enum import Enum

class GameState(Enum):
    """Represent an ongoing game, a win, or a draw."""

    IN_PROGRESS = "IN_PROGRESS"
    WON = "WON"
    DRAW = "DRAW"

class Game:
    """Manage turns and results for two players or a human against an AI."""

    def __init__(self, ai: AIPlayer | None = None) -> None:
        """Start an empty game with X first and an optional AI playing O."""
        self.board : Board = Board()
        self.current_player : str = "X"
        self.state : GameState = GameState.IN_PROGRESS
        self.winner : str | None  = None
        self.ai = ai

    def get_board(self) -> Board:
        """Return the current board."""
        return self.board

    def get_player(self) -> str:
        """Return the current player's symbol, X or O."""
        return self.current_player

    def get_winner(self) -> str | None:
        """Return the winning symbol, or None if no player has won."""
        return self.winner

    def is_computer_turn(self) -> bool:
        """Return whether the game is ongoing and the AI is due to play."""
        return (
            self.ai is not None
            and self.current_player == "O"
            and self.state is GameState.IN_PROGRESS
        )

    def make_computer_move(self) -> bool:
        """Apply the AI's move, returning False if it cannot take a turn."""
        if self.ai is None or not self.is_computer_turn():
            return False

        row, col = self.ai.choose_move(self.board, self.current_player)
        return self.make_move(row, col)
    
    def make_move(self, row: int, col: int) -> bool:
        """Place the current player's mark. Return True for a valid move or False if the move is rejected.
        Check for a win or draw, then switch players if the game continues.
        """
        if self.state is not GameState.IN_PROGRESS:
            return False

        current_player = self.get_player()

        if not self.board.place_mark(row, col, current_player):
            return False

        if self.board.has_won(current_player):
            self.state = GameState.WON
            self.winner = self.current_player
        
        elif self.board.is_full():
            self.state = GameState.DRAW

        else:
            self.alternate_turn()

        return True

    def alternate_turn(self) -> None:
        """Switch the current player between X and O."""
        if self.current_player == "X":
            self.current_player = "O"

        else:
            self.current_player = "X"