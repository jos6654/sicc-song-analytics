# analytic.py
#
# Parent class of all analytics

# Possible analytics:
# Implemented:
    # Most common word
    # Number of songs
    # Size of vocab

# To-Do:
    # Overall positivity/negativity
    # Release history

from abc import ABC, abstractmethod

class Analytic(ABC):

    def __init__(self, lyric_list: list):
        # lyric_list is list of lists of strings that are the words to a song
        self.lyric_list = lyric_list
        super().__init__()

    @abstractmethod
    def analyze(self):
        pass
