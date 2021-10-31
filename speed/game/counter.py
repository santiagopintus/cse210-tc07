class Counter:
    """Keeps track of the number of score the player has
    
    Stereotype:
        Information Holder

    Attributes:
        __score (int): the number of points the player has
    Methods: 
        increment(), decrement(), reset(), get_points()
    """
    def __init__(self, score=0):
        """The class contructor

        Args: 
            Self: An instance of Counter
        """
        self.__score = score

    def increment(self, score=1):
        self.__score += score

    def decrement(self, score=1):
        self.__score -= score

    def reset(self):
        self.__score = 0

    def get_score(self):
        return self.__score