import random

class Deck:
    """
    Purpose: Represents a standard deck of 52 playing cards.
    
    Author: William
    """

    def __init__(self):
        """
        Purpose: Initialize the deck with 52 cards and shuffle them.

        Args:
            None

        Returns:
            None

        Author: William
        """
        self.cards = []
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        values = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
            }
        
        for suit in suits:
            for rank in ranks:
                card = (rank, suit, values[rank])
                self.cards.append(card)
                
        self.shuffle()
        
    def shuffle(self):
        """
        Purpose: Randomly reorder the cards in the deck.

        Args:
            None

        Returns:
            None

        Author: William
        """
        random.shuffle(self.cards)
        
    def deal_card(self):
        """
        Purpose: Remove and return the top card from the deck.

        Args:
            None

        Returns:
            tuple: A card stored as (rank, suit, value) or None if empty.

        Author: William
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        return None