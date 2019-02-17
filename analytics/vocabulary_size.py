# vocabulary_size.py
from analytic import Analytic


class VocabularySize(Analytic):

    def analyze(self):
        """
        This Analytic subclass simply converts the passed-in list of song lyrics into a set
        in order to eliminate duplicates and then converts back to a list.
        :return: The length of the new list
        """
        vocabulary_list = []
        for lyrics in self.lyric_list:
            vocabulary_list.extend(lyrics)
        return str(len(set(vocabulary_list)))