from io import TextIOWrapper


def part_one(file: TextIOWrapper):
    operations = file.read().split("\n")
    cycles = []
    x_history = []
    x_value = 1
    [cycles.extend((0,) if op == "noop" else (0, int(op.split(" ")[1])))
     for op in operations]
    for i in range(len(cycles)):
        x_value += cycles[i]
        x_history.append((x_value - cycles[i], x_value))
    return sum([i * x_history[i - 1][0] for i in (20, 60, 100, 140, 180, 220)])


def part_two(file: TextIOWrapper):
    operations = file.read().split("\n")
    cycles = []
    x_history = []
    x_value = 1
    [cycles.extend((0,) if op == "noop" else (0, int(op.split(" ")[1])))
     for op in operations]

    for i in range(len(cycles)):
        x_value += cycles[i]
        x_history.append((x_value - cycles[i], x_value))

    for row in (x_history[:40], x_history[40:80], x_history[80:120], x_history[120:160], x_history[160:200], x_history[200:240]):
        displayed_row = []
        for i in range(len(row)):
            displayed_row.append("#" if i in (row[i][0], row[i][0] - 1, row[i][0] + 1) else "-")
        print("".join(displayed_row))


if __name__ == "__main__":
    with open("day10/input.txt", "r") as f:
        print(part_two(f))
