# ============================================
# KANNADA MIX - SMART TRANSLITERATION SYSTEM
# Dictionary + AI-based Transliteration
# ============================================

# 1. Kannada Dictionary
word_rules = {
    "namaskara": "ನಮಸ್ಕಾರ",
    "kannada": "ಕನ್ನಡ",
    "amma": "ಅಮ್ಮ",
    "appa": "ಅಪ್ಪ",
    "nanna": "ನನ್ನ",
    "naanu": "ನಾನು",
    "nanu": "ನಾನು",
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
    "dhanyavaada": "ಧನ್ಯವಾದ"
}
spelling_variations ={}


# 2. Initialize IndicXlit AI Engine
import argparse
import torch

# Allow the trusted checkpoint's Namespace object
torch.serialization.add_safe_globals([argparse.Namespace])

from ai4bharat.transliteration import XlitEngine

try:
    engine = XlitEngine("kn", beam_width=10)
    print("IndicXlit initialized successfully!")

except Exception as error:
    engine = None
    print("IndicXlit initialization error:", error)


# 3. Transliterate a Single Word
def transliterate_word(word):

    word = word.strip()

    if not word:
        return word

    lower_word = word.lower()

    # Check dictionary first
    if lower_word in word_rules:
        return word_rules[lower_word]

    # Use AI engine if dictionary word is unavailable
    if engine is not None:
        try:
            result = engine.translit_word(word, topk=3)

            candidates = result.get("kn", [])

            if isinstance(candidates, list) and candidates:
                return candidates[0]

            if isinstance(candidates, str) and candidates:
                return candidates

        except Exception as error:
            print("Transliteration error:", error)

    # Return original word if transliteration fails
    return word


# 4. Transliterate a Complete Sentence
def transliterate_sentence(sentence):

    words = sentence.split()

    translated_words = []

    for word in words:
        translated_word = transliterate_word(word)
        translated_words.append(translated_word)

    return " ".join(translated_words)


# 5. Main Program
def main():

    print("\n================================")
    print("       KANNADA MIX")
    print("================================")

    user_input = input("\nEnter a sentence: ")

    output = transliterate_sentence(user_input)

    print("\nKannada Output:")
    print(output)

    print("\n================================")


# 6. Run Program
if __name__ == "__main__":
    main()