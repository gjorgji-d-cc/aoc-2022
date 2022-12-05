from io import TextIOWrapper
import re

stacks = [
    ["P", "F", "M", "Q", "W", "G", "R", "T"],
    ["H", "F", "R"],
    ["P", "Z", "R", "V", "G", "H", "S", "D"],
    ["Q", "H", "P", "B", "F", "W", "G"],
    ["P", "S", "M", "J", "H"],
    ["M", "Z", "T", "H", "S", "R", "P", "L"],
    ["P", "T", "H", "N", "M", "L"],
    ["F", "D", "Q", "R"],
    ["D", "S", "C", "N", "L", "P", "H"],
]


def crate_mover_9000(amount: int, from_stack: int, to_stack: int):
    [stacks[to_stack - 1].append(stacks[from_stack - 1].pop())
        for _ in range(amount)]


def crate_mover_9001(amount: int, from_stack: int, to_stack: int):
    [stacks[to_stack - 1].append(element)
        for element in [stacks[from_stack - 1].pop()
                        for _ in range(amount)][::-1]]


def part_one(file: TextIOWrapper):
    [crate_mover_9000(int(split[1]), int(split[3]), int(split[5]))
        for split in [re.split("\s", action)
                      for action in [line.removesuffix("\n")
                                     for line in file.readlines()]]]
    return "".join([s.pop() for s in stacks])


def part_two(file: TextIOWrapper):
    [crate_mover_9001(int(split[1]), int(split[3]), int(split[5]))
        for split in [re.split("\s", action)
                      for action in [line.removesuffix("\n")
                                     for line in file.readlines()]]]
    return "".join([s.pop() for s in stacks])


if __name__ == "__main__":
    with open("/Users/gjorgjidimeski/Projects/aoc/day05/input.txt", "r") as f:
        print(part_two(f))
