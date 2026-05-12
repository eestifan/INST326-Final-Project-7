def place_bet(player_chips, player_hand=None, dealer_hand=None, bet=0):
    """
    Purpose: Handle the wagering system by either asking for a bet or updating chips after the round.
    Args:
        player_chips (int): The player's current chip count.
        player_hand (Hand): The player's hand after the round ends. Default is None.
        dealer_hand (Hand): The dealer's hand after the round ends. Default is None.
        bet (int): The amount that was wagered. Default is 0.
    Returns:
        int: The bet amount (when asking for a bet) or the updated chip count (when settling up).
    Author: Efieson Estifanos
    """
    # if the hands are empty that means we haven't started yet so ask for a bet
    if player_hand == None or dealer_hand == None:
        print("You currently have " + str(player_chips) + " chips.")
        wager = int(input("How much would you like to bet? "))
        return wager
    
    # get the player score
    player_score = player_hand.calculate_value()
    # get the dealer score
    dealer_score = dealer_hand.calculate_value()
    
    # make a variable to hold the outcome
    outcome = ""
    
    # put both hands in a list so we can find the winner
    hands = [("player", player_score), ("dealer", dealer_score)]
    # use max to find whichever hand has the highest score, if it's over 21 then make it -1 so it loses
    winner = max(hands, key=lambda h: h[1] if h[1] <= 21 else -1)
    
    # check if the player busted
    if player_score > 21:
        outcome = "lose"
    # check if the dealer busted
    elif dealer_score > 21:
        outcome = "win"
    # check if it's a tie
    elif player_score == dealer_score:
        outcome = "push"
    # check if player won
    elif winner[0] == "player":
        outcome = "win"
    # otherwise dealer won
    else:
        outcome = "lose"
    
    # now do stuff based on the outcome
    if outcome == "win":
        # player won so add the bet to their chips
        player_chips = player_chips + bet
        print(f"You won {bet} chips! You now have {player_chips} chips.")
    elif outcome == "lose":
        # player lost so take the bet away
        player_chips = player_chips - bet
        print(f"You lost {bet} chips. You now have {player_chips} chips.")
    elif outcome == "push":
        # it was a tie so nothing happens
        print(f"Push — your bet is returned. You still have {player_chips} chips.")
    
    # send back the new chip count
    return player_chips
