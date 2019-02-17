# analytic.py
#
# Parent class of all analytics

# Possible analytics:
# Implemented:
    # Most common word
    # Number of songs
    # Size of vocab
    # Release history

# To-Do:
    # Overall positivity/negativity


from abc import ABC, abstractmethod

class Analytic(ABC):

    def __init__(self, lyric_list = [], url_list = []):
        # lyric_list is list of lists of strings that are the words to a song
        self.lyric_list = lyric_list
        self.url_list = url_list
        super().__init__()

    @abstractmethod
    def analyze(self):
        pass
