def genearateDocument(characters, document):
    count_characters = [0]*256  # all the characters

    for i in characters:
        count_characters[ord(i)] += 1

    count_document = [0]*256
    for i in document:
        count_document[ord(i)] += 1

    for i in range(0, 256):
        # if the characters are not available in the
        # character string then it can not make the document
        if count_characters[i] < count_document[i]:
            return False
        else:
            continue

    return True


def main():

    #character = str(input())
    #document = str(input())
    # print(character)
    # print(document)

    character = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"
    print(genearateDocument(character, document))


if __name__ == "__main__":
    main()
