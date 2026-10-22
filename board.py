EMPTY = " "
SIZE = 3

class Board:
    """A square Tic-Tac-Toe board."""

    def __init__(self) -> None:
        self._size = SIZE
        self._grid = [[EMPTY] * SIZE for _ in range(SIZE)]

    @property
    def size(self) -> int:
        return self._size

    def cell(self, row: int, col: int) -> str:
        """Return the mark at row, col (counting from 0)."""
        return self._grid[row][col]

    def _in_range(self, row: int, col: int) -> bool:
        return 0 <= row < self._size and 0 <= col < self._size

    def place_mark(self, row: int, col: int, mark: str) -> bool:
        """Place mark at row, col. Return True if placed, False if not allowed."""
        if not self._in_range(row, col):
            return False
        if self._grid[row][col] != EMPTY:
            return False
        self._grid[row][col] = mark
        return True

    def empty_cells(self) -> list[tuple[int, int]]:
        """Return a list of (row, col) pairs for every empty cell."""
        return [(r, c) for r in range(self._size) for c in range(self._size)
                if self._grid[r][c] == EMPTY]

    def is_full(self) -> bool:
        return not self.empty_cells()

    def copy(self) -> "Board":
        """Return an independent copy of this board."""
        clone = Board()
        clone._grid = [row[:] for row in self._grid]
        return clone

    def has_won(self, mark: str) -> bool:
        """Return whether the given mark has a winning row, column, or diagonal."""
        for row in range(self._size):
            if all(self._grid[row][col] == mark for col in range(self._size)):
                return True
            
        for col in range(self._size):
            if all(self._grid[row][col] == mark for row in range(self._size)):
                return True
            
        if all(self._grid[i][i] == mark for i in range(self._size)):
            return True

        if all(self._grid[i][self._size - i - 1] == mark for i in range(self._size)):
            return True
        
        return False
    
    def __str__(self) -> str:
        separator = "-+-".join("-" * self._size)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)