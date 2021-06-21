one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"


def validString(one, two, three):
    if len(one) + len(two) != len(three):
        return False

    return interWeave(one, two, three, 0, 0)


def interWeave(one, two, three, i, j):
    k = i + j

    if k == len(three):
        return True

    # increase the i pointer until it is matching with the third string
    if i < len(one) and one[i] == three[k]:
        if interWeave(one, two, three, i+1, j):
            return True

    # increase the j pointer until it is matching with third string
    if j < len(two) and two[j] == three[k]:
        return interWeave(one, two, three, i, j+1)

    return False


print(validString(one, two, three))
