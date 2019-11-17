from lib.game_utils import print_message

def congratulate(state):
    """
    Handles informing the player about their victory
    """
    win_message = f"Congrations I guess."
    print_message(win_message)
    return None


def roast(state):
    """
    Handle humiliating the player for their defeat.
    """
    loss_message = f"This is why your VC won't call you."
    print_message(loss_message)
    return None


def introduce_game():
    """
    This function handles all the 'UI' for starting the game.
    """
    message = f"Game starting with default values."
    print_message(message)


def turn_prompt(turn_number):
    """
    Should execute every turn. Handles UI for introducing challenges.
    """
    message = f"Turn: {turn_number}"
    print_message(message)
    proceed = input("Proceed?\n")
