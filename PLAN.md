1. Goal: Build a tic-tac-toe game that runs in the terminal. It allows a player to compete against another player or an AI opponent.

2. **Requirements**

| ID | Requirement | Type | Priority | How verified |
|---|---|---|---|---|
| R1 | The board contains 3 rows and 3 columns. | Functional | High | Check that a new board has three rows, each containing three empty cells. |
| R2 | X always goes first. | Functional | High | Start a game in each mode and check that X takes the first turn. |
| R3 | A valid move places the current player’s symbol in the selected cell and switches turns. | Functional | High | Make a valid move, then check the cell and the next player. |
| R4 | Invalid moves display an error without changing the board or using up the turn. | Functional | High | Try occupied cells, out-of-range positions, and non-numeric input; check the message, board, and current player. |
| R5 | The board is printed after every valid move. | Functional | High | Play moves in both modes and check that the updated board appears after each human or computer move. |
| R6 | The game detects wins across rows, columns, and diagonals. | Functional | High | Check every winning row, column, and diagonal for both X and O. |
| R7 | A full board without a winner results in a draw. | Functional | High | Use a full board with no winning line and check that a draw is reported. |
| R8 | In versus-computer mode, the human plays X and the computer plays O. | Functional | High | Select versus-computer mode and check the symbols used by each side. |
| R9 | Easy AI selects a random empty cell. | Functional | High | Check that selections are empty cells and that different controlled random choices produce the corresponding moves. |
| R10 | Hard AI uses minimax and never loses when playing second. | Functional | High | Review the algorithm and explore every possible human move sequence, checking that the result is always a computer win or a draw. |

3. **Components**  
    - `board.py`: Contains the `Board` class, which manages the board’s state.
    - `ai.py`: Contains the AI classes, which select the computer’s moves.
    - `game.py`: Manages turns, game modes, and win or draw checks.
    - `main.py`: Handles menus, user input, and printing.
    - `tests/`: Contains pytest tests that verify the game’s behavior.

4. **Decisions**

| Decision | Options | Chosen | Reason |
|---|---|---|---|
| How to organize the AI classes | One AI class with difficulty checks, or an abstract base class with separate subclasses | An abstract `AI` class with a `choose_move(board, mark)` method implemented by `EasyAI` and `HardAI` | Each difficulty handles its own move-selection logic, while the game uses the same interface. |
| How to store the board | A flat list of nine cells, or a nested list containing three rows of three cells | A nested list representing the 3 × 3 board | It matches the board’s layout and allows cells to be accessed using row and column indices. |

5. **What changed**
    - Added a `GameState` enum and an optional AI opponent to `Game` so both modes use the same turn, win, and draw handling.
    - Added player names in `main.py`, using a dictionary to map names to X and O. This keeps display details separate from the game rules.
    - Added `Board.remove_mark()` after the initial Board implementation so minimax can undo simulated moves and leave the real board unchanged.
    - Reprint the board after a player selects an occupied cell so they can see the available positions before trying again.
