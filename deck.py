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

    def reset_deck(self, player_hand, dealer_hand):
    """
    Purpose: Announce the result of the last game and reset the deck for a new round.
    Args:
        player_hand (Hand): The player's hand from the last game.
        dealer_hand (Hand): The dealer's hand from the last game.
    Returns:
        None
    Author: Efieson Estfianos
    """
    player_score = player_hand.calculate_value()
    dealer_score = dealer_hand.calculate_value()
    
    # Conditional expression to figure out the result (technique #1)
    if player_score > 21:
        last_result = "Player busted!"
    elif dealer_score > 21:
        last_result = "Dealer busted, player wins!"
    else:
        last_result = "Player wins!" if player_score > dealer_score else \
                      "Dealer wins." if dealer_score > player_score else \
                      "It's a push!"
    
    # f-string with an expression inside (technique #3)
    print(f"--- {last_result} (Player: {player_score}, Dealer: {dealer_score}, Diff: {abs(player_score - dealer_score)}) ---")
    print("Reshuffling the deck for a new round...")
    self.__init__()
    print(f"Deck is ready! {len(self.cards)} cards shuffled.")
    
        
    
        
        

    
    

