class Word:
    """ The word class keeps the word moving on the screen 
    and if the word was guessed, it removes it from the screen,
    and from the current_words list.
    """

    def __init__(self):
        self.word = None