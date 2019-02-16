# common_words.py
#
#

from analytic import Analytic

class CommonWords(Analytic):

    def __init__(self, lyric_list):
        Analytic.__init__(self, lyric_list)
        
    
    def analyze(self):
        word_dict = {}
        for song_lyrics in self.lyric_list:
            for word in song_lyrics:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
        
        s = sorted(word_dict.items(), key = lambda x: x[1], reverse = True)

        print(s[:3])



    