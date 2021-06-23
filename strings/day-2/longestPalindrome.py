# longest palindrome substring


def checkPalindrome(string):

    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True


def validPalindromes(string):

    maxLen = 0
    palindromeString = ""

    # for all the combinations call the checkPalindrome
    for i in range(0, len(string)):
        for j in range(0, len(string)):

            if checkPalindrome(string[i:j]) == True:
                if len(string[i:j]) > maxLen:
                    palindromeString = string[i:j]
                    maxLen = len(string[i:j])

            else:
                continue

    return palindromeString


print(validPalindromes("abaxyzzyxf"))
