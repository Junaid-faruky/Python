def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1, 10):
                    if is_valid(board, i, j, k):
                        board[i][j] = k
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or \
           board[row//3*3+i//3][col//3*3+i%3] == num:
            return False
    return True

# Example board with 0 as empty
board = [[5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0], ...]  # Complete 9x9 input
solve(board)
print(board)
