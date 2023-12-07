import copy
import functools
from datetime import datetime


@functools.total_ordering
class Hand:
    def __init__(self, hand: str):
        self.hand = hand
        self.all_cards = "AKQT98765432J"
        self.joker = "J"
        self.joker_positions = []
        for idx, c in enumerate(hand):
            if c == self.joker:
                self.joker_positions.append(idx)

    def __str__(self):
        hand_without_jokers = copy.deepcopy(self)
        hand_without_jokers.put_back_the_jokers()
        return f"cards: {self.hand}, strength: {self.get_strength_of_hand()}, without jokers: {hand_without_jokers.hand}"

    def __eq__(self, other):
        if self.get_strength_of_hand() == other.get_strength_of_hand():
            # Insert the Jokers again and compare
            self_hand = copy.deepcopy(self)
            other_hand = copy.deepcopy(self)
            self_hand.put_back_the_jokers()
            other_hand.put_back_the_jokers()

            if self_hand == other_hand:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.get_strength_of_hand() < other.get_strength_of_hand():
            # This hand has lower strength than the other one, return True
            return True

        if self.get_strength_of_hand() > other.get_strength_of_hand():
            # This hand has higher strength than the other one, return False
            return False

        # Hands have equal strength, compare card by card
        # But now we need to insert the Jokers again
        self_hand = copy.deepcopy(self)
        other_hand = copy.deepcopy(other)
        self_hand.put_back_the_jokers()
        other_hand.put_back_the_jokers()

        card_value = self.all_cards[::-1]
        for self_card, other_card in zip(self_hand.hand, other_hand.hand):
            if card_value.index(self_card) < card_value.index(other_card):
                return True
            if card_value.index(self_card) > card_value.index(other_card):
                return False
        # All cards equal, return False
        return False

    def put_back_the_jokers(self) -> None:
        if not self.joker_positions:
            return
        for x in self.joker_positions:
            hand_list = list(self.hand)
            hand_list[x] = self.joker
            self.hand = "".join(hand_list)
        return

    def get_strength_of_hand(self) -> int:
        """
        Get the strength of the hand, according to the following list:
        7: 5 of a kind
        6: 4 of a kind
        5: Full house (3 and 2)
        4: 3 of a kind
        3: 2 pairs
        2: 1 pair
        1: High card (none of the above)

        :return:     The strength of the hand as an int. See above
        """

        # Find 5 of a kind
        for card in self.all_cards:
            count = self.hand.count(card)
            if count == 5:
                return 7

        # Find 4 of a kind
        for card in self.all_cards:
            count = self.hand.count(card)
            if count == 4:
                return 6

        # Find full house (3 and 2)
        # First find 3 cards
        for card_find_3 in self.all_cards:
            count_find_3 = self.hand.count(card_find_3)
            if count_find_3 == 3:
                # Found 3 cards, now find 2 other
                cards_with_find_3_removed = self.all_cards.replace(card_find_3, "")
                hand_with_find_3_removed = self.hand.replace(card_find_3, "")
                for card_find_2 in cards_with_find_3_removed:
                    count_find_2 = hand_with_find_3_removed.count(card_find_2)
                    if count_find_2 == 2:
                        # Full house found
                        return 5
                # We found 3 cards, but not a full house. Then it is a 3 of a kind
                return 4

        # Find 2 pairs
        # First find one pair
        for card_find_2a in self.all_cards:
            count_find_2a = self.hand.count(card_find_2a)
            if count_find_2a == 2:
                # Found first pair, now find a second pair
                cards_with_find_2a_removed = self.all_cards.replace(card_find_2a, "")
                hand_with_find_2a_removed = self.hand.replace(card_find_2a, "")
                for card_find_2b in cards_with_find_2a_removed:
                    count_find_2b = hand_with_find_2a_removed.count(card_find_2b)
                    if count_find_2b == 2:
                        # Second pair found
                        return 3
                # We found one pair, but not two pairs
                return 2

        # We didn't find any type of hand, then it is just the highest card
        return 1


class HandTools:
    @staticmethod
    def get_strongest_possible_hand(original_hand: Hand) -> Hand:
        all_cards = "AKQT98765432"
        joker = "J"

        if joker not in original_hand.hand:
            # No joker card in the hand, just return the hand
            return original_hand

        # Get first joker and replace
        highest_card = copy.deepcopy(original_hand)
        for replacement_card in all_cards:
            hand_to_test = copy.deepcopy(original_hand)
            hand_to_test.hand = hand_to_test.hand.replace(joker, replacement_card, 1)
            hand_tested = HandTools.get_strongest_possible_hand(hand_to_test)
            if highest_card < hand_tested:
                highest_card = hand_tested
        return highest_card


def main():
    print("Start of script")
    # puzzle_input_filename = "./example_input.txt"
    puzzle_input_filename = "./puzzle_input.txt"
    with open(puzzle_input_filename) as f:
        file_content = f.readlines()
    file_content = [x.strip() for x in file_content]

    # for row in file_content:
    #     print(f"{row}")
    print(f"Number of hands: {len(file_content)}")

    start = datetime.now()

    # Create list of dicts with hands and bids. The get_strongest_ method will make sure to add the strongest
    # possible hand if the hand contains Jokers.
    hands_and_bids = []
    for row in file_content:
        hand_and_bid_split = row.split()
        hand_and_bid = {"hand": HandTools.get_strongest_possible_hand(Hand(hand_and_bid_split[0])),
                        "bid": int(hand_and_bid_split[1])}
        hands_and_bids.append(hand_and_bid)

    # Sort the list of hands
    sorted_hands_and_bids = sorted(hands_and_bids, key=lambda x: x["hand"])

    total_winning = 0
    for idx, hands_and_bids in enumerate(sorted_hands_and_bids):
        rank = idx + 1
        winning = rank * hands_and_bids["bid"]
        total_winning += winning

    end = datetime.now()
    print(f"Process time: {end-start}")
    print(f"{total_winning=}")


if __name__ == "__main__":
    main()
