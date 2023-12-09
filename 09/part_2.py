import copy
from datetime import datetime
from typing import List


def get_derivative_from_sequencet(sequence: List[int]) -> List[int]:
    derivative_sequence = []
    for idx in range(len(sequence)):
        if idx == len(sequence)-1:
            break
        derivative = sequence[idx+1] - sequence[idx]
        derivative_sequence.append(derivative)
    return derivative_sequence


def sequence_is_all_zero(sequence: List[int]) -> bool:
    for value in sequence:
        if value != 0:
            return False
    return True


def main():
    print("Start of script")
    # puzzle_input_filename = "./example_input.txt"
    puzzle_input_filename = "./puzzle_input.txt"
    with open(puzzle_input_filename) as f:
        file_content = f.readlines()
    file_content = [x.strip() for x in file_content]

    # for row in file_content:
    #     print(f"{row}")

    start = datetime.now()

    # Parse all history data
    history = []
    for row in file_content:
        sequence = list(map(int, row.split()))
        history.append(sequence)

    sum_all_values = 0

    # Find derivative
    for sequence in history:
        sequence_levels = [copy.deepcopy(sequence)]
        last_level_all_zeros = False
        while not last_level_all_zeros:
            derivative = get_derivative_from_sequencet(sequence_levels[-1])
            sequence_levels.append(derivative)
            if sequence_is_all_zero(derivative):
                last_level_all_zeros = True
        # print(f"{sequence_levels=}")

        # Predict next value
        sequence_levels_depth = len(sequence_levels)
        # print(f"{sequence_levels_depth=}")
        last_level = copy.deepcopy(sequence_levels[-1])
        # print(f"{last_level=}")
        previous_value = 0
        last_level_derivative = 0
        for level in range(sequence_levels_depth-1, -1, -1):
            # print(f"{level=}")
            # print(f"{last_level_derivative=}")
            previous_value = sequence_levels[level][0] - last_level_derivative
            last_level_derivative = previous_value
        sum_all_values += previous_value
        print(f"Previous predicted value: {previous_value}")

    end = datetime.now()
    print(f"Process time: {end-start}")
    print(f"Sum of all predicted values: {sum_all_values}")


if __name__ == "__main__":
    main()
