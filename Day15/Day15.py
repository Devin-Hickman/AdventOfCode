def solution(startNumbers, turnDesired):
    numTurnSaid = {}
    turnCount = 1
    numTimesSaid = {}
    lastNumSpoken = None
    for x in startNumbers:
        numTurnSaid[x] = turnCount
        numTimesSaid[x] = 1
        turnCount += 1
        lastNumSpoken = x

    while turnCount <= turnDesired:
        if lastNumSpoken not in numTimesSaid or numTimesSaid[lastNumSpoken] == 1:
            nextNum = 0
            numTurnSaid[lastNumSpoken] = turnCount - 1
            if nextNum in numTimesSaid:
                numTimesSaid[nextNum] += 1
            else:
                numTimesSaid[nextNum] = 1
        else:
            nextNum = turnCount - 1 - numTurnSaid[lastNumSpoken]
            numTurnSaid[lastNumSpoken] = turnCount - 1
            if nextNum in numTimesSaid:
                numTimesSaid[nextNum] += 1
            else:
                numTimesSaid[nextNum] = 1

        turnCount += 1
        lastNumSpoken = nextNum

    return lastNumSpoken

print(solution([0,3,6], 2020))
print(solution([0,3,6], 30000000))