import os
import nltk
from nltk.corpus import words, wordnet
from database.hdf5 import HDF5
nltk.download('words')
nltk.download('omw-1.4')
nltk.download('wordnet')


class Lexicon:        
    def __init__(self):
        self.db = HDF5('lexicon.hdf5')
        self._import_words()
        self._import_synsets()

    def _import_words(self):
        try: 
            return words.words()
        except LookupError:
            nltk.download('words')

    def _import_synsets(self):
        try: 
            return wordnet.synsets('A')
        except LookupError:
            nltk.download('wordnet')
            nltk.download('omw-1.4')

    def _get_meaning_from_nltk(self, word):
        synsets = wordnet.synsets(word)
        try: 
            return synsets[0].definition()
        except IndexError:
            return None 

    def fetch_meaning(self, word):
        return self.db.get(f"{word}/meaning")

    def word_list(self):
        return words.words()







