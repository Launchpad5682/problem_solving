
# naive solution

a = 0
b = 1


def fibonacci(n):

    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)

# optimized solution


def fibOptimized(n):

    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        series = []

        for i in range(n):
            series.append(0)

        series[0] = 0
        series[1] = 1

        for index in range(2, n):
            series[index] = series[index-1] + series[index-2]

        return series[n-1]


n = int(input())

# print(fibonacci(n))
print(fibOptimized(n))
