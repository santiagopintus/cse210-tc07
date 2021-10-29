class Counter:
    """Keeps track of the number of points the player has
    
    Stereotype:
        Information Holder

    Attributes:
        __points (int): the number of points the player has
    Methods: 
        increment(), decrement(), reset(), get_points()
    """
    def __init__(self, points=0):
        """The class contructor

        Args: 
            Self: An instance of Counter
        """
        self.__points = points

    def increment(self):
        self.__points += 1

    def decrement(self):
        self.__points -= 1

    def reset(self):
        self.__points = 0

    def get_points(self):
        return self.__points