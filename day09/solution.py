from io import TextIOWrapper


def next_tail_location(head, tail):
    head_proximity = (head,
                      (head[0], head[1] + 1),
                      (head[0], head[1] - 1),
                      (head[0] + 1, head[1]),
                      (head[0] - 1, head[1]),
                      (head[0] + 1, head[1] + 1),
                      (head[0] - 1, head[1] - 1),
                      (head[0] + 1, head[1] - 1),
                      (head[0] - 1, head[1] + 1))
    valid_moves_tail = (tail,
                        (tail[0], tail[1] + 1),
                        (tail[0], tail[1] - 1),
                        (tail[0] + 1, tail[1]),
                        (tail[0] - 1, tail[1]),
                        (tail[0] + 1, tail[1] + 1),
                        (tail[0] - 1, tail[1] - 1),
                        (tail[0] + 1, tail[1] - 1),
                        (tail[0] - 1, tail[1] + 1))
    if tail in head_proximity:
        return tail
    possible_moves = (set(head_proximity)
                      .intersection(set(valid_moves_tail)))
    min_score = min([calculate_position_score(m, head)
                    for m in possible_moves])
    return [m for m in possible_moves if calculate_position_score(m, head) == min_score][0]


def calculate_position_score(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def part_one(file: TextIOWrapper):
    moves = [[line.split(" ")[0], int(line.split(" ")[1])]
             for line in file.read().split("\n")]
    head, tail = (0, 0), (0, 0)
    positions = set()
    positions.add(tail)

    while len(moves) > 0:
        if moves[0][0] == "R":
            head = (head[0] + 1, head[1])
        if moves[0][0] == "L":
            head = (head[0] - 1, head[1])
        if moves[0][0] == "U":
            head = (head[0], head[1] + 1)
        if moves[0][0] == "D":
            head = (head[0], head[1] - 1)
        tail = next_tail_location(head, tail)
        positions.add(tail)
        moves[0][1] -= 1
        if moves[0][1] <= 0:
            moves.pop(0)

    return len(positions)


def part_two(file: TextIOWrapper):
    moves = [[line.split(" ")[0], int(line.split(" ")[1])]
             for line in file.read().split("\n")]
    head, tails = (0, 0), [(0, 0) for _ in range(9)]
    positions = set()
    positions.add(tails[8])

    while len(moves) > 0:
        if moves[0][0] == "R":
            head = (head[0] + 1, head[1])
        if moves[0][0] == "L":
            head = (head[0] - 1, head[1])
        if moves[0][0] == "U":
            head = (head[0], head[1] + 1)
        if moves[0][0] == "D":
            head = (head[0], head[1] - 1)
        tails[0] = next_tail_location(head, tails[0])
        for i in range(1, len(tails)): 
            tails[i] = next_tail_location(tails[i - 1], tails[i])

        positions.add(tails[8])
        moves[0][1] -= 1
        if moves[0][1] <= 0:
            moves.pop(0)

    return len(positions)


if __name__ == "__main__":
    with open("day09/input.txt", "r") as f:
        print(part_two(f))
