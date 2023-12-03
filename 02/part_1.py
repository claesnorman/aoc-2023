print("Start of script")
puzzle_input_filename = "./puzzle_input.txt"
with open(puzzle_input_filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]
# print(f"{content}")

total_cubes = {"red": 12, "green": 13, "blue": 14}

number_of_possible_games = 0
id_list = []

for row in content:
    found_cubes = {"red": 0, "green": 0, "blue": 0}

    # Split by : to get ID and all sets
    row_splitted = row.split(":")
    id_text = row_splitted[0]
    all_sets_string = row_splitted[1].strip()
    # print(f"{row_splitted[0]}: {all_sets_string}")
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
            too_many_cubes_in_set = True

            # Extract cube quantity and colour
            number_of_cubes = int(cube.split(" ")[0])
            colour_of_cubes = cube.split(" ")[1]
            # print(f"{number_of_cubes=}, {colour_of_cubes=}")

            if number_of_cubes > total_cubes[colour_of_cubes]:
                # Not possible
                print(f"NOT possible: {colour_of_cubes}={number_of_cubes}, max={total_cubes[colour_of_cubes]}")
                break
        else:  # No break
            too_many_cubes_in_set = False
            print(f"Possible: {sett}")
        if too_many_cubes_in_set:
            break
    else:  # No break, all sets ok
        print(f"ALL SETS POSSIBLE")
        game_id = int(id_text.split(" ")[1])
        print(f"{game_id=}")
        id_list.append(game_id)

print(f"{id_list=}")
print(f"Sum of game IDs: {sum(id_list)}")
