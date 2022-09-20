from core.lexicon import Lexicon

def seed_word_definitions():
    lexicon = Lexicon()
    word_list = lexicon._import_words()
        
    for word in word_list:    
        print(f"Fetching {word} from nltk...")

        if (lexicon.fetch_meaning(word) == None):
            meaning = lexicon._get_meaning_from_nltk(word)

            lexicon.db.store(word, {'meaning': meaning})
            print(f"Saving {word} definition.")

seed_word_definitions()