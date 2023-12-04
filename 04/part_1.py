import math
from typing import List


def get_numbers_from_text(s: str) -> List[int]:
    s_numbers = s.strip().split()
    i_numbers = []
    for s_number in s_numbers:
        i_numbers.append(int(s_number))
    # print(f"{i_numbers=}")
    return i_numbers


print("Start of script")
puzzle_input_filename = "./puzzle_input.txt"
with open(puzzle_input_filename) as f:
    file_content = f.readlines()
file_content = [x.strip() for x in file_content]

# for row in file_content:
#     print(f"{row}")

points = []
for row in file_content:
    card_split = row.split(":")
    card_split = [x.strip() for x in card_split]
    card_title = card_split[0]
    card_data = card_split[1]
    # print(f"{card_title=}, {card_data=}")

    winning_numbers = get_numbers_from_text(card_data.split("|")[0])
    my_numbers = get_numbers_from_text(card_data.split("|")[1])
    my_winning_numbers = list(set(winning_numbers) & set(my_numbers))
    print(f"{my_winning_numbers=}")
    if len(my_winning_numbers):
        points.append(int(math.pow(2, len(my_winning_numbers)-1)))
    else:
        points.append(0)
print(f"{points=}")
print(f"{sum(points)=}")
