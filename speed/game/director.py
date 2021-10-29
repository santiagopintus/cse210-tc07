from game import constants
from game.reader import Reader
from game.counter import Counter
from game.judge import Judge
from game.cleaner import Cleaner
from game.word import Word
from game import constants

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        output_service (OutputService): The output mechanism.
        reader (Reader): The words file reader.
        counter (Counter): The points counter.
        judge (Judge): An instance of the judge class
        word (Word): An instance of the word class
        cleaner (Cleaner): An instance of the cleaner class
        keep_playing (boolean): Whether or not the game can continue.
        constants (Constants): The game constants.
        current_words (list): A list of the current words on the screen.
        score (Score): The current score.
    """

    def __init__(self, input_service, output_service):
        self.input_service = input_service
        self.output_service = output_service
        self.reader = Reader()
        self.counter = Counter()
        self.judge = Judge()
        self.word = Word()
        self.cleaner = Cleaner()
        self.keep_playing = True
        self.constants = constants
        self.current_words = []
        self.score = 0
    
    def start_game(self):
        self.prepare()


    def prepare(self):
        self.reader.read_file(self.constants.LIBRARY)
        self.current_words = self.reader.get_current_words(self.constants.STARTING_WORDS)
        print(self.current_words)

        