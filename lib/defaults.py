
class Basic:
    """
    Just a container for holding the default values. Future implementations could 
    have Easy, or Hard starting values.
    """

    def __init__(self):
        self.months = 24
        self.funding = 2 * 10**6
        self.motivation = 0
        self.player_data = None


BASIC = Basic()
