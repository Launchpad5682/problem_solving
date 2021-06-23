
from collections import defaultdict


def miniCharWords(arr):
    dictionary = {}

    # storing values
    for i in arr:
        dictionary[i] = {}
        for j in i:
            if dictionary[i].get(j, 'empty') == 'empty':
                dictionary[i][j] = 1
                continue

            dictionary[i][j] = dictionary[i][j] + 1

    # making counts
    counts = {}

    for i in dictionary:
        for j in i:
            if counts.get(j, 'empty') == 'empty':
                counts[j] = dictionary[i][j]
                continue

            counts[j] = max(counts[j], dictionary[i][j])

    # returning array
    arr = []

    for i in counts:
        for j in range(0, counts[i]):
            arr.append(i)

    return arr


def main():
    words=["this", "that", "did", "deed", "them!", "a"]
    print(miniCharWords(words))


if __name__ == "__main__":
    main()
