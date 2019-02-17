# common_words.py
#
#

from analytic import Analytic

class CommonWords(Analytic):


    def analyze(self):
        word_dict = {}
        total_words = 0
        for song_lyrics in self.lyric_list:
            for word in song_lyrics:
                total_words += 1
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
        
        s = sorted(word_dict.items(), key = lambda x: x[1], reverse = True)

        print(f"Total Words: {total_words}")

        return s[:3]
        



    