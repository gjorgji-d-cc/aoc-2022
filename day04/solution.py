import re


def is_overlapped(elf1: list, elf2: list):
    return (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1])


def is_partly_overlapped(elf1: list, elf2: list):
    return (elf1[0] >= elf2[0] and elf1[0] <= elf2[1]) or (elf1[1] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[0] <= elf1[1]) or (elf2[1] >= elf1[0] and elf2[1] <= elf1[1]) 


def part_one():
    with open("/Users/gjorgjidimeski/Projects/aoc/day04/input.txt", "r") as f:
        return sum([1 if is_overlapped(input[0], input[1]) else 0 for input in [([int(e) for e in single[0].split("-")], [int(e) for e in single[1].split("-")]) for single in [pair.split(",") for pair in re.split("\n", f.read()) if pair != ""]]])


def part_two():
    with open("/Users/gjorgjidimeski/Projects/aoc/day04/input.txt", "r") as f:
        return sum([1 if is_partly_overlapped(input[0], input[1]) else 0 for input in [([int(e) for e in single[0].split("-")], [int(e) for e in single[1].split("-")]) for single in [pair.split(",") for pair in re.split("\n", f.read()) if pair != ""]]])


if __name__ == "__main__":
    print(part_two())
