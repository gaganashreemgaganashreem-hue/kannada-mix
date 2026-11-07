from transliterator import transliterate_word

words = [
    "namaskara",
    "kannada",
    "amma",
    "appa",
    "nanna",
    "naanu",
    "neenu",
    "neeru",
    "mane",
    "oota",
    "banni",
    "hogi",
    "haudu",
    "illa",
    "beda",
    "illi",
    "alli",
    "chennagide",
    "hegiddira",
    "dhanyavaada"
]

for word in words:
    print(word, "->", transliterate_word(word))