from tokenizer import tokenize
from language_identifier import identify_token

messages = [
    "Hello Kannada!",
    "ನಮಸ್ಕಾರ ಎಲ್ಲರೂ",
    "Hello 😊",
    "I have 2 apples.",
    "ನಾನು learning Python",
    "Wow!!! Great work 🎉",
    "Order 25 costs 150 rupees.",
    "ನಮಸ್ಕಾರ 😊 ಹೇಗಿದ್ದೀರಾ?",
    "Meet me at 10 AM.",
    "Good morning ❤️ Let's learn Kannada!"
]

for i, message in enumerate(messages, 1):
    print(f"\nMessage {i}: {message}")

    tokens = tokenize(message)

    for token in tokens:
        category = identify_token(token)
        print(token, ":", category)