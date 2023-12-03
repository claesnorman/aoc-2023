

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

# Create a list with the numbers and its coordinates
number_list = []
for y, row in enumerate(digit_map):
    numbers = row.split(".")
    x = 0
    for number in numbers:
        if not number:
            x += 1
            continue
        print(f"{x=},{y=},{number=}")
        number_list.append((x, y, number))
        x += 1
        x += len(number)

print(number_list)

# Create a "map" with the * symbol only from the input file
symbol_map = []
for row in content:
    new_row = ""
    for char in row:
        if char == "*":
            new_row += "*"
        else:
            new_row += "."
    # print(f"{new_row}")
    symbol_map.append(new_row)

gear_ratios = []
for y_star, row in enumerate(symbol_map):
    print(f"Row {y_star:3}: {row}")

    for x_star, char in enumerate(row):
        gear_numbers = []
        if char == "*":
            # We found a star, now find adjacent numbers by traversing the numbers list with coordinates
            for number in number_list:
                x_number = number[0]
                y_number = number[1]
                number_string = number[2]
                x_min = x_star - len(number_string)
                x_max = x_star + 1
                y_min = y_star - 1
                y_max = y_star + 1
                if x_min <= x_number <= x_max and y_min <= y_number <= y_max:
                    # print("MATCH!")
                    # print(f"Star - Coord: {x_star},{y_star}")
                    # print(f"Value: {number_string} - Coord: {x_number},{y_number}")
                    # print(f"Allowed range: {x_min}-{x_max},{y_min}-{y_max}")
                    gear_numbers.append(number_string)
                    if len(gear_numbers) == 2:
                        print("TWO MATCHES")
                        print(f"{gear_numbers=}")
                        gear_ratios.append(int(gear_numbers[0])*int(gear_numbers[1]))

print(f"{gear_ratios=}")
sum_gear_ratios = sum(gear_ratios)
print(f"{sum_gear_ratios=}")
