board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


"""
row, column and subgrid
fill the options and when get wrong, backtrack the code
-> Rule 1: The element shouldn't be present in the row(use row as a variable)
-> Rule 2: The element shouldn't be present in the col(use col as a variable)
-> Rule 3: Check for the digit in subgrid too
"""


def solveSudoku(board, row, col):

    # check it has reached the last column
    if col == len(board[row]):
        row += 1
        col = 0

        # check if it is the last row, it has reached the last element of the matrix
        if row == len(board):
            return True

    # if it's 0 then can place any number
    if board[row][col] == 0:
        return digitPlace(row, col, board)

    return solveSudoku(board, row, col + 1)


def digitPlace(row, col, board):

    for digit in range(1, 10):
        if canPlace(digit, row, col, board):
            board[row][col] = digit
            if solveSudoku(board, row, col+1):
                return True

    # if nothing works then set the board value back to 0
    board[row][col] = 0
    return False


def canPlace(value, row, col, board):

    rowElements = board[row]
    colElements = map(lambda c: c[col], board)  # map(function, iterable)

    # values found in row or column
    if value in rowElements or value in colElements:
        return False

    # checking subgrid
    subGridRow = (row // 3) * 3  # floor division
    subGridCol = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            row2check = subGridRow + i
            col2check = subGridCol + j
            valuePresent = board[row2check][col2check]

            if valuePresent == value:
                return False
            

    return True


solveSudoku(board,0,0)
print(board)
