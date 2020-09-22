sudoku1 = [
    [1, 0, 0, 2, 5, 0, 6, 0, 8],
    [0, 4, 0, 0, 8, 0, 0, 5, 0],
    [5, 0, 8, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 4, 0, 8, 0, 0],
    [4, 0, 0, 8, 0, 1, 0, 6, 0],
    [0, 5, 0, 0, 2, 6, 0, 0, 0],
    [7, 0, 4, 1, 6, 2, 5, 0, 0],
    [6, 0, 5, 4, 7, 0, 1, 2, 3],
    [2, 0, 0, 5, 3, 8, 7, 0, 0],
]

sudoku2 = [
    [0, 7, 0, 0, 0, 0, 0, 0, 9],
    [5, 1, 0, 4, 2, 0, 6, 0, 0],
    [0, 8, 0, 3, 0, 0, 7, 0, 0],
    [0, 0, 8, 0, 0, 1, 3, 7, 0],
    [0, 2, 3, 0, 8, 0, 0, 4, 0],
    [4, 0, 0, 9, 0, 0, 1, 0, 0],
    [9, 6, 2, 8, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 1, 0, 4, 0, 0],
    [7, 0, 0, 2, 0, 3, 0, 9, 6]
]

sudoku3 = [
    [0, 0, 0, 0, 0, 0, 6, 1, 9],
    [0, 2, 3, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 1, 4, 0, 0, 2, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [7, 0, 8, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 3, 4, 0],
    [0, 0, 0, 0, 0, 0, 4, 6, 7],
    [8, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 1, 2, 0, 0, 0]
]

sudoku4 = [
    [0, 0, 6, 0, 9, 0, 2, 0, 0],
    [0, 0, 0, 7, 0, 2, 0, 0, 0],
    [9, 0, 0, 0, 3, 0, 0, 0, 6],
    [0, 9, 0, 5, 0, 8, 0, 7, 0],
    [7, 5, 0, 0, 0, 0, 0, 1, 9],
    [1, 0, 0, 0, 4, 0, 0, 0, 5],
    [0, 1, 0, 3, 0, 9, 0, 8, 0],
    [0, 0, 0, 2, 0, 1, 0, 0, 0],
    [0, 0, 9, 0, 8, 0, 1, 0, 0]
]

backtracked = 0


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("- - - - - - - - - - - - - - - -")
        for j in range(len(board)):
            if j == 0:
                print("|", end="")
            elif j % 3 == 0:
                print("|", end="")
            print(f" {board[i][j]} ", end="")
            if j == 8:
                print("|")
    print("- - - - - - - - - - - - - - - -")


def findEmptyBox(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

    return (-1, -1)


def validRowCol(board, row, col, num):
    for r in range(len(board)):
        if r != row and board[r][col] == num:
            return False
    for c in range(len(board)):
        if c != col and board[row][c] == num:
            return False
    return True


def validSquare(board, row, col, num):
    for r in range(3*(row//3), (3*(row//3))+3):
        for c in range(3*(col//3), (3*(col//3))+3):
            if r != row and c != col and board[r][c] == num:
                return False

    return True


def valid(board, row, col, num):
    return validRowCol(board, row, col, num) and validSquare(board, row, col, num)


def solver(board):
    global backtracked

    row, col = findEmptyBox(board)
    if row == -1:
        printBoard(board)
        if backtracked < 3000:
            print(f"Difficulty Level: Easy, Backtracked: {backtracked} times")
        else:
            print(f"Difficulty Level: Hard, Backtracked: {backtracked} times")
        return True

    for num in range(1, 10):
        if valid(board, row, col, num):
            board[row][col] = num
            if solver(board):
                return True

            board[row][col] = 0
            backtracked = backtracked+1

    return False


solver(sudoku1)
solver(sudoku2)
solver(sudoku3)
solver(sudoku4)
