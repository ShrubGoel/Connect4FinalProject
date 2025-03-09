import unittest
from board import Board
from player import Player
from game import Game

rows = 6
columns = 7

#All tests written by Mason

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_empty(self):
        for row in self.board.board:
            for cell in row:
                self.assertEqual(cell, " ")  # Ensure all cells are empty initially

    def test_get_next_open_row(self):
        self.assertEqual(self.board.get_next_open_row(3), rows - 1)  # Last row should be empty
        self.board.drop_piece(rows - 1, 3, "X")
        self.assertEqual(self.board.get_next_open_row(3), rows - 2)  # Next available row
        for i in range(rows):  # Fill the column from row 0 upwards
            self.board.drop_piece(i, 3, "X")
        self.assertIsNone(self.board.get_next_open_row(3))  # No open row left

    def test_drop_piece(self):
        self.board.drop_piece(rows - 1, 3, "X")
        self.assertEqual(self.board.board[rows - 1][3], "X")
        self.board.drop_piece(rows - 2, 3, "O")
        self.assertEqual(self.board.board[rows - 2][3], "O")

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.game = Game(self.board, self.players)

    def test_switch_player(self):
        self.assertEqual(self.game.current_player_index, 0)
        self.game.switch_player()
        self.assertEqual(self.game.current_player_index, 1)
        self.game.switch_player()
        self.assertEqual(self.game.current_player_index, 0)

    def test_winning_move_horizontal(self):
        for col in range(4):
            self.board.drop_piece(rows - 1, col, "X")  # Ensure pieces fall to the bottom row
        self.assertTrue(self.game.winning_move("X"))

    def test_winning_move_vertical(self):
        for row in range(4):
            self.board.drop_piece(row, 2, "O")  # Pieces stack vertically
        self.assertTrue(self.game.winning_move("O"))

    def test_winning_move_positive_diagonal(self):
        # Create a diagonal manually by dropping pieces in staggered order
        for i in range(4):
            for j in range(i):  # Drop extra pieces to fill spaces below diagonal
                self.board.drop_piece(rows - j - 1, i, "O")
            self.board.drop_piece(rows - i - 1, i, "X")  # Drop piece for diagonal
        self.assertTrue(self.game.winning_move("X"))

    def test_winning_move_negative_diagonal(self):
        for i in range(4):
            for j in range(i):  # Drop extra pieces to fill spaces below diagonal
                self.board.drop_piece(j, i, "X")
            self.board.drop_piece(i, i, "O")  # Drop piece for diagonal
        self.assertTrue(self.game.winning_move("O"))

    def test_no_winning_move(self):
        self.board.drop_piece(5, 0, "X")
        self.board.drop_piece(5, 1, "O")
        self.board.drop_piece(5, 2, "X")
        self.board.drop_piece(5, 3, "O")
        self.assertFalse(self.game.winning_move("X"))
        self.assertFalse(self.game.winning_move("O"))
