# song_number.py

from analytic import Analytic

class SongNumber(Analytic):

    def analyze(self):
        return len(self.lyric_list)