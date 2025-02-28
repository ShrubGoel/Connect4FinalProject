rows = 6
columns = 7

class Board:
    def __init__(self):
        self.board = [[" " for _ in range(columns)] for _ in range(rows)]

    def print_board(self):
        print("\n  1 2 3 4 5 6 7")  # Column headers (extra space for alignment)
        print(" -----------------")  # Divider line
        for row in self.board:
            print("| " + " ".join(row) + " |")  # Proper spacing for alignment
        print(" -----------------")  # Bottom border

    def is_valid_move(self, column):
        return 0 <= column < columns and self.board[0][column] == " "

    def get_next_open_row(self, column):
        for row in range(rows - 1, -1, -1):
            if self.board[row][column] == " ":
                return row
        return None

    def drop_piece(self, row, column, piece):
        self.board[row][column] = piece

    def is_full(self):
        return all(self.board[0][col] != " " for col in range(columns))
