import re

words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("input/day1.txt", "r") as f:
    text = [line.strip() for line in f.readlines()]


def extract(line: str):
    return "".join(c for c in line.strip() if c.isdecimal())


def extract_advanced(line: str):
    found = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", line)
    line_digits = []
    for token in found:
        line_digits.append(words.get(token, token))
    return "".join(line_digits)


def transform(number_str: str):
    if len(number_str) == 1:
        return number_str * 2
    elif len(number_str) > 2:
        return "".join([number_str[i] for i in (0, -1)])
    else:
        return number_str


result = sum(list(map(int, map(transform, (map(extract_advanced, text))))))
print(result)
