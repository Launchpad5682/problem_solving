
def caesarCipher(string, k):

    ciphered_string = ""
    for i in string:

        ascii = ord(i)
        ascii += k

        if ascii <= 122:
            ciphered_string += chr(ascii)

        else:
            ascii = (ascii - 122) + 96
            ciphered_string += chr(ascii)

    return ciphered_string


def main():
    string = str(input())
    k = int(input())

    print(caesarCipher(string, k))


if __name__ == "__main__":
    main()
