import parts.core as core
import parts.member as memeber
from random import randint

PLAY_DATA = None


def load_data():
    global PLAY_DATA
    PLAY_DATA = core.Core([memeber.Member("bill", 22), memeber.Member("bob", 22)],
                          [memeber.Member("suraj", 22), memeber.Member("pierre", 22)],
                          100,
                          100)

def month_pass(months_current):
    months_left = months_current-1
    event = roll_d(20)
    print("a month has passed, {} months remain, event {} has occurred".format(months_left, event))



def roll_d(x):
    return randint(0, x)


def main_loop(months, player_data):
    print("gameplay loop here with {} months".format(months))
    month_pass(months)



def main():
    load_data()
    months = 60
    print("Starting....")
    main_loop(months, PLAY_DATA)


if __name__=="__main__":
    # Load config file
    main()
    print("Stopping...")


