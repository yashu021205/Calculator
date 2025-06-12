def print_board(board):
    
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()

def check_winner(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = input(f"{player}, where do you want to go? (row and column from 0 to 2, like '1 2'): ")
            row, col = map(int, move.strip().split())
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Oops! Numbers must be from 0 to 2. Try again.")
        except:
            print("Oops! Please enter two numbers separated by a space. Try again.")

def tic_tac_toe():
    print("Welcome to Tic Tac Toe! 🎉\n")
    print("Player 1 is X and Player 2 is O\n")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(f"Player {current_player}")
        
        if board[row][col] != " ":
            print("That spot is taken! Try a different one.\n")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Hooray! Player {current_player} wins! 🎉\n")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie! Great job both players! 🤝\n")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
