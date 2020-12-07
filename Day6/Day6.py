def partOne():
    filename = "input.txt"
    f = open(filename, "r")
    totalCount = 0
    anyYes = set()
    for line in f:
        if (line == "\n"):
            totalCount += len(anyYes)
            anyYes.clear()
            continue

        line = line.strip()
        for char in line:
            anyYes.add(char)

    if (len(anyYes) > 0):
        totalCount += len(anyYes)
        f.close()
    return totalCount


def partTwo():
    filename = "input.txt"
    f = open(filename, "r")
    totalCount = 0
    peopleInGroup = 0
    yesCount = {}
    for line in f:
        if (line == "\n"):
            for key,value in yesCount.items():
                if(value == peopleInGroup):
                    totalCount+=1
            peopleInGroup = 0
            yesCount.clear()
            continue

        line = line.strip()
        peopleInGroup += 1
        for char in line:
            if char in yesCount:
                yesCount[char] += 1
            else:
                yesCount[char] = 1

    for key, value in yesCount.items():
        if (value == peopleInGroup):
            totalCount += 1
    f.close()
    return totalCount

print("Part One ", partOne())
print("Part Two ", partTwo())




