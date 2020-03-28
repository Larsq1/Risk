# Class for card


class Card(object):
    """
    card one can get in a risk game
    """

    def __init__(self, territory, symbol):
        """
        Initialize card with territory and symbol
        :param territory: the territory belonging to the card
        :param symbol: the symbol belonging to the card
        """
        self.territory = territory
        self.symbol = symbol
