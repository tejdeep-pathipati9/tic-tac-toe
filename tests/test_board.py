from board import Board

def test_new_board_has_nine_empty_cells():
    board = Board()

    assert len(board.empty_cells()) == 9