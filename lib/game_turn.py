import lib.messages as messages


def turn(state):
    """
    This function is responsable for propelling the game forward.
    """
    victory = defeat = False

    state.months_since_founding += 1
    messages.turn_prompt(state.months_since_founding)

    if state.months_since_founding > 5:
        defeat = True

    return state, (victory, defeat)
