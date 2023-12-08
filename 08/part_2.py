import copy
import math
from datetime import datetime


class Node:
    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return f"name:{self.name}, left:{self.left}, right:{self.right}"


def get_nodes_ending_with(node_map: dict, ends_with: str) -> list:
    node_map_to_search_in = copy.deepcopy(node_map)
    result = []
    for key, val in node_map_to_search_in.items():
        if key[-1] == ends_with:
            result.append(key)
    return result


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
    start_nodes_end_with = "A"
    end_nodes_end_with = "Z"
    start_nodes = get_nodes_ending_with(node_map, start_nodes_end_with)
    print(f"Start nodes: {start_nodes}")
    print(f"Number of start nodes: {len(start_nodes)}")

    steps = []
    for node_text in start_nodes:
        start_node = node_text
        print(f"Node to test: {start_node}")
        num_steps = 0
        for navigation in navigation_instructions(navigation_instructions_text):
            node = node_map[start_node]
            next_node = None
            if navigation == "L":
                next_node = node.left
            if navigation == "R":
                next_node = node.right
            num_steps += 1
            if next_node[-1] == end_nodes_end_with:
                print(f"We reached the goal in {num_steps} steps!")
                steps.append(num_steps)
                break
            start_node = next_node

    print("We´re done, find the lowest common denominator")

    # The least amount of steps is the least common denominator between all steps
    lcm = math.lcm(*steps)

    end = datetime.now()
    print(f"Process time: {end-start}")
    print(f"Steps for the different paths: {steps}")
    print(f"Least amount of steps: {lcm=}")


if __name__ == "__main__":
    main()
