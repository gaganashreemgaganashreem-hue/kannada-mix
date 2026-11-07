import regex

# Pattern to identify different tokens
TOKEN_PATTERN = regex.compile(
    r"\p{Extended_Pictographic}"
    r"(?:\uFE0F)?(?:\p{Emoji_Modifier})?"
    r"(?:\u200D\p{Extended_Pictographic}(?:\uFE0F)?(?:\p{Emoji_Modifier})?)*"
    r"|\p{Regional_Indicator}{2}"
    r"|[\p{L}\p{M}]+(?:['’][\p{L}\p{M}]+)*"
    r"|\p{N}+(?:[.,]\p{N}+)*"
    r"|[^\s]"
)

def tokenize(text):
    tokens = TOKEN_PATTERN.findall(text)
    return tokens


# Test example
message = "Hello Kannada 😊! I am 20 years old."

result = tokenize(message)

print("Original Message:", message)
print("Tokens:", result)