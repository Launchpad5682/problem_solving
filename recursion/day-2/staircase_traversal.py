
def stairCaseTraversal(height, maxSteps):
    numOfWays = [0 for x in range(height+1)]
    numOfWays[0] = 1
    numOfWays[1] = 1

    for currentHeight in range(2, height+1):
        step = 1
        while step <= maxSteps and step <= currentHeight:
            numOfWays[currentHeight] += numOfWays[currentHeight-step]
            step += 1

    return numOfWays[height]


print(stairCaseTraversal(4, 2))
