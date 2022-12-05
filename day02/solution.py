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
    "A X": "A Z",  
    "A Y": "A X",  
    "A Z": "A Y",  
    "B X": "B X",  
    "B Y": "B Y",  
    "B Z": "B Z",  
    "C X": "C Y",  
    "C Y": "C Z",  
    "C Z": "C X",  
    "": ""
}


def part_one():
    with open("/Users/gjorgjidimeski/Projects/aoc/day02/input.txt", "r") as f:
        return sum(map(lambda c: combinations[c], re.split("\n", f.read())))


def part_two():
    with open("/Users/gjorgjidimeski/Projects/aoc/day02/input.txt", "r") as f:
        return sum(map(lambda c: combinations[c], map(lambda c: alt_combinations[c], re.split("\n", f.read()))))


if __name__ == "__main__":
    print(part_two())
