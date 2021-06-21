# n-queen problem

# check row, column, diagonal

def canPlace(x, y, chessBoard):
    n = len(chessBoard)

    for i in range(0, n):
        for j in range(0, n):
            if chessBoard[i][j] == "Q":
                if x == i or y == j or (x+y) == (i+j) or (x-y) == (i-j):
                    # checking row, column, diagonals
                    return False

    return True

# solving row-wise


def solve(chessBoard, row, solution):
    n = len(chessBoard)

    if row == n:
        solution = int(solution) + 1
        print("Solution: "+str(solution))
        print("---"*n)
        for i in range(0, n):
            for j in range(0, n):
                print(chessBoard[i][j]+"|", end=" ")
            print()
            print("---"*n)

        return solution

    for j in range(0, n):
        if canPlace(row, j, chessBoard) == True:
            chessBoard[row][j] = "Q"
            solution = solve(chessBoard, row+1, solution)
            chessBoard[row][j] = "x"  # backtrack step

    return solution

def main():

    n = int(input("Enter NxN chess board size: "))
    chessBoard = []
    row = []
    for i in range(0, n):
        row.append('x')

    for i in range(0, n):
        chessBoard.append(row.copy())

    row = 0
    solution_count = 0
    solution_count = solve(chessBoard, row, solution_count)
    print(solution_count)


if __name__ == "__main__":
    main()
