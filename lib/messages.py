def congratulate(state):
    """
    Handles informing the player about their victory
    """
    print(f"Congrations I guess.")
    return None


def roast(state):
    """
    Handle humiliating the player for their defeat.
    """
    print(f"This is why your VC won't call you.")
    return None


def introduce_game():
    """
    This function handles all the 'UI' for starting the game.
    """
    message = f"Game starting with default values."
    print(message)


def turn_prompt(turn_number):
    """
    Should execute every turn. Handles UI for introducing challenges.
    """
    message = f"Turn: {turn_number}"
    print(message)
    proceed = input("Proceed?\n")
