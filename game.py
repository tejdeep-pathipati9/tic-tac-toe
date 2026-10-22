from board import Board
from enum import Enum

class GameState(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    WON = "WON"
    DRAW = "DRAW"

class Game:
    def __init__(self) -> None:
        self.board : Board = Board()
        self.current_player : str = "X"
        self.state : GameState = GameState.IN_PROGRESS
        self.winner : str | None  = None

    def get_board(self) -> Board:
        """Return the current board"""
        return self.board

    def get_player(self) -> str:
        """Return the player whose turn it is"""
        return self.current_player

    def get_winner(self) -> str | None:
        return self.winner
    
    def make_move(self, row: int, col: int) -> bool:
        """Place mark at row, col. Return True if placed, False if not."""
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
        if self.current_player == "X":
            self.current_player = "O"

        else:
            self.current_player = "X"
        