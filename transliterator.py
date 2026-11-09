# Basic Kannada transliteration rules

word_rules = {
    "namaskara": "ನಮಸ್ಕಾರ",
    "kannada": "ಕನ್ನಡ",
    "amma": "ಅಮ್ಮ",
    "appa": "ಅಪ್ಪ",
    "nanna": "ನನ್ನ",
    "naanu": "ನಾನು",
    "neenu": "ನೀನು",
    "neeru": "ನೀರು",
    "mane": "ಮನೆ",
    "oota": "ಊಟ",
    "banni": "ಬನ್ನಿ",
    "hogi": "ಹೋಗಿ",
    "haudu": "ಹೌದು",
    "illa": "ಇಲ್ಲ",
    "beda": "ಬೇಡ",
    "illi": "ಇಲ್ಲಿ",
    "alli": "ಅಲ್ಲಿ",
    "chennagide": "ಚೆನ್ನಾಗಿದೆ",
    "hegiddira": "ಹೇಗಿದ್ದೀರಾ",
    "dhanyavaada": "ಧನ್ಯವಾದ",
    "ide": "ಇದೆ",
    "nange": "ನಂಗೆ"
}


def transliterate_word(word):
    word = word.lower()

    if word in word_rules:
        return word_rules[word]

    return word

if __name__ == "__main__":
    words = ["namaskara", "kannada", "amma", "appa", "neeru"]
    for word in words:
        print(word, "->", transliterate_word(word))
    print(transliterate_word("alli"), transliterate_word("ide"), transliterate_word("hello"))
