from language_identifier import identify_word

test_words = [
    "naanu",
    "nanu",
    "college",
    "camera",
    "tomorrow",
    "exam",
    "123",
    "ನಮಸ್ಕಾರ",
    "😊",
    "hogthiddini"
]

for word in test_words:
    print(word, "→", identify_word(word))