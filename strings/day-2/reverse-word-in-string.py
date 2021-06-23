def reverseWords(string):

    temp = ""

    size = len(string)

    arr = []
    index = 0 
    for i in range(0, size):
        if ord(string[i]) == 32:
            arr.append(temp)
            arr.append(" ")
            temp = ""

        else:
            temp += string[i]

    # last word
    if len(temp) != 0:
        arr.append(temp)

    arr.reverse()

    return "".join(arr)


print(reverseWords("Demo is the best!"))


### break the string and then reverse and join