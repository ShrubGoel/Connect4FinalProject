#game.py created by Shubh

class Game: #Shubh, Initializes the game with a board and a list of players
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.current_player_index = 0

    def switch_player(self): #Shubh, Switches the turn to the other player.
        self.current_player_index = 1 - self.current_player_index

    def winning_move(self, piece): #Shubh,checks if the given player has won by connecting four pieces in a row, column, or diag; returns bool
        board = self.board.board
        rows, columns = len(board), len(board[0])

        #Shubh, Horizontal check
        for row in range(rows):
            for col in range(columns - 3):
                if all(board[row][col + i] == piece for i in range(4)):
                    return True

        #Shubh, Vertical check
        for col in range(columns):
            for row in range(rows - 3):
                if all(board[row + i][col] == piece for i in range(4)):
                    return True

        #Shubh, Positive diagonal check (\)
        for row in range(rows - 3):
            for col in range(columns - 3):
                if all(board[row + i][col + i] == piece for i in range(4)):
                    return True

        #Shubh, Negative diagonal check (/)
        for row in range(3, rows):
            for col in range(columns - 3):
                if all(board[row - i][col + i] == piece for i in range(4)):
                    return True

        return False
