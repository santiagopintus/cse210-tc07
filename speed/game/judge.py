class Judge:
    """A Judger that evaluates if the word the user typed is in 
    the current words in screen.

    Attributes:
        __current_words: The current words in screen.
    Methods:
        set_current_words: Set the current words to be compared with.
        judge_word: Judge if the word is in the current words.
    
    """
    def __init__(self):
        """The class contructor

        Args: 
            Self: An instance of Judge
        """
        self.__current_words = []
        self.__current_word = ""

    def set_current_words(self, words):
        """Set the current words to be compared with"""
        self.__current_words = words

    def judge_word(self):
        """Judge if the word is in the current words"""
        if self.__current_word in self.__current_words:
            return self.__current_word
        return False

    def set_current_word(self, letter):
        """Set the current word to be compared with"""
        self.__current_word += letter
    
    def clear_current_word(self):
        """Clear the current word"""
        self.__current_word = ""

    def get_current_word(self):
        """Returns the current word to be rendered.

        Args:
            self (OutputService): An instance of OutputService.
        """
        return self.__current_word