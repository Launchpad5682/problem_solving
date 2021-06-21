powerset = []
subset = []


def search(k, n, arr):

    if k == n:
        powerset.append(subset.copy())

    else:
        subset.append(arr[k])
        search(k+1, n, arr)
        subset.pop()
        search(k+1, n, arr)


arr = [5,2,62,3]
search(0, len(arr), arr)

print(powerset)
print(len(powerset))