import re

def canHoldGoldBag(bag, values):
    if bag in checkedBags:
        return checkedBags[bag]

    if "no other bag" in values:
        checkedBags[bag] = False
        return False
    elif "shiny gold bag" in values:
        checkedBags[bag] = True
        return True

    for inner in bagToHeld[bag]:
        if canHoldGoldBag(inner, bagToHeld[inner]):
            checkedBags[bag] = True
            return True

    return False

filename = "input.txt"
f = open(filename, "r")

bagCount = 0
bagToHeld = {}
checkedBags = {}
lineCount = 0

for line in f:
    lineCount += 1
    line = line.strip("\n")
    split = line.split("contain")
    key = re.sub(r'\d', '', split[0]).replace("bags", "bag").strip()
    value = re.sub(r'\d', '', split[1]).strip('.').replace(',', '').replace("bags", "bag").strip().split()
    bagToHeld[key] = []
    held = ""
    for s in value:
        held += s + " "
        if (s == "bag"):
            bagToHeld[key].append(held.rstrip())
            held = ""

count = 0
for key, value in bagToHeld.items():
    if canHoldGoldBag(key, value):
        count += 1

print(count)

