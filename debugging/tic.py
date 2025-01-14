#!/usr/bin/python3

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there's a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def valid_input(board):
    """Validate the user input."""
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. The spot is either taken or out of bounds.")
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")

def tic_tac_toe():
    """Play the Tic-Tac-Toe game."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        print(f"Player {player}'s turn")
        row, col = valid_input(board)
        board[row][col] = player
        player = "O" if player == "X" else "X"
    
    print_board(board)
    print(f"Player {player} wins!")

if __name__ == "__main__":
    tic_tac_toe()
