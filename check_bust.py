def check_bust(hand):
    """
    Purpose: Check if a hand has gone over 21.

    Args:
        hand (Hand): The hand object

    Returns:
        bool: True if the hand is bust, False otherwise

    Author: Devante 
    """

    # Step 1: Get the value of the hand
    total = hand.calculate_value()

    # Step 2: Return True if over 21, otherwise False
    return True if total > 21 else False
