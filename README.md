# Connect4FinalProject
# Connect 4 Final Project

# main.py (Driver File) → Manages user input and game flow.
# board.py → Handles board logic (grid, moves, win checks).
# player.py → Defines the Player class.
# game.py → Manages game state, player turns, and win conditions.

# Class Blueprints
#  Board Class:
#   class Board:
#   	def __init__(self):  #Creates an empty 6x7 board.
#   	def is_valid_move(self, column: int) -> bool:  #Checks if a column has space for a move.
#   	def get_next_open_row(self, column: int) -> int: 	# Finds the lowest available row in a column.  
#     def drop_piece(self, row: int, column: int, piece: str):  #Places the player's piece in the board.
#     def is_full(self) -> bool:  #Checks if the board is completely filled.
#     def print_board(self):  #Prints the current board state.

#  Player Class:
#   class Player: def __init__(self, name: str, piece: str): #Creates a player with a name and game piece ('X' or 'O').

#  Game Class:
#   class Game:
#   	def __init__(self, board: Board, players: list):  #Initializes the game with a board and two players.
#     def switch_player(self):  #Switches the turn to the other player.
#     def winning_move(self, piece: str) -> bool:  #Checks if the current player has won.

# Lists
#  Board Grid: A 6x7 nested list representing the Connect Four board, where each element is initially empty.
#  Players List: A list containing two Player objects, one for each player.

# Board Class Functions
#  is_valid_move(column)
#   Purpose: Checks if a move can be made in the given column.
#   Arguments: column (integer) – The column where the player wants to place a piece.
#   Return Type: Boolean – True if the move is valid, False otherwise.

#  get_next_open_row(column)
#   Purpose: Finds the lowest open row in the given column.
#   Arguments: column (integer) – The column to check.
#   Return Type: Integer – The row index where the piece can be placed.

#  drop_piece(row, column, piece)
#   Purpose: Places a piece on the board at the specified location.
#   Arguments: row (integer) – The row index, column (integer) – The column index, piece (string) – The player’s game piece (‘X’ or ‘O’). 
#   Return Type: None.

#  is_full()
#   Purpose: Checks if the board is completely filled.
#   Arguments: None.
#   Return Type: Boolean – True if the board is full, False otherwise.

#  print_board()
#   Purpose: Displays the current state of the board.
#   Arguments: None.
#   Return Type: None.

# Game Class Functions
#  switch_player()
#   Purpose: Switches the turn to the other player.
#   Arguments: None.
#   Return Type: None.

#  winning_move(piece)
#   Purpose: Checks if the current player has won by connecting four pieces in a row, column, or diagonal.
#   Arguments: piece (string) – The player’s game piece (‘X’ or ‘O’).
#   Return Type: Boolean – True if the player has won, False otherwise.




