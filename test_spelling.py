
from transliterator import transliterate_word

words = ["nanu", "naan", "dhanyavada", "namaskaara", "namaskara"]

for word in words:
    print(word, "→", transliterate_word(word))