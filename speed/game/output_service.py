from asciimatics.screen import Screen
from game import constants

class OutputService:

    def __init__(self, screen):
        self.screen = screen

    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    def draw_word(self, word):
        """Renders the given word on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            word (word): The word to render.
        """ 
        position = word.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(word, x, y, 7) # WHITE

    def draw_actors(self, words):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for word in words:
            self.draw_word(word)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh()    