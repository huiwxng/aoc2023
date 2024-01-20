import re

with open("input.txt", "r") as f:
    content = f.readlines()

def p1():
    total = 0
    for jumbled_value in content:
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
    return total

# part 2
def p2():
    total = 0
    regex_query = "\d|one|two|three|four|five|six|seven|eight|nine"
    string_to_digit_dict = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    for jumbled_value in content:
        list = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", jumbled_value)
        num = ""
        first = list[0]
        if first.isdigit():
            num += first
        else:
            num += string_to_digit_dict[first]
        second = list[-1]
        if second.isdigit():
            num += second
        else:
            num += string_to_digit_dict[second]
        total += int(num)
    return total

def main():
    print(p1())
    print(p2())

main()