class Hand:
    """
    Purpose: Represents the cards held by a player or dealer in Blackjack.

    Author: Kerwin
    """

    def __init__(self):
        """
        Purpose: Initialize an empty hand.

        Args:
            None

        Returns:
            None

        Author: Kerwin
        """
        self.cards = []

    def add_card(self, card):
        """
        Purpose: Add a card to the hand.

        Args:
            card (tuple): A card stored as (rank, suit, value)

        Returns:
            None

        Author: Kerwin
        """
        self.cards.append(card)

    def calculate_value(self):
        """
        Purpose: Calculate the total value of the hand while adjusting Aces
        so the hand is less likely to go over 21.

        Args:
            None

        Returns:
            int: The total value of the hand

        Author: Kerwin
        """
        # start total at 0
        # count how many aces we have
        # loop through cards and add values
        # if card is an ace, track it
        # if total goes over 21, adjust ace values from 11 → 1
        # return final total

        total = 0
        ace_count = 0

        for card in self.cards:
            rank, suit, value = card
            total += value
            if rank == "Ace":
                ace_count += 1

        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        return total

    def is_bust(self):
        """
        Purpose: Check whether the hand value is greater than 21.

        Args:
            None

        Returns:
            bool: True if the hand is bust, otherwise False

        Author: Kerwin
        """
        return self.calculate_value() > 21

    def display_hand(self):
        """
        Purpose: Display all cards currently in the hand.

        Args:
            None

        Returns:
            None

        Author: Kerwin
        """
        for card in self.cards:
            rank, suit, value = card
            print(f"{rank} of {suit}")