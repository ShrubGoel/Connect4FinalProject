import unittest
from board import Board
from game import Game

# Assuming rows and columns are defined globally
rows = 6
columns = 7


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = board.Board()

    def test_initial_board_empty(self):
        for row in self.board.board:
            for cell in row:
                self.assertEqual(cell, " ")


    def test_get_next_open_row(self):
        self.assertEqual(self.board.get_next_open_row(3), rows - 1)  # Should be last row
        self.board.drop_piece(rows - 1, 3, "X")
        self.assertEqual(self.board.get_next_open_row(3), rows - 2)  # Next available row
        for i in range(rows):  # Fill the column
            self.board.drop_piece(i, 3, "X")
        self.assertIsNone(self.board.get_next_open_row(3))  # No open row left

    def test_drop_piece(self):
        self.board.drop_piece(rows - 1, 3, "X")
        self.assertEqual(self.board.board[rows - 1][3], "X")
        self.board.drop_piece(rows - 2, 3, "O")
        self.assertEqual(self.board.board[rows - 2][3], "O")

    def setUp(self):
        self.board = Board()
        self.players = ["X", "O"]
        self.game = Game(self.board, self.players)

    def test_switch_player(self):
        self.assertEqual(self.game.current_player_index, 0)
        self.game.switch_player()
        self.assertEqual(self.game.current_player_index, 1)
        self.game.switch_player()
        self.assertEqual(self.game.current_player_index, 0)

    def test_winning_move_horizontal(self):
        for col in range(4):
            self.board.drop_piece(5, col, "X")
        self.assertTrue(self.game.winning_move("X"))

    def test_winning_move_vertical(self):
        for row in range(4):
            self.board.drop_piece(row, 2, "O")
        self.assertTrue(self.game.winning_move("O"))

    def test_winning_move_positive_diagonal(self):
        for i in range(4):
            self.board.drop_piece(5 - i, i, "X")
        self.assertTrue(self.game.winning_move("X"))

    def test_winning_move_negative_diagonal(self):
        for i in range(4):
            self.board.drop_piece(i, i, "O")
        self.assertTrue(self.game.winning_move("O"))

    def test_no_winning_move(self):
        self.board.drop_piece(5, 0, "X")
        self.board.drop_piece(5, 1, "O")
        self.board.drop_piece(5, 2, "X")
        self.board.drop_piece(5, 3, "O")
        self.assertFalse(self.game.winning_move("X"))
        self.assertFalse(self.game.winning_move("O"))

