import pickle
from nltk.corpus import reuters
from nltk.corpus import brown

print("Creating word list...")
WORDLIST = [w.lower() for w in set(reuters.words()) | set(brown.words()) if w.isalpha()]
print(f"Number of words: {len(WORDLIST)}")

print("Creating list of words with 7 unique characters...")
# Getting all words with 7 unique characters:
WORDS_7 = [w for w in WORDLIST if len(set(w)) == 7]
print(f"Number of words: {len(WORDS_7)}")

if __name__ == "__main__":
    file = open('wordlist.txt', 'wb')
    pickle.dump(WORDLIST, file)
    file.close()

    file = open('words7.txt', 'wb')
    pickle.dump(WORDS_7, file)
    file.close()
