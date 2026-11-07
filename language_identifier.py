import regex

def identify_token(token):

    # Check for Kannada
    if regex.search(r'[\u0C80-\u0CFF]', token):
        return "Kannada"

    # Check for English
    elif regex.fullmatch(r'[A-Za-z]+', token):
        return "English"

    # Check for numbers
    elif regex.fullmatch(r'\d+', token):
        return "Number"

    # Check for emojis
    elif regex.search(r'\p{Extended_Pictographic}', token):
        return "Emoji"

    # Check for punctuation
    elif regex.fullmatch(r'\p{P}+', token):
        return "Punctuation"

    else:
        return "Other"


# Test sentence
tokens = ["ನಮಸ್ಕಾರ", "Hello", "😊", "123", "!"]

for token in tokens:
    print(token, ":", identify_token(token))