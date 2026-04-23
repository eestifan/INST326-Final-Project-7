from hand import Hand

def main():
    """
    Purpose: Run a small test of the Hand class for the project milestone.

    Args:
        None

    Returns:
        None

        Author: Kerwin
    """
    hand = Hand()
    hand.add_card(("Ace", "Spades", 11))
    hand.add_card(("King", "Hearts", 10))

    print("Current hand:")
    hand.display_hand()
    print(f"Hand value: {hand.calculate_value()}")

if __name__ == "__main__":
    main()