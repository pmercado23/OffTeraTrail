class Basic:
    """
    Just a container for holding the default values. Future implementations could
    have Easy, or Hard starting values.
    """

    def __init__(self):
        self.funds_remaining = 20 * 10 ** 6
        self.founders = ["Richard", "Erlich"]
        self.employees = ["Gilfoyle", "Danesh"]
        self.stock_remaining = 100 * 10 ** 9


BASIC_STARTING_STATE = Basic()
