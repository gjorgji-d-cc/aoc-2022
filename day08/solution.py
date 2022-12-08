from io import TextIOWrapper


def part_one(file: TextIOWrapper):
    forest = [tuple([int(c) for c in s]) for s in file.read().split("\n")]
    visible_trees = set()

    for row in range(len(forest)):
        max = -1
        for col in range(len(forest[row])):
            if max < forest[row][col]:
                visible_trees.add((row, col))
                max = max if max > forest[row][col] else forest[row][col]
        max = -1
        for col in range(len(forest[row]))[::-1]:
            if max < forest[row][col]:
                visible_trees.add((row, col))
                max = max if max > forest[row][col] else forest[row][col]

    for col in range(len(forest[0])):
        max = -1
        for row in range(len(forest)):
            if max < forest[row][col]:
                visible_trees.add((row, col))
                max = max if max > forest[row][col] else forest[row][col]
        max = -1
        for row in range(len(forest))[::-1]:
            if max < forest[row][col]:
                visible_trees.add((row, col))
                max = max if max > forest[row][col] else forest[row][col]

    return len(visible_trees)


def part_two(file: TextIOWrapper):
    forest = [tuple([int(c) for c in s]) for s in file.read().split("\n")]
    rows, cols = len(forest), len(forest[0])
    maximum = 0
    for row in range(rows):
        if row == 0 or row == rows - 1:
            continue
        for col in range(cols):
            if col == 0 or col == cols - 1:
                continue
            l, t, r, b = 0, 0, 0, 0

            for test_col_top in range(col)[::-1]:
                t += 1
                if forest[row][test_col_top] >= forest[row][col]:
                    break

            for test_col_bottom in range(col, cols)[1:]:
                b += 1
                if forest[row][test_col_bottom] >= forest[row][col]:
                    break

            for test_row_left in range(row)[::-1]:
                l += 1
                if forest[test_row_left][col] >= forest[row][col]:
                    break

            for test_row_right in range(row, rows)[1:]:
                r += 1
                if forest[test_row_right][col] >= forest[row][col]:
                    break

            maximum = max(maximum, l * t * r * b)

    return maximum


if __name__ == "__main__":
    with open("day08/input.txt", "r") as f:
        print(part_two(f))
