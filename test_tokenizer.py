from tokenizer import tokenize

messages = [
    "Hello Kannada!",
    "ನಮಸ್ಕಾರ ಎಲ್ಲರೂ",
    "Hello 😊",
    "I have 2 apples.",
    "I am learning Python in 2026.",
    "Wow!!! Great work 🎉",
    "Order #25 costs 150 rupees.",
    "ನಮಸ್ಕಾರ 😊 ಹೇಗಿದ್ದೀರಾ?",
    "Meet me at 10:30 AM.",
    "Good morning ❤️ Let's learn Kannada!"
]

for i, message in enumerate(messages, start=1):
    print(f"\nMessage {i}: {message}")
    print("Tokens:", tokenize(message))