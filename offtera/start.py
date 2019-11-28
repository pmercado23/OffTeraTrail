import offtera.messages as messages
import offtera.game_state as game_state
import offtera.defaults as defaults


def start_game():
    """
    Should instantiate game state
    """
    messages.introduce_game()
    initial_state = game_state.GameState(load_from=defaults.BASIC_STARTING_STATE)
    return initial_state
