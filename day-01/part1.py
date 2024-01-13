import re

# part one

f = open("input.txt", "r")
total = 0
for jumbled_value in f:
    # first = ""
    # second = ""
    num = ""
    for char in jumbled_value:
        if char.isdigit():
            # first = char
            num += char
            break
    for char in reversed(jumbled_value):
        if char.isdigit():
            # second = char
            num += char
            break
    # print(first + second)
    # print(result)
    total += int(num)
print(total)
f.close()
