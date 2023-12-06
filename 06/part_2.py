def main():
    print("Start of script")
    # puzzle_input_filename = "./example_input.txt"
    puzzle_input_filename = "./puzzle_input.txt"
    with open(puzzle_input_filename) as f:
        file_content = f.readlines()
    file_content = [x.strip() for x in file_content]

    for row in file_content:
        print(f"{row}")

    # Parse input file
    time_text = file_content[0].split(":")[1].strip().replace(" ", "")
    race_time = int(time_text)
    print(f"{race_time=}")

    distance_text = file_content[1].split(":")[1].strip().replace(" ", "")
    race_record_distance = int(distance_text)
    print(f"{race_record_distance=}")

    # The increase in velocity (mm/s) per ms of charging
    charge_factor = 1

    num_of_possible_record = 0
    for charge_time in range(race_time):
        velocity = charge_time * charge_factor
        travel_time = race_time - charge_time
        distance = travel_time * velocity
        # print(f"{race_time=}, {charge_time=}, {velocity=}, {distance=}")
        if distance > race_record_distance:
            # print("RECORD")
            num_of_possible_record += 1

    print(f"{num_of_possible_record=}")


if __name__ == "__main__":
    main()
