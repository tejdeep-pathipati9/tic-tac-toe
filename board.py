EMPTY = " "
SIZE = 3

class Board:
    """Manage a 3 X 3 board using zero-based row and column indices."""

    def __init__(self) -> None:
        """Create an empty board."""
        self._size: int = SIZE
        self._grid: list[list[str]] = [[EMPTY] * SIZE for _ in range(SIZE)]

    @property
    def size(self) -> int:
        """Return the number of rows and columns."""
        return self._size

    def cell(self, row: int, col: int) -> str:
        """Return the mark or empty space at the given position."""
        return self._grid[row][col]

    def _in_range(self, row: int, col: int) -> bool:
        """Return whether the position is on the board."""
        return 0 <= row < self._size and 0 <= col < self._size

    def place_mark(self, row: int, col: int, mark: str) -> bool:
        """Place a mark, returning False for occupied or off-board cells."""
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
        """Return whether the board has no empty cells."""
        return not self.empty_cells()

    def copy(self) -> "Board":
        """Return an independent copy of this board."""
        clone = Board()
        clone._grid = [row[:] for row in self._grid]
        return clone

    def remove_mark(self, row: int, col: int) -> None:
        """Clear a cell; leave the board unchanged for off-board positions."""
        if self._in_range(row, col):
            self._grid[row][col] = EMPTY

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
        """Return the board as rows of cells separated by grid lines."""
        separator = "-+-".join("-" * self._size)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)
