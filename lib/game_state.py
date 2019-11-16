class GameState:
    """
    We call turn() on an instance of GameState and assign the result 
    to the new GameState. See main.

    """

    def __init__(self, months, funding_cost, motivation, player_data):
        self.months_since_founding = 0
        self.funds_remaining = None

        # How are founders different then employees?
        # Maybe the give a special bonus/penalty?
        self.founders = []

        # A list of Employee's (this makes me wish Python was typed)
        self.employees = []

        # I'm envisaging this as a percentage of ownership and once it fall below
        # 50 there's penalties, once it's below 10 you lose. Maybe you can decrement
        # stock remaining to increase an Employee's morale?
        self.stock_remaining = 100.0


def load_data():
    return Player([Person("harry"), Person("dan")],
                  [Person("suraj"), Person("pierre")],
                  100000,
                  100)
