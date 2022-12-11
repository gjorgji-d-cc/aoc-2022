from io import TextIOWrapper
from math import floor
import functools


class Monkey:
    def __init__(self, input: str):
        bps = [s.strip() for s in input.split("\n")[1:]]
        self.items = [int(i) for i in bps[0].removeprefix(
            "Starting items: ").split(", ")]
        self.operation = bps[1].removeprefix("Operation: new = ")
        self.divisible_by = int(bps[2].removeprefix("Test: divisible by "))
        self.cases = {True: int(bps[3].removeprefix("If true: throw to monkey ")), False: int(
            bps[4].removeprefix("If false: throw to monkey "))}
        self.throws = 0

    def throw_next(self, reduce_worry):
        self.items[0] = eval(self.operation.replace(
            "old", str(self.items[0])))
        if reduce_worry:
            self.items[0] = floor(self.items[0] / 3)
        else:
            self.items[0] = self.items[0]
        self.throws += 1
        return (self.cases[self.items[0] % self.divisible_by == 0], self.items.pop(0))


# 10605
def part_one(file: TextIOWrapper):
    monkey_bp = file.read().split("\n\n")
    monkeys = [Monkey(bp) for bp in monkey_bp]

    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                throw = monkey.throw_next(True)
                monkeys[throw[0]].items.append(throw[1])

    srtd = sorted([m.throws for m in monkeys])
    return srtd[-1] * srtd[-2]


# 2713310158
def part_two(file: TextIOWrapper):
    monkey_bp = file.read().split("\n\n")
    monkeys = [Monkey(bp) for bp in monkey_bp]

    mod = eval("*".join([str(m.divisible_by) for m in monkeys]))

    for _ in range(10_000):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                throw = monkey.throw_next(False)
                monkeys[throw[0]].items.append(throw[1] % mod)

    srtd = sorted([m.throws for m in monkeys])
    print(srtd)
    return srtd[-1] * srtd[-2]


if __name__ == "__main__":
    with open("day11/input.txt", "r") as f:
        print(part_two(f))
