

def main():
    state = start_game()
    victory = defeat = False
    while not (victory or defeat):
        state, (victory, defeat) = turn(state)
    if victory:
        congratulate(state)
    else:
        roast(state)
    return 0


if __name__ == "__main__":
    main()
