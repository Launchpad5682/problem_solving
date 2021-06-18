
permutation = [] # permutation 
permutations = [] # all the permutations


def search(arr, chosen):

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
            search(arr, chosen)
            chosen[index] = False
            permutation.pop()


arr = [1, 2, 3]
chosen = []
size = len(arr)

# setting chosen to False
for i in range(size):
    chosen.append(False)

search(arr, chosen)
print(permutations)
