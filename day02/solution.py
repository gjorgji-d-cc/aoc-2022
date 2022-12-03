import re

combinations = {
    "A X": 4,  # rock rock
    "A Y": 8,  # rock paper
    "A Z": 3,  # rock scissors
    "B X": 1,  # paper rock
    "B Y": 5,  # paper paper
    "B Z": 9,  # paper scissors
    "C X": 7,  # scissors rock
    "C Y": 2,  # scissors paper
    "C Z": 6,  # scissors scissors
    "": 0
}

alt_combinations = {
    "A X": "A Z",  # rock rock
    "A Y": "A X",  # rock paper
    "A Z": "A Y",  # rock scissors
    "B X": "B X",  # paper rock
    "B Y": "B Y",  # paper paper
    "B Z": "B Z",  # paper scissors
    "C X": "C Y",  # scissors rock
    "C Y": "C Z",  # scissors paper
    "C Z": "C X",  # scissors scissors
    "": ""
}


def compute_round(opponent: str, outcome: str):
    pass


def part_one():
    with open("/Users/gjorgjidimeski/Projects/aoc/day02/input.txt", "r") as f:
        return sum(map(lambda c: combinations[c], re.split("\n", f.read())))


def part_two():
    with open("/Users/gjorgjidimeski/Projects/aoc/day02/input.txt", "r") as f:
        return sum(map(lambda c: combinations[c], map(lambda c: alt_combinations[c], re.split("\n", f.read()))))


if __name__ == "__main__":
    print(part_two())
