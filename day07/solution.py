from io import TextIOWrapper


class BaseNode:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name


class File(BaseNode):
    def __init__(self, parent, name, size):
        super().__init__(parent, name)
        self.size = size

    def get_size(self):
        return self.size


class Directory(BaseNode):
    def __init__(self, parent, name):
        super().__init__(parent, name)
        self.children = []

    def get_size(self):
        return sum([child.get_size() for child in self.children]) if len(self.children) > 0 else 0

    def get_child(self, name):
        return [child for child in self.children if child.name == name][0]


def build_tree(file: TextIOWrapper):
    root = Directory(None, "/")
    current_dir = root
    directories = {root}
    commands = file.read().split("\n")

    for command in [c.split(" ") for c in commands]:
        if command[0] == "$" and command[1] == "cd":
            if command[2] == "/":  # $ cd /
                current_dir = root
            elif command[2] == "..":  # $ cd ..
                current_dir = current_dir.parent
            else:  # $ cd 'name'
                current_dir = current_dir.get_child(command[2])
        elif command[0] == "dir":  # directory in ls
            new_dir = Directory(current_dir, command[1])
            current_dir.children.append(new_dir)
            directories.add(new_dir)
        elif not command[0] == "$":  # file in ls
            current_dir.children.append(
                File(current_dir, command[1], int(command[0])))

    return (root, directories)


def part_one(file: TextIOWrapper):
    _, directories = build_tree(file)
    return sum([size for size in [dir.get_size() for dir in directories] if size <= 100000])


def part_two(file: TextIOWrapper):
    root, directories = build_tree(file)
    return min([size for size in [dir.get_size() for dir in directories] if size >= 30000000 - (70000000 - root.get_size())])


if __name__ == "__main__":
    with open("/Users/gjorgjidimeski/Projects/aoc/day07/input.txt", "r") as f:
        print(part_two(f))
