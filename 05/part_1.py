from typing import Dict


def convert_source_to_dest(source: int, conversion_map: Dict) -> int:
    # print(f"Convert src={source} in map={conversion_map['name']}")
    for conversion in conversion_map["conversions"]:
        src_min = conversion["src_range_start"]
        src_max = src_min + conversion["range_length"] - 1
        if source < src_min or source > src_max:
            # Not this conversion
            continue
        # This conversion covers the source
        src_delta = source - src_min
        dst = conversion["dst_range_start"] + src_delta
        # print(f"Conversion found, {dst=}")
        return dst
    else:  # No conversion found, then destination = source
        # print(f"No conversion found, return {source=}")
        return source


def main():
    print("Start of script")
    puzzle_input_filename = "./example_input.txt"
    # puzzle_input_filename = "./puzzle_input.txt"
    with open(puzzle_input_filename) as f:
        file_content = f.readlines()
    file_content = [x.strip() for x in file_content]

    # for row in file_content:
    #     print(f"{row}")

    # Get all seeds as a list of int
    seeds_text = file_content[0].split(":")[1].strip().split()
    seeds = [int(x) for x in seeds_text]
    # print(f"{seeds=}")
    print(f"Number of seeds: {len(seeds)}")

    # Find all mappings
    source_to_dest_maps = []
    source_to_dest_map = {}
    for row in file_content:
        if "seeds:" in row:
            continue
        row = row.strip()
        if not row:
            continue
        # print(f"{row}")
        if ":" in row:  # Start of new map
            # Save old map if any, and clean 'work in progress' map
            if source_to_dest_map:
                print(f"{source_to_dest_map}")
                source_to_dest_maps.append(source_to_dest_map)
            source_to_dest_map = {"name": row.rstrip(":").split()[0], "conversions": []}
            continue
        numbers = row.split()
        conversion = {"dst_range_start": int(numbers[0]),
                      "src_range_start": int(numbers[1]),
                      "range_length": int(numbers[2])}
        source_to_dest_map["conversions"].append(conversion)

    # Reach end of file, add the last map to maps
    print(f"{source_to_dest_map}")
    source_to_dest_maps.append(source_to_dest_map)

    # Since we´re interested in the lowest location only (which is the last conversion), then we only need to keep the lowest conversion)
    last_source_to_dest_map = source_to_dest_maps[-1]
    # print(f"Let's manipulate the last conversion map with name: {last_source_to_dest_map['name']}")
    sorted_conversions = sorted(last_source_to_dest_map["conversions"], key=lambda x: x["dst_range_start"])
    new_last_map = {"name": last_source_to_dest_map["name"], "conversions": [sorted_conversions[0]]}
    source_to_dest_maps.pop()
    source_to_dest_maps.append(new_last_map)

    # Print the source-to-dest maps
    for source_to_dest_map in source_to_dest_maps:
        print(f"{source_to_dest_map=}")

    lowest_location = -1
    for seed in seeds:
        src = seed
        # print(f"Starting with {seed=}")
        for conversion_map in source_to_dest_maps:
            dst = convert_source_to_dest(source=src, conversion_map=conversion_map)
            # print(f"Source: {src}, Destination: {dst}")
            if conversion_map["name"] == "humidity-to-location":
                # We reached the end of the chain
                if lowest_location == -1 or dst < lowest_location:
                    # print("Found new lowest location")
                    lowest_location = dst
                break
            src = dst
    print(f"{lowest_location=}")


if __name__ == "__main__":
    main()
