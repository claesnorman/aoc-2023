from datetime import datetime


class Node:
    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return f"name:{self.name}, left:{self.left}, right:{self.right}"


def navigation_instructions(navigation_text: str, max_iterations: int = 0):
    idx = 0
    iteration = 0
    stop_iterating = False
    while not stop_iterating:
        yield navigation_text[idx]
        idx += 1
        iteration += 1
        if idx == len(navigation_text):
            idx = 0
        if max_iterations and iteration == max_iterations:
            stop_iterating = True


def main():
    print("Start of script")
    # puzzle_input_filename = "./example_input.txt"
    puzzle_input_filename = "./puzzle_input.txt"
    with open(puzzle_input_filename) as f:
        file_content = f.readlines()
    file_content = [x.strip() for x in file_content]

    # for row in file_content:
    #     print(f"{row}")

    navigation_instructions_text = ""
    node_map = {}
    for idx, row in enumerate(file_content):
        if idx == 0:
            navigation_instructions_text = row
            continue
        if not row:
            continue

        name_directions = row.split("=")
        name = name_directions[0].strip()
        directions = name_directions[1].strip().replace("(", "").replace(")", "")
        directions_split = directions.split(",")
        left = directions_split[0].strip()
        right = directions_split[1].strip()
        node_map[name] = Node(name, left, right)

    # for key, val in node_map.items():
    #     print(f"{key=}, node=({val})")

    start = datetime.now()
    start_node = "AAA"
    end_node = "ZZZ"
    num_steps = 0

    for navigation in navigation_instructions(navigation_instructions_text):
        print(f"This node: {start_node}")
        node = node_map[start_node]
        next_node = None
        if navigation == "L":
            next_node = node.left
        if navigation == "R":
            next_node = node.right
        print(f"Next node: {next_node}")
        num_steps += 1
        if next_node == end_node:
            print("We reached the goal!")
            break
        start_node = next_node

    end = datetime.now()
    print(f"Process time: {end-start}")
    print(f"Number of steps: {num_steps}")


if __name__ == "__main__":
    main()
