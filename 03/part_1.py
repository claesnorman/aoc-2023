from typing import List


def is_symbol_close_to(sym_map: List[str], num_x: int, num_y: int, num: str):
    x_min = num_x - 1
    if x_min == -1:
        x_min = 0

    y_min = num_y - 1
    if y_min == -1:
        y_min = 0

    x_max = num_x + len(num)
    if x_max >= len(sym_map[num_y]):
        x_max = len(sym_map[num_y]) - 1

    y_max = num_y + 1
    if y_max >= len(sym_map):
        y_max = len(sym_map) - 1

    for y_search in range(y_min, y_max+1):
        row_search = sym_map[y_search]
        for x_search in range(x_min, x_max+1):
            if row_search[x_search] != ".":
                return True
    return False


print("Start of script")
puzzle_input_filename = "./puzzle_input.txt"
with open(puzzle_input_filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

# Create a "map" with the digits only from the input file
digit_map = []
for row in content:
    new_row = ""
    for char in row:
        try:
            i = int(char)
            new_row += char
        except ValueError:
            new_row += "."
    # print(f"{new_row}")
    digit_map.append(new_row)
# print("")

# Create a "map" with the symbols only from the input file
symbol_map = []
for row in content:
    new_row = ""
    for char in row:
        if char == ".":
            new_row += "."
            continue
        try:
            i = int(char)
            new_row += "."
        except ValueError:
            new_row += char
    # print(f"{new_row}")
    symbol_map.append(new_row)

part_numbers = []
# Find numbers and coordinates
for y, row in enumerate(digit_map):
    numbers = row.split(".")
    x = 0
    for number in numbers:
        if not number:
            x += 1
            continue
        is_adjacent = is_symbol_close_to(symbol_map, x, y, number)
        print(f"{x=},{y=},{number=}, {is_adjacent}")
        if is_adjacent:
            part_numbers.append(int(number))
        x += 1
        x += len(number)

print(f"{part_numbers=}")
sum_of_part_numbers = sum(part_numbers)
print(f"Sum: {sum_of_part_numbers}")
