from board import Board
from player import Player
from game import Game

#Main.py coded by Mason

def main():
    print("Welcome to Connect Four!")

    # Get player names
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    # Create board and players
    board = Board()
    players = [Player(player1_name, "X"), Player(player2_name, "O")]
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
