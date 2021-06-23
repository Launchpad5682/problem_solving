
# O(n^3) solution, will try for better approach

def isValid(ipaddress):

    ipaddress = ipaddress.split(".")

    for i in ipaddress:
        if (len(i) > 3 or int(i) < 0 or int(i) > 255) or (len(i) > 1 and int(i) == 0) or (len(i) > 1 and int(i) != 0 and i[0] == '0'):
            return False

    return True


def validIPaddresses(string):
    stringNew = string
    size = len(string)

    if size > 12:
        return []

    validIPs = []

    for i in range(1, size - 2):
        for j in range(i+1, size - 1):
            for k in range(j+1, size):
                stringNew = stringNew[:k] + "." + stringNew[k:]
                stringNew = stringNew[:j] + "." + stringNew[j:]
                stringNew = stringNew[:i] + "." + stringNew[i:]

                if isValid(stringNew):
                    validIPs.append(stringNew)

                stringNew = string

    return validIPs


def main():

    string = "1921680"
    print(validIPaddresses(string))


if __name__ == "__main__":
    main()
