import random

class Reader:
    """Reads the file with words from constants
    and returns a list with the words. It also selects 
    random words from the list according to the quantity given.

    Attributes:
        file: file with words
        words: list with words
    Methods:
        read_file: reads the file with words and keeps it in words list
        get_words: returns the words list
        select_words: selects random words from the list
    """
    def __init__(self):
        """The class contructor

        Args: 
            Self: An instance of Reader
        """
        self.__file = None
        self.__words = []

    def read_file(self, file):
        """Reads the file with words and keeps it in words list
        
        Args:
            self: an instance of Reader
            file: file with words
        """
        self.__file = file
        for word in self.__file:
            self.__words.append(word)
    
    def get_current_words(self, quantity):
        """Selects random words from the list
        and returns them in a list

        Args: 
            self: an instance of Reader
            quantity: quantity of words to be selected
        """
        current_words = []
        for _ in range(quantity):
            current_words.append(random.choice(self.__words))
        return current_words