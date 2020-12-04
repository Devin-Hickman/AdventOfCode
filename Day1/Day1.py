def twoSum(input,target):
    mySet = set()
    for val in input:
        x = int(val)
        complement = target - x
        if complement in mySet:
            return x, complement
        else:
            mySet.add(x)
    return 0,0

def threeSum(input, target):
   i = 1
   for val in input:
        first, second = twoSum(input[i:], target - val)
        if(first != 0 and second != 0):
            return first, second, val
        elif (first ==0 and second ==0 and val == target):
            return 0
        i += 1

filename = "input.txt"
f = open(filename, "r")
input = []
target = 2020
for val in f:
    input.append(int(val))
first, second = twoSum(input, target)
print("2Sum:" + str(first * second))
first, second, third = threeSum(input, target)
print("3Sum: " + str(first * second * third))




