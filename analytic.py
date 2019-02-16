# analytic.py
#
# Parent class of all analytics

# Possible analytics:

# Number of songs
# Number of albums
# Most common word
# Size of vocab
# Overall positivity/negativity
# Release history

from abc import ABC, abstractmethod

class Analytic(ABC):

    def __init__(self, lyric_list: list):
        self.lyric_list = lyric_list
        super().__init__()

    @abstractmethod
    def analyze(self):
        pass
