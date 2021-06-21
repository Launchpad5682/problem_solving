keypad = {
    1: [],
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
    0: [],
}

mnemonics_comb = []
comb = []


def mnemonics(num, index):
    if len(comb) == len(num):
        # process it
        mnemonics_comb.append(comb.copy())

    else:
        if len(keypad[num[index]]) == 0 and index < len(num):
            comb.append(num[index])
            index += 1
            mnemonics(num, index)
            comb.pop()

        else:
            for element in keypad[num[index]]:
                comb.append(element)
                mnemonics(num, index+1)
                comb.pop()


mnemonics([1, 9, 0, 5], index=0)
print(mnemonics_comb)

"""
[[1, 'w', 0, 'j'],
 [1, 'w', 0, 'k'], 
 [1, 'w', 0, 'l'], 
 [1, 'x', 0, 'j'], 
 [1, 'x', 0, 'k'], 
 [1, 'x', 0, 'l'],
 [1, 'y', 0, 'j'],
 [1, 'y', 0, 'k'], 
 [1, 'y', 0, 'l'], 
 [1, 'z', 0, 'j'], 
 [1, 'z', 0, 'k'], 
 [1, 'z', 0, 'l']]
 """
