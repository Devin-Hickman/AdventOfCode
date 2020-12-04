def isValidPasswordMinMax(min, max, char, password):
    charCount = 0
    for c in password:
        if c == char:
            charCount += 1
    return charCount >= min and charCount <= max

def isValidPasswordIndex(i1, i2, char, password):
    return (password[i1] == char or password[i2] == char) and password[i1] != password[i2]

filename = "input.txt"
f = open(filename, "r")
numValidMinMax = 0
numValidIndex = 0
for line in f:
    lineArr = line.split()
    minMaxVals = lineArr[0].split("-")
    min = int(minMaxVals[0])
    max = int(minMaxVals[1])
    char = lineArr[1][0]
    password = lineArr[2]
    if isValidPasswordMinMax(min, max, char, password):
        numValidMinMax += 1
    if isValidPasswordIndex(min -1, max -1, char, password):
        numValidIndex +=1

print ("MinMax: " + str(numValidMinMax))
print ("Index:" + str(numValidIndex))
