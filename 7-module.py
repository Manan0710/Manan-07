# Tic-Tac-Toe game in Python (for 2 players)

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def print_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a win
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full
def is_draw():
    return ' ' not in board

# Game loop
current_player = 'X'

while True:
    print_board()
    move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1

    if board[move] != ' ':
        print("Invalid move! Try again.")
        continue

    board[move] = current_player

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    if is_draw():
        print_board()
        print("It's a draw!")
        break

    # Switch players
    current_player = 'O' if current_player == 'X' else 'X'
