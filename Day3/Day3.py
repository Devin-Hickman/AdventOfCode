def findNumTress(right, down, f):
    curIndex = 0
    treeCount = 0
    lineCount = 0
    for line in f:
        if(lineCount % down == 0):
            line = line.strip()
            if line[curIndex] == '#':
                treeCount += 1
            curIndex += right
            curIndex %= len(line)
        lineCount+= 1
    return treeCount


filename = "input.txt"
f = open(filename, "r")
trees = []
for line in f:
    trees.append(line)

print("First ans: " + str(findNumTress(3, 1,trees)))

a = findNumTress(1,1,trees)
b = findNumTress(3,1,trees)
c = findNumTress(5,1,trees)
d = findNumTress(7,1,trees)
e = findNumTress(1,2,trees)

print ("Second ans: " + str(a * b * c * d * e))



