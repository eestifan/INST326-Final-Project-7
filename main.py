from hand import Hand
from deck import Deck

def main():
    """
    Purpose: Run a simple game of Blackjack using Hand and Deck classes.

    Args:
        None

    Returns:
        None

    Authors: Kerwin/William
    """

    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Dealt from the deck instead of hard-coded
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    while True:
        print("\n--- Your Hand ---")
        player_hand.display_hand()
        current_value = player_hand.calculate_value()
        print(f"Current value: {current_value}")

        if player_hand.is_bust():
            print("Bust! You went over 21.")
            break
        
        if player_hand.has_blackjack():
            print("Blackjack! You win!")
            break

        choice = input("Would you like to (H)it or (S)tand? ").lower()

        if choice == 'h':
            player_hand.add_card(deck.deal_card())
        elif choice == 's':
            print(f"Standing with a total of {current_value}.")
            break
        else:
            print("Invalid input. Please enter 'H' or 'S'.")

    if not player_hand.is_bust() and not player_hand.has_blackjack():
        print("\n--- Dealer's Turn ---")
        while dealer_hand.calculate_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        
        dealer_hand.display_hand()
        print(f"Dealer's total: {dealer_hand.calculate_value()}")

        player_score = player_hand.calculate_value()
        dealer_score = dealer_hand.calculate_value()

        if dealer_score > 21:
            print("Dealer busted! You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif dealer_score > player_score:
            print("Dealer wins.")
        else:
            print("It's a push.")

    print("\nGame Over. Thanks for playing!")

if __name__ == "__main__":
    main()