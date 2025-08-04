def valid(board, row, col, num):
    if any(board[row][i] == num for i in range(9)): return False
    if any(board[i][col] == num for i in range(9)): return False
    start_r, start_c = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_r+i][start_c+j] == num: return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if valid(board, i, j, num):
                        board[i][j] = num
                        if solve(board): return True
                        board[i][j] = 0
                return False
    return True

# Example usage with a 9x9 grid with zeros as blanks
puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]
if solve(puzzle):
    for row in puzzle: print(row)
else:
    print("No solution.")
