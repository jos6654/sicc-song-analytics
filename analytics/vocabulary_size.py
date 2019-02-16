# vocabulary_size.py
from analytic import Analytic


class VocabularySize(Analytic):

    def analyze(self):
        lyrics = list(set(self.lyric_list))
        return len(lyrics)