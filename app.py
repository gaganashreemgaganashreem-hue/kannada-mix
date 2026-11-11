from flask import Flask, render_template, request
import re

from language_identifier import identify_word
from transliterator import transliterate_word

app = Flask(__name__)


def process_text(text):
    # Split text while preserving spaces and punctuation
    tokens = re.findall(r'\w+|[^\w\s]|\s+', text, re.UNICODE)

    result = []

    for token in tokens:

        # Preserve spaces
        if token.isspace():
            result.append(token)
            continue

        # Identify the type of token
        word_type = identify_word(token)

        # Convert only recognized Romanized Kannada words
        if word_type in("ROMANIZED_KANNADA","UNCLASSIFIED_LATIN"):
            converted = transliterate_word(token)
            
    
            result.append(converted)

        # Preserve English, numbers, Kannada script,
        # punctuation, emojis and uncertain words
        else:
            result.append(token)

    return "".join(result)


@app.route("/", methods=["GET", "POST"])
def home():

    input_text = ""
    output_text = ""

    if request.method == "POST":

        input_text = request.form.get("text", "")

        output_text = process_text(input_text)

    return render_template(
        "index.html",
        input_text=input_text,
        output_text=output_text,
        result=output_text
    )


if __name__ == "__main__":
    app.run(debug=True)