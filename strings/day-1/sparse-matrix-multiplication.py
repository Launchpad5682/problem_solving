# sparse matrix multiplication

def matrixMultiplication(a, n, m, b, x, y):
    results = []
    for i in range(n):
        arr = []
        for j in range(y):
            arr.append(0)
        results.append(arr)

    printMatrix(results)
    for i in range(n):
        for j in range(y):
            for k in range(m):
                results[i][j] += (a[i][k] * b[k][j])

    return results


def printMatrix(c):

    for i in c:
        print(i)


def main():
    """
    a = []
    b = []

    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input()))

        a.append(row.copy())

    x = int(input("Enter the number of rows: "))
    y = int(input("Enter the number of columns: "))

    for i in range(x):
        row = []
        for j in range(y):
            row.append(int(input()))

        b.append(row.copy())
    """
    X = [[1, 7, 3],
         [3, 5, 6],
         [6, 8, 9]]
    Y = [[1, 1, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]

    #c = matrixMultiplication(a, n, m, b, x, y)
    c = matrixMultiplication(X, 3, 3, Y, 3, 4)
    printMatrix(c)


if __name__ == "__main__":
    main()
