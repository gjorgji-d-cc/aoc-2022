from sys import stdin


def get_priority(char: str):
    return ord(char) - ord("A" if char.isupper() else "a") + (1 if char.islower() else + 27)


def part_one():
    sum = 0
    for line in stdin:
        first_set = set(line[:int(len(line) / 2)])
        secnd_set = set(line[int(len(line) / 2):])
        sum += get_priority(first_set.intersection(secnd_set).pop())
        print(sum)


def part_two():
    sum = 0
    with open("/Users/gjorgjidimeski/Projects/lisp/day02/input.txt", "r") as f:
        lines = f.readlines()
        groups = [[lines[i], lines[i + 1], lines[i + 2]]
                  for i in range(0, len(lines))[::3]]
    for group in groups:
        sets = [set(group.pop()), set(group.pop()), set(group.pop())]
        [set.remove("\n") if "\n" in set else None for set in sets]
        intersection = sets[0].intersection(sets[1]).intersection(sets[2]).pop()
        sum += get_priority(intersection)
    return sum


if __name__ == "__main__":
    print(part_two())
