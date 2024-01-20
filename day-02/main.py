import re

with open("input.txt", "r") as f:
    content = f.readlines()

# part 1
def p1():
    total = 0
    possible = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for id, game in enumerate(content, start=1):
        for num, color in re.findall(r"(\d+) (red|green|blue)", game):
            if possible[color] < int(num):
                break
        else:
            total += id

    return total

def p2():
    sum = 0
    for id, game in enumerate(content, start=1):
        max = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        power = 1
        for num, color in re.findall(r"(\d+) (red|green|blue)", game):
            if max[color] < int(num):
                max[color] = int(num)
        power *= max["red"] * max["green"] * max["blue"]
        sum += power
    return sum

def main():
    print(p1())
    print(p2())

main()
