from io import TextIOWrapper
import math


def part_one(file: TextIOWrapper):
    chars = list(file.read())
    return min([i if len(set(chars[i: i + 4])) == 4 else math.inf for i in range(len(chars) - 3)]) + 4


def part_two(file: TextIOWrapper):
    chars = list(file.read())
    return min([i if len(set(chars[i: i + 14])) == 14 else math.inf for i in range(len(chars) - 13)]) + 14


if __name__ == "__main__":
    with open("/Users/gjorgjidimeski/Projects/aoc/day06/input.txt", "r") as f:
        print(part_two(f))

