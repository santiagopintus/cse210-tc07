import random
from game import constants

class Word:
    """ The word class keeps the word moving on the screen 
    and if the word was guessed, it removes it from the screen,
    and from the current_words list.

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance.
        _y (Point): The vertical distance.
    """
    
    def __init__(self, text):
        """The class constructor.
        
        Args:
            self (Word): An instance of word.
        """
        self._text = text
        self._x = random.randint(0, constants.MAX_X)

    def increment_x(self):
        """Gets a new point that is the sum of this and 1.

        Args:
            self (Point): An instance of Point.

        Returns:
            Point: A new Point that is the sum.
        """
        self._x += 1
        return self._x

    def decrement(self):
        """Gets a new point that is the subtraction of this and 1.

        Args:
            self (Point): An instance of Point.

        Returns:
            Point: A new Point that is the subtraction.
        """
        self._x -= 1
        return self._x
        

    def get_x(self):
        """Gets the horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def get_text(self):
        """Gets the text.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            string: The text.
        """
        return self._text

    # def reverse(self):
    #     """Gets a new Point that is the reverse of this one.
        
    #     Args:
    #         self (Point): An instance of Point.
            
    #     Returns:
    #         Point: A new Point that is reversed.
    #     """
    #     x = self._x * -1
    #     y = self._y * -1
    #     return Word(x, y)