from flask import Flask, render_template, request
from transliterator import transliterate_word

app = Flask(__name__)

ENGLISH_WORDS = {"meeting", "time", "phone", "battery", "camera",
                 "price", "but", "super", "nice", "good"}

def convert_sentence(text):
    out = []
    for word in text.split():
        core = word.strip(",.!?")
        punct = word[len(word.rstrip(",.!?")):]
        if core.lower() in ENGLISH_WORDS:
            out.append(word)                      # keep English as is
        else:
            out.append(transliterator.py(core.lower()) + punct)
    return " ".join(out)

@app.route("/", methods=["GET", "POST"])
def home():
    text, result = "", ""
    if request.method == "POST":
        text = request.form.get("text", "")
        result = convert_sentence(text)
    return render_template("index.html", text=text, result=result)

if __name__ == "__main__":
    app.run(debug=True)
