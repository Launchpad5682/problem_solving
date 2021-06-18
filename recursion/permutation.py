
permutation = []
permutations = []


def search():

    # process permutation
    if len(permutation) == len(arr):
        permutations.append(permutation.copy())

    else:
        size = len(arr)
        for index in range(size):
            if chosen[index] == True:
                continue

            chosen[index] = True
            permutation.append(arr[index])
            search()
            chosen[index] = False
            permutation.pop()


arr = [1, 2, 3]
chosen = []
size = len(arr)

for i in range(size):
    chosen.append(False)

search()
print(permutations)
