# Tic-Tac-Toe

A Python terminal game for two players or one player against the computer. Easy AI chooses a random empty cell, while Hard AI uses minimax to avoid losing when it plays second.

## Requirements

- Python 3.10 or later.
- The packages listed in `requirements.txt`, including pytest.

## Setup

Clone the repository and open the project folder:

```bash
git clone https://github.com/tejdeep-pathipati9/tic-tac-toe.git
cd tic-tac-toe
```

Create and activate a virtual environment on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

With the virtual environment active, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the game

From the project folder, run:

```bash
python main.py
```

1. Choose **Two players** or **Versus Computer**.
2. In computer mode, choose **Easy** or **Hard**. The human plays X and the computer plays O.
3. Enter the player names. X always goes first.
4. Enter a row and column from 1 to 3, separated by a space. For example, `2 3` selects the second row and third column.

The board appears at the start and after each accepted move. Invalid input, positions outside the board, and occupied cells show an error and let the same player try again. A row, column, or diagonal of matching marks wins; a full board without a winner is a draw.

## Run the tests

With the virtual environment active, run all tests from the project folder:

```bash
pytest
```

For individual test results, use:

```bash
pytest -v
```

Tests cover the board, turns, wins, draws, and AI behavior. Seeded randomness keeps the results repeatable.