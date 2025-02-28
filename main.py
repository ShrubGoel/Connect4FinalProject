from board import Board
from player import Player
from game import Game

def main():
    print("Welcome to Connect Four!")
    board = Board()
    players = [Player("Player 1", "X"), Player("Player 2", "O")]
    game = Game(board, players)

    board.print_board()

    while True:
        player = players[game.current_player_index]
        try:
            column = int(input("\n{} ({}), choose a column (1-7): ".format(player.name, player.piece))) - 1

            if board.is_valid_move(column):
                row = board.get_next_open_row(column)
                board.drop_piece(row, column, player.piece)
                board.print_board()

                if game.winning_move(player.piece):
                    print("🎉 {} ({}) wins!".format(player.name, player.piece))
                    break
                elif board.is_full():
                    print("It's a draw!")
                    break
                else:
                    game.switch_player()
            else:
                print("Invalid move. Column full or out of range.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
