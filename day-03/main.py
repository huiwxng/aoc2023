import re

with open("input.txt", "r") as f:
    content = f.readlines()

def p1():
    sum = 0
    re_sym = r"[^\d\.\n]"
    re_num = r"\d+"
    sym_neighbors = set()

    for row, line in enumerate(content):
        for sym in re.finditer(re_sym, line):
            col = sym.start()
            for r in range(-1, 2):
                for c in range(-1, 2):
                    sym_neighbors.add((row + r, col + c))

    for row, line in enumerate(content):
        for n in re.finditer(re_num, line):
            num_start = n.start()
            num_end = n.end()
            num = int(line[num_start:num_end])
            for i in range(num_start, num_end):
                if (row, i) in sym_neighbors:
                    sum += num
                    break

    return sum

def p2():
    sum = 0
    re_sym = r"\*"
    re_num = r"\d+"
    gears = {}

    for row, line in enumerate(content):
        for sym in re.finditer(re_sym, line):
            col = sym.start()
            gears[(row, col)] = []

    for row, line in enumerate(content):
        for n in re.finditer(re_num, line):
            num = int(line[n.start():n.end()])
            for r in range(row - 1, row + 2):
                for c in range(n.start() - 1, n.end() + 1):
                    if (r, c) in gears:
                        gears[(r, c)].append(num)

    for i in gears.values():
        if len(i) == 2:
            sum += i[0] * i[1]

    return sum

def main():
    print(p1())
    print(p2())

main()