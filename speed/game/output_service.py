from asciimatics.screen import Screen
from game import constants
from game.word import Word

class OutputService:

    def __init__(self, screen):
        self.__screen = screen
        self.__current_words = None
        self.__score = 0
        self.__current_word = None
        self.__instances_words = []

    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self.__screen.clear_buffer(7, 0, 0)
        self.__screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self.__screen.print_at("Buffer: " + self.__current_word + "-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    
    def set_current_words(self, words):
        """Sets the current words to be rendered.

        Args:
            self (OutputService): An instance of OutputService.
            words (list): The words to render.
        """
        self.__current_words = words

    def set_score(self, score):
        """Sets the current score to be rendered.

        Args:
            self (OutputService): An instance of OutputService.
            score (int): The score to render.
        """
        self.__score = str(score)

    def set_current_word(self, word):
        """Sets the word the user is typing to be rendered.
        
        Args:
            self (OutputService): An instance of OutputService.
            word (word): The word to render.
        """
        self.__current_word = word

    def draw_score(self):
        """Renders the current score.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self.__screen.print_at("Score: " + self.__score, 0, 0, 7) # WHITE
    
    def draw_current_word(self):
        """Renders the current word the user is typing.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self.__screen.print_at("Buffer: " + self.__current_word, 0, constants.MAX_Y, 7) # WHITE

    
    def refresh_screen(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self.__screen.refresh()

    def create_word_instances(self):
        """Creates a list of instances of the words to be rendered.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self.__instances_words.clear()
        for word in self.__current_words:
            word = Word(word)
            self.__instances_words.append(word)

    def draw_current_words(self):
        """Renders the current words to be rendered.

        Args:
            self (OutputService): An instance of OutputService.
        """
        y = 2
        for word in self.__instances_words:
            self.draw_word(word, y)
            y += 2
    
    def draw_word(self, word, y=0):
        """Renders the given word on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            word (word): The word to render.
        """ 
        direction = word.get_direction()
        x = word.get_x()
        text = word.get_text()

        if direction == "for" and x >= constants.MAX_X:
            word.invert_direction()

        if direction == "back" and x <= 0:
            word.invert_direction()

        if direction == "for":
            word.increment_x()
        else:
            word.decrement_x()

        self.__screen.print_at(text, x, y, 7) # WHITE

    def remove_word(self, word_guessed):
        """Removes the given word from the screen.

        Args:
            self (OutputService): An instance of OutputService.
            word_guessed (word): The word to remove.
        """
        for word in self.__instances_words:
            if word.get_text() == word_guessed:
                print(word)
                self.__instances_words.remove(word)
                break