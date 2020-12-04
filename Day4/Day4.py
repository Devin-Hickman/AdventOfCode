import re

def isValidPassportPartOne(passport):
    keyList = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passPortKeyList = []
    splitPort = passport.split()

    for str in splitPort:
        passPortKeyList.append(str.split(":")[0])

    for key in keyList:
        if key not in passPortKeyList:
            return False

    return True

def isValidPassportPartTwo(passport):
    splitPort = passport.split()
    validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    dict = {}
    for str in splitPort:
        dict[str.split(":")[0]] = str.split(":")[1]

    for key, value in dict.items():
        if key == "byr" and not isValidValue(1920, 2002, value):
            return False
        elif key == "iyr" and not isValidValue(2010, 2020, value):
            return False
        elif key == "eyr" and not isValidValue(2020, 2030, value):
            return False
        elif key == "pid":
            if(re.search("^[0-9]{9}$", value)) is None:
                return False
        elif key == "ecl" and value not in validEyeColors:
            return False
        elif key == "hcl":
            if(re.search("^#[a-f0-9]{6}$", value)) is None:
                return False
        elif key == "hgt":
            if "cm" in value:
                try:
                    if not isValidValue(150, 193, int(value.split("c")[0])):
                        return False
                except:
                    return False
            elif "in" in value:
                try:
                    if not isValidValue(59, 76, int(value.split("i")[0])):
                        return False
                except:
                    return False
            else:
                return False

    return True


def isValidValue(min, max, value):
    return min <= int(value) <= max

filename = "input.txt"
f = open(filename, "r")
passPort = ""
validPassportsPartOne = 0
validPassportsPartTwo = 0
for line in f:
    if line == "\n":
        passPort = passPort.strip()
        if isValidPassportPartOne(passPort):
            validPassportsPartOne += 1
            if isValidPassportPartTwo(passPort):
                validPassportsPartTwo += 1
        passPort = ""
    else:
        passPort += line

if passPort != "":
    if isValidPassportPartOne(passPort):
        validPassportsPartOne += 1
        if isValidPassportPartTwo(passPort):
            validPassportsPartTwo += 1

print("Num valid passports part One: " + str(validPassportsPartOne))
print("Num valid passports part Two: " + str(validPassportsPartTwo))
