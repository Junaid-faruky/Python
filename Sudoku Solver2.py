def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if solve(board): return True
                        board[r][c] = 0
                return False
    return True

def is_valid(board, r, c, num):
    row = all(num != board[r][i] for i in range(9))
    col = all(num != board[i][c] for i in range(9))
    box = all(num != board[r//3*3+i][c//3*3+j] for i in range(3) for j in range(3))
    return row and col and box

sudoku = [
 [5,3,0,0,7,0,0,0,0],
 [6,0,0,1,9,5,0,0,0],
 [0,9,8,0,0,0,0,6,0],
 [8,0,0,0,6,0,0,0,3],
 [4,0,0,8,0,3,0,0,1],
 [7,0,0,0,2,0,0,0,6],
 [0,6,0,0,0,0,2,8,0],
 [0,0,0,4,1,9,0,0,5],
 [0,0,0,0,8,0,0,7,9]
]

solve(sudoku)
for row in sudoku: print(row)
