
def palindroneCheck(string):

    n = len(string)
    i = 0
    j = n-1
    while i <= j:
        if string[i] == string[j]:
            i += 1
            j -= 1

        else:
            return False

    return True


def main():
    string = str(input())

    if len(string) == 0:
        print("Invalid string")

    else:
        print(palindroneCheck(string=string))


if __name__ == "__main__":
    main()
