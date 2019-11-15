from parts import gameplay_loop

class CoreData:
    def __init__(self, months, funding_cost, motivation, player_data):
        self.months = months
        self.funding_cost = funding_cost
        self.motivation = motivation
        self.loss = False
        self.player_data = player_data


class Player:
    def __init__(self, founders, team, funding, options):
        self.founders = founders
        self.team = team
        self.funding = funding
        self.options = options


class Person:
    def __init__(self, name):
        self.name = name
        self.health = 100


def load_data():
    return Player([Person("harry"), Person("dan")],
                          [Person("suraj"), Person("pierre")],
                          100000,
                          100)



def main():
    player_data = load_data()
    game_data = CoreData(60, 10, 100, player_data)
    print("Starting....")
    gameplay_loop.main_game_loop(game_data)


if __name__=="__main__":
    # Load config file
    main()
    print("Stopping...")


