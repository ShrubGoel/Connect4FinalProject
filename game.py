class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def winning_move(self, piece):
        board = self.board.board
        rows, columns = len(board), len(board[0])

        # Horizontal check
        for row in range(rows):
            for col in range(columns - 3):
                if all(board[row][col + i] == piece for i in range(4)):
                    return True

        # Vertical check
        for col in range(columns):
            for row in range(rows - 3):
                if all(board[row + i][col] == piece for i in range(4)):
                    return True

        # Positive diagonal check (\)
        for row in range(rows - 3):
            for col in range(columns - 3):
                if all(board[row + i][col + i] == piece for i in range(4)):
                    return True

        # Negative diagonal check (/)
        for row in range(3, rows):
            for col in range(columns - 3):
                if all(board[row - i][col + i] == piece for i in range(4)):
                    return True

        return False
