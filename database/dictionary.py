from graveyard.rdb import Rdb
from global_functions import chunks
import json
import progressbar
import sys
from nltk.corpus import words, wordnet

r = Rdb().setup()
word_list = words.words()

def check_rdb(word, category):
    if (r.get(f"lexicon-empty-{category}-{word}") == '1'):
        return False
    return True

def set_empty(word, category):
    r.set(f"lexicon-empty-{category}-{word}", 1)
    return True



for word in word_list:    
    print(f"Fetching {word}...")
    syns = wordnet.synsets(word)

    # Meaning
    if (check_rdb(word, 'meaning')):
        try:
            meaning = syns[0].definition()
            r.set(f"lexicon-meaning-{word}", meaning)
        except IndexError:
            set_empty(word, 'meaning')
    
    # Synonyms
    if (check_rdb(word, 'synonym')):
        synonyms = []
        antonyms = []
        for syn in syns:
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        if (synonyms):
            for i, s in enumerate(synonyms):
                r.set(f"lexicon-synonyms-{word}-{i}", s)
        else:
            set_empty(word, 'synonym')

        if (antonyms):
            for i, a in enumerate(antonyms):
                r.set(f"lexicon-antonyms-{word}-{i}", a)
        else:
            set_empty(word, 'antonym')
        


    