class GameState:
    """
    We call turn() on an instance of GameState and assign the result
    to the new GameState. See main.

    """

    def __init__(
        self, load_from=None, months=0, funding_cost=0, motivation=0, player_data=0,
    ):
        self.months_since_founding = 0
        if load_from is None:
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
        else:
            self.funds_remaining = load_from.funds_remaining
            self.founders = load_from.founders
            self.employees = load_from.employees
            self.stock_remaining = load_from.stock_remaining
