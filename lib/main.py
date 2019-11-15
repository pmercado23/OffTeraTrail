from random import randint


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


def month_pass(game_data):
    game_data.months -= 1
    event = roll_d(20)
    print("a month has passed, {} months remain, event {} has occurred".format(game_data.months, event))
    funding_decrease(game_data, 50)
    print("you have {} left in funding".format(game_data.player_data.funding))



def funding_decrease(game_data, costs):
    game_data.player_data.funding -= costs


def check_loss(game_data):
    if (game_data.player_data.funding <= 0 or game_data.months <= 0):
        game_data.loss = True


def roll_d(x):
    return randint(0, x)


def game_loop(game_data):
    while (not game_data.loss):
        print("gameplay loop here with {} months".format(game_data.months))
        month_pass(game_data)
        check_loss(game_data)



def main():
    player_data = load_data()
    game_data = CoreData(60, 10, 100, player_data)
    print("Starting....")
    game_loop(game_data)


if __name__=="__main__":
    # Load config file
    main()
    print("Stopping...")


