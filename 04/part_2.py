import math
from typing import List, Any


def get_numbers_from_text(s: str) -> List[int]:
    s_numbers = s.strip().split()
    i_numbers = []
    for s_number in s_numbers:
        i_numbers.append(int(s_number))
    # print(f"{i_numbers=}")
    return i_numbers


def join_lists(list_a, list_b) -> List[Any]:
    joined_list = list(set(list_a) & set(list_b))
    return joined_list


print("Start of script")
puzzle_input_filename = "./puzzle_input.txt"
with open(puzzle_input_filename) as f:
    file_content = f.readlines()
file_content = [x.strip() for x in file_content]

# for row in file_content:
#     print(f"{row}")

cards = []
for row in file_content:
    card_split = row.split(":")
    card_split = [x.strip() for x in card_split]
    card_title = card_split[0]
    card_no = int(card_title.split()[-1])
    card_data = card_split[1]
    # print(f"{card_no=}, {card_data=}")

    winning_numbers = get_numbers_from_text(card_data.split("|")[0])
    my_numbers = get_numbers_from_text(card_data.split("|")[1])

    cards.append({"winning_numbers": winning_numbers, "my_numbers": my_numbers})

    # my_winning_numbers = join_lists(winning_numbers, my_numbers)
    # number_of_wins = len(my_winning_numbers)
    # print(f"{number_of_wins=}, {my_winning_numbers=}")

# for idx, card in enumerate(cards):
#     my_winning_numbers = join_lists(card["winning_numbers"], card["my_numbers"])
#     print(f"{idx:3}: {card}, {my_winning_numbers}")

# A list to keep track of the number of different cards. We pre-fill it with 1, which is the original card
card_quantities = [1 for i in range(len(cards))]
for idx, card in enumerate(cards):
    number_of_winning_numbers = len(join_lists(card["winning_numbers"], card["my_numbers"]))
    print(f"Card {idx} has {number_of_winning_numbers} number of winning numbers.")
    if number_of_winning_numbers == 0:
        # No winning numbers on this card, let's continue to the next card
        continue

    number_of_this_card = card_quantities[idx]
    # print(f"{number_of_this_card=}")
    for j in range(idx+1, idx+1+number_of_winning_numbers):
        if j > len(card_quantities):
            print(f"Index out of bounds, {j=}")
            continue
        card_quantities[j] += number_of_this_card
    print(f"{card_quantities=}")

print(f"{sum(card_quantities)=}")
