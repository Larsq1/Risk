# Class for territories
from Army import Army


class Territory(object):
    """
    territory on a risk map
    """

    def __init__(self, name, continent):
        """
        Initialize Territory with a name and the corresponding continent
        :param name: name of the territory
        :param continent: name of the corresponding continent
        """
        self.name = name
        self.continent = continent
        self.army = Army()
