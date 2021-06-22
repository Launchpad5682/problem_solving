
def runLengthEncoding(string):
    count = 0
    encoded_string = ""
    character = ""

    for i in string:
        if character == "":
            character = i
            count = 1

        else:
            if character == i:
                count += 1

            else:
                if count < 10 and count > 0:
                    encoded_string += str(count) + character

                if count >= 10:

                    while count >= 10:
                        encoded_string += str(9) + character
                        count -= 9

                    if count > 0:
                        encoded_string += str(count) + character

                count = 1
                character = i

    if count < 10 and count > 0:
        encoded_string += str(count) + character

    if count >= 10:

        while count >= 10:
            encoded_string += str(9) + character
            count -= 9

        if count > 0:
            encoded_string += str(count) + character


        count = 1
        character = i

    return encoded_string


def main():

    string = str(input())

    encoded_string = runLengthEncoding(string)

    print(encoded_string)


if __name__ == "__main__":
    main()
