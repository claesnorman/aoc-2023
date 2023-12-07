import functools
from datetime import datetime


@functools.total_ordering
class Hand:
    def __init__(self, hand: str):
        self.hand = hand
        self.all_cards = "AKQJT98765432"

    def __str__(self):
        return f"cards: {self.hand}, strength: {self.get_strength_of_hand()}"

    def __eq__(self, other):
        if self.get_strength_of_hand() == other.get_strength_of_hand() and self.hand == other.hand:
            return True
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
        card_value = self.all_cards[::-1]
        for self_card, other_card in zip(self.hand, other.hand):
            if card_value.index(self_card) < card_value.index(other_card):
                return True
            if card_value.index(self_card) > card_value.index(other_card):
                return False
        # All cards equal, return False
        return False

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
                # We found 3 cards, but not a full house. Then it is a 3 of a kimd
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

    hands_and_bids = []
    for row in file_content:
        hand_and_bid_split = row.split()
        hand_and_bid = {"hand": Hand(hand_and_bid_split[0]),
                        "bid": int(hand_and_bid_split[1])}
        hands_and_bids.append(hand_and_bid)

    # Test data
    # hands_and_bids = [
    #     {"hand": Hand("77777"), "bid": 1},
    #     {"hand": Hand("74AQ5"), "bid": 1},
    #     {"hand": Hand("A7AAA"), "bid": 1},
    #     {"hand": Hand("A7333"), "bid": 1},
    #     {"hand": Hand("3AK7K"), "bid": 1},
    #     {"hand": Hand("7JJ2J"), "bid": 1},
    #     {"hand": Hand("42424"), "bid": 1},
    #     {"hand": Hand("7TQ7T"), "bid": 1},
    # ]

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
