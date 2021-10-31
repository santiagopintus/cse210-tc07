from game import constants
from game.reader import Reader
from game.counter import Counter
from game.judge import Judge
from game.cleaner import Cleaner
from game.word import Word
from game import constants
from time import sleep

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
        current_word (Word): The current word being guessed.
    """

    def __init__(self, input_service, output_service):
        self.input_service = input_service
        self.output_service = output_service
        self.reader = Reader()
        self.counter = Counter()
        self.judge = Judge()
        # self.word = Word()
        self.cleaner = Cleaner()
        self.keep_playing = True
        self.constants = constants
        self.current_words = []
        self.score = 0
        self.current_word = None
    
    def start_game(self):
        self.prepare()
        while self.keep_playing:
            letter = self._get_inputs()
            self._do_updates(letter)
            self._do_outputs()
            sleep(self.constants.SLEEP_TIME)

    def prepare(self):
        self.reader.read_file(self.constants.LIBRARY)
        self.current_words = self.reader.get_current_words(self.constants.STARTING_WORDS)
        self.judge.set_current_words(self.current_words)
        self.output_service.set_current_words(self.current_words)
        self.output_service.create_word_instances()

    def _get_inputs(self):
        user_input = self.input_service.get_letter()
        if user_input == "*":
            self.judge.clear_current_word()
            return ''
        else:
            return user_input
    
    def _do_updates(self, letter):
        self.judge.set_current_word(letter)
        word_guessed = self.judge.judge_word()

        if word_guessed:
            self.judge.clear_current_word()
            self.output_service.remove_word(word_guessed)
            self.output_service.create_word_instances()
            self.counter.increment()
            self.current_word = None
        else:
            self.current_word = self.judge.get_current_word()
            self.output_service.set_current_word(self.current_word)
        
        self.score = self.counter.get_score()
        self.output_service.set_score(self.score)
    
    def _do_outputs(self):
        self.output_service.clear_screen()
        self.output_service.draw_score()
        self.output_service.draw_current_word()
        self.output_service.draw_current_words()
        self.output_service.refresh_screen()