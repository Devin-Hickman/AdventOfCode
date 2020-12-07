import math

filename = "input.txt"
f = open(filename, "r")


rowIndex=0
colIndex=0
maxSeatId = 0
minSeatId = 1000000
seatIDs = []

def getLower(left, right):
    return math.floor((left + right)/2)

def getUpper(left, right):
    return math.floor((left + right)/2) + 1

def getSeat(row, col):
    return (8 * row) + col

for line in f:
    leftRow = 0
    rightRow = 127
    leftcol = 0
    rightCol = 7
    for char in line:
        if(char == 'F'):
            rowIndex = rightRow = getLower(leftRow, rightRow)
        elif(char == 'B'):
            rowIndex = leftRow = getUpper(leftRow, rightRow)
        elif(char == 'L'):
            colIndex = rightCol = getLower(leftcol, rightCol)
        elif (char == 'R'):
            colIndex = leftcol = getUpper(leftcol, rightCol)

    maxSeatId = max(maxSeatId, getSeat(rowIndex, colIndex))
    minSeatId = min(minSeatId, getSeat(rowIndex, colIndex))
    seatIDs.append(getSeat(rowIndex, colIndex))

for i in range(minSeatId,maxSeatId):
    if i not in seatIDs:
        print("Missing seat", i)

print("max ", maxSeatId)
print("min ", minSeatId)




