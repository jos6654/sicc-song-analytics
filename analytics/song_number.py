# song_number.py

from analytic import Analytic

class SongNumber(Analytic):

    def analyze(self):
        """
        This Analytic subclass very simply returns the length of the list of songs
        :return: The number of songs in the list
        """
        return str(len(self.lyric_list))