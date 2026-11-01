
# Simple Tic-Tac-Toe Game

board = [" " for i in range(9)]

def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True

    return False

def play_game():
    current_player = "X"

    for turn in range(9):
        display_board()

        print("Player", current_player)

        try:
            choice = int(input("Choose a position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice < 0 or choice > 8:
            print("Invalid position! Choose between 1 and 9.")
            continue

        if board[choice] != " ":
            print("Position already taken! Try again.")
            continue

        board[choice] = current_player

        if check_winner(current_player):
            display_board()
            print("Congratulations! Player", current_player, "wins!")
            return

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    display_board()
    print("It's a Draw!")

play_game()
