def check_bust(hand):
    """
    Purpose: Check if a hand has gone over 21.

    Args:
        hand (Hand): The hand object

    Returns:
        bool: True if the hand is bust, False otherwise

    Author: Devante Thompson
    """

    # Step 1: Get the value of the hand
    total = hand.calculate_value()

    # Step 2: Check if value is greater than 21
    if total > 21:
        return True
    else:
        return False