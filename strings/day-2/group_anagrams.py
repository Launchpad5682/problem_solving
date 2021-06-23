
def anagramHelper(string):
    sum = 0
    for i in string:

        sum += ord(i)

    return sum


def anagramList(words, chosen):

    anagramPairs = []

    for index, element in enumerate(words):
        if chosen[index] == False:
            arr = [element]
            #print(index)
            chosen[index] = True
            for i, j in enumerate(words[index+1:]):
                if anagramHelper(element) == anagramHelper(j):
                    arr.append(j)
                    #print(index+i+1)
                    chosen[index+i+1] = True

            anagramPairs.append(arr)

    return anagramPairs


def main():
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    chosen = [False] * len(words)
    print(anagramList(words, chosen))


if __name__ == "__main__":

    main()
