import re
from transliterator import word_rules, spelling_variations

# Common English words for the initial baseline
english_words = {
    "i", "you", "we", "they", "he", "she",
    "the", "is", "are", "was", "am",
    "college", "school", "camera", "tomorrow",
    "today", "exam", "computer", "project",
    "good", "morning", "hello", "thank",
    "please", "have", "going", "come"
}


def identify_word(word):
    word = word.strip()

    if not word:
        return "EMPTY"

    if word.isdigit():
        return "NUMBER"

    if re.search(r"[\u0C80-\u0CFF]", word):
        return "KANNADA_SCRIPT"

    if not any(char.isalnum() for char in word):
        return "SYMBOL_OR_EMOJI"

    normalized = word.lower()

    if normalized in word_rules or normalized in spelling_variations:
        return "ROMANIZED_KANNADA"

    if normalized in english_words:
        return "ENGLISH"

    if word.isascii() and word.isalpha():
        return "UNCLASSIFIED_LATIN"

    return "UNKNOWN"