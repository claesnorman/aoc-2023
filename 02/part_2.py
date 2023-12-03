print("Start of script")
puzzle_input_filename = "./puzzle_input.txt"
with open(puzzle_input_filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]
# print(f"{content}")

powers = []
for idx, row in enumerate(content):
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    # Split by : to get ID and all sets
    row_splitted = row.split(":")
    id_text = row_splitted[0]
    all_sets_string = row_splitted[1].strip()
    # print(f"{all_sets_string}")

    # Split sets by ; to get individual sets
    all_sets_list = all_sets_string.split(";")
    all_sets_list = [x.strip() for x in all_sets_list]
    # print(f"{all_sets_list}")

    for set_string in all_sets_list:

        # Split set by , to get individual cube quantity and colour
        sett = set_string.split(",")
        sett = [x.strip() for x in sett]
        # print(f"{sett=}")

        for cube in sett:
            # Extract cube quantity and colour
            number_of_cubes = int(cube.split(" ")[0])
            colour_of_cubes = cube.split(" ")[1]
            if number_of_cubes > min_cubes[colour_of_cubes]:
                min_cubes[colour_of_cubes] = number_of_cubes
    print(f"Lowest min for row {idx:3}: {min_cubes}")
    powers.append(min_cubes["red"]*min_cubes["green"]*min_cubes["blue"])

print(f"{powers=}")
print(f"{sum(powers)=}")
