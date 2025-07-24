def print_board(board):
    for row in board:
        print(" | ".join(row))

def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(row[i] == player for row in board):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player

board = [[" "]*3 for _ in range(3)]
player = "X"
for _ in range(9):
    print_board(board)
    r, c = map(int, input(f"Player {player}, enter row and col (0-2): ").split())
    if board[r][c] == " ":
        board[r][c] = player
        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        player = "O" if player == "X" else "X"
    else:
        print("Cell taken, try again.")
else:
    print("Draw!")
