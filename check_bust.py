def check_bust(hand, limit=21):
    """
    Purpose: Check if a hand has gone over 21.

    Args:
        hand (Hand): The hand object
        limit (int): Maximum allowed hand value before busting

    Returns:
        bool: True if the hand is bust, False otherwise

    Author: Devante 
    """

    # Step 1: Get the value of the hand
    total = hand.calculate_value()

    # Step 2: Return True if over limit, otherwise False
    return True if total > limit else False
