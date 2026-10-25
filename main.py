import random
from ai import EasyAI, HardAI
from game import Game, GameState

def ask_for_game_mode() -> int:
    print("\nChoose a game mode\n")
    print(" 1. Two players")
    print(" 2. Versus Computer")

    choice = input("\nEnter your choice: ").strip()

    while not choice.isdigit() or choice not in ("1", "2"):
        choice = input("Invalid choice! Please enter 1 or 2: ").strip()

    return int(choice)


def ask_computer_difficulty_level() -> int:
    print("\nChoose a difficulty level\n")
    print(" 1. Easy")
    print(" 2. Hard")

    level = input("\nEnter your preferred difficulty level: ").strip()

    while not level.isdigit() or level not in ("1", "2"):
        level = input("Invalid choice! Please enter 1 or 2: ").strip()
        
    return int(level)

def ask_for_input_from_player(game: Game, names: dict[str, str]) -> tuple[int, int]:
    while True:
        grid_index = input(f"\n{names[game.get_player()]}, enter row and column (1-3), like 2 3: ").split()

        if len(grid_index) != 2:
            print("Invalid input! Enter a row and column, for example: 2 3.")
            continue

        if not grid_index[0].isdigit():
            print("Invalid row! Enter a number.")
            continue

        if grid_index[0] not in ("1", "2", "3"):
            print("Row must be 1, 2, or 3.")
            continue

        if not grid_index[1].isdigit():
            print("Invalid column! Enter a number.")
            continue

        if grid_index[1] not in ("1", "2", "3"):
            print("Column must be 1, 2, or 3.")
            continue

        return int(grid_index[0]) - 1, int(grid_index[1]) - 1

def ask_for_player_names(choice) -> dict[str, str]:
    names = {}

    if choice == 1:
        player_1 = input("\nEnter Player 1's name (X): ").strip()
        names["X"] = str(player_1)

        player_2 = input("\nEnter Player 2's name (O): ").strip()
        names["O"] = str(player_2)

        print(f"\n{names['X']} plays X and goes first.")
        print(f"{names['O']} plays O.")

    if choice == 2:
        player_1 = input("\nEnter Player 1's name (X): ").strip()
        names["X"] = str(player_1)

        names["O"] = "Computer"

        print(f"\n{names['X']} plays X and goes first.")
        print(f"{names['O']} plays O.\n")

    return names

def main() -> None:
    print("\nWelcome to Tic Tac Toe!!!")

    game_mode = ask_for_game_mode()
    ai = None

    if game_mode == 2:
        difficulty = ask_computer_difficulty_level()
        rng = random.Random()

        if difficulty == 1:
            ai = EasyAI(rng)
        else:
            ai = HardAI(rng)

    names = ask_for_player_names(game_mode)
    game = Game(ai)

    print(game.get_board())

    while game.state is GameState.IN_PROGRESS:
        computer_turn = game.is_computer_turn()

        if computer_turn:
            print("\nComputer's turn (O).")
            result = game.make_computer_move()
        else:
            row, col = ask_for_input_from_player(game, names)
            result = game.make_move(row, col)

        if result is False:
            if computer_turn:
                print("The computer could not make a valid move.")
                return

            print("That cell is already taken. Please try again.\n")
            print(game.get_board())
            continue

        print()
        print(game.get_board())

        winner = game.get_winner()

        if winner is not None:
            print(f"\n{names[winner]} ({winner}) wins!")
        elif game.state is GameState.DRAW:
            print("\nIt's a draw!")


if __name__ == "__main__":
    main()