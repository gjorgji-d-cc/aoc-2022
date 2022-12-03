import re


def part_one():
    with open("/Users/gjorgjidimeski/Projects/aoc/day01/input.txt", "r") as f:
        elve_calories = re.split("\n\n", f.read())
    return max([sum(calories) for calories in [[int(n) for n in re.split("\n", c) if n != ""] for c in elve_calories]])

        

def part_two():
    with open("/Users/gjorgjidimeski/Projects/aoc/day01/input.txt", "r") as f:
        elve_calories = re.split("\n\n", f.read())
    return sum(sorted([sum(calories) for calories in [[int(n) for n in re.split("\n", c) if n != ""] for c in elve_calories]])[-3:])


if __name__ == "__main__":
    print(part_two())
