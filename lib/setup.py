import lib.messages as messages
import lib.game_state as game_state
import lib.defaults as defaults


def start_game():
    """
    Should instantiate game state
    """
    messages.introduce_game()
    initial_state = game_state.GameState(
        load_from=defaults.BASIC_STARTING_STATE)
    return initial_state
