import os

MAX_X = 60
MAX_Y = 20
FRAME_LENGTH = 0.08
STARTING_WORDS = 5
SLEEP_TIME = 0.05
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
