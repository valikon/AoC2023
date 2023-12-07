import re

cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("input/day2.txt", "r") as f:
    text = [line.strip().split(":") for line in f.readlines()]


def extract(line: [[str]]):
    game = extract_game(line[0])
    sets = extract_sets(line[1].strip())
    return game, sets


def extract_game(s: [str]):
    return int("".join(re.findall(r"\d+", s)))


def extract_sets(s: str):
    sets = s.split(";")
    return list(map(map_set, sets))


def map_set(s: str):
    set_result = {}
    for item in s.strip().split(", "):
        x = re.findall(r"\d+|red|green|blue", item)
        set_result[x[1]] = int(x[0])
    return set_result


structured_input = list(map(extract, text))


# Part 1
def validate_game(game):
    sets = game[1]
    valid = True
    for s in sets:
        if (s.get("blue", 0) > cubes["blue"] or
                s.get("red", 0) > cubes["red"] or
                s.get("green", 0) > cubes["green"]):
            valid = False
    return valid


valid_games = list(filter(validate_game, structured_input))

print("Part 1:", sum(list(map(lambda x: x[0], valid_games))))

print("///////////////////////////////////")


# Part 2
def minimum_cubes_power(game):
    sets = game[1]
    blue = 0
    red = 0
    green = 0
    for s in sets:
        if s.get("red", 0) > red:
            red = s.get("red")
        if s.get("green", 0) > green:
            green = s.get("green")
        if s.get("blue", 0) > blue:
            blue = s.get("blue")
    return red * green * blue


games = list(map(minimum_cubes_power, structured_input))
print("Part 2:", sum(games))
