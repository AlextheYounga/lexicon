from core.lexicon import Lexicon
import json

def test_lexicon_import_words():
    lexicon = Lexicon()
    word_list = lexicon.word_list()

    assert word_list[0] == 'A'