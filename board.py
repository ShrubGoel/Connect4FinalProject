#board.py created by Shubh

rows = 6
columns = 7

class Board:
    def __init__(self): # Shubh, initializes an empty 6x7 grid using a nested list,
        self.board = [[" " for _ in range(columns)] for _ in range(rows)]

    def print_board(self): #Shubh, prints board
        print("\n  " + "   ".join(str(i + 1) for i in range(columns)))  # Column numbers aligned
        print("  " + "-" * (columns * 4 - 1))  # Top border
        for row in self.board:
            print("| " + " | ".join(row) + " |")  # Board with vertical dividers
            print("  " + "-" * (columns * 4 - 1))  # Horizontal row dividers

    def is_valid_move(self, column): #Shubh, checks if top row of a column is empty
        return 0 <= column < columns and self.board[0][column] == " "

    def get_next_open_row(self, column): #Shubh, returns index of lowest available row (bottom to top)
        for row in range(rows - 1, -1, -1):
            if self.board[row][column] == " ":
                return row
        return None

    def drop_piece(self, row, column, piece): #Shubh, modifies self.board[row][column] to store the player's piece.
        self.board[row][column] = piece

    def is_full(self): #Shubh, checks if entire top column is full
        return all(self.board[0][col] != " " for col in range(columns))
