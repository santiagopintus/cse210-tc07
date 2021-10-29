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

    def set_current_words(self, words):
        """Set the current words to be compared with"""
        self.__current_words = words

    def judge_word(self, word):
        """Judge if the word is in the current words"""
        if word in self.__current_words:
            return True
        return False