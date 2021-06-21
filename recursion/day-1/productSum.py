# naive and best solution as per my knowledge

depth = 1
sum = 0


def productSum(arr, depth):
    sum = 0

    for i in arr:
        if type(i) is list:
            depth += 1
            sum += depth*productSum(i, depth)
            depth -= 1

        else:
            sum += i

    return sum


arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
#arr = [1, 2, 3, [1, 3], 3, 4]
print(productSum(arr, depth))
