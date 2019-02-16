# song_number.py

from analytic import Analytic

class Song_Number(Analytic):

    def analyze(self):
        return len(self.lyric_list)