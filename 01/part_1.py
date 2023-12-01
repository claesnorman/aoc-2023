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


print("Start of script")
puzzle_input_filename = "./puzzle_input.txt"
with open(puzzle_input_filename) as f:
    content = f.readlines()

# print(f"{content}")
content = [x.strip() for x in content]
# print(f"{content}")

total_sum = 0

for row in content:
    row_forward = row
    row_backward = row[::-1]
    # print(f"Forward: {row_forward}, Backward: {row_backward}")
    first_digit = find_first_digit(row_forward)
    last_digit = find_first_digit(row_backward)
    this_rows_value = (10 * first_digit) + last_digit
    print(f"{row=}, {first_digit=}, {last_digit=}, {this_rows_value=}")
    total_sum += this_rows_value

print(f"Total sum: {total_sum}")
