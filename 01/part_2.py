import copy
from typing import List


def find_first_digit(s: str) -> int:
    if not s:
        raise ValueError(f"s is empty")
    for c in s:
        try:
            i = int(c)
        except ValueError as e:
            # Not a digit, continue
            continue
        # print(f"{i}")
        return i
    raise ValueError(f"s did not contain a digit, s={s}")


def replace_first_occurrence(s: str, old_list: List[str], new_list: List[str]) -> str:
    # print(f"{s=}")
    lowest_idx = -1
    lowest_old = "N/A"
    lowest_new = "N/A"
    for old, new in zip(old_list, new_list):
        try:
            idx = s.index(old)
            # print(f"{old=}, {idx=}")
            if lowest_idx == -1 or idx < lowest_idx:
                lowest_idx = idx
                lowest_old = old
                lowest_new = new
            # print(f"{lowest_old=}, {lowest_idx=}, {lowest_new=}")
        except ValueError:
            continue
    # print(f"{lowest_old=}, {lowest_idx=}, {lowest_new=}")
    return_this = s if lowest_idx == -1 else s.replace(lowest_old, lowest_new, 1)
    # print(f"{return_this=}")
    return return_this


print("Start of script")
puzzle_input_filename = "./puzzle_input.txt"
with open(puzzle_input_filename) as f:
    content = f.readlines()

# print(f"{content}")
content = [x.strip() for x in content]
# print(f"{content}")

total_sum = 0

look_for_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
look_for_backward_list = [x[::-1] for x in look_for_list]
replace_with_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for original_row in content:
    # replace "letter digits" with "real digits"
    original_row_forward = copy.deepcopy(original_row)

    # print(f"{original_row=}")
    row_forward = replace_first_occurrence(s=original_row_forward, old_list=look_for_list, new_list=replace_with_list)
    first_digit = find_first_digit(row_forward)
    print(f"{first_digit=}")

    # Reverse
    original_row_backward = copy.deepcopy(original_row[::-1])
    row_backward = replace_first_occurrence(s=original_row_backward, old_list=look_for_backward_list, new_list=replace_with_list)
    last_digit = find_first_digit(row_backward)
    print(f"{last_digit=}")

    this_rows_value = (10 * first_digit) + last_digit
    total_sum += this_rows_value

print(f"Total sum: {total_sum}")
