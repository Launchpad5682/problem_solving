
def firstNonRepeating(string):
    count = [0] * 26

    # storing values
    for i in string:
        count[ord(i) - 97] += 1

    index = -1
    k = 0

    ## checking first occurrence 
    for i in string:
        if count[ord(i)-97] == 1:
            index = k
            break

        k += 1

    return index


def main():

    string = str(input())

    index = firstNonRepeating(string)
    print(index)


if __name__ == "__main__":
    main()
